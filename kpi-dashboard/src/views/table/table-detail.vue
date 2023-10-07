<template>
    <div>
        <a-spin :spinning="loading_status" size="large" :delay="100" tip="数据加载中">
            <div class="d_flex fd_c gap_20 h_p100">
                <table-filter v-if="filter_data.index_class" :filter_data="filter_data"
                    @getFilterOptions="handleFilterOptions"></table-filter>
                <table-main v-if="table_data.table_id" :table_data="table_data" :page_data="page_data" :spin_status="fetching_status" :clean_expand="clean_expand" class="h_p100"
                    @getDateRange="handleRangeOptions"
                    @getPageOptions="handlePageOptions"
                    @getChildOptions="handleChildOptions"></table-main>
            </div>
        </a-spin>
    </div>



</template>

<style>
@import url('@/assets/style/overwrite.css');
@import url('@/assets/style/colorset.css');
@import url('@/assets/style/common.css');
</style>

<script>
import { defineComponent, ref } from 'vue';
import { Spin } from 'ant-design-vue';
import TableFilter from '@/components/table/table-filter.vue';
import TableMain from '@/components/table/table-main.vue';

import dayjs from 'dayjs';
import 'dayjs/locale/zh-cn';
import locale from 'ant-design-vue/es/date-picker/locale/zh_CN';

import { api } from '@/utils/commonApi.js';
import { tableRouteMap, orgMap } from '@/assets/config/table-data.js';
import { useRoute } from 'vue-router';

const myApi = api();

export default defineComponent({
    name: "EnterpriseTable",
    components: {
        'table-filter': TableFilter,
        'table-main': TableMain,
        'a-spin': Spin
    },
    data() {
        return {}
    },
    setup() {
        const route = useRoute();
        
        return {
            locale,
            loading_status: ref(false),
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
                data_range: ref([]),
                page: ref(1),
                size: ref(0),
                parent: ref()
            }),
            page_data: ref({
                current:ref(),
                total:ref(),
                pageSize:ref(),
                sizeOptions:ref([])
            }),
            fetching_status: ref(false),
            clean_expand: ref(false)
        }
    },
    mounted() {
        this.loading_status = true
        this.getFilterData().then(
            ()=>{
                // this.loading_status = true;
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
                this.getTableData().then(()=>{this.loading_status = false;});

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
            this.fetching_status = true;
            const post_data = {
                index:this.search_form.index,
                date:this.search_form.data_range,
                group:this.search_form.org_group,
                page:this.search_form.page,
                size:this.search_form.size
            }
            const table_res = await myApi.post('/api/table/getTableData',post_data)
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
            console.log(1)
            this.clean_expand = true
            // 处理分页数据
            this.page_data.current = table_data.page_no,
            this.page_data.total = table_data.data_total,
            this.page_data.pageSize = table_data.data.length,
            this.page_data.sizeOptions = [String(table_data.data.length),String(table_data.data.length*2),String(table_data.data.length*3)]

            this.fetching_status = false;
        },
        handleRangeOptions(dataRange) {
            this.search_form.data_range = dataRange.date_range
            this.getTableData();
        },
        handleFilterOptions(item) {
            this.search_form.org_group = item.org;
            this.search_form.index = item.index;
            this.search_form.class = item.class;
            this.getTableData();
        },
        handlePageOptions(item) {
            this.search_form.page = item.page
            this.search_form.size = item.size
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
                const child_res = await myApi.post('/api/table/getTableData',child_form)
                target_data.children = child_res.data.data
                this.clean_expand = false
                // 处理合并表头
                // const column_date = this.table_data.table_columns.find((item)=>item.key=='detail_date')
                // console.log(column_date)
                // column_date.customCell = (_,index) => {if (index == item.key) {console.log(index);return {rowSpan: child_res.data.data.length + 1}}}
                // 处理合并表头结束
                this.fetching_status = false
            } 
        }
    }
})

</script>