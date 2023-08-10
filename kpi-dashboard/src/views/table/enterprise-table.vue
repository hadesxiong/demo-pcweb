<template>
    <div>
        <table-filter></table-filter>
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
// import axios from 'axios';

export default defineComponent({
    name:"EnterpriseTable",
    components:{
        'table-filter':TableFilter
    },
    data() {
        return {}
    },
    setup() {
        return {}
    }
})

</script>