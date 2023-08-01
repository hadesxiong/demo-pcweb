<template>
    <div>
        <a-menu style="width: 12vw; min-width: 220px;" mode="inline">
            <a-sub-menu v-for="item in menu_data" :key="item.menu_key">
                <template #icon><icon-park :type=item.menu_icon theme="outline" size="16"></icon-park></template>
                <template #title>{{ item.menu_title }}</template>
                <a-menu-item v-for="sub_item in item.sub_menu" :key="sub_item.menu_key">{{ sub_item.menu_title
                }}</a-menu-item>
            </a-sub-menu>
        </a-menu>
    </div>
</template>

<script>
import { defineComponent } from 'vue';
import { IconPark } from "@icon-park/vue-next/es/all";

export default defineComponent({
    name: 'SideMenu',
    // props: ['icon'],
    components: {
        IconPark
    },
    data() {
        this.menu_data = [
            { menu_key: 'dashboard', menu_title: '数据看板', menu_icon: 'DashboardOne', sub_menu: [{ menu_key: 'dashboard-important', menu_title: '重要指标分析', menu_icon: '' }, { menu_key: 'dashboard-other', menu_title: '同业指标分析', menu_icon: '' }] },
            { menu_key: 'rank', menu_title: '业绩排行', menu_icon: 'NewComputer', sub_menu: [{ menu_key: 'rank-important', menu_title: '重要指标排行', menu_icon: '' }] },
            { menu_key: 'table', menu_title: '数据报表', menu_icon: 'Notes', sub_menu: [{ menu_key: 'enterprise-table', menu_title: '企金数据报表', menu_icon: '' }, { menu_key: 'retail-table', menu_title: '零售数据报表', menu_icon: '' }, { menu_key: 'bank-table', menu_title: '同业数据报表', menu_icon: '' }, { menu_key: 'other-table', menu_title: '其他数据报表', menu_icon: '' }] }
        ];
        return {};
    },
    setup() {
        return {};
    },
});
</script>