<template>
    <div>
        <db-card1 :retailCustomer_data="dbCard1_data"></db-card1>
    </div>
</template>

<style>
@import url('../../assets/style/colorset.css');
@import url('../../assets/style/common.css');
</style>

<script>
import {defineComponent, ref} from 'vue';
import DBNCard1 from '../../components/dashboard-new/dbn-card1'
import axios from 'axios';

export default defineComponent({
    name:'DashboardOther',
    components:{
        'db-card1': DBNCard1
    },
    setup(){
        return {
            dbCard1_data:ref({})
        }
    },
    mounted() {
      this.getRetailData();  
    },
    methods:{
        async getRetailData() {
            const retailData_res = await axios.get('http://localhost:8080/demo/dashboard/dashboardn-card1.json')
            this.dbCard1_data = retailData_res.data
        }
    }
});

</script>