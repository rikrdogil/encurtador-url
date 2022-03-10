<template>
   <v-container fluid>
    <v-layout row wrap>
      
            <v-flex xs12 sm12  mt-3>
    <v-card  color="secondary">
    <v-card-title >
      Urls geradas
      <v-spacer></v-spacer>

    </v-card-title>
    <v-data-table
      :page="page"
      :pageCount="numberOfPages"
      :headers="headers"
      :items="urls"
      :items-per-page="10"
       :total-items="totalUrls"
      :loading="loading"
      :rows-per-page-items="[10]"
    :pagination.sync= "pagination"
      
    

    >
 
     <template v-slot:items="props">
      <td>  <a :href="props.item.urlEncurtada" target="_black">{{ props.item.urlEncurtada }}</a> </td>
     <td>{{ props.item.codigoUrl }}</td>
        <td > {{ new Date(props.item.dataExpiracao ).toLocaleDateString() }}</td>
           <td>{{ props.item.url }}</td>

    </template>
   
   
    </v-data-table>
    </v-card>
            </v-flex>
    </v-layout>
   </v-container>
</template>
<style scoped></style>
<script>
import axios from "axios";
export default {
  name: "Admin",
  data() {
    return {
    
      page: 1,
      totalUrls: 0,
      numberOfPages: 0,
      urls: [],
      loading: true,
      pagination: {},
      headers: [
        { text: "Url encurtada", value: "urlEncurtada" ,sortable: false },
        { text: "Codigo", value: "codigoUrl",sortable: false   },
        { text: "Expira em", value: "dataExpiracao",sortable: false  },
        { text: "URL", value: "url", sortable: false },
      
      ],
    };
  },
  watch: {
    pagination: {
      handler() {
         this.readDataFromAPI()
          
      },
    },
    deep: true
  },
    mounted () {
      this.readDataFromAPI()
       
    },
  methods: {
    readDataFromAPI() {
      this.loading = true;
      const { page, rowsPerPage } = this.pagination;
       console.log("Pagina e registros ", page, rowsPerPage);
 
      axios
        .get(
          "urls?size="+rowsPerPage+"&page="+page
        )
        .then((response) => {
          this.loading = false
          this.urls = response.data.items
          this.totalUrls = response.data.total
          this.numberOfPages = response.data.size
        });
    },
  }

};
</script>