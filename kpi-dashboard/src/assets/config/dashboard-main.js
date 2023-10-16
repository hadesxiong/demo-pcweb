// 数据看板相关配置
export const cardConfMap = {
  rt_cb: {
    card_title: "零售客户建设情况",
    tag_name: "客户建设",
    tag_class: "tag_pink_purple",
    card_col: 6,
  },
  et_cb: {
    card_title: "企金客户建设情况",
    tag_name: "客户建设",
    tag_class: "tag_pink_purple",
    card_col: 12,
  },
  all_lcrj: {
    card_title: "理财日均保有量",
    tag_name: "转型与质量发展",
    tag_class: "tag_orange",
    card_col: 12,
  },
};

export const vBarConfMap = {
  all_yyjsr: {
    bar_title: "营业净收入 - 近6月",
    tag_name: "财物效益",
    tag_class: "tag_magenta",
    map_list: ["EF_001", "RF_001", "BF_001"],
  },
  all_eva: {
    bar_title: "EVA - 近6月",
    tag_name: "财物效益",
    tag_class: "tag_magenta",
    map_list: ["EF_002", "RF_002", "BF_002"],
  },
};

export const vBarConfOptions = {
  tooltip: {},
  grid: {
    left: "0%",
    right: "4%",
    bottom: "3%",
    width: "100%",
    height: "100%",
    containLabel: true,
  },
  yAxis: {
    type: "value",
    splitLine: { lineStyle: { type: "dashed" } },
  },
  xAxis: {
    type: "category",
    data: [],
    axisLine: { lineStyle: { color: "#E5E8EF", type: "dashed" } },
    axisLabel: { color: "#86909C", type: "dashed" },
  },
  series: [
    {
      name: "企金条线",
      type: "bar",
      stack: "total",
      barCategoryGap: "65%",
      label: { show: false },
      emphasis: { focus: "none" },
      itemStyle: { color: "#246EFF" },
      data: [],
    },
    {
      name: "零售条线",
      type: "bar",
      stack: "total",
      label: { show: false },
      emphasis: { focus: "none" },
      itemStyle: { color: "#00B2FF" },
      data: [],
    },
    {
      name: "同业条线",
      type: "bar",
      stack: "total",
      label: { show: false },
      emphasis: { focus: "none" },
      itemStyle: { color: "#81E2FF" },
      data: [],
    },
  ],
};

export const hBarConfMap = {
  all_aum: {
    bar_title: "AUM日均数据",
    tag_name: "转型与质量发展",
    tag_class: "tag_orange",
    map_list: ["ED_005", "RD_001"],
    y_list: ["企金", "零售"],
    color_map: ["#246eff", "#6AA1FF"],
  },
};

export const hBarConfOptions = {
  tooltip: {},
  grid: {
    left: "0%",
    right: "4%",
    bottom: "4%",
    top: "0%",
    containLabel: true,
  },
  xAxis: {
    type: "value",
    boundaryGap: [0, 0.01],
    splitLine: { lineStyle: { color: "#e5e8ef" } },
    axisLabel: { color: "#4e5969", margin: 8 },
  },
  yAxis: {
    type: "category",
    data: [],
    axisLine: { lineStyle: { color: "#e5e8ef" } },
    axisLabel: { color: "#4e5969" },
  },
  series: [
    {
      name: "企金",
      type: "bar",
      barCategoryGap: "25%",
      data: [],
      itemStyle: { color: "#246eff", borderRadius: [0, 4, 4, 0] },
    },
  ],
};

export const changeLineConfMap = {
  all_ckrj: {
    line_title: "存款日均情况 - 近6月",
    tag_name: "转型与质量发展",
    tag_class: "tag_orange",
    series_name: ["一般性存款", "低成本存款"],
    change_map: [
      { key: "enterprise", value: "企金" },
      { key: "retail", value: "零售" },
    ],
    map_list: {
      enterprise: ["ED_003", "ED_004"],
      retail: ["RD_002", "RD_003"],
    },
  },
};

export const changeLineConfOptions = {
  tooltip: {},
  grid: {
    left: 0,
    right: 8,
    top: 4,
    bottom: 12,
    height: "95%",
    containLabel: true,
  },
  xAxis: {
    type: "category",
    data: [],
    axisLine: { lineStyle: { color: "#e5e8ef", type: "dashed" } },
    axisLabel: {
      interval: 0,
      color: "#86909c",
      type: "dashed",
      align: "center",
      rich: {
        start: { padding: [0, 0, 0, 35] },
        end: { padding: [0, 35, 0, 0] },
      },
    },
    boundaryGap: false,
  },
  yAxis: {
    type: "value",
    axisLabel: { margin: 24 },
    splitLine: { lineStyle: { type: "dashed" } },
  },
  series: [
    {
      name: "",
      data: [],
      type: "line",
      smooth: true,
      symbol: "none",
      lineStyle: { color: "#3469ff" },
      areaStyle: { color: "" },
    },
    {
      name: "",
      data: [],
      type: "line",
      smooth: true,
      symbol: "none",
      lineStyle: { color: "#722ED1" },
      areaStyle: { color: "" },
    },
  ],
};
