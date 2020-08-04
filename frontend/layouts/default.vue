<template>
  <v-app id="app" dark>
    <v-content>
      <v-container>
        <nuxt />
      </v-container>
    </v-content>
    <v-footer :fixed="fixed" app>
      <span>&copy; 2020</span>
    </v-footer>
  </v-app>
</template>

<script>

  export default {
    name: 'App',
    fetch ({ store }) {
    },
    methods: {
    },
    data () {
      return {
        title: 'My Search'
      }
    }
  }
</script>
