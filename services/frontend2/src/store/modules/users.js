import axios from 'axios';

const state = {
  user: null,
};

const getters = {
  isAuthenticated: state => !!state.user,
  stateUser: state => state.user,
};

const actions = {
  async register({dispatch}, form) {
    await axios.post('cadastro', form);
  
    await dispatch('logIn');
  },
  async logIn({dispatch}, user) {
    await axios.post('login', user); 
    await dispatch('viewMe');
  },
  async viewMe({commit}) {
    let {data} = await axios.get('users/dados');
    await commit('setUser', data);
  },
   // eslint-disable-next-line no-empty-pattern
  async logOut({commit}) {
    let user = null;
    commit('logout', user);
  }
};

const mutations = {
  setUser(state, username) {
    state.user = username;
  },
  logout(state, user){
    state.user = user;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};
