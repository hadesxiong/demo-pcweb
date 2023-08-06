<template>
    <div style="width: auto;display: flex;">
        <db-bar v-if="bar_data.db_option" :option_data="bar_data.db_option" :title="bar_data.db_title"></db-bar>
    </div>
</template>

<script>
import DashboardBar from '../../components/dashboard/db-bar';
import { defineComponent } from 'vue';
import axios from 'axios';

export default defineComponent({
    name:'dashboard-main',
    components:{
        'db-bar':DashboardBar
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