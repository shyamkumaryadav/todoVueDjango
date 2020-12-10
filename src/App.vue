<template>
  <v-app>
    <v-app-bar
      app
      hide-on-scroll
      dense
      flat
    >
    <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
    <v-toolbar-title>Todo</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn
      icon
      @click="changeTheme"
    >
      <v-icon>mdi-theme-light-dark</v-icon>
    </v-btn>
    </v-app-bar>
    <v-navigation-drawer v-model="drawer" fixed app temporary>
      <template v-slot:prepend>
        <v-list-item two-line>
          <v-list-item-avatar>
            <img
              src="#"
            />
          </v-list-item-avatar>

          <v-list-item-content>
            <v-list-item-title
              >shyamkumar</v-list-item-title
            >
            <v-list-item-subtitle
              >admin</v-list-item-subtitle
            >
          </v-list-item-content>
        </v-list-item>
      </template>
      <v-divider></v-divider>
      <v-list nav dense>
        <v-list-item-group>
          <v-list-item :to="{path: '/'}">
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item>

          <v-list-item :to="{path: '/about'}">
            <v-list-item-icon>
              <v-icon>mdi-decagram</v-icon>
            </v-list-item-icon>
            <v-list-item-title>About us</v-list-item-title>
          </v-list-item>

          <v-list-item :to="{path: '/terms'}">
            <v-list-item-icon>
              <v-icon>mdi-information</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Terms</v-list-item-title>
          </v-list-item>

        </v-list-item-group>
      </v-list>
      <template v-slot:append>
        <div class="pa-2">
          <v-btn block> Logout </v-btn>
        </div>
      </template>
    </v-navigation-drawer>


    <v-main>
      <router-view></router-view>
    </v-main>

    <v-footer absolute app>
        <v-row no-gutters justify="center">
          <v-col
          class="text-center py-4"
          cols="12"
          >
            Made by <v-icon color="red">mdi-heart</v-icon> <strong>Shyamkumar Yadav</strong>
          </v-col>

        </v-row>
    </v-footer>
  </v-app>
</template>

<script>

export default {
  name: 'App',
  created(){
    const theme = localStorage.getItem('theme') === "true"
    this.$vuetify.theme.dark = theme
  },
  methods:{
    changeTheme(){
      localStorage.setItem('theme', !this.$vuetify.theme.dark)
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark
    }
  },
  data: () => ({
    drawer: false
  }),
};
</script>
