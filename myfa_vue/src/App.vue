<template>
  <div>
    <nav-bar />
    <SuccessToast v-if="$store.state.SuccessToast" action="خروج " />
    <router-view />
  </div>
</template>

<style lang="scss" >
body {
  background-image: url(@/assets/bg-site.svg);
}
</style>

<script>
import SuccessToast from './components/SuccessToast'
import axios from 'axios'
export default {
  components: { SuccessToast },
  name: "App",
  data() {
    return
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
    if (localStorage.getItem('token')) {
      axios.defaults.headers.common.Authorization = 'Token ' + localStorage.getItem('token')
    }
  }
}
</script>
