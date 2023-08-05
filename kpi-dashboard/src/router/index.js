// 导入你的组件
// import LayoutMain from '../components/layout/layout-main.vue';

// 定义路由配置
const routes = [
  {
    path: "/",
    redirect: "/dashboard-main",
  },
  {
    path: "/dashboard-main",
    component: () => import("../views/dashboard/dashboard-main.vue"),
  },
  {
    path: "/dashboard-other",
    component: () => import("../views/dashboard/dashboard-other.vue"),
  },
  {
    path: "/data-manage",
    component: () => import("../views/manage/data-manage.vue"),
  },
  {
    path: "/org-manage",
    component: () => import("../views/manage/org-manage.vue"),
  },
  {
    path: "/user-manage",
    component: () => import("../views/manage/user-manage.vue"),
  },
  {
    path: "/rank-important",
    component: () => import("../views/rank/rank-important.vue"),
  },
  {
    path: "/data-table",
    component: () => import("../views/table/data-table.vue"),
  },
];

export default routes;
