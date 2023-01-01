<template>
    <div>
        <!-- poster -->
        <div class="flex justify-between">
            
            <a href="/posterpage"
            class=" flex  hover:to-violet-900 hover:from-fuchsia-700 font-Negar text-white  text-2xl bg-gradient-to-bl from-violet-900 to-fuchsia-700 rounded-lg px-6 py-3 w-60  text-center items-center justify-center">
            
            
            نمایش همه
            <svg aria-hidden="true" class="ml-2 -mr-1 w-4 h-4" fill="currentColor" viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd"
            d="M10.293 3.293a1 1 0 011.414 0l6  6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
            clip-rule="evenodd"></path>
        </svg>
    </a>
    <h2
        class=" font-Negar text-white flex text-2xl bg-gradient-to-bl from-violet-900 to-fuchsia-700 rounded-lg px-6 py-3 w-60 text-center items-center justify-center">
        پوستر های اخیر</h2>
</div>
        <br/>
        <swiper :slidesPerView="1" :spaceBetween="50" :breakpoints="
    {
        '640': { slidesPerView: 1, spaceBetween: 50, },
        '856': { slidesPerView: 2, spaceBetween: 50, },
        '1210': { slidesPerView: 3, spaceBetween: 50, },
    }" :modules="modules" class="mySwiper my-14 w-3/5 mx-auto  justify-center">



            <SwiperSlide v-for=" portfolio in getPosters.reverse().slice(0, 5)" :key="portfolio">

                <div
                    class="max-w-sm font-Negar  rounded-lg border  shadow-md bg-gray-900/40 border-gray-700 ">

                    <img class=" rounded" :src="'http://127.0.0.1:8000/media/p/' + portfolio.topic" alt="khali">

                    <div class="p-5 ">

                        <h7 class="mt-2 text-xl font-bold tracking-tight  text-white lg:text-2xl">
                            {{ portfolio.case }}</h7>
                        <p class="mt-5 font-normal   text-gray-200 ">{{ portfolio.subject }}</p>

                    </div>
                </div>
            </SwiperSlide>
        </swiper>
        <!-- banner -->
        <div class="flex justify-between">
            <a href="/bannerpage"
                class="inline-flex  hover:to-violet-900 hover:from-fuchsia-700 font-Negar text-white text-center  text-2xl bg-gradient-to-bl from-violet-900 to-fuchsia-700 rounded-lg px-6 py-3 w- items-center justify-center">
                نمایش همه <svg aria-hidden="true" class="ml-2 -mr-1 w-4 h-4" fill="currentColor" viewBox="0 0 20 20"
                    xmlns="http://www.w3.org/2000/svg">
                    <path fill-rule="evenodd"
                        d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
                        clip-rule="evenodd"></path>
                </svg>
            </a>
            <h2
                class=" font-Negar text-white text-center  text-2xl bg-gradient-to-bl from-violet-900 to-fuchsia-700 rounded-lg px-6 py-3 w-60 items-center justify-center">
                بنر های اخیر</h2>

        </div>
        <br/>
        <swiper :slidesPerView="1" :spaceBetween="50" :breakpoints="
    {
        '640': { slidesPerView: 1, spaceBetween: 50, },
        '856': { slidesPerView: 2, spaceBetween: 50, },
        '1210': { slidesPerView: 3, spaceBetween: 50, },
    }" :modules="modules" class="mySwiper my-14 w-3/5 mx-auto  justify-center">


            <SwiperSlide v-for=" portfolio in getBanners.reverse().slice(0, 5)" :key="portfolio">

                <div
                    class="max-w-sm font-Negar  rounded-lg border  shadow-md bg-gray-900/40 border-gray-700 ">

                    <img class=" rounded" :src="'http://127.0.0.1:8000/media/p/' + portfolio.topic" alt="khali">

                    <div class="p-5 ">

                        <h7 class="mt-2 text-xl font-bold tracking-tight  text-white lg:text-2xl">
                            {{ portfolio.case }}</h7>
                        <p class="mt-5 font-normal  text-gray-200 ">{{ portfolio.subject }}</p>

                    </div>
                </div>
            </SwiperSlide>
        </swiper>
        <!-- logo -->
        <div class="flex justify-between">
            
            <a href="/logopage"
            class=" inline-flex  hover:to-violet-900 hover:from-fuchsia-700 font-Negar text-white text-center  text-2xl bg-gradient-to-bl from-violet-900 to-fuchsia-700 rounded-lg px-6 py-3 w-60 items-center justify-center">
            نمایش همه
            <svg aria-hidden="true" class="ml-2 -mr-1 w-4 h-4" fill="currentColor" viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd"
            d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
            clip-rule="evenodd"></path>
        </svg>
    </a>
    <h2
        class=" font-Negar text-white text-center  text-2xl bg-gradient-to-bl from-violet-900 to-fuchsia-700 rounded-lg px-6 py-3 w-60 items-center justify-center">
        لوگو های اخیر</h2>
        </div>
        <br/>
        <swiper :slidesPerView="1" :spaceBetween="50" :breakpoints="
    {
        '640': { slidesPerView: 1, spaceBetween: 50, },
        '856': { slidesPerView: 2, spaceBetween: 50, },
        '1210': { slidesPerView: 3, spaceBetween: 50, },
    }" :modules="modules" class="mySwiper my-14 w-3/5 mx-auto  justify-center">



            <SwiperSlide v-for=" portfolio in getLogo.reverse().slice(0, 5)" :key="portfolio">

                <div
                    class="max-w-sm font-Negar  rounded-lg border  shadow-md bg-gray-900/40 border-gray-700 ">

                    <img class=" rounded" :src="'http://127.0.0.1:8000/media/p/' + portfolio.topic" alt="khali">

                    <div class="p-5 ">

                        <h7 class="mt-2 text-xl font-bold tracking-tight  text-white lg:text-2xl">
                            {{ portfolio.case }}</h7>
                        <p class="mt-5 font-normal   text-gray-200 ">{{ portfolio.subject }}</p>

                    </div>
                </div>
            </SwiperSlide>
        </swiper>
        <!-- bussinesscard -->
        <div class="flex justify-between">
            
            <a href="/bussinesscardpage"
            class=" inline-flex  hover:to-violet-900 hover:from-fuchsia-700 font-Negar text-white text-center  text-2xl bg-gradient-to-bl from-violet-900 to-fuchsia-700 rounded-lg px-6 py-3 w-60 items-center justify-center">
            نمایش همه 
            <svg aria-hidden="true" class="ml-2 -mr-1 w-4 h-4" fill="currentColor" viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd"
            d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
            clip-rule="evenodd"></path>
        </svg>
    </a>
    <h2
        class=" font-Negar text-white text-center  text-2xl bg-gradient-to-bl from-violet-900 to-fuchsia-700 rounded-lg px-6 py-3 w-64 items-center justify-center">
        بیزینس کارت های اخیر</h2>
        </div>
        <br/>
        <swiper :slidesPerView="1" :spaceBetween="50" :breakpoints="
    {
        '640': { slidesPerView: 1, spaceBetween: 50, },
        '856': { slidesPerView: 2, spaceBetween: 50, },
        '1210': { slidesPerView: 3, spaceBetween: 50, },
    }" :modules="modules" class="mySwiper my-14 w-3/5 mx-auto  justify-center">



            <SwiperSlide v-for=" portfolio in getBcard.reverse().slice(0, 5)" :key="portfolio">

                <div
                    class="max-w-sm font-Negar  rounded-lg border  shadow-md bg-gray-900/40 border-gray-700 ">

                    <img class=" rounded" :src="'http://127.0.0.1:8000/media/p/' + portfolio.topic" alt="khali">

                    <div class="p-5 ">

                        <h7 class="mt-2 text-xl font-bold tracking-tight  text-white lg:text-2xl">
                            {{ portfolio.case }}</h7>
                        <p class="mt-5 font-normal  text-gray-200 ">{{ portfolio.subject }}</p>

                    </div>
                </div>
            </SwiperSlide>
        </swiper>
        <!-- vectorart -->
        <div class="flex justify-between">
            
            <a href="/bussinesscardpage"
            class=" inline-flex  hover:to-violet-900 hover:from-fuchsia-700 font-Negar text-white text-center  text-2xl bg-gradient-to-bl from-violet-900 to-fuchsia-700 rounded-lg px-6 py-3 w-60 items-center justify-center">
            نمایش همه 
            <svg aria-hidden="true" class="ml-2 -mr-1 w-4 h-4" fill="currentColor" viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd"
            d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
            clip-rule="evenodd"></path>
        </svg>
    </a>
    <h2
        class=" font-Negar text-white text-center  text-2xl bg-gradient-to-bl from-violet-900 to-fuchsia-700 rounded-lg px-6 py-3 w-64 items-center justify-center">
        وکتور آرت های اخیر</h2>
        </div>
        <br/>
        <swiper :slidesPerView="1" :spaceBetween="50" :breakpoints="
    {
        '640': { slidesPerView: 1, spaceBetween: 50, },
        '856': { slidesPerView: 2, spaceBetween: 50, },
        '1210': { slidesPerView: 3, spaceBetween: 50, },
    }" :modules="modules" class="mySwiper my-14 w-3/5 mx-auto  justify-center">



            <SwiperSlide v-for=" portfolio in getVectors.reverse().slice(0, 5)" :key="portfolio">

                <div
                    class="max-w-sm font-Negar  rounded-lg border  shadow-md bg-gray-900/40 border-gray-700 ">

                    <img class=" rounded" :src="'http://127.0.0.1:8000/media/p/' + portfolio.topic" alt="khali">

                    <div class="p-5 ">

                        <h7 class="mt-2 text-xl font-bold tracking-tight  text-white lg:text-2xl">
                            {{ portfolio.case }}</h7>
                        <p class="mt-5 font-normal  text-gray-200 ">{{ portfolio.subject }}</p>

                    </div>
                </div>
            </SwiperSlide>
        </swiper>
    </div>



</template>
<script>
import axios from "axios"
import { Swiper, SwiperSlide } from "swiper/vue";
import "swiper/css";
export default {
    name: 'PortfolioCards',
    data() {
        return {
            portfolios: []
        }
    },
    computed: {
        getPosters() {
            return this.portfolios.filter(p => p.case === 'پوستر')
        },
        getBanners() {
            return this.portfolios.filter(b => b.case === 'بنر')
        },
        getLogo() {
            return this.portfolios.filter(l => l.case === 'لوگو')
        },
        getBcard() {
            return this.portfolios.filter(bc => bc.case === 'بیزینس کارت')
        },
        getVectors() {
            return this.nemuoneKareman.filter(p => p.case === 'وکتور')
        }

    },
    components: {
        Swiper,
        SwiperSlide,
    },
    mounted() {
        this.getPortfolios()
    },
    methods: {
        getPortfolios() {
            axios
                .get('/api/v1/portfolios')
                .then((r) => {
                    console.log(r.data)
                    this.portfolios = r.data
                })
                .catch((e) => {
                    console.log(e)
                })
        }
    },
    setup() {
        return {
            modules: [],
        };
    },
};
</script>

<style>
.swiper-slide {
    text-align: center;
    font-size: 18px;


    /* Center slide text vertically */
    display: -webkit-box;
    display: -ms-flexbox;
    display: -webkit-flex;
    display: flex;
    -webkit-box-pack: center;
    -ms-flex-pack: center;
    -webkit-justify-content: center;
    justify-content: center;
    -webkit-box-align: center;
    -ms-flex-align: center;
    -webkit-align-items: center;
    align-items: center;
}

.swiper-slide img {
    display: block;
    width: 100%;
    height: 100%;
    object-fit: cover;
}
</style>