<template>
    <div>
        <NavBar />
        <SuccessToast v-if="toast" action=" ثبت سفارش" class=" m-80" />
        <div>
            <form @submit.prevent="submit"
                class="text-right  mt-10 mb-10 ml-60 mr-60 p-5  rounded-lg shadow border  bg-gray-900/60 border-gray-700">
                <div class="flex items-center text-center justify-center">
                    <svg class=" w-16 h-16" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>
                    <h1 class="text-center text-5xl text-white font-Negar"> ثبت سفارش</h1>ّ
                </div>
                <p class="font-Negar my-6  text-white">توجه!!!برای ثبت سفارش ابتدا باید وارد شوید
                </p>
                <div class="mb-6">
                    <label for="topic"
                        class="block  text-right mb-2 text-2xl  font-Negar  text-white">عنوان</label>
                    <input type="text" id="topic"
                        class="shadow-sm text-right border  text-2xl  rounded-lg  block w-full p-2.5 bg-gray-700/40 border-gray-600 placeholder-gray-400 text-white  shadow-sm-light"
                        placeholder="" required v-model="form.topic">
                </div>
                <div class="mb-6">
                    <label for="format"
                        class="block mb-2 text-2xl font-Negar  text-white">قالب</label>
                    <input type="text" id="format"
                        class="shadow-sm  border  text-2xl  rounded-lg text-right block w-full p-2.5 bg-gray-700/40 border-gray-600 placeholder-gray-400 text-white  shadow-sm-light"
                        placeholder="" required v-model="form.case">
                    <p class="font-Negar  text-white">برای قالب یکی از موارد (لوگو -وکتور - بیزینس کارت - بنر
                        - پوستر) را تایپ نمایید</p>
                </div>
                <div class="mb-6">
                    <label for="subject"
                        class=" text-right block mb-2 text-2xl  font-Negar  text-white">موضوع</label>
                    <input type="text" id="subject"
                        class="shadow-sm  border  text-2xl text-right rounded-lg  block w-full p-2.5 bg-gray-700/40 border-gray-600 placeholder-gray-400 text-white  shadow-sm-light"
                        placeholder="" required v-model="form.subject">
                </div>
                <div class="mb-6">
                    <label for="content"
                        class="block mb-2 text-2xl  font-Negar  text-white">متن</label>
                    <textarea id="content" rows="4"
                        class="block text-right p-2.5 w-full text-xl    rounded-lg border  bg-gray-700/40 border-gray-600 placeholder-gray-400 text-white  focus:border-blue-500"
                        placeholder=".....متن پوستر را بنویسید" required v-model="form.content"></textarea>
                </div>
                <div class="mb-6">
                    <label for="description"
                        class="block mb-2 text-2xl  font-Negar  text-white">توضیحات</label>
                    <textarea id="description" rows="4"
                        class="block text-right p-2.5 w-full text-xl    rounded-lg border  bg-gray-700/40 border-gray-600 placeholder-gray-400 text-white  focus:border-blue-500"
                        placeholder=".....اگر توضیحی دارید بنویسید" v-model="form.description"></textarea>
                </div>

                <!-- <div>
                        <label class="block mb-2 text-2xl  font-Negar  text-white"
                            for="file_input">بارگزاری تصویر</label>
                        <input type="file" @change="onFileChange" v-on:change="form.o_image"
                            class="block w-full text-2xl   border rounded-lg cursor-pointer  text-gray-400 focus:outline-none bg-gray-700/40 border-gray-600 placeholder-gray-400">
                        <p class="mt-1 text-2xl   text-gray-300" id="file_input_help">SVG, PNG, JPG
                        </p>
                </div> -->
                <br>
                <button type="submit"
                    class=" inline-flex  hover:to-violet-900 hover:from-fuchsia-700 font-Negar text-white text-center  text-2xl bg-gradient-to-bl from-violet-900 to-fuchsia-700 rounded-lg px-6 py-3 w-60 items-center justify-center">ثبت
                    سفارش</button>
            </form>

        </div>
    </div>
</template>
<script>
import NavBar from '@/components/NavBar.vue'
import SuccessToast from '@/components/SuccessToast.vue'
import axios from 'axios'
export default {
    name: 'SabtSefaresh',
    components: {
        NavBar,
        SuccessToast
    },
    data() {
        return {
            form: {},
            toast: false
        }
    },
    methods: {
        submit() {
            console.log(this.form)
            axios
                .post('/api/v1/orders/', this.form)
                .then((r) => {
                    console.log(r)
                    this.toast = true
                    setTimeout(() => {
                        this.$router.push('/')
                    }, 2000);
                })
                .catch((e) => {
                    console.log(e)
                    setTimeout(() => {
                        alert('برای ثبت سفارش ابتدا وارد شوید//دوباره تلاش کنید')
                    }, 100);
                })
        }


    }
}
</script>