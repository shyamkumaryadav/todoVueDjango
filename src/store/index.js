import Vue from 'vue'
import Vuex from 'vuex'
import User from './modules/User'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    is_Online: navigator.onLine
  },
  mutations: {
    setLine(state, payload){
      state.is_Online = payload
    }
  },
  getters:{
    is_Online: state => state.is_Online
  },
  // dispatch
  actions: {
    setConnected({commit}, payload){
      commit('setLine', payload)
    }
  },
  modules: {
    User
  }
})
