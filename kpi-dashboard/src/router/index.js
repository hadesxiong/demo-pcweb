import { createRouter, createWebHistory } from "vue-router";

// 定义路由配置
const routes = [
  {
    path: "/",
    redirect: "/dashboard-other",
  },
  {
    name: "dashboard-main",
    path: "/dashboard-main",
    component: () => import("@/views/dashboard/dashboard-main.vue"),
    meta: {
      breadcrumb: ["数据看板", "重要指标分析"],
      sub:"dashboard",
      menu:"dashboard-main"
    },
  },
  {
    name: "dashboard-other",
    path: "/dashboard-other",
    component: () => import("@/views/dashboard/dashboard-other.vue"),
    meta: {
      breadcrumb: ["数据看板", "同业指标分析"],
      sub:"dashboard",
      menu:"dashboard-other"
    },
  },
  {
    name: "rank-important",
    path: "/rank-important",
    component: () => import("@/views/rank/rank-important.vue"),
    meta: {
      breadcrumb: ["业绩排行", "重要指标排行"],
      sub:"rank",
      menu:"rank-important"
    },
  },
  {
    name: "rank-detail",
    path: "/rank-important/rank-detail/:rank_id",
    component: () => import("@/views/rank/rank-detail.vue"),
    meta: {
      breadcrumb: ["业绩排行", "重要指标排行", "业绩详情"],
      sub:"rank",
      menu:"rank-important"
    },
  },
  {
    name:"table-detail",
    path:"/:table_class-table",
    component:()=> import('@/views/table/table-detail.vue'),
    meta:{
      breadcrumb:['数据报表'],
      sub:"table",
    }
  },
  {
    name:"data-manage",
    path: "/data-manage",
    component: () => import("@/views/manage/data-manage.vue"),
    meta: {
      breadcrumb: ["数据管理", "数据导入"],
      sub:"settings",
      menu:"data-manage"
    },
  },
  {
    name: "data-detail",
    path: "/data-manage/data-detail/:data_id",
    component: () => import("@/views/manage/data-detail.vue"),
    meta: {
      breadcrumb: ["数据管理", "数据导入", "导入数据详情"],
      sub:"settings",
      menu:"data-manage"
    },
  },
  {
    name:"org-manage",
    path: "/org-manage",
    component: () => import("@/views/manage/org-manage.vue"),
    meta: {
      breadcrumb: ["数据管理", "机构管理"],
      sub:"settings",
      menu:"org-manage"
    },
  },
  {
    name:"user-manage",
    path: "/user-manage",
    component: () => import("@/views/manage/user-manage.vue"),
    meta: {
      breadcrumb: ["数据管理", "用户管理"],
      sub:"settings",
      menu:"user-manage"
    },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// 导航守卫

router.beforeEach((to, from, next) => {
  // 在路由导航之前执行的逻辑
  // table动态赋值
  if (to.name == 'table-detail') {
    to.meta.menu = to.path.substring(1)
  }


  // 跳转
  next()
});


export default router;
