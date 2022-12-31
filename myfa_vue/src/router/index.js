import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RegisterForm from '@/views/RegisterForm.vue'
import NemuoneKar from '@/views/NemuoneKar.vue'
import LogIn from '@/views/LogIn.vue'
import SabtSefaresh from '@/views/SabtSefaresh.vue'
import AboutMe from '@/views/AboutMe.vue'
import BussinesscardPage from '@/views/BussinesscardPage.vue'
import BannerPage from '@/views/BannerPage.vue'
import LogoPage from '@/views/LogoPage.vue'
import PosterPage from '@/views/PosterPage.vue'


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  }
  ,
  {
    path: '/register',
    name: 'register',
    component: RegisterForm
  }
  ,
  {
    path: '/nemuonekar',
    name: 'nemuonekar',
    component: NemuoneKar
  }
  ,
  {
    path: '/login',
    name: 'login',
    component: LogIn
  }
  ,
  {
    path: '/sabtsefaresh',
    name: 'sabtsefaresh',
    component: SabtSefaresh
  }
  ,
  {
    path: '/aboutme',
    name: 'aboutme',
    component: AboutMe
  }
  ,
  {
    path: '/bussinesscardpage',
    name: 'bussinesscardpage',
    component: BussinesscardPage
  }
  ,
  {
    path: '/logopage',
    name: 'logopage',
    component: LogoPage
  }
  ,
  {
    path: '/bannerpage',
    name: 'bannerpage',
    component: BannerPage
  }
  ,
  {
    path: '/posterpage',
    name: 'posterpage',
    component: PosterPage
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
