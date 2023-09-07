<template>
    <div class="d_flex fd_c gap_20 h_p100">
        <table-filter v-if="filter_data.index_class" :filter_data="filter_data"
            @getFilterOptions="execSearch"></table-filter>
        <table-main v-if="table_data.table_id" :table_data="table_data" @getFilterOptions="execSearch"></table-main>
    </div>
</template>

<style>
@import url('../../assets/style/overwrite.css');
@import url('../../assets/style/colorset.css');
@import url('../../assets/style/common.css');
</style>

<script>
import { defineComponent, ref } from 'vue';
import TableFilter from '@/components/table/table-filter.vue';
import TableMain from '@/components/table/table-main.vue';

import axios from 'axios';
import { useRoute } from 'vue-router';


export default defineComponent({
    name: "EnterpriseTable",
    components: {
        'table-filter': TableFilter,
        'table-main': TableMain,
    },
    data() {
        return {}
    },
    setup() {
        const route = useRoute();
        // console.log(route.params.table_class)
        return {
            filter_data: ref([]),
            table_data: ref([]),
            query_data: ref({}),
            table_class: ref(route.params.table_class),
        }
    },
    mounted() {
        this.getFilterData();
        this.getTableData();
    },
    methods: {
        async getFilterData() {
            const filter_res = await axios.get('/demo/table/table-filter.json');
            this.filter_data = filter_res.data
        },
        async getTableData() {
            const table_res = await axios.get('/demo/table/table-main.json');
            this.table_data = table_res.data;
        },
        async execSearch(item) {
            console.log(item);
        }
    }
})

</script>