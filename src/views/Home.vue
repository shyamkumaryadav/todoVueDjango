<template>
  <v-container>
    <v-row>
      <v-img
      src="https://bad.src/not/valid"
      lazy-src="https://picsum.photos/id/11/100/60"
      max-width="500"
      max-height="300"
    >
      <template v-slot:placeholder>
        <v-row
          class="fill-height ma-0"
          align="center"
          justify="center"
        >
          <v-progress-circular
            indeterminate
            color="grey lighten-5"
          ></v-progress-circular>
        </v-row>
      </template>
    </v-img>
    </v-row>
  </v-container>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
  created(){
    document.title = "Home"
    // created but not use 
  },
  watch: {
  //  i am watch why? this
  },
  methods:{
    // Call me
  },
  computed:{
  },
  data: () => ({
    // i am data
  }),
  
}
</script>
