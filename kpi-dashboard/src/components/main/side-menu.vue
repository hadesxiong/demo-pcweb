<template>
    <div>
        <a-menu>
            <a-sub-menu>
                <template #icon></template>
                <template #title></template>
                <a-menu-item></a-menu-item>
            </a-sub-menu>
        </a-menu>
    </div>
</template>

<script>
import {defineComponent} from 'vue';

export default defineComponent({
    props:['icon'],
    components:{},
    setup(){
        return {
            // 动态menu数据demo
            menu_data : [
                {has_sub:false,sub_menu:{menu_key:'',menu_icon:'',menu_title:''},menu_item:[{menu_key:'home_1',menu_icon:'',menu_title:'首页'}]},
                {has_sub:true,sub_menu:{menu_key:'dashboard',menu_icon:'dashboard-outlined',menu_title:''},menu_item:[]}
            ]
        };
    },
});
</script>