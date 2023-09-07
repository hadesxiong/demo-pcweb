<template>
  <div class="h_p100">
      <router-view></router-view>
  </div>
</template>

<style>
@import url('./assets/style/common.css');

</style>

<script>
// import LayoutMain from './components/layout/layout-main.vue';
// import LoginMain from './views/login/login-main.vue'
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'App',
  components: {
    // 'layout-main':LayoutMain,
    // 'login-main':LoginMain
  },
  data() {
    return {
    };
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
  height: 100%;
  width: 100%;
}
</style>