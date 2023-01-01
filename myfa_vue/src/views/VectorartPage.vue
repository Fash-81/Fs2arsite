<template>
    <NavBar/>
    <h1 class="text-5xl mt-10 text-center  text-white font-Negar">وکتور آرت ها</h1>
      <div class="overflow-x-auto items-center sm:rounded-lg w-7/8 mx-20 mb-10 ">
        <table class=" w-full text-xl text-center  font-Negar  -white mt-20">
            <thead class="text-3xl  uppercase bg-gradient-to-l from-violet-900 to-purple-700 text-white">
                <tr class="mt-5">
                    <th scope="col" class="py-3 px-6">
                        تصویر
                    </th>
                    <th scope="col" class=" hidden lg:table-cell py-3 px-5">
                        توضیحات
                    </th>
 
                    <th scope="col" class="  py-3 px-6">
                        عنوان
                    </th>
                </tr>
            </thead>
            <tbody v-for="Portfilio in getVectors"
                    :key="Portfilio">
                <tr class=" border-b bg-gray-900/40 border-gray-700 text-white"   >
                    <td class=" flex justify-center py-4 px-10">
                        <img class="   rounded" :src="'http://127.0.0.1:8000/media/p/' + Portfilio.topic" :alt="Portfilio.topic"
                            width="150" height="300">
                    </td>
                    <td class=" hidden lg:table-cell py-4 px-5">
                        {{ Portfilio.description }}
                    </td>

                    <td class=" py-4 px-6">
                        {{ Portfilio.subject }}
                    </td>
                </tr>

            </tbody>
        </table>
    </div>

</template>
<script>
import NavBar from '@/components/NavBar.vue'
import axios from 'axios'
export default {
    name: 'VectorartPage',
    components: {
        NavBar
    },
    data() {
        return {
            nemuoneKareman: []
        }
    },
    computed: {
        getVectors() {
            return this.nemuoneKareman.filter(v => v.case === 'وکتور')
        }
    },
    mounted() {
        this.getNemuoneKareman()
    },
    methods: {
        getNemuoneKareman() {
            axios
                .get('/api/v1/portfolios')
                .then((r) => {
                    console.log(r.data)
                    this.nemuoneKareman = r.data
                })
                .catch((e) => {
                    console.log(e)
                })

        }
    }
}
</script>