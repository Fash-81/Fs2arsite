<template>
    <div class=" lg:ml-20 lg:mr-20 ">

        <button id="dropdownAvatarNameButton" data-dropdown-toggle="dropdownAvatarName" class="inline-flex  hover:to-violet-900 hover:from-fuchsia-700 font-Negar text-white   text-2xl bg-gradient-to-bl from-violet-900 to-fuchsia-700 rounded-lg px-6 py-3 items-center justify-center" type="button">
    <span class="sr-only">Open user menu</span>
    <!-- <img  class="mr-2 w-8 h-8 rounded-full" src="" alt=""> -->
    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 18 20" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>

  </button>

<!-- Dropdown menu -->
<div id="dropdownAvatarName" class="text-right font-Negar hidden mr-5 z-10 w-44  rounded divide-y  bg-gray-700 divide-gray-600">
    <div class="py-3 px-4 text-sm  text-white">
      <div class=" font-Negar text-2xl text-center">کاربر وارد شده</div>
    </div>
    <ul class="py-1 text-lg   text-gray-200" aria-labelledby="dropdownInformdropdownAvatarNameButtonationButton">
      <li>
        <a href="/posterpage" class="block py-2  px-4  hover:bg-gray-600 hover:text-white">پوستر</a>
      </li>
      <li>
        <a href="/bannerpage" class="block py-2 px-4   hover:bg-gray-600 hover:text-white"> بنر</a>
      </li>
      <li>
        <a href="/logopage" class="block py-2 px-4   hover:bg-gray-600 hover:text-white">لوگو </a>
        <a href="/bussinesscardpage" class="block py-2 px-4   hover:bg-gray-600 hover:text-white">بیزینس کارت </a>
      </li>
    </ul>
    <div class="py-1">
      <a @click="logout" class="block py-2 px-4 text-lg    hover:bg-gray-600 text-gray-200 hover:text-white">خروج</a>
    </div>
</div>


    </div>
</template>

<script>
export default{
    name: 'MenuList',
    methods:{
        logout(){
            this.$store.commit('removeToken')
            this.$store.commit('SuccessToast')
            setTimeout(() => {
                this.$store.state.SuccessToast = false
            }, 1000);
        }
    }
}
</script>