   

<script>
import axios from 'axios';

export default {
  name: 'UrlEncurtada',
  props: ['codigo_url'],
data () {
    return {
      info: null,
      loading: true,
      errored: false,
      textError: null,
      isRedirectpage: true
    }
},


    async created() {
    
    await axios.get(`/${this.codigo_url}`)
        .then(response => {
          window.location.href = response.data.url; 
       
             } )
         .catch(error => {
            console.log(error)
            this.$router.push('404')
        
      })
    
  },

   

};
</script>
