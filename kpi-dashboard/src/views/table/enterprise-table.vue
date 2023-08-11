<template>
    <div>
        <table-filter v-if="filter_data.enterprise_filter" :filter_data="filter_data"></table-filter>
    </div>
</template>

<style>
@import url('../../assets/style/overwrite.css');
@import url('../../assets/style/colorset.css');
@import url('../../assets/style/common.css');
</style>

<script>
import { defineComponent } from 'vue';
import TableFilter from '../../components/table/table-filter.vue';
// import { IconPark } from "@icon-park/vue-next/es/all";
import axios from 'axios';

export default defineComponent({
    name:"EnterpriseTable",
    components:{
        'table-filter':TableFilter
    },
    data() {
        return {
            filter_data:{}
        }
    },
    setup() {
        return {}
    },
    mounted() {
        this.getFilterData();
    },
    methods:{
        async getFilterData() {
            const filter_res = await axios.get('http://localhost:8080/demo/table/table-filter.json');
            this.filter_data = filter_res.data
            // console.log(this.filter_data)
        }
    }
})

</script>