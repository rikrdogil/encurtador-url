import axios from 'axios'
import Vue from 'vue'

import App from './App.vue'

import Vuetify from "vuetify";
import "vuetify/dist/vuetify.min.css";

import router from './router'
import store from './store'
// Helpers
import colors from 'vuetify/es5/util/colors'

Vue.use(Vuetify, {
  theme: {
    primary: colors.cyan.darken2, // #E53935
    secondary: colors.orange.accent3, // #FFCDD2
    accent: colors.indigo.base, // #3F51B5
    error: '#FF5252',
    info: '#2196F3',
    success: '#4CAF50',
    warning: '#FFC107'

  }
})

Vue.config.productionTip = false

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:8000/';  // nosso FastAPI backend

axios.interceptors.response.use(undefined, function (error) {
  if (error) {
    const originalRequest = error.config;
    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      store.dispatch('logOut');
      return router.push('login')
    }
  }
});



/* eslint-disable no-new */
new Vue({
 
  store,
  router,
  render: h => h(App),
  
}).$mount('#app')
