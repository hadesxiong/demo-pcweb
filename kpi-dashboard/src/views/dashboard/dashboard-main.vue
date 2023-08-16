<template>
    <a-row type="flex" :gutter="[20,20]" style="display: flex; align-items: stretch;">
        <a-col flex="auto">
            <db-pie v-if="pie_data.db_option" :db_data="pie_data"></db-pie>
        </a-col>
        <a-col flex="auto">
            <db-radar v-if="radar_data.db_option" :db_data="radar_data"></db-radar>
        </a-col>
        <a-col flex="auto">
            <db-bar v-if="bar_data.db_option" :db_data="bar_data"></db-bar>
        </a-col>
        <a-col :span="9">
            <db-card1 v-if="card1_data.db_other" :db_data="card1_data"></db-card1>
        </a-col>
        <a-col flex="auto">
            <db-card2 v-if="card2_data.db_other" :db_data="card2_data"></db-card2>
        </a-col>
        <a-col>
            <db-bar2 v-if="bar2_data.db_option" :db_data="bar2_data"></db-bar2>
        </a-col>
        <a-col>
            <db-line v-if="line_data.db_option" :db_data="line_data"></db-line>
        </a-col>
    </a-row>
    <!-- <div class="v-db_con"> -->

        <!-- <db-radar></db-radar>
        
        <db-card1></db-card1>

        <db-bar2></db-bar2> -->
    <!-- </div> -->
</template>

<style>
@import url('../../assets/style/common.css');
@import url('../../assets/style/colorset.css');

.v-db_con {
    width: auto;
    min-width: 1280px;
    /* height: 100%; */
    display: flex;
    gap: 20px;
}
</style>

<script>
import DashboardBar from '../../components/dashboard/db-bar.vue';
import DashboardBar2 from '../../components/dashboard/db-bar2.vue';
import DashboardPie from '../../components/dashboard/db-pie.vue';
import DashboardRadar from '../../components/dashboard/db-radar.vue';
import DashboardCard1 from '../../components/dashboard/db-card.vue';
import DashboardCard2 from '../../components/dashboard/db-card2.vue';
import DashboardLine from '../../components/dashboard/db-line.vue';
import { defineComponent } from 'vue';
import axios from 'axios';

export default defineComponent({
    name:'dashboard-main',
    components:{
        'db-bar':DashboardBar,
        'db-bar2':DashboardBar2,
        'db-pie':DashboardPie,
        'db-radar':DashboardRadar,
        'db-card1':DashboardCard1,
        'db-card2':DashboardCard2,
        'db-line':DashboardLine
    },
    data() {
        return {
            bar_data:{},
            pie_data:{},
            radar_data:{},
            card1_data:{},
            card2_data:{},
            bar2_data:{},
            line_data:{}
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
            // console.log(this.bar_data);

            // db-pie
            const dbpie_data = await axios.get('http://localhost:8080/demo/dashboard/dashboard-pie.json')
            // console.log(dbpie_data.data)
            this.pie_data = dbpie_data.data.db_pie;
            // console.log(this.pie_data)

            // db-radar
            const dbradar_data = await axios.get('http://localhost:8080/demo/dashboard/dashboard-radar.json');
            // console.log(dbradar_data.data.db_radar);
            this.radar_data = dbradar_data.data.db_radar;
            // console.log(this.radar_data);

            // db-card1
            const dbcard1_data = await axios.get('http://localhost:8080/demo/dashboard/dashboard-card1.json');
            // console.log(dbcard1_data.data.db_card1)
            this.card1_data = dbcard1_data.data.db_card1;
            // console.log(this.card1_data);

            // db-card2
            const dbcard2_data = await axios.get('http://localhost:8080/demo/dashboard/dashboard-card2.json');
            // console.log(dbcard2_data.data.db_card2);
            this.card2_data = dbcard2_data.data.db_card2;
            // console.log(this.card2_data);

            // db-bar2
            const dbbar2_data = await axios.get('http://localhost:8080/demo/dashboard/dashboard-bar2.json');
            // console.log(dbbar2_data);
            this.bar2_data = dbbar2_data.data.db_bar2;
            // console.log(this.bar2_data);

            // db-line
            const dbline_data = await axios.get('http://localhost:8080/demo/dashboard/dashboard-line.json');
            console.log(dbline_data);
            this.line_data = dbline_data.data.db_line;
            console.log(this.line_data);
        }
    }
})
</script>