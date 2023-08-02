<template>
    <div class="side_con">
        <a-menu style="" mode="inline" :inline-collapsed="menu_collapsed">
            <a-sub-menu v-for="item in menu_data" :key="item.menu_key">
                <template #icon><icon-park :type=item.menu_icon theme="outline" size="16"></icon-park></template>
                <template #title>{{ item.menu_title }}</template>
                <a-menu-item v-for="sub_item in item.sub_menu" :key="sub_item.menu_key">{{ sub_item.menu_title
                }}</a-menu-item>
            </a-sub-menu>
            <div class="triggle_con">
                <a-button type="text" @click="toggleCollapsed" class="triggle_btn">
                    <template #icon>
                        <icon-park v-if="menu_collapsed" type="MenuFoldOne" theme="filled" size="16" fill="#4E5969"
                            class="triggle_icon"></icon-park>
                        <icon-park v-else type="MenuUnfoldOne" theme="filled" size="16" fill="#4E5969"
                            class="triggle_icon"></icon-park>
                    </template>
                </a-button>
            </div>
        </a-menu>


    </div>
</template>

<style>
.side_con {
    width: 11vw;

}
.mg-auto {
    margin: auto;
}
.triggle_con {
    height: inherit;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
}

.triggle_btn {
    background-color: #F7F8FA;
    display: inline-flex;
    align-items: center;
}
.flex_end {
    align-items: flex-end !important;
}

.triggle_icon {
    font-size: 18px;
    cursor: pointer;
    transition: color 0.3s;
    display: flex;
    align-items: center;
    line-height: inherit;
    margin: auto;
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
            menu_collapsed: false,
            selectedKeys: [],
            openKeys: [],
            preOpenKeys: [],

        });
        const toggleCollapsed = () => {
            state.menu_collapsed = !state.menu_collapsed;
            state.openKeys = state.menu_collapsed ? [] : state.preOpenKeys;
        }
        return {
            ...toRefs(state),
            toggleCollapsed
        };
    },
});
</script>