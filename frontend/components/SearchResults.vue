<template>
    <v-flex xs5 offset-sm2>
      <v-card>
        <v-toolbar color="dimgray" dark>
          <v-toolbar-title>Search results TOP-10</v-toolbar-title>
        </v-toolbar>

        <v-list two-line subheader>


          <v-list-tile
            v-for="item in search_result"
            :key="item.id"
            :id="'search-result-' + item.id"
            :textid="item.text_id"
            @click="fetchSentences"
          >
            <v-list-tile-avatar>
              <h3>{{ item._score }}</h3>
            </v-list-tile-avatar>
              <v-tooltip bottom>
                <template v-slot:activator="{ on }">
                  <v-list-tile-content v-on="on">
                    <v-list-tile-title>{{ "Text id = " + item.text_id }}</v-list-tile-title>
                    <v-list-tile-sub-title>{{ item.content }}</v-list-tile-sub-title>
                  </v-list-tile-content>
                </template>
                <span>{{ item.content }}</span>
              </v-tooltip>
          </v-list-tile>
        </v-list>
      </v-card>
    </v-flex>
</template>

<script>
  import { mapState } from 'vuex'
  import axios from 'axios'

  export default {

    fetch ({ store }) {
    },
    computed: mapState([
      'search_result'
    ]),
    data () {
      return {
      }
    },
    methods: {
        testMe(t){
            console.log(t)
        },
        fetchSentences(e){
            axios.get(`http://0.0.0.0:8000/v1.0/raw_text/${e.currentTarget.getAttribute('textid')}`)
                .then(response => {
                    this.$store.commit('set_sentences',  response.data.sentences )
                })
      .catch(e => { console.log(e) })
      }



    }
  }
</script>
