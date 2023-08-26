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
import { defineComponent, ref } from "vue";
import { IconPark } from "@icon-park/vue-next/es/all";

export default defineComponent({
  name: "SiderMenu",
  components: {
    'icon-park': IconPark,
  },
  props:{
    menu_data: {type:Array},
    menu_keys: {type:Object}
  },
  data() {
    return {
      res_data:'',
    };
  },
  setup(props) {
    console.log(props.menu_keys);
    return {
      selectedKeys: ref([props.menu_keys.selectedKeys]),
      openKeys: ref([props.menu_keys.openKeys]),
    };
  },
  methods:{
    // async getMenuData() {
    //   const menu_res = await axios.get('http://localhost:8080/demo/menu.json');
    //   this.menu_data = menu_res.data;
    // },
  },
  mounted() {
    // this.getMenuData();
    // this.openKeys = [this.$route.matched];
    // this.selectedKeys = [this.$route.name];
    // console.log(this.$route.matched,1,this.$route.name)
    // console.log(this.$route)
      // console.log(this.$route);
      // const current_path = this.$route.path;
      // return current_path;
    // console.log(this.menu_keys)
    
  }
});
</script>
