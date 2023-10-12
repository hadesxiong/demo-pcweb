<template>
    <a-layout>
        <a-layout-header class="c-layout_header">
            <div class="c-header_logo">
                <header-logo></header-logo>
            </div>
            <div class="c-header_other">
                <header-other :user_name="user_name"></header-other>
            </div>
        </a-layout-header>
        <a-layout>
            <a-layout-sider :collapsedWidth="60" :collapsible="true" :min-width="220" :max-width="220" :width="220"
                v-model:collapsed="menu_collapsed" class="c-layout_sider mt_60">
                <sider-menu v-if="this.$route.name" :menu_data="menu_data" :menu_keys="menuKeys"></sider-menu>
                <template #trigger>
                    <icon-fold v-if="menu_collapsed" theme="filled" size="16" fill="#4E5969"></icon-fold>
                    <icon-unfold v-else theme="filled" size="16" fill="#4E5969"></icon-unfold>
                </template>
            </a-layout-sider>
            <a-layout-content class="mt_60" id="content_con">
                <div class="c-bread_con">
                    <a-breadcrumb>
                        <a-breadcrumb-item v-for="(item, index) in breadcrumb" :key="index">
                            {{ item }}
                        </a-breadcrumb-item>
                    </a-breadcrumb>
                </div>
                <div class="c-main_con mt_20">
                    <router-view :key="$route.path"></router-view>
                </div>
            </a-layout-content>
        </a-layout>
    </a-layout>
</template>
  
<style>
@import url('@/assets/style/common.css');
@import url('@/assets/style/overwrite.css');

.c-layout_header {
    display: flex;
    justify-content: space-between;
    position: fixed;
    z-index: 1;
    width: 100%;
}

.c-layout_sider {
    overflow: auto;
    height: calc(100vh - 60px);
    position: fixed;
    left: 0;
    top: 0;
    bottom: 0;
}

.c-header_other {
    display: flex;
    align-items: center;
}

.c-bread_con {
    width: 100%;
    height: auto;
    font-weight: 500;
}

.c-main_con {
    width: 100%;
    overflow: auto;
    /* background-color: #f2f3f3; */
    color: black;
    height: calc(100% - 40px);
    min-width: 1200px;
}
</style>
  
<script>
import { defineComponent, ref } from 'vue';
import { MenuFoldOne, MenuUnfoldOne } from '@icon-park/vue-next';
import { Layout, LayoutHeader, LayoutSider, LayoutContent, Breadcrumb, BreadcrumbItem } from 'ant-design-vue';

import HeaderLogo from './header/header-logo.vue';
import HeaderOther from './header/header-other.vue';
import SiderMenu from './sider/sider-menu.vue';

import { menuMap } from '@/assets/config/menu';


export default defineComponent({
    name: 'LayoutMain',
    components: {
        'icon-fold': MenuFoldOne,
        'icon-unfold': MenuUnfoldOne,
        'a-layout': Layout,
        'a-layout-header': LayoutHeader,
        'a-layout-sider': LayoutSider,
        'a-layout-content': LayoutContent,
        'a-breadcrumb': Breadcrumb,
        'a-breadcrumb-item': BreadcrumbItem,
        'header-logo': HeaderLogo,
        'header-other': HeaderOther,
        'sider-menu': SiderMenu,
    },
    data() {
        return {}
    },
    setup() {
        const user_name = localStorage.getItem('user_name')
        return {
            menu_collapsed: ref(false),
            menu_data: ref(menuMap),
            user_name
        }
    },
    computed: {
        breadcrumb() {
            // console.log(this.$route)
            const matchedRoutes = this.$route.matched;
            const breadcrumb = [];
            // console.log(matchedRoutes);
            matchedRoutes.forEach(route => {
                if (route.meta && route.meta.breadcrumb) {
                    // 将每个路由的 breadcrumb 数组合并到总的面包屑数组中
                    breadcrumb.push(...route.meta.breadcrumb);
                }
            });
            return breadcrumb;
        },
        menuKeys() {
            const menu_keys = {openKeys: this.$route.meta.sub, selectedKeys: this.$route.meta.menu};
            // console.log(menu_keys)
            return menu_keys
        }
    }
}
);
</script>