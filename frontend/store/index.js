export const state = () => ({
  sentences: [],
  search_result: [],
  texts: []
})

export const mutations = {
  set_sentences (state, payload) {
    state.sentences = payload
  },

  set_search_result (state, payload) {
    state.search_result = payload
  },

  set_texts (state, payload) {
    state.texts = payload
  },

  push_text(state, payload){
    state.texts.push(payload)
  }
}
