import { createRouter, createWebHistory } from "vue-router";

// 定义路由配置
const routes = [
  {
    path: "/",
    redirect: "/dashboard-other",
  },
  {
    name: "数据看板",
    children: [
      {
        path: "/dashboard-main",
        component: () => import("../views/dashboard/dashboard-main.vue"),
        name: "重要指标分析",
      },
      {
        path: "/dashboard-other",
        component: () => import("../views/dashboard/dashboard-other.vue"),
        name: "同业指标分析",
      },
    ],
  },
  {
    name: "业绩排行",
    children: [
      {
        path: "/rank-important",
        component: () => import("../views/rank/rank-important.vue"),
        name: "重要指标排行",
        children: [
          {
            path: "/rank-detail",
            component: () => import("../views/rank/rank-detail.vue"),
            name: "指标详情",
          },
        ],
      },
    ],
  },
  {
    name: "数据报表",
    children: [
      {
        path: "/enterprise-table",
        component: () => import("../views/table/enterprise-table.vue"),
        name: "企金数据报表",
      },
      {
        path: "/retail-table",
        component: () => import("../views/table/retail-table.vue"),
        name: "零售数据报表",
      },
      {
        path: "/bank-table",
        component: () => import("../views/table/bank-table.vue"),
        name: "同业数据报表",
      },
      {
        path: "/other-table",
        component: () => import("../views/table/other-table.vue"),
        name: "其他数据报表",
      },
    ],
  },
  {
    name: "数据管理",
    children: [
      {
        path: "/data-manage",
        component: () => import("../views/manage/data-manage.vue"),
        name: "数据导入",
        children: [
          {
            path: "/data-detail",
            component: () => import("../views/manage/data-detail.vue"),
            name: "导入详情",
          },
        ],
      },
      {
        path: "/org-manage",
        component: () => import("../views/manage/org-manage.vue"),
        name: "机构管理",
      },
      {
        path: "/user-manage",
        component: () => import("../views/manage/user-manage.vue"),
        name: "用户管理",
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
