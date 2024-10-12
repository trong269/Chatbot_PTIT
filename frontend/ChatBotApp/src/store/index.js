// src/store/index.js
import { createStore } from 'vuex';

export default createStore({
  state: {
    user: null,
    token: null,
    currentConversation: {
      messages: [],
    },
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    },
    setToken(state, token) {
      state.token = token;
    },
    setCurrentConversation(state, conversation) {
      state.currentConversation = conversation;
    },
  },
  actions: {},
  modules: {},
});
