// 导入你的组件
import db_main from "../views/dashboard/db_main.vue";
import table_main from "../views/table/table_main.vue";
import App from '../App.vue';

// 定义路由配置
const routes = [
  {
    path: "/",
    component:App
  },
  {
    path: "/db_main",
    name: "db_main",
    component: db_main,
  },
  {
    path: "/table_main",
    name: "table_main",
    component: table_main,
  },
];

export default routes;
