import { createApp } from 'vue'
import App from './App.vue'

// 引入antd
import Antd from 'ant-design-vue';

// createApp(App).mount('#app')
const app = createApp(App);
app.use(Antd).mount('#app')
