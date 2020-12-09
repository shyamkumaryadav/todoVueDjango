<template>
  <v-container>
    <v-row>
      <h1>Todo</h1>
      <v-col>
        <input type="text" placeholder="Enter Title" name="title" v-model="title">
        <input type="text" name="body" placeholder="Enter Body" v-model="body">
        <button @click="todoAdd">Post</button>
      </v-col>
    </v-row>
      <div v-for="(todo, index) in todos" :key="index">
        <p :class="todo.is_done ? 'text-decoration-line-through' : ''" @click="todoDone(todo)">{{todo.title}} {{ todo.is_done }} </p><button @click="todoDelete(todo, index)">[X]</button>
      </div>
  </v-container>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
  created(){
    const name = 'csrftoken'
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                this.cook = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    fetch('/api/todos/')
    .then(res => res.json())
    .then(data => this.todos = data)
    .catch(err => console.error("Error: " + err))
  },
  methods:{
    todoDone(todo){
      // todo.is_done = !todo.is_done
      fetch(todo.url, {
        method: 'PUT',
        mode: 'cors',
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': this.cook
        },
        body: JSON.stringify({'is_done': !todo.is_done, 'body':todo.body, 'title':todo.title, 'user':todo.user})
      })
      .then(res => res.json())
      .then(data => {
        todo.is_done=data.is_done
      })
      .catch(error => console.error("Error: " + error))
    },
    todoAdd(){
      if(this.title == ''){
        alert("Enter Title")
      }
      else if(this.body == ''){
        alert("Enter body")
      }else{
        fetch('/api/todos/', {
          method: 'POST',
          mode: 'cors',
          credentials: 'include',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': this.cook
          },
          body: JSON.stringify({'body':this.body, 'title':this.title, 'user': this.todos[0].user})
        })
        .then(res => res.json())
        .then(data => {
          this.todos.push(data)
          this.title = ''
          this.body = ''
        })
        .catch(error => console.error("Error: " + error))
      }     
    },
    todoDelete(todo, index){
      fetch(todo.url,{
        method: 'DELETE',
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': this.cook
        }
      })
      .then(data => this.todos.splice(index, 1))
      .catch(error => console.log("Error: " + error))
    }
  },
  data(){
    return{
      todos : [],
      cook: '',
      title: '',
      body: '',
    }
  }
}
</script>
