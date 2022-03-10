<template>

  <v-container fluid >
      <v-layout align-center justify-center>
     
    <v-flex xs12 sm8 md5>
             <v-card class="elevation-2">
       <v-toolbar dark color="secondary">
             <v-toolbar-title>Cadastro</v-toolbar-title>
                     </v-toolbar>
                     <v-card-text>
                        <v-form
                        ref="form"
                         v-model="valid"
    lazy-validation>
                            <v-text-field
                name="username"
                
                label="Login"
                id="username"
                type="text"
                required
                v-model="user.username"
                   :rules="usernameRules"
                ></v-text-field>
        
           
              <v-text-field
                name="full_name"
                label="Nome"
                id="full_name"
                type="text"
                v-model="user.full_name"
                 :rules="full_nameRules"
                required></v-text-field>
          
              <v-text-field
                name="password"
                label="Senha"
                id="password"
                type="password"
                required
                v-model="user.password"
                 :rules="passwordRules"
                ></v-text-field>
                 <v-btn 
                           class="secondary"   
                        @click="submit"

                     >
      Cadastrar
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
  name: 'Register',
data() {
   
    return {
      user: {
        username: '',
        full_name: '',
        password: '',
      },
       valid: true,
      username: '',
      usernameRules: [
        v => !!v || 'Login é obrigatório'
      ],
      full_name: '',
      full_nameRules: [
        v => !!v || 'Nome é obrigatório'
      ],
     password: '',
      passwordRules: [
        v => !!v || 'Senha é obrigatório'
      ],
    };
  },
  methods: {
    ...mapActions(['register']),
    async submit() {
          if (this.$refs.form.validate()) {
      try {
            await this.register(this.user);
  
      } catch (error) {
        throw 'Login já existe tente outro';
      }
          } }
    
  },
};
</script>
