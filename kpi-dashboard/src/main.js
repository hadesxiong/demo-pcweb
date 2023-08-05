import { createApp } from 'vue'
import App from './App.vue'

// 引入antd
import Antd from 'ant-design-vue';
// 引入Vue Router
import { createRouter, createWebHistory } from 'vue-router';

import routes from './router/index'

const router = createRouter({
    history: createWebHistory(),
    routes
  });

// createApp(App).mount('#app')
const app = createApp(App);
app.use(Antd);  
app.use(router);

app.mount('#app');
