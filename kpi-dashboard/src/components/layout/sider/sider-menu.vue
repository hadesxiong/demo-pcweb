<template>
  <div class="side_con">
    <a-menu mode="inline" class="menu_con" v-model:openKeys="openKeys" v-model:selectedKeys="selectedKeys">
      <a-sub-menu v-for="item in menu_data" :key="item.menu_key">
        <template #icon><icon-park :type="item.menu_icon" theme="outline" size="16"></icon-park></template>
        <template #title>{{ item.menu_title }}</template>
        <a-menu-item v-for="sub_item in item.sub_menu" :key="sub_item.menu_key">
          {{ sub_item.menu_title }}
          <!-- <router-link :to="{path: sub_item.menu_path}"></router-link> -->
          <router-link :to="{name:sub_item.menu_name,params:sub_item.menu_params}"></router-link>
        </a-menu-item>
      </a-sub-menu>
    </a-menu>
  </div>
</template>

<style>
@import url('../../../assets/style/common.css');

.side_con {
  width: 100%;
  height: 100%;
}

.menu_con {
  height: 100%;
  color: #1d2129;
}
</style>

<script>
import { defineComponent, reactive, toRefs } from "vue";
import { IconPark } from "@icon-park/vue-next/es/all";

import axios from 'axios';

export default defineComponent({
  name: "SiderMenu",
  // props: ['icon'],
  components: {
    'icon-park': IconPark,
  },
  data() {
    return {
      res_data:'',
      menu_data:''
    };
  },
  setup() {
    const state = reactive({
      // menu_collapsed: false,
      selectedKeys: ['dashboard-other'],
      openKeys: ['dashboard'],
      preOpenKeys: [],
    });
    
    return {
      ...toRefs(state),
    };
  },
  methods:{
    async getMenuData() {
      const menu_res = await axios.get('http://localhost:8080/demo/menu.json');
      this.menu_data = menu_res.data;
    },
  },
  mounted() {
    this.getMenuData();
  }
});
</script>
