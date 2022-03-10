<template>
  
  <v-app>
    <v-navigation-drawer v-model="sidebar" app 
  v-if="!$route.meta.hideNavbar"
    >
      <v-list  > 
        <v-list-tile
          v-for="item in menuItems"
          :key="item.title"
          :to="item.path">
          <v-list-tile-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>{{ item.title }}</v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>

    <v-toolbar  app 
    class="primary"
    dark
    v-if="!$route.meta.hideNavbar"
    >
      <span class="hidden-sm-and-up">
        <v-toolbar-side-icon @click="sidebar = !sidebar">
        </v-toolbar-side-icon>
      </span>
      <v-toolbar-title >
        <router-link to="/" tag="span" style="cursor: pointer">
          {{ appTitle }}
        </router-link>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-xs-only" v-if="isLoggedIn">

            
        <v-btn
          flat
          v-for="item in menuItemsLogado"
          :key="item.title" 
          :to="item.path" 
         >
          <v-icon left dark>{{ item.icon }}</v-icon>
          {{ item.title }}
        </v-btn>
    <v-btn flat
         @click="logout" >
           <v-icon left dark>lock</v-icon>
         Sair
            </v-btn>
       
         
      </v-toolbar-items>
        <v-toolbar-items class="hidden-xs-only" v-else>
          <v-btn
          flat
          v-for="item in menuItems"
          :key="item.title" 
          :to="item.path" 
         >
          <v-icon left dark>{{ item.icon }}</v-icon>
          {{ item.title }}
        </v-btn>
          </v-toolbar-items>
    </v-toolbar>
    
    <v-content>
      <router-view></router-view>
    </v-content>
    
  </v-app>

</template>

<script>

export default {
  name: "App",
  computed: {
    isLoggedIn: function() {
      return this.$store.getters.isAuthenticated;
    }
  },
  methods: {
    async logout () {
      await this.$store.dispatch('logOut');
      this.$router.push('/login');
    }
  },
  data(){
    return {
      appTitle: 'FastUrl',
      sidebar: false,
      menuItems: [
         { title: 'Inicial', path: '/', icon: 'house' },
          { title: 'Admin', path: '/admin', icon: 'dashboard' },
          { title: 'Cadastrar', path: '/cadastro', icon: 'face' },
          { title: 'Entrar', path: '/login', icon: 'lock_open' }
     ],
       menuItemsLogado: [
         { title: 'Inicial', path: '/', icon: 'house' },
          { title: 'Admin', path: '/admin', icon: 'dashboard' }
     
     
     ]
    }
  },
};
</script>
<style>

</style>
