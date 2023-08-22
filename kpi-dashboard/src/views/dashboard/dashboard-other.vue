<template>
    <div class="of_h">
        <a-row :gutter="[20, 20]" style="display: flex; align-items: stretch;">
            <a-col :span="24">
                <db-card1 :card_data="dbCard1_data"></db-card1>
            </a-col>
            <a-col :span="12">
                <db-bar2 v-if="dbBar2_data.db_id" :bar_data="dbBar2_data" :db_id="dbBar2_data.db_id"></db-bar2>
            </a-col>
            <a-col :span="12">
                <db-card1 :card_data="dbCard2_data"></db-card1>
            </a-col>
            <a-col :span="12">
                <db-line v-if="dbLine_data.db_id" :db_data="dbLine_data" :db_id="dbLine_data.db_id"></db-line>
            </a-col>
            <a-col :span="12">
                <db-bar1 v-if="dbBar1_data.db_id" :bar_data="dbBar1_data"></db-bar1>
            </a-col>
            <a-col :span="12">
                <db-bar1 v-if="dbBar1_2_data.db_id" :bar_data="dbBar1_2_data"></db-bar1>
            </a-col>
            <a-col :span="12">
                <db-card1 v-if="dbCard3_data.db_id" :card_data="dbCard3_data"></db-card1>
            </a-col>
        </a-row>
    </div>
</template>

<style>
@import url('../../assets/style/colorset.css');
@import url('../../assets/style/common.css');

::-webkit-scrollbar {
  display: none; /* Chrome Safari */
}
</style>

<script>
import { defineComponent, ref } from 'vue';
import DBNCard1 from '../../components/dashboard-new/dbn-card1';
import DBNBar2 from '../../components/dashboard-new/dbn-bar2';
import DBNBar1 from '../../components/dashboard-new/dbn-bar1';
import DBLine from '../../components/dashboard/db-line.vue';
import axios from 'axios';

export default defineComponent({
    name: 'DashboardOther',
    components: {
        'db-card1': DBNCard1,
        'db-bar2': DBNBar2,
        'db-bar1': DBNBar1,
        'db-line': DBLine
    },
    setup() {
        return {
            dbCard1_data: ref({}),
            dbBar2_data: ref({}),
            dbCard2_data: ref({}),
            dbBar1_data: ref({}),
            dbLine_data: ref({}),
            dbBar1_2_data: ref({}),
            dbCard3_data: ref({})
        }
    },
    mounted() {
        this.getRetailData();
        this.getAUMData();
        this.getEnterPriseData();
        this.getIncomeData();
        this.getHoldData();
        this.getEVAData();
        this.getLCData();
    },
    methods: {

        // 获取零售客户建设情况
        async getRetailData() {
            const rtc_res = await axios.get('http://localhost:8080/demo/dashboard/dashboardn-card1.json');
            this.dbCard1_data = rtc_res.data;
        },
        async getAUMData() {
            const AUMData_res = await axios.get('http://localhost:8080/demo/dashboard/dashboardn-bar2.json');
            this.dbBar2_data = AUMData_res.data;
            console.log(this.dbBar2_data)
        },
        async getEnterPriseData() {
            const epc_res = await axios.get('http://localhost:8080/demo/dashboard/dashboardn-card2.json');
            this.dbCard2_data = epc_res.data;
        },
        async getIncomeData() {
            const income_res = await axios.get('http://localhost:8080/demo/dashboard/dashboardn-bar1.json');
            this.dbBar1_data = income_res.data;
        },
        async getHoldData() {
            const dbline_data = await axios.get('http://localhost:8080/demo/dashboard/dashboard-line.json');
            this.dbLine_data = dbline_data.data;
        },
        async getEVAData() {
            const eva_res = await axios.get('http://localhost:8080/demo/dashboard/dashboardn-bar1-2.json');
            this.dbBar1_2_data = eva_res.data;
        },
        async getLCData() {
            const lc_res = await axios.get('http://localhost:8080/demo/dashboard/dashboardn-card3.json');
            this.dbCard3_data = lc_res.data;
        }
    }
});

</script>