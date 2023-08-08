<template>
    <div class="v-db_con">
        <db-pie></db-pie>
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
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
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
        }
    },
    mounted(){
        this.getDbData();
    },
    methods: {
        async getDbData() {
            const db_data = await axios.get('./demo/dashboard/dashboard-bar.json');
            // console.log(db_data.data);
            this.bar_data = db_data.data.db_bar;
            console.log(this.bar_data);
        }
    }
})
</script>