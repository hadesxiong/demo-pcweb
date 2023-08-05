import { createRouter, createWebHistory } from 'vue-router';

// 定义路由配置
const routes = [
  {
    path: "/",
    redirect: "/dashboard-main",
  },
  {
    path: "/dashboard-main",
    component: () => import("../views/dashboard/dashboard-main.vue"),
    meta:{
      breadcrumb:['数据看板','重要指标分析']
    }
  },
  {
    path: "/dashboard-other",
    component: () => import("../views/dashboard/dashboard-other.vue"),
    meta:{
      breadcrumb:['数据看板','同业指标分析']
    }
  },
  {
    path: "/data-manage",
    component: () => import("../views/manage/data-manage.vue"),
    meta:{
      breadcrumb:['数据管理','数据导入']
    }
  },
  {
    path: "/org-manage",
    component: () => import("../views/manage/org-manage.vue"),
    meta:{
      breadcrumb:['数据管理','机构管理']
    }
  },
  {
    path: "/user-manage",
    component: () => import("../views/manage/user-manage.vue"),
    meta:{
      breadcrumb:['数据管理','用户管理']
    }
  },
  {
    path: "/rank-important",
    component: () => import("../views/rank/rank-important.vue"),
    meta:{
      breadcrumb:['业绩排行','重要指标排行']
    }
  },
  {
    path: "/data-table",
    component: () => import("../views/table/data-table.vue"),
    meta:{
      breadcrumb:['数据报表','企金数据报表']
    }
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
