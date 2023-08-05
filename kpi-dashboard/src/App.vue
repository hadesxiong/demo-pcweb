<template>
  <a-layout>
    <a-layout-header class="layout_header">
      <div class="header_logo">
        <HeaderLogo></HeaderLogo>
      </div>
      <div class="header_other">
        <HeaderOther></HeaderOther>
      </div>
    </a-layout-header>
    <a-layout>
      <a-layout-sider :collapsedWidth="60" :collapsible="true" :min-width="220" :max-width="220" :width="220"
        v-model:collapsed="menu_collapsed">
        <SideMenu></SideMenu>
        <template #trigger>
          <icon-park v-if="menu_collapsed" type="MenuFoldOne" theme="filled" size="16" fill="#4E5969"></icon-park>
          <icon-park v-else type="MenuUnfoldOne" theme="filled" size="16" fill="#4E5969"></icon-park>
        </template>
      </a-layout-sider>
      <a-layout-content>
        <div class="bread_con">
          <a-breadcrumb>
            <a-breadcrumb-item v-for="item in bread_data" :key="item.data_key">{{item.data_title}}</a-breadcrumb-item>
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
@import url('./assets/style/common.css');
.layout_header {
  display: flex;
  justify-content: space-between;
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
  height: auto;
  background-color: aqua;
}
</style>

<script>
import HeaderLogo from './components/layout/header/header-logo.vue';
import HeaderOther from './components/layout/header/header-other.vue';
import SideMenu from './components/layout/sider/side-menu.vue';
import { IconPark } from "@icon-park/vue-next/es/all";
import { defineComponent, ref } from 'vue';

export default defineComponent({
  name: 'App',
  components: {
    SideMenu,
    IconPark,
    HeaderLogo,
    HeaderOther
  },
  data() {
    // 面包屑数据样例
    this.bread_data = [
      {data_title:'数据看板',data_key:'dashboard',data_path:''},
      {data_title:'重要指标分析',data_key:'dashboard-kpi',data_path:''}
    ];
    return {
      menu_collapsed:ref(false),
    }
  },
  setup() {
    return {}
  },
}
); 
</script>

<style>
@import url(./assets/style/overwrite.css);

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>