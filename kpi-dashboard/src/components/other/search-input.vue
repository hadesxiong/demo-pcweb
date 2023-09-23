<template>
    <div>
        
    </div>
</template>

<style>
</style>

<script>
import { defineComponent, ref } from 'vue';
import { Dropdown, Select, Spin } from 'ant-design-vue';

export default defineComponent({
    name: 'SearchInput',
    components: {
        'a-dropdown': Dropdown,
        'a-select': Select,
        'a-spin': Spin
    },
    props:{
        
    }
})
</script>