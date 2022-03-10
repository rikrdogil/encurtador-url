import Vue from "vue";
import Router from "vue-router";

import store from '@/store';


const routerOptions = [
  { path: "/", component: "Inicial" },
    { path: "/login", component: "Login" },
    { path: "/cadastro", component: "Cadastro" },
    { path: "/admin", component: "Admin", meta: { requiresAuth: true } },
    { path: '/404', name: '404', component: "404"},
    { path: '/:codigo_url', name: 'UrlEncurtada', component: "UrlEncurtada", props: true, meta: {
      hideNavbar: true,
     } },
    
    
];

const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`../views/${route.component}.vue`)
  };
});

Vue.use(Router);

const router= new Router({
  mode: "history",
  routes
});


router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.isAuthenticated) {
      next();
      return;
    }
    next('/login');
  } else {
    next();
  }
});

export default router