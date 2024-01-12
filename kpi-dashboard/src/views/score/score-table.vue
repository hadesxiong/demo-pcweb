<template>
    <div class="h_p100">
        <!-- 主页面 -->
        <div class="d_flex fd_c gap_20 h_p100">
            <table-main v-if="table_data.table_id" :table_data="table_data" :page_data="page_data" :spin_status="fetching_status" :clean_expand="clean_expand" class="h_p100"
                :extra_filter="true"
                :filter_list="filter_data"
                @getMenuOptions="handleMenuOptions"
                @getDateRange="handleRangeOptions"
                @getPageOptions="handlePageOptions"
                @getChildOptions="handleChildOptions"></table-main>
        </div>
    </div>
</template>

<style>
@import url('@/assets/style/overwrite.css');
@import url('@/assets/style/colorset.css');
@import url('@/assets/style/common.css');
</style>

<style scoped>
</style>

<script>
import { defineComponent, ref } from 'vue';
// import { Skeleton } from 'ant-design-vue';
import TableMain from '@/components/table/table-main.vue';

import dayjs from 'dayjs';
import 'dayjs/locale/zh-cn';
import locale from 'ant-design-vue/es/date-picker/locale/zh_CN';

import { api } from '@/utils/commonApi.js';
import { orgOptions, scoreOptions } from '@/assets/config/score-table.js'; 

const myApi = api();

export default defineComponent({
    name: 'ScoreTable',
    components: {
        'table-main': TableMain,
        // 'a-skeleton': Skeleton
    },
    data() {
        return {
            filter_data: [
                {filter_name:'org_map',filter_data:orgOptions},
                {filter_name:'score_map',filter_data:scoreOptions}
            ]
        }
    },
    setup() {
        return {
            locale,
            loading_status: ref(false),
            score_data: ref({}),
            table_data: ref({
                table_columns: ref([]),
                table_data: ref([]),
                table_id: ref([])
            }),
            search_form: ref({
                org_option: ref(1),
                score_option: ref('all'),
                date_range: ref([]),
                page: ref(1),
                size: ref(0),
                parent: ref()
            }),
            page_data: ref({
                current: ref(),
                total: ref(),
                pageSize: ref(),
                sizeOptions: ref([])
            }),
            fetching_status: ref(false),
            clean_expand: ref(false)
        }
    },
    mounted() {
        this.loading_status = true
        this.search_form.index = 'all'
        this.search_form.date_range = [
            dayjs().add(-1,'month').startOf('month').format('YYYY-MM-DD'),
            dayjs().add(-1,'month').endOf('month').format('YYYY-MM-DD'),
        ]
        this.getTableData().then(()=>{this.loading_status = false;})
        this.getScoreData().then(()=>{})
    },
    methods: {
        async getTableData() {
            // const table_res = await axios.get('/demo/table/table-main.json');
            this.fetching_status = true;
            const post_data = {
                index:this.search_form.score_option,
                date:this.search_form.date_range,
                group:this.search_form.org_option,
                page:this.search_form.page,
                size:this.search_form.size
            }
            // const table_res = await myApi.post('/api/table/getTableData',post_data)
            const table_res = await myApi.post('/api/score/getScoreTable',post_data)
            // console.log(table_res)
            let table_data = {}
            if (typeof(table_res.data) == 'string') {
                table_data = eval('('+table_res.data+')')
            } else {
                table_data = table_res.data
            }
            // console.log(table_data)
            this.table_data.table_columns = table_data.title
            this.table_data.table_data = table_data.data
            // 为data添加key
            this.table_data.table_data = this.table_data.table_data.map((item, index) => { return { ...item, key: index.toString() } });
            this.table_data.table_id = 'table_id'
            this.clean_expand = true
            // 处理分页数据
            this.page_data.current = table_data.page_no,
            this.page_data.total = table_data.data_total,
            this.page_data.pageSize = table_data.data.length,
            this.page_data.sizeOptions = [String(table_data.data.length),String(table_data.data.length*2),String(table_data.data.length*3)]

            this.fetching_status = false;
        },
        async getScoreData() {
            const org_num = localStorage.getItem('org_num')
            const data_date = dayjs().add(-1,'month').endOf('month').format('YYYY-MM-DD')
            const score_res = await myApi.get('/api/score/getScoreData',{params:{org:org_num,date:data_date}})
            this.score_data = score_res.data.data
            console.log(this.score_data)
        },
        handleRangeOptions(dateRange) {
            this.search_form.date_range = dateRange.date_range
            this.getTableData();
        },
        handlePageOptions(item) {
            this.search_form.page = item.page
            this.search_form.size = item.size
            this.getTableData()
        },
        handleMenuOptions(item) {
            this.search_form[item.title] = item.data.ref_code
            this.getTableData()
        },
        async handleChildOptions(item) {
            // 判断数据是否为空
            const target_data = this.table_data.table_data.find((each)=>each.key === item.key)
            if (target_data.children.length == 0 ) {
                this.fetching_status = true
                const child_form = {
                    index: this.search_form.index,
                    date: [item.date,item.date],
                    parent: item.parent,
                    group: 1,
                    type: 'parent',
                }
                const child_res = await myApi.post('/api/score/getScoreTable',child_form)
                target_data.children = child_res.data.data
                this.clean_expand = false
                this.fetching_status = false
            } 
        }
    }
})
</script>