<template>
  <v-layout justify-center align-center>
    <v-flex>
      <div class="text-xs-center">
        <img height="400px" src="/logo_transparent.png" alt="My Search" class="mb-5" />
      </div>
        <h1>Search similar sentences in existing texts</h1>
          <v-container fluid grid-list-md>
            <ListItems></ListItems>
          </v-container>
        <h1>Or upload your own text</h1>
      <v-container fluid>
        <v-layout row wrap>
          <v-flex xs12>
            <v-textarea
              outline
              counter
              no-resize
              :rules="rules"
              :value="value"
              name="TextInput"
              label="Text"
              rows="12"
              hint="~1mb or 1024**2 symbols"
              @input="setVal"
            ></v-textarea>
          </v-flex>
        </v-layout>
         <v-layout row wrap>
          <v-flex xs12>
            <v-btn color="info" name="TextInputProcess" v-on:click="postPost">Process</v-btn>
            <template v-if="loading">
              <v-progress-circular
                :width="3"
                color="green"
                indeterminate
              ></v-progress-circular>
            </template>
          </v-flex>
        </v-layout>
      </v-container>
      <v-container fluid>
        <v-layout row>
          <SentenceList></SentenceList>
          <SearchResults></SearchResults>
        </v-layout>
      </v-container>
    </v-flex>
  </v-layout>
</template>

<script>
import axios from 'axios'
import ListItems from '../components/ListItems'
import SentenceList from '../components/SentenceList'
import SearchResults from '../components/SearchResults'
let axiosDefaults = require('axios/lib/defaults')

axiosDefaults.xsrfHeaderName = 'X-CSRFTOKEN'
axiosDefaults.xsrfCookieName = 'csrftoken'

export default {
  fetch ({ store }) {
    },
    components: {ListItems, SentenceList, SearchResults},
    data () {
    return {
      errors: [],
      value: '',
      loading: false,
      rowsPerPageItems: [4, 8, 12],
      pagination: {
        rowsPerPage: 4
      },
    }
  },
  methods: {postPost () {
    this.loading = true;
    axios.post(`http://0.0.0.0:8000/v1.0/raw_text`, {
      raw_text: this.value}).then(response => {
        console.log(response)
        this.$store.commit('set_sentences',  response.data.sentences )
        this.$store.commit('push_text', response.data)
        window.scrollTo(256, 4200)
        this.loading = false
      })
      .catch(e => { this.errors.push(e) })
  },
  setVal (val) {
    this.value = val
  }
  }}
</script>