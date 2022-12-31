<template>
    <NavBar />
    <div class=" absolute lg:relative items-center text-center justify-center mx-40 mt-40  ">
        <div
            class="relative flex flex-col min-w-0 break-words b   bg-gray-900/70 text-white w-full mb-6 shadow-xl rounded-lg mt-30">
            <div class="px-6">
                <!-- <div class="flex flex-wrap justify-center"> -->
                <div class="w-full  px-4 lg:order-2 flex justify-center">
                    <div class="relative flex items-center justify-center">
                        <img alt="..." src="../assets/profile-pic.jpg"
                            class="shadow-xl rounded-full h-auto align-middle border-none absolute  "
                            style="max-width: 250px;" />
                    </div>
                </div>
                <div class="w-full lg:w-4/12 px-4 lg:order-3 lg:text-right lg:self-center">
                    <div class="py-6 px-3 mt-0">

                    </div>
                </div>
                <div class="w-full lg:w-4/12 px-4 lg:order-1">
                    <div class="flex justify-center py-4 lg:pt-4 pt-8">

                    </div>
                </div>
                <!-- </div> -->
                <div class="   ml-30   text-white font-Negar mt-16">

                    <div>
                        <h3 class="text-4xl items-center text-center justify-between leading-normal mb-2">
                            فاطمه احمدنژاد شرامین
                        </h3>
                    </div>
                    <div class="mt-5 flex items-center text-center justify-center">
                        <p class="px-5">کرج-ایران</p>
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                            xmlns="http://www.w3.org/2000/svg">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z">
                            </path>
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
                        </svg>
                    </div>
                    <div class=" mt-5 flex items-center text-center justify-center">
                        <p class="px-5">یک معلم گرافیست یا یه گرافیست معلم</p>
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                            xmlns="http://www.w3.org/2000/svg">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z">
                            </path>
                        </svg>
                    </div>
                    <div class="my-5 flex items-center text-center justify-center">
                        <p class="px-5">دانشجوی علوم کامپیوتر خوارزمی</p>
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                            xmlns="http://www.w3.org/2000/svg">
                            <path d="M12 14l9-5-9-5-9 5 9 5z"></path>
                            <path
                                d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z">
                            </path>
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M12 14l9-5-9-5-9 5 9 5zm0 0l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14zm-4 6v-7.5l4-2.222">
                            </path>
                        </svg>
                    </div>
                </div>
                <hr>
                <div class="mt-5 py-5 flex justify-between font-Negar  text-right">
                    <div>
                        <div class="  mx-10 flex items-center text-center justify-center">
                            <p class=" text-3xl">دست آوردها</p>
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                                xmlns="http://www.w3.org/2000/svg">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z">
                                </path>
                            </svg>
                        </div>
                        <p class="text-center pt-2">مدال نقره جهانی المپیاد علوم زمین</p>
                        <p class=" text-center pt-2">مدال طلا کشوری المپیاد علوم زمین</p>
                        <p class=" text-center pt-2"> برگزیده کشوری مسابقات فرهنگی هنری رشته وبلاگ نویسی</p>
                        <p class=" text-center pt-2"> مدال برنز تیمی مسابقه ریاضی ا-لیمپیاد</p>
                        <p class=" text-center pt-2">مدال نقره و برنز در مسابقات دوئل و چلچراغ خانه ریاضی</p>
                        <p class=" text-center pt-2">پروژه خواب رم جزو 10 پروژه برتر مسابقات علوم اعصاب شناختی</p>
                    </div>
                    <div>
                        <div class="  mx-10 flex items-center text-center justify-center">
                            <p class=" text-3xl">سوابق شغلی</p>
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                                xmlns="http://www.w3.org/2000/svg">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z">
                                </path>
                            </svg>
                        </div>
                        <p class=" text-center pt-2">مدرس المپیاد در کلاس های استانی استان البرز-دوره اول و دوم فرزانگان4کرج- باشگاه دانش پژوهان</p>
                        <p class=" text-center pt-2">واحد اجرایی المپیاد دبیرستان فرزانگان 4 کرج</p>
                        <p class=" text-center pt-2">استاد راهنمای پروژه برنامه نویسی اسکرچ مقطع ابتدایی</p>
                        <p class=" text-center pt-2">رابط کمیته علوم زمین باشگاه دانش پژوهان</p>
                        <p class=" text-center pt-2">طراح پوستر های المپیاد استانی و فرزانگان  4 کرج</p>
                    </div>
                    <div>
                        <div class="mx-10 flex items-center text-center justify-center">
                            <p class=" text-3xl">سوابق تحصیلی</p>
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                                xmlns="http://www.w3.org/2000/svg">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253">
                                </path>
                            </svg>
                        </div>
                        <p class=" text-center pt-2">متوسطه اول فرزانگان 4 کرج</p>
                        <p class=" text-center pt-2">دیپلم فرزانگان 4 کرج</p>
                        <p class=" text-center pt-2">دانشجوی علوم کامپیوتر دانشگاه خوارزمی</p>
                    </div>
                </div>

                <div class="mt-5 py-5 flex font-Negar  justify-between text-right">
                    <div>
                        <div class="  mx-10 flex items-center text-center justify-center">
                            <p class="  text-3xl">تحقیقات</p>
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                                xmlns="http://www.w3.org/2000/svg">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z">
                                </path>
                            </svg>
                        </div>
                        <p class=" text-center pt-2"> تاثیر خواب رم بر عملکرد اجرایی مسابقات علوم اعصاب شناختی</p>
                    </div>
                    <div>
                        <div class="  mx-10 flex items-center text-center justify-center ">
                            <p class=" text-3xl">مهارت ها</p>
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                                xmlns="http://www.w3.org/2000/svg">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z">
                                </path>
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
                            </svg>
                        </div>
                        <p class=" text-center pt-2">تسلط بر نرم افزار های ایلاستریتور - فتوشاپ و توانایی کار با سایر  نرم افزار های ادوبی مثل پریمیر و000 </p>
                        <p class=" text-center pt-2">مسلط بر زبان پایتون- اسکرچ</p>
                        <p class=" text-center pt-2">ICDL مسلط بر مهارت های</p>
                        <p class=" text-center pt-2">مسئولیت پذیر</p>
                    </div>
                    <div>
                        <div class="mx-10 flex items-center text-center justify-center">
                            <p class=" text-3xl">راه ارتباطی</p>
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                                xmlns="http://www.w3.org/2000/svg">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z">
                                </path>
                            </svg>
                        </div>
                        <p class=" text-center pt-2">Instagram: fatemeh.ahmadneZhad_</p>
                        <p class=" text-center pt-2">Telegram: @Fash_81</p>
                        <p class=" text-center pt-2">Telephone: 09337213591</p>
                        <p class=" text-center pt-2">Email: fahmadnezhad1395@gmail.com</p>
                    </div>
                </div>

            </div>
        </div>
    </div>
</template>
<script>
import NavBar from '@/components/NavBar.vue'

export default {
    name: 'AboutMe',
    components: {
        NavBar
    }
}
</script>