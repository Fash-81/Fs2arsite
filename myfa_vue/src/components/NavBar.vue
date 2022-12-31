<template>
  <nav class="p-4 w-full  bg-gray-900 border-gray-700 rounded-b-3xl">
    <div class="container flex flex-wrap justify-between items-center mx-auto">
      <div class="flex">
        <img src="../assets/fs2ar-logo.svg" class="mr-3  h-10" alt="FS2ARLogo">
        <span class="self-center text-xl lg:text-3xl font-semibold whitespace-nowrap text-white">FS2AR</span>
      </div>
      <div class="hidden w-full lg:block md:w-auto" id="mobile-menu">
        <ul
          class="flex flex-col font-Negar  p-4  rounded-lg border  md:flex-row sm:space-x-6 md:space-x-10    md:border-0 bg-gray-800 md:bg-gray-900 border-gray-700">
          <li>
            <a href="/"
              class="block text-2xl py-2 pr-4 pl-3  rounded  md:border-0 md:p-0 text-gray-200 md:hover:text-blue-400 hover:bg-gray-700 hover:text-blue-200 md:hover:bg-transparent"
              aria-current="page">صفحه اصلی</a>
          </li>
          <li>
            <a href="/nemuonekar"
              class="block text-2xl py-2 pr-4 pl-3 rounded   md:border-0  md:p-0 text-gray-200 md:hover:text-blue-400 hover:bg-gray-700 hover:text-blue-200 md:hover:bg-transparent"
              aria-current="page">نمونه کارها</a>
          </li>
          <li>
            <a href="/sabtsefaresh"
              class="block text-2xl py-2 pr-4 pl-3  rounded  md:border-0  md:p-0 text-gray-200 md:hover:text-blue-400 hover:bg-gray-700 hover:text-blue-200 md:hover:bg-transparent">ثبت
              سفارش</a>
          </li>
          <li>
            <a href="/aboutme"
              class="block text-2xl py-2 pr-4 pl-3 rounded md:border-0  md:p-0 text-gray-200 md:hover:text-blue-400 hover:bg-gray-700 hover:text-blue-200 md:hover:bg-transparent">درباره
              من</a>
          </li>
        </ul>
      </div>
      <div>
        <button v-if="!$store.state.isAuthenticated"
          class=" hidden relative mr-10 lg:block   focus:ring-4 focus:outline-none  font-medium rounded-lg  px-2 py-2 text-center  hover:to-violet-900 hover:from-fuchsia-700 font-Negar text-white   text-2xl bg-gradient-to-bl from-violet-900 to-fuchsia-700  items-center justify-center"
          type="button" data-modal-toggle="authentication-modal">
          <a href="/login" class="flex"> <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1"></path>
            </svg>
            ورود | ساخت حساب</a>
        </button>
        <a v-if="!$store.state.isAuthenticated" href="/login" class="flex lg:hidden mr-10"> <svg class="w-8 h-8"
            fill="none" stroke="gray" viewBox="0 0 20 21" xmlns="http://www.w3.org/2000/svg">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1"></path>
          </svg></a>
        <MenuList v-else />

      </div>
    </div>
  </nav>

</template>
<script>
import MenuList from './MenuList.vue'
export default {
  name: "NavBar",
  components: { MenuList }
}
</script>