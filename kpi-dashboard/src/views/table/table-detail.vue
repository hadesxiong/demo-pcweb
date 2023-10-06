<template>
    <div class="d_flex fd_c gap_20 h_p100">
        <table-filter v-if="filter_data.index_class" :filter_data="filter_data"
            @getFilterOptions="handleFilterOptions"></table-filter>
        <table-main v-if="table_data.table_id" :table_data="table_data" @getDateRange="handleRangeOptions"></table-main>
    </div>
</template>

<style>
@import url('@/assets/style/overwrite.css');
@import url('@/assets/style/colorset.css');
@import url('@/assets/style/common.css');
</style>

<script>
import { defineComponent, ref } from 'vue';
import TableFilter from '@/components/table/table-filter.vue';
import TableMain from '@/components/table/table-main.vue';

import dayjs from 'dayjs';
import 'dayjs/locale/zh-cn';
import locale from 'ant-design-vue/es/date-picker/locale/zh_CN';

// import axios from 'axios';
import { api } from '@/utils/commonApi.js';
import { tableRouteMap, orgMap } from '@/assets/config/table-data.js';
import { useRoute } from 'vue-router';

const myApi = api();

export default defineComponent({
    name: "EnterpriseTable",
    components: {
        'table-filter': TableFilter,
        'table-main': TableMain,
    },
    data() {
        return {}
    },
    setup() {
        const route = useRoute();
        
        return {
            locale,
            filter_data: ref({
                org_filter: ref(orgMap),
                index_class: ref([]),
                index_list: ref([])
            }),
            table_data: ref({
                table_columns: ref([]),
                table_data: ref([]),
                table_id: ref()
            }),
            query_data: ref({}),
            table_class: ref(route.params.table_class),
            class_line: ref(tableRouteMap[route.params.table_class]),
            search_form: ref({
                org_group: ref(1),
                index: ref([]),
                class: ref([]),
                type: ref('normal'),
                data_range: ref([])
            })
        }
    },
    mounted() {
        this.getFilterData().then(
            ()=>{
                const class_list = this.filter_data.index_class.filter(item=>item.value!='all').map(item=>item.value)
                const index_list = class_list.flatMap(each_class=>{
                    const obj = this.filter_data.index_list.find(item => item.class == each_class)
                    return obj? obj.label_list:[]
                }).map(item => item.value)
                this.search_form.index = index_list;
                this.search_form.data_range = [
                    dayjs().add(-5,'month').startOf('month').format('YYYY-MM-DD'),
                    dayjs().add(-5,'month').endOf('month').format('YYYY-MM-DD'),
                ]
                this.getTableData();
            }
        );
        // 初始化参数
        // this.getTableData();
    },
    methods: {
        async getFilterData() {
            const filter_res = await myApi.get('/api/table/getTableFilter',{params:{line:this.class_line}})
            this.filter_data.index_list = filter_res.data.data.index_list;
            this.filter_data.index_class = filter_res.data.data.index_class;
        },
        async getTableData() {
            // const table_res = await axios.get('/demo/table/table-main.json');
            const post_data = {
                index:this.search_form.index,
                date:this.search_form.data_range,
                group:this.search_form.org_group
            }
            const table_res = await myApi.post('/api/table/getTableData',post_data)
            // console.log(table_res.data)
            this.table_data.table_columns = table_res.data.title
            this.table_data.table_data = table_res.data.data
            this.table_data.table_id = 'table_id'
            // console.log(this.table_data)
        },
        handleRangeOptions(dataRange) {
            console.log(dataRange);
            this.search_form.data_range = [
                dayjs(dataRange[0]).startOf('month').format('YYYY-MM-DD'),
                dayjs(dataRange[1]).endOf('month').format('YYYY-MM-DD')
            ]
        },
        handleFilterOptions(item) {
            this.search_form.org_group = item.org;
            this.search_form.index = item.index;
            this.search_form.class = item.class;
            console.log(this.search_form)
            console.log(item)
            // this.getTableData();
        }
    }
})

</script>