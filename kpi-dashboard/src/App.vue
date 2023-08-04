<template>
  <a-layout>
    <a-layout-header>
      <HeaderLogo></HeaderLogo>
    </a-layout-header>
    <a-layout>
      <a-layout-sider :collapsedWidth="80" :collapsible="true" :min-width="220" :max-width="220" :width="220"
        v-model:collapsed="menu_collapsed">
        <SideMenu></SideMenu>
        <template #trigger>
          <icon-park v-if="menu_collapsed" type="MenuFoldOne" theme="filled" size="16" fill="#4E5969"></icon-park>
          <icon-park v-else type="MenuUnfoldOne" theme="filled" size="16" fill="#4E5969"></icon-park>
        </template>
      </a-layout-sider>
      <a-layout-content></a-layout-content>
    </a-layout>
  </a-layout>
</template>

<script>
import HeaderLogo from './components/layout/header-logo.vue'
import SideMenu from './components/layout/side-menu.vue';
import { IconPark } from "@icon-park/vue-next/es/all";
import { defineComponent, ref } from 'vue';

export default defineComponent({
  name: 'App',
  components: {
    SideMenu,
    IconPark,HeaderLogo
  },
  data() {
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
