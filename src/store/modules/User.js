import AuthService from '@/services/auth.service'


const user = JSON.parse(localStorage.getItem('user'));
const initialState = user
  ? { loggedIn: true, user }
  : { loggedIn: false, user: null };

export default {
    // namespaced: true,
    state:{
        username: 'Null',
        email: 'None',
        id: 'None',
        auth: initialState
    },
    mutations:{
        loginSuccess(state, user) {
            state.auth = user;
        },
        loginFailure(state) {
            state.auth.loggedIn = false;
            state.auth.user = null;
        },
        logout(state) {
            state.auth.loggedIn = false;
            state.auth.user = null;
        },
        registerSuccess(state) {
            state.auth.loggedIn = false;
        },
        registerFailure(state) {
            state.auth.loggedIn = false;
        }
    },
    // dispatch
    actions:{
        login({ commit }, user) {
            return AuthService.login(user).then(
                user => {
                    if (user.access && user.refresh){
                        commit('loginSuccess', {...user, loggedIn:true})
                    }
                    return Promise.resolve(user)
                },
                error => {
                commit('loginFailure')
                return Promise.reject(error)
                }
            )
        },
        logout({ commit }) {
            AuthService.logout()
            commit('logout')
        },
        register({ commit }, user) {
            return AuthService.register(user).then(
                data => {
                    commit('registerSuccess')
                    return Promise.resolve(data)
                },
                error => {
                    commit('registerFailure')
                    return Promise.reject(error)
                })
        }
    },
    getters:{

    },
  }