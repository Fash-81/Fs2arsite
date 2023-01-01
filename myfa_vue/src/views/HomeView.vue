<template>
  <div class="home">
    <NavBar />
    
    <PortfolioCards class="m-20 justify-center"/>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import PortfolioCards from '@/components/PortfolioCards.vue'
export default {
  name: 'HomeView',
  components: {
    NavBar,
    PortfolioCards
  }
}
</script>