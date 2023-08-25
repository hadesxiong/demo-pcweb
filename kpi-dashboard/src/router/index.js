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
    },
  },
  {
    name: "dashboard-other",
    path: "/dashboard-other",
    component: () => import("@/views/dashboard/dashboard-other.vue"),
    meta: {
      breadcrumb: ["数据看板", "同业指标分析"],
    },
  },
  {
    name: "rank-important",
    path: "/rank-important",
    component: () => import("@/views/rank/rank-important.vue"),
    meta: {
      breadcrumb: ["业绩排行", "重要指标排行"],
    },
  },
  {
    name: "rank-detail",
    path: "/rank-important/rank-detail/:rank_id",
    component: () => import("@/views/rank/rank-detail.vue"),
    meta: {
      breadcrumb: ["业绩排行", "重要指标排行", "业绩详情"],
    },
  },
  {
    name:"table-detail",
    path:"/table-detail/:table_class",
    component:()=> import('@/views/table/table-detail.vue'),
    meta:{
      breadcrumb:['数据报表']
    }
  },
  {
    name:"data-manage",
    path: "/data-manage",
    component: () => import("@/views/manage/data-manage.vue"),
    meta: {
      breadcrumb: ["数据管理", "数据导入"],
    },
  },
  {
    name: "data-detail",
    path: "/data-manage/data-detail",
    component: () => import("@/views/manage/data-detail.vue"),
    meta: {
      breadcrumb: ["数据管理", "数据导入", "导入数据详情"],
    },
  },
  {
    name:"org-manage",
    path: "/org-manage",
    component: () => import("@/views/manage/org-manage.vue"),
    meta: {
      breadcrumb: ["数据管理", "机构管理"],
    },
  },
  {
    name:"user-manage",
    path: "/user-manage",
    component: () => import("@/views/manage/user-manage.vue"),
    meta: {
      breadcrumb: ["数据管理", "用户管理"],
    },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// 导航守卫

router.beforeEach((to, from, next) => {
  const openKey = "数据看板"; // 菜单的 openKey

  const foundRoute = routes.find(route => {
    return route.name === to.name && route.meta.breadcrumb.includes(openKey);
  });

  if (foundRoute) {
    next({path:to.path}); // 执行跳转
  } else {
    next({ path: "/dashboard-other" }); // 默认跳转到指定路由
  }
});

export default router;
