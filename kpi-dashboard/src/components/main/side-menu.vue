<template>
    <div>
        <a-menu style="width: 300px;" mode="horizontal">
            <a-sub-menu v-for="item in menu_data" :key="item.menu_key">
                <template #title>{{ item.menu_title }}</template>
                <!-- <a-menu-item></a-menu-item> -->
            </a-sub-menu>
        </a-menu>
    </div>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'SideMenu',
    // props: ['icon'],
    components: {},
    data() {
        this.menu_data = [
            { menu_key: 'home', menu_title: '首页', menu_icon: 'home-outlined', sub_menu: [] },
            { menu_key: 'dashboard', menu_title: '数据看板', menu_icon: 'dashboard-outlined', sub_menu: [{ menu_key: 'dashboard-important', menu_title: '重要指标分析', menu_icon: '' }] },
            { menu_key: 'rank', menu_title: '业绩排行', menu_icon: 'number-outlined', sub_menu: [] }
        ];
        return {};
    },
    setup() {
        return {};
    },
});
</script>