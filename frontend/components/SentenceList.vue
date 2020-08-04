<template>
    <v-flex xs5>
      <v-card>
        <v-toolbar color="dimgray" dark>

          <v-toolbar-title>Text sentences</v-toolbar-title>

        </v-toolbar>

        <v-list two-line id="sentenceList">
          <template v-for="(item, index) in sentences">
            <v-list-tile
              :key="index"
              @click="searchSentences"
              :id="'sentence-' + item.id"
            >
              <v-tooltip bottom>
                <template v-slot:activator="{ on }">
                  <v-list-tile-content v-on="on">
                    <v-list-tile-title v-html="item.content" max-height="4096"></v-list-tile-title>
                  </v-list-tile-content>
                </template>
                <span>{{ item.content }}</span>
              </v-tooltip>
            </v-list-tile>

          </template>
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
      'sentences'
    ]),
    data () {
      return {
      }
    },
    methods: {
        testMe(t){
            console.log(t)
        },
      searchSentences(e){
          axios.get(`http://0.0.0.0:8000/v1.0/get_similar_sentences?sentence_id=${e.currentTarget.id.replace('sentence-', '')}`)
                  .then(response => {
                    this.$store.commit('set_search_result',  response.data )
                })
          }
    }
  }
</script>
