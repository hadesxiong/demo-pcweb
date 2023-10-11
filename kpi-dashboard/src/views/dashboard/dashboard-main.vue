<template>
    <div class="of_h">
        <a-row :gutter="[20, 20]" style="display: flex; align-items: stretch;">
            <a-col :span="24">
                <db-card1 :card_data="rt_cb" :org_filter="orgFilter_data"
                    :db_index="'rt_cb'" @getDBFilters="handleDBFilters" key="rt_cb"></db-card1>
            </a-col>
            <a-col :span="12">
                <db-bar2 :bar_data="all_aum" :org_filter="orgFilter_data" 
                    :db_index="'all_aum'" @getDBFilters="handleDBFilters" key="all_aum"></db-bar2>
            </a-col>
            <a-col :span="12">
                <db-card1 v-if="et_cb" :card_data="et_cb" :org_filter="orgFilter_data"
                    :db_index="'et_cb'" @getDBFilters="handleDBFilters" key="et_cb"></db-card1>
            </a-col>
            <a-col :span="12">
                <db-line :line_data="all_ckrj" :org_filter="orgFilter_data" 
                :db_index="'all_ckrj'" @getDBFilters="handleDBFilters" key="all_ckrj"></db-line>
            </a-col>
            <a-col :span="12">
                <db-bar1 :bar_data="all_yyjsr" :org_filter="orgFilter_data"
                    :db_index="'all_yyjsr'" @getDBFilters="handleDBFilters" key="all_yyjsr"></db-bar1>
            </a-col>
            <a-col :span="12">
                <db-bar1 :bar_data="all_eva" :org_filter="orgFilter_data"
                    :db_index="'all_eva'" @getDBFilters="handleDBFilters" key="all_eva"></db-bar1>
            </a-col>
            <a-col :span="12">
                <db-card1 :card_data="all_lcrj" :org_filter="orgFilter_data"
                    :db_index="'all_lcrj'" @getDBFilters="handleDBFilters" key="all_lcrj"></db-card1>
            </a-col>
        </a-row>
    </div>
</template>

<style>
@import url('@/assets/style/colorset.css');
@import url('@/assets/style/common.css');

::-webkit-scrollbar {
    display: none;
}
</style>

<script>
import { defineComponent, ref } from 'vue';

import CardOne from '@/components/dashboard/card-one.vue';
import BarOne from '@/components/dashboard/bar-one.vue';
import BarTwo from '@/components/dashboard/bar-two.vue';
import LineOne from '@/components/dashboard/line-one.vue';

import { Col, Row } from 'ant-design-vue';

import { api } from '@/utils/commonApi.js';

import dayjs from 'dayjs';
import 'dayjs/locale/zh-cn';
import locale from 'ant-design-vue/es/date-picker/locale/zh_CN';

dayjs.locale('zh-cn');
const myApi = api();

export default defineComponent({
    name: 'DashboardMain',
    components: {
        'db-card1': CardOne,
        'db-bar1': BarOne,
        'db-bar2': BarTwo,
        'db-line': LineOne,
        'a-col': Col,
        'a-row': Row
    },
    setup() {
        return {
            orgFilter_data: ref([]),
            rt_cb: ref({}),
            et_cb: ref({}),
            all_lcrj: ref([]),
            all_yyjsr: ref({}),
            all_eva: ref({}),
            all_aum: ref({}),
            all_ckrj: ref({}),
            init_org: ref({}),
            init_date: ref([dayjs().add(-5, 'month'), dayjs()]),
            locale,
            search_form: ref({
                org: ref(),
                date: ref(),
                mark: ref('all')
            }),
            dashboard_data: ref({})
        }
    },
    async mounted() {
        const user_org = {org_num:localStorage.getItem('org_num'),org_name:localStorage.getItem('org_name')}
        this.init_org = user_org

        // 获取当前登陆用户所在机构
        const orgDeteil_params = {type:'single',target:user_org['org_num']}
        const orgDetail_res = await myApi.get('/api/org/getOrgInfo',{params:orgDeteil_params})
        this.org_group = orgDetail_res.data.data.org_group

        // 获取当前登陆用户所在分组的机构筛选
        const orgFilter_params = {type:'tree',target:user_org['org_num'],group:this.org_group}
        const orgFilter_res = await myApi.get('/api/org/getOrgInfo',{params:orgFilter_params})
        this.orgFilter_data = orgFilter_res.data.data

        // 获取初始化的数据看板
        this.search_form.org = this.init_org.org_num;
        this.search_form.date = [
            this.init_date[0].startOf('month').format('YYYY-MM-DD'),
            this.init_date[1].endOf('month').format('YYYY-MM-DD'),
        ]
        const init_dashRes = await this.getDashboardData(
            this.search_form.org,this.search_form.date,this.search_form.mark
        )
        this.dashboard_data = init_dashRes.data.data
        console.log(this.dashboard_data)
        this.drawDashboard(this.dashboard_data)
    },
    methods: {
        // 定义更新数据方法
        async getDashboardData(org,date,mark) {
            const dash_params = {org: org,start:date[0],end:date[1],mark}
            const dash_res = await myApi.get('/api/dashboard/getDashboard',{params:dash_params})
            return dash_res
        },
        // 接收每个组件传递的org/date/mark
        async handleDBFilters(item) {
            const db_res = await this.getDashboardData(item.org,item.date,item.mark);
            this.drawDashboard(db_res.data.data)
        },
        drawDashboard(data) {
            const dbIndex_list = Object.keys(data);
            dbIndex_list.forEach(
                (item)=>{ this[item] = data[item]}
            )
        }
    }
});

</script>