<template>
  <div class="side_con">
    <a-menu mode="inline" class="menu_con" v-model:openKeys="openKeys" v-model:selectedKeys="selectedKeys">
      <a-sub-menu v-for="item in menu_data" :key="item.menu_key" @click="handleMenuClick">
        <template #icon>
          <component :is="item.menu_icon" theme="outline" size="16"></component>
        </template>
        <template #title>{{ item.menu_title }}</template>
        <a-menu-item v-for="sub_item in item.sub_menu" :key="sub_item.menu_key">
          {{ sub_item.menu_title }}
          <router-link :to="{name:sub_item.menu_name,params:sub_item.menu_params}"></router-link>
        </a-menu-item>
      </a-sub-menu>
    </a-menu>
  </div>
</template>

<style>
@import url('@/assets/style/common.css');

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
import { defineComponent, ref } from "vue";
import { DashboardOne, NewComputer, Notes, Data } from '@icon-park/vue-next';
import { Menu, SubMenu, MenuItem} from 'ant-design-vue';

export default defineComponent({
  name: "SiderMenu",
  components: {
    'icon-dashboard': DashboardOne,
    'icon-computer': NewComputer,
    'icon-notes': Notes,
    'icon-data': Data,
    'a-menu': Menu,
    'a-sub-menu': SubMenu,
    'a-menu-item': MenuItem,
  },
  props:{
    menu_data: {type:Array},
    menu_keys: {type:Object}
  },
  data() {
    return {};
  },
  setup(props) {
    // console.log(props.menu_keys);
    return {
      selectedKeys: ref([props.menu_keys.selectedKeys]),
      openKeys: ref([props.menu_keys.openKeys]),
    };
  },
  methods:{
    // async getMenuData() {
    //   const menu_res = await axios.get('/demo/menu.json');
    //   this.menu_data = menu_res.data;
    // },
    handleMenuClick() {
      console.log(this.selectedKeys,this.openKeys)
    }
  },
  mounted() {}
});
</script>
