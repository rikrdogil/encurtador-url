<template>
  <v-container fluid>
    <v-layout row wrap>
      <v-flex xs12 class="text-xs-center" mt-5>
        <h1>Bem vindo ao FastUrl</h1>
      </v-flex>
      <v-flex xs12 sm6 offset-sm3 mt-3>
<v-form
                        ref="form"
                        
    lazy-validation>
                            <v-text-field
                name="url"
                
                label="Url"
                id="url"
                type="text"
                required
                 v-model="form.url"
                  :rules="urlRules"
              
                ></v-text-field>
        
           
              <v-text-field
                name="codigoUrl"
                label="Código Personalizado (opcional)"
                id="codigoUrl"
                type="text"            
                required
                v-model="form.codigoUrl"
                ></v-text-field>
          
              <v-text-field
                name="dataExpiracao"
                label="Data expiração (opcional)"
                id="dataExpiracao"
                type="date"
                v-model="form.dataExpiracao"
             
             
                ></v-text-field>
                 <v-btn 
                           class="secondary"   
                        @click="submit"

                     >
      Cadastrar
    </v-btn>
            </v-form>
      </v-flex>
        <v-flex xs12 sm6 offset-sm3 mt-3>
           <v-alert
         :value="true"
      type="success"
        v-if="success"
      v-html="info" 
    
    >
    
    </v-alert>
          
          <v-alert
      :value="true"
      type="error"
       v-if="errored"
        v-html="textError" 
    >

    </v-alert>
 
        </v-flex>
     
    </v-layout>
  </v-container>
</template>
<script>
import axios from 'axios';
export default {
  name: 'Home',
    data() {
    return {
      form: {
       url:'',
        codigoUrl:'',
        dataExpiracao:''
      },
    info: null,
    textError:null,
    errored: false,
    success: false,
valid: true,
      url: '',
      urlRules: [
        v => !!v || 'Url é obrigatório'
      ],
     
    
    };
  },
  
    methods: {
   // ...mapActions(['createUrl']),
    async submit() {

   if (this.$refs.form.validate()) {
      await axios.post('url', this.form)
     .then(response => {
              if (response.data.urlEncurtada){
                this.errored = false
                this.success = true
                this.info = "<a href="+response.data.urlEncurtada+">"+response.data.urlEncurtada+"</a>"
              }
              })
       .catch(error => {
                  console.log(error)
                 this.success = false
                 this.textError = 'Ocorreu um erro tente navamente'
                this.errored = true
              })
             

   }
   
    }
  }

}
</script>

