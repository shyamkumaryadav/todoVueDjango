import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify';
// import 'roboto-fontface/css/roboto/roboto-fontface.css' // it's very light yes ? no
// import '@mdi/font/css/materialdesignicons.css' // it's very light yes ? no
import store from './store'

// Vue.config.productionTip = false // Set this to false to prevent the production tip on Vue startup
// Vue.config.devtools = false // true (false in production builds)
// Vue.config.silent = true // Suppress all Vue logs and warnings (false)

new Vue({
  router,
  vuetify,
  store,
  render: h => h(App),
  created(){
    window.addEventListener('offline', function(){
      store.dispatch('setConnected', false)
    })
    window.addEventListener('online', function(){
      store.dispatch('setConnected', true)
    })
  }
}).$mount('#app')
