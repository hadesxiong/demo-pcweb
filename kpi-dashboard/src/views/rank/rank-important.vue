<template>
    <div>
        <rank-main v-if="rank_list" :rank_list="rank_list"></rank-main>
    </div>
</template>

<style>

</style>

<script>
import {defineComponent} from 'vue';
import RankMain from '../../components/rank/rank-main';
import axios from 'axios';

export default defineComponent({
    name:'rank-important',
    components:{
        'rank-main': RankMain
    },
    data() {
        return {
            rank_list:[]
        }
    },
    mounted() {
        this.getRankData();
    },
    methods: {
        async getRankData() {
            const rank_res = await axios.get('./demo/rank/rank-important.json');
            console.log(rank_res);
            this.rank_list = rank_res.data;
            console.log(this.rank_list)
        }
    }
});

</script>