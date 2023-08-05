<template>
  <div>
    <layout-main></layout-main>
  </div>
</template>

<style>
@import url('./assets/style/common.css');

</style>

<script>
import LayoutMain from './components/layout/layout-main.vue';
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'App',
  components: {
    'layout-main':LayoutMain
  },
  data() {
    return {}
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