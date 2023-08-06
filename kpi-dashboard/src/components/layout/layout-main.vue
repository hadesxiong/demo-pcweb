<template>
    <a-layout>
        <a-layout-header class="c-layout_header">
            <div class="c-header_logo">
                <header-logo></header-logo>
            </div>
            <div class="c-header_other">
                <header-other></header-other>
            </div>
        </a-layout-header>
        <a-layout>
            <a-layout-sider :collapsedWidth="60" :collapsible="true" :min-width="220" :max-width="220" :width="220"
                v-model:collapsed="menu_collapsed" class="c-layout_sider mt_60">
                <sider-menu></sider-menu>
                <template #trigger>
                    <icon-park v-if="menu_collapsed" type="MenuFoldOne" theme="filled" size="16" fill="#4E5969"></icon-park>
                    <icon-park v-else type="MenuUnfoldOne" theme="filled" size="16" fill="#4E5969"></icon-park>
                </template>
            </a-layout-sider>
            <a-layout-content class="mt_60">
                <div class="c-bread_con">
                    <a-breadcrumb>
                        <a-breadcrumb-item v-for="(item, index) in breadcrumb" :key="index">{{ item }}</a-breadcrumb-item>
                    </a-breadcrumb>
                </div>
                <div class="c-main_con mt_20">
                    <router-view></router-view>
                </div>
            </a-layout-content>
        </a-layout>
    </a-layout>
</template>
  
<style>
@import url('../../assets/style/common.css');
@import url('../../assets/style/overwrite.css');

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
        'header-logo': HeaderLogo,
        'header-other': HeaderOther,
        'sider-menu': SiderMenu,
        'icon-park': IconPark
    },
    data() {

        return {
            menu_collapsed: ref(false),
        }
    },
    setup() {
        return {}
    },
    computed: {
        breadcrumb() {
            const matchedRoutes = this.$route.matched;
            const breadcrumb = [];

            matchedRoutes.forEach(route => {
                if (route.meta && route.meta.breadcrumb) {
                    // 将每个路由的 breadcrumb 数组合并到总的面包屑数组中
                    breadcrumb.push(...route.meta.breadcrumb);
                }
            });

            return breadcrumb;
        }
    }
}
);
</script>