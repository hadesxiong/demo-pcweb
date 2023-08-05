<template>
    <a-layout>
        <a-layout-header class="layout_header">
            <div class="header_logo">
                <header-logo></header-logo>
            </div>
            <div class="header_other">
                <header-other></header-other>
            </div>
        </a-layout-header>
        <a-layout>
            <a-layout-sider :collapsedWidth="60" :collapsible="true" :min-width="220" :max-width="220" :width="220"
                v-model:collapsed="menu_collapsed" class="layout_sider mt_60">
                <sider-menu></sider-menu>
                <template #trigger>
                    <icon-park v-if="menu_collapsed" type="MenuFoldOne" theme="filled" size="16" fill="#4E5969"></icon-park>
                    <icon-park v-else type="MenuUnfoldOne" theme="filled" size="16" fill="#4E5969"></icon-park>
                </template>
            </a-layout-sider>
            <a-layout-content class="mt_60">
                <div class="bread_con">
                    <a-breadcrumb>
                        <a-breadcrumb-item v-for="item in bread_data" :key="item.data_key">{{ item.data_title
                        }}</a-breadcrumb-item>
                    </a-breadcrumb>
                </div>
                <div class="main_con mt_20">
                    <router-view></router-view>
                </div>
            </a-layout-content>
        </a-layout>
    </a-layout>
</template>
  
<style>
@import url('../../assets/style/common.css');
@import url('../../assets/style/overwrite.css');

.layout_header {
    display: flex;
    justify-content: space-between;
    position: fixed;
    z-index: 1;
    width: 100%;
}
.layout_sider {
    overflow: auto;
    height: calc(100vh - 60px);
    position: fixed;
    left: 0;
    top: 0;
    bottom: 0;
}

.header_other {
    display: flex;
}

.bread_con {
    width: 100%;
    height: auto;
    font-weight: 500;
}

.main_con {
    width: 100%;
    overflow: auto;
    background-color: #FFF;
    color: black;
    height: calc(100% - 40px);
}
</style>
  
<script>
import HeaderLogo from './header/header-logo.vue';
import HeaderOther from './header/header-other.vue';
import SiderMenu from './sider/sider-menu.vue';
import { IconPark } from "@icon-park/vue-next/es/all";
import { defineComponent, ref } from 'vue';

export default defineComponent({
    name: 'LayoutMain',
    components: {
        'header-logo':HeaderLogo,
        'header-other':HeaderOther,
        'sider-menu':SiderMenu,
        'icon-park':IconPark
    },
    data() {
        // 面包屑数据样例
        this.bread_data = [
            { data_title: '数据看板', data_key: 'dashboard', data_path: '' },
            { data_title: '重要指标分析', data_key: 'dashboard-kpi', data_path: '' }
        ];
        return {
            menu_collapsed: ref(false),
        }
    },
    setup() {
        return {}
    },
}
);
</script>