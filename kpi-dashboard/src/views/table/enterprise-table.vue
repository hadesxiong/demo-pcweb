<template>
    <div class="d_flex fd_c gap_20">
        <table-filter v-if="filter_data.index_class" :filter_data="filter_data"></table-filter>
        <table-main v-if="table_data.table_id" :table_data="table_data"></table-main>
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
import TableMain from '../../components/table/table-main.vue';
// import { IconPark } from "@icon-park/vue-next/es/all";
import axios from 'axios';


export default defineComponent({
    name:"EnterpriseTable",
    components:{
        'table-filter':TableFilter,
        'table-main':TableMain,
    },
    data() {
        return {
            filter_data:{},
            table_data:{}
        }
    },
    setup() {
        return {}
    },
    mounted() {
        this.getFilterData();
        this.getTableData();
    },
    methods:{
        async getFilterData() {
            const filter_res = await axios.get('http://localhost:8080/demo/table/table-filter.json');
            this.filter_data = filter_res.data
            // console.log(this.filter_data)
        },
        async getTableData() {
            const table_res = await axios.get('http://localhost:8080/demo/table/table-main.json');
            this.table_data = table_res.data;
        }
    }
})

</script>