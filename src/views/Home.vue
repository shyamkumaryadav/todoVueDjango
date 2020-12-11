<template>
  <v-container>
    <v-row>
      <h1>Todo <span v-if="$store.state.User.auth.status.loggedIn" @click="$store.dispatch('logout')">Login</span></h1>
      
      <v-col>
        <input type="text" placeholder="Enter username" name="title" v-model="title">
        <input type="text" name="body" placeholder="Enter password" v-model="body">
        <button @click="todoAdd">login</button>
      </v-col>
    </v-row>
    <v-row>
      <p>{{ $store.state.User.auth }}</p>
    </v-row>
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
      
    },
    todoAdd(){
      if(this.title == ''){
        alert("Enter Title")
      }
      else if(this.body == ''){
        alert("Enter body")
      }else{
        this.$store.dispatch('login', {username:this.title, password:this.body})
      }     
    },
    
  },

  data: () => ({
    todos : [],
    cook: '',
    title: '',
    body: '',
  })
}
</script>
