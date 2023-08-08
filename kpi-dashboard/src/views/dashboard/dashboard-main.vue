<template>
    <div class="v-db_con">
        <db-pie v-if="pie_data.db_option" :db_data="pie_data"></db-pie>
        <!-- <db-radar></db-radar>
        <db-bar v-if="bar_data.db_option" :option_data="bar_data.db_option" :title="bar_data.db_title"></db-bar>
        <db-card1></db-card1>
        <db-card2></db-card2>
        <db-bar2></db-bar2> -->
    </div>
</template>

<style>
.v-db_con {
    width: 100%;
    min-width: 1280px;
    /* height: 100%; */
    display: flex;
    gap: 20px;
}
</style>

<script>
// import DashboardBar from '../../components/dashboard/db-bar.vue';
// import DashboardBar2 from '../../components/dashboard/db-bar2.vue';
import DashboardPie from '../../components/dashboard/db-pie.vue';
// import DashboardRadar from '../../components/dashboard/db-radar.vue';
// import DashboardCard1 from '../../components/dashboard/db-card.vue';
// import DashboardCard2 from '../../components/dashboard/db-card2.vue';
import { defineComponent } from 'vue';
import axios from 'axios';

export default defineComponent({
    name:'dashboard-main',
    components:{
        // 'db-bar':DashboardBar,
        // 'db-bar2':DashboardBar2,
        'db-pie':DashboardPie,
        // 'db-radar':DashboardRadar,
        // 'db-card1':DashboardCard1,
        // 'db-card2':DashboardCard2
    },
    data() {
        return {
            bar_data:{},
            pie_data:{}
        }
    },
    mounted(){
        this.getDbData();
    },
    methods: {
        async getDbData() {

            // db-bar
            const dbbar_data = await axios.get('http://localhost:8080/demo/dashboard/dashboard-bar.json');
            // console.log(dbbar_data.data);
            this.bar_data = dbbar_data.data.db_bar;
            console.log(this.bar_data);

            // db-pie
            const dbpie_data = await axios.get('http://localhost:8080/demo/dashboard/dashboard-pie.json')
            // console.log(dbpie_data.data)
            this.pie_data = dbpie_data.data.db_pie;
            console.log(this.pie_data)
        }
    }
})
</script>