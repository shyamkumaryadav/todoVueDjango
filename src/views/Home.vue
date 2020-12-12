<template>
  <v-container>
    <v-row>
      <h1>Todo <span v-if="$store.state.User.auth.loggedIn" @click="$store.dispatch('logout')">Login</span></h1>
      
      <v-col>
        <input type="text" placeholder="Enter username" name="title" v-model="title">
        <input type="text" name="body" placeholder="Enter password" v-model="body">
        <button @click="todoAdd">login</button>
      </v-col>
    </v-row>
    <v-row>
      <v-row v-for="todo in todos" :key="todo.url">
        <h1><a :href="todo.url">{{ todo.title }}</a></h1>
      </v-row>
    </v-row>
    <v-row>
      <v-row><p>{{ $store.state.User }}</p></v-row>
      <v-row v-if="$store.state.User.auth.loggedIn">
        <v-row><p >Access: {{ $store.state.User.auth.user.access }}</p></v-row>
        <v-row><p >Access: {{ parseJwt(this.$store.state.User.auth.user.access) }}</p></v-row>
      </v-row>
      <v-row v-if="$store.state.User.auth.loggedIn">
        <v-row><p >Refresh: {{ $store.state.User.auth.user.refresh }}</p></v-row>
        <v-row><p >Refresh: {{ parseJwt(this.$store.state.User.auth.user.refresh) }}</p></v-row>
      </v-row>
    </v-row>
  </v-container>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
  created(){
    fetch('/api/todos/')
    .then(res => res.json())
    .then(data => this.todos = data)
    .catch(err => console.error("Error: " + err))
  },
  methods:{
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
    parseJwt (token) {
      console.log(token)
      var base64Url = token.split('.')[1]
      var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/')
      var jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
          return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
      }).join(''))
      console.log("Data", jsonPayload)
      return JSON.parse(jsonPayload);
    }
  },
  computed:{
  },
  data: () => ({
    todos: [],
    cook: '',
    title: '',
    body: '',
  }),
  
}
</script>
