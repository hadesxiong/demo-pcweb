<template>
    <div class="side_con">
        <a-menu style="" mode="inline" class="menu_con">
            <a-sub-menu v-for="item in menu_data" :key="item.menu_key">
                <template #icon><icon-park :type=item.menu_icon theme="outline" size="16"></icon-park></template>
                <template #title>{{ item.menu_title }}</template>
                <a-menu-item v-for="sub_item in item.sub_menu" :key="sub_item.menu_key">{{ sub_item.menu_title
                }}</a-menu-item>
            </a-sub-menu>
        </a-menu>

    </div>
</template>

<style>
@import url('../../assets/style/common.css');

.side_con {
    width: 100%;
    height: 100%;
}
.menu_con {
    height: 100%;
    color: #1D2129;
}
</style>

<script>
import { defineComponent, reactive, toRefs } from 'vue';
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
            { menu_key: 'table', menu_title: '数据报表', menu_icon: 'Notes', sub_menu: [{ menu_key: 'enterprise-table', menu_title: '企金数据报表', menu_icon: '' }, { menu_key: 'retail-table', menu_title: '零售数据报表', menu_icon: '' }, { menu_key: 'bank-table', menu_title: '同业数据报表', menu_icon: '' }, { menu_key: 'other-table', menu_title: '其他数据报表', menu_icon: '' }] },
            { menu_key: 'settings', menu_title: '数据管理', menu_icon: 'Data', sub_menu: [{ menu_key: 'data-import', menu_title: '数据导入', menu_icon: '' }, { menu_key: 'org_manage', menu_title: '机构管理', menu_icon: '' }, { menu_key: 'user_manage', menu_title: '用户管理', menu_icon: '' }] }
        ];
        return {};
    },
    setup() {
        const state = reactive({
            // menu_collapsed: false,
            selectedKeys: [],
            openKeys: [],
            preOpenKeys: [],

        });
        return {
            ...toRefs(state)
        };
    },
});
</script>