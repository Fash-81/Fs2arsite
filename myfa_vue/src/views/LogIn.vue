<template>
    <div>
        <NavBar />
        <SuccessToast v-if="toast" action="ورود" class=" m-5 " />
        <div class="flex flex-col  items-center justify-center px-6 py-8 mx-auto  lg:py-0">
            <div
                class="w-full  rounded-lg shadow border mt-20 max-w-md xl:p-0 bg-gray-900/70 border-gray-700">

                <div>
                    <button type="button" class=" mt-2 ml-2  bg-transparent rounded-lg text-sm p-1.5  inline-flex items-center hover:bg-gray-600 hover:text-white" data-modal-toggle="defaultModal"><a href="/">
                    <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
                    <span class="sr-only">Close modal</span>
                    </a>  
                </button>


                    <h1
                        class="text-xl text-center font-bold leading-tight tracking-tight  md:text-2xl text-white">
                        ورود به حساب کاربری
                    </h1>

                    <form @submit.prevent="submit" class="m-5" action="#">
                        <div>
                            <label for="text"
                                class="block mb-2 text-right text-sm font-medium  text-white">نام کاربری
                                </label>
                            <input type="text" name="username" id="username" v-model="form.username"
                                class=" border 0  sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 bg-gray-700/60 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500"
                                placeholder="abcd" required>
                        </div>
                        <div>
                            <label for="password"
                                class="block text-right mb-2 text-sm font-medium  text-white">رمز
                                عبور</label>
                            <input type="password" name="password" id="password" v-model="form.password"
                                placeholder="••••••••"
                                class=" border 0  sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 bg-gray-700/60 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500"
                                required>
                        </div>
                       <div class="mt-5 mb-3">
                        <button type="submit"
                            class="w-full inline-flex  hover:to-violet-900 hover:from-fuchsia-700 font-Negar text-white text-center  text-2xl bg-gradient-to-bl from-violet-900 to-fuchsia-700 rounded-lg px-6 py-3 items-center justify-center">ورود</button>
                        </div>
                            <div class=" text-right text-sm font-medium  text-gray-300"> حساب ندارید؟<a
                                href="/register"
                                class=" hover:underline text-blue-500"> ساخت حساب </a>
                        </div>

                    </form>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
import axios from 'axios'
import NavBar from '@/components/NavBar.vue'
import SuccessToast from '@/components/SuccessToast.vue'
export default {
    name: "LogIn",
    components:{
        NavBar,
        SuccessToast
    },
    data () {
        return {
            form: {},
            toast: false
        }
    },
    methods: {
        submit() {
            axios
              .post('/api/v1/token/login/', this.form)
              .then((r)=>{
                const token = r.data.auth_token
                this.$store.commit('setToken',token)
                localStorage.setItem('token',token)
                console.log('Token ' + token)
                axios.defaults.headers.common.Authorization ='Token ' + token
                this.toast =true
                setTimeout(() => {
                        this.$router.push('/')
                    }, 2000);
            })
            .catch((e)=>{
                    console.log(e)
                    setTimeout(() =>{
                        alert(' نام کاربری یا رمزعبور اشتباه می باشد')
                    },100);
                })
        }
    }
}
</script>