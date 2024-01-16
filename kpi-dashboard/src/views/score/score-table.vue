<template>
    <div class="h_p100">
        <div v-if="loading_status" class="d_flex fd_c gap_20 h_p100">
            <div class="bg_white w_p100 p_20 d_flex fd_c gap_8">
                <div class="w_p100 h_a d_flex gap_20 jc_c fai_c">
                    <a-skeleton :active="true" :paragraph="{ rows: 1, width:'100%' }" :title="false"></a-skeleton>
                </div>
                <div class="w_p100 h_a d_flex gap_20 jc_c fai_c">
                    <a-skeleton-image :active="true"></a-skeleton-image>
                    <a-skeleton :active="true" :paragraph="{ rows: 7, width:'100%' }" :title="false"></a-skeleton>
                </div>
            </div>
            <div class="bg_white w_p100 h_a br_2 p_20 d_flex fd_c gap_20">
                <div class="w_p100 h_a d_flex gap_20 jc_sb fai_c">
                    <div class="d_flex gap_20">
                        <a-skeleton-input :active="true"></a-skeleton-input>
                        <a-skeleton-input :active="true"></a-skeleton-input>
                        <a-skeleton-input :active="true"></a-skeleton-input>
                    </div>
                    <a-skeleton-button :active="true"></a-skeleton-button>
                </div>
                <a-skeleton :active="true" :paragraph="{ rows: 16, width:'100%' }" :title="false"></a-skeleton>
            </div>
        </div>
        <div v-else class="h_p100 d_flex fd_c gap_20">
            <div class="d_flex fd_c bg_white gap_20 p_20" :class="db_collaspe ? 'normal_height' : 'collapse_height'">
                <div class="d_flex jc_sb">
                    <div class="d_flex gap_20">
                        <div>考核数据时间: {{score_info.score_date}}</div>
                        <div>考核机构: {{score_info.score_org}}</div>
                    </div>
                    <div>
                        <a-button v-if="db_collaspe" type="text" class="br_2 fai_c d_flex fc_brand6"
                            style="width:auto;padding: 4px 15px;" @click="toggleIndex">
                            <template #icon>
                                <icon-doubleUp size="14" class="mr_8 lh_1"></icon-doubleUp>
                                收起
                            </template>
                        </a-button>
                        <a-button v-else type="text" class="br_2 fai_c d_flex fc_brand6" style="width:auto;padding: 4px 15px;"
                            @click="toggleIndex">
                            <template #icon>
                                <icon-doubleDown size="14" class="mr_8 lh_1"></icon-doubleDown>
                                展开
                            </template>
                        </a-button>
                    </div>

                </div>
                <div class="d_flex bg_white fai_c">
                    <div>
                        <gauge-one :gauge_data="score_data" :color_list="score_color" db_index="gauge_one"></gauge-one>
                    </div>
                    <div class="d_flex fwrap_w gap_20">
                            <a-row :gutter="[20,20]">
                                <a-col :lg="8" :xl="6" v-for="(item,index) in score_data" :key="item.index_num">
                                    <step-one v-if="item.index_num" :step_data="item" :color="step_color[index]"></step-one>
                                </a-col>
                            </a-row>
                    </div>
                </div>
            </div>
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
    </div>

</template>

<style>
@import url('@/assets/style/overwrite.css');
@import url('@/assets/style/colorset.css');
@import url('@/assets/style/common.css');

.ant-skeleton.ant-skeleton-element .ant-skeleton-image {
    width: 200px;
    height: 200px;
}
</style>

<style scoped>
.normal_height {
    height: auto;
}
.collapse_height {
    height: 72px;
    overflow: hidden;
}
</style>

<script>
import { defineComponent, ref } from 'vue';
import { Col,Row, Skeleton, SkeletonButton, SkeletonInput, SkeletonImage, Button } from 'ant-design-vue';
import { DoubleUp, DoubleDown } from '@icon-park/vue-next';
import TableMain from '@/components/table/table-main.vue';
import GaugeOne from '@/components/dashboard/gauge-one.vue';
import StepOne from '@/components/dashboard/step-one.vue';

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
        'step-one': StepOne,
        'gauge-one': GaugeOne,
        'a-col': Col,
        'a-row': Row,
        'a-skeleton': Skeleton,
        'a-skeleton-button': SkeletonButton,
        'a-skeleton-input': SkeletonInput,
        'a-skeleton-image': SkeletonImage,
        'a-button': Button,
        'icon-doubleUp': DoubleUp,
        'icon-doubleDown': DoubleDown

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
            score_data: ref([]),
            score_info:ref({
                score_org: localStorage.getItem('org_name'),
                score_date: dayjs().add(-1,'month').endOf('month').format('YYYY-MM')
            }),
            score_color: ref(['#2563EB','#FF6E66','#C34CD9','#F7BA1E','#1EF734']),
            step_color: ref(['blue','red','pink','yellow','green']),
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
            clean_expand: ref(false),
            db_collaspe: ref(true)
        }
    },
    mounted() {
        this.loading_status = true
        this.search_form.index = 'all'
        this.search_form.date_range = [
            dayjs().add(-1,'month').startOf('month').format('YYYY-MM-DD'),
            dayjs().add(-1,'month').endOf('month').format('YYYY-MM-DD'),
        ]
        this.getScoreData().then(
            ()=>{
                this.getTableData().then(()=>{this.loading_status = false;})
            }
        )
    },
    methods: {
        async getTableData() {
            this.fetching_status = true;
            const post_data = {
                index:this.search_form.score_option,
                date:this.search_form.date_range,
                group:this.search_form.org_option,
                page:this.search_form.page,
                size:this.search_form.size
            }
            const table_res = await myApi.post('/api/score/getScoreTable',post_data)
            let table_data = {}
            if (typeof(table_res.data) == 'string') {
                table_data = eval('('+table_res.data+')')
            } else {
                table_data = table_res.data
            }
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
        },
        toggleIndex() {
            this.db_collaspe = !this.db_collaspe;
        },
    }
})
</script>