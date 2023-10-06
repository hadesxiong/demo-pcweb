import { createRouter, createWebHistory } from "vue-router";

import { checkAuth } from "@/utils/checkAuth";

// 定义路由配置
const routes = [
  {
    name:"login",
    path:"/login",
    component:() => import("@/views/login/login-main.vue"),
    meta:{
      requireAuth:false
    }
  },
  {
    name: "layout-main",
    path: "/",
    component: ()=> import("@/components/layout/layout-main.vue"),
    redirect:"/dashboard-main",
    children: [
      {
        name: "dashboard-main",
        path: "/dashboard-main",
        component: () => import("@/views/dashboard/dashboard-main.vue"),
        meta: {
          breadcrumb: ["数据看板", "重要指标分析"],
          sub:"dashboard",
          menu:"dashboard-main",
          requireAuth:true
        },
      },
      {
        name: "rank-important",
        path: "/rank-important",
        component: () => import("@/views/rank/rank-important.vue"),
        meta: {
          breadcrumb: ["业绩排行", "重要指标排行"],
          sub:"rank",
          menu:"rank-important",
          requireAuth:true
        },
      },
      {
        name: "rank-detail",
        path: "/rank-important/rank-detail/:rank_id",
        component: () => import("@/views/rank/rank-detail.vue"),
        meta: {
          breadcrumb: ["业绩排行", "重要指标排行", "业绩详情"],
          sub:"rank",
          menu:"rank-important",
          requireAuth:true
        },
      },
      {
        name:"table-detail",
        path:"/:table_class-table",
        component:()=> import('@/views/table/table-detail.vue'),
        meta:{
          breadcrumb:['数据报表'],
          sub:"table",
          menu:'table-detail',
          requireAuth:true
        }
      },
      {
        name:"data-manage",
        path: "/data-manage",
        component: () => import("@/views/manage/data-manage.vue"),
        meta: {
          breadcrumb: ["数据管理", "数据导入"],
          sub:"settings",
          menu:"data-manage",
          requireAuth:true
        },
      },
      {
        name: "data-detail",
        path: "/data-manage/data-detail/:data_id",
        component: () => import("@/views/manage/data-detail.vue"),
        meta: {
          breadcrumb: ["数据管理", "数据导入", "导入数据详情"],
          sub:"settings",
          menu:"data-manage",
          requireAuth:true
        },
      },
      {
        name:"org-manage",
        path: "/org-manage",
        component: () => import("@/views/manage/org-manage.vue"),
        meta: {
          breadcrumb: ["数据管理", "机构管理"],
          sub:"settings",
          menu:"org-manage",
          requireAuth:true
        },
      },
      {
        name:"user-manage",
        path: "/user-manage",
        component: () => import("@/views/manage/user-manage.vue"),
        meta: {
          breadcrumb: ["数据管理", "用户管理"],
          sub:"settings",
          menu:"user-manage",
          requireAuth:true
        },
      },
    ]
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// 导航守卫

router.beforeEach((to, from, next) => {
  // 在路由导航之前执行的逻辑
  if(to.meta.requireAuth) {
    if(checkAuth()) {
      next();
    } else {
      next('/login');
    }
  } else {
    next();
  }
  // table动态赋值
  if (to.name == 'table-detail') {
    to.meta.menu = to.path.substring(1)
  }
  // 跳转
  // next()
});

export default router;