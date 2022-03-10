<template>

   
         <v-container fluid>
            <v-layout align-center justify-center>
               
               <v-flex xs12 sm8 md5>
                  <v-card class="elevation-2">
                     <v-toolbar dark color="secondary">
                        <v-toolbar-title>Login</v-toolbar-title>
                     </v-toolbar>
                     <v-card-text>
                        <v-form 
                         ref="form"
                         
                           lazy-validation
                           >
                           <v-text-field
                              prepend-icon="person"
                              name="username"
                              id="username"
                              label="Login"
                              type="text"
                              v-model="form.username"
                               :rules="usernameRules"
                               required
                           ></v-text-field>
                           <v-text-field
                              id="password"
                              prepend-icon="lock"
                              name="password"
                              label="Senha"
                              type="password"
                              v-model="form.password"
                               :rules="passwordRules"
                               required
                           ></v-text-field>
                           <v-btn 
                           class="secondary"   
                        @click="submit"

                     >
      Entrar
    </v-btn>
                        </v-form>
                     </v-card-text>
                  
                  </v-card>
               </v-flex>
            </v-layout>
         </v-container>
    
  
</template>

<script>
import { mapActions } from 'vuex';



export default {
  name: 'Login',
  data() {''
    return {
      form: {
        username:'',
        password:'',
      },
      valid: true,
      username: '',
      usernameRules: [
        v => !!v || 'Login é obrigatório'
      ],
     
     password: '',
      passwordRules: [
        v => !!v || 'Senha é obrigatório'
      ],
    };
  },
  methods: {
    ...mapActions(['logIn']),
    async submit() {
   if (this.$refs.form.validate()) {
     
  

   
   try {

    const User = new FormData();
      User.append('username', this.form.username);
      User.append('password', this.form.password);
     await this.logIn(User);
   
 
      this.$router.push('/admin'); 

       }
     catch (err) {
         
            console.log(err)
     }

       }
    

        
      
    }
  }
}
</script>

<style></style>
