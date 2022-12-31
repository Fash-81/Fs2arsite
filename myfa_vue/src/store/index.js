import { createStore } from "vuex";

export default createStore({
  state: {
    token: "",
    isAuthenticated: false,
    SuccessToast: false,
  },
  getters: {},
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem("token")) {
        const token = localStorage.getItem("token");
        state.token = token;
        state.isAuthenticated = true;
      }
    },
    setToken(state, token) {
      state.token = token;
      state.isAuthenticated = true;
    },
    removeToken(state) {
      state.token = "";
      state.isAuthenticated = false;
      localStorage.removeItem("token");
    },
    SuccessToast(state) {
      state.SuccessToast = true;
    },
  },
  actions: {},
  modules: {},
});
