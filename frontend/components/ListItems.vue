<template>
  <v-container fluid grid-list-md>
    <v-data-iterator
      :items="texts"
      :rows-per-page-items="rowsPerPageItems"
      :pagination.sync="pagination"
      content-tag="v-layout"
      row
      wrap
    >
      <template v-slot:item="props">
        <v-flex
          xs12
          sm6
          md4
          lg3
        >
          <v-card

            hover="true"
          >
            <v-card-title><h4>{{ props.item.slug }}</h4></v-card-title>
            <v-divider></v-divider>
            <v-list dense>
              <v-list-tile>
                <v-list-tile-content>Id:</v-list-tile-content>
                <v-list-tile-content class="align-end">{{ props.item.id}}</v-list-tile-content>
              </v-list-tile>
              <v-list-tile>
                <v-list-tile-content>Created at:</v-list-tile-content>
                <v-list-tile-content class="align-end">{{ props.item.created_at.toLocaleString()}}</v-list-tile-content>
              </v-list-tile>
              <v-btn color="info" :id="props.item.id" @click="fetchSentences">Get sentences</v-btn>
            </v-list>
          </v-card>
        </v-flex>
      </template>
    </v-data-iterator>
  </v-container>
</template>

<script>
  import axios from 'axios'
  import { mapState } from 'vuex'

  export default {
      fetch ({ store }) {
  },
    computed: mapState([
      'texts'
    ]),
    data () {
      return{
        rowsPerPageItems: [4, 8, 12],
        pagination: {
        rowsPerPage: 4
        },
      }
    },
    mounted(){
      axios.get(`http://0.0.0.0:8000/v1.0/raw_text`).then(response => {
        this.$store.commit('set_texts',  response.data )
      }).catch(e => { console.log(e) })
    },
    methods: {
      fetchSentences(e){
        axios.get(`http://0.0.0.0:8000/v1.0/raw_text/${e.currentTarget.id}`)
                .then(response => {
                  this.$store.commit('set_sentences',  response.data.sentences )
                  window.scrollTo(256, 4200)
                })
      .catch(e => { console.log(e) })
      }
  }}
</script>
