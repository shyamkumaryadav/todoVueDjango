<template>
  <div class="home">
    <img src='{ logo }' alt="not find">
    <h6></h6>
    <p>@/assets/logo.png  {{ name }}</p>
    <HelloWorld msg="Shyamkumar yadav"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import logo from  '@/assets/logo.png'

export default {
  name: 'Home',
  components: {
    HelloWorld
  },
  data(){
    return{
      name: "shyamkumar yadav"
    }
  }
}
</script>
