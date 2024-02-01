<template>
  <div class="h_p100">
      <router-view></router-view>
  </div>
</template>

<style>
@import url('@/assets/style/common.css');
@import url('@/assets/style/overwrite.css');

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

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'App',
  components: {},
  data() {
    return {};
  },
  setup() {
    return {}
  },
}
); 
</script>
