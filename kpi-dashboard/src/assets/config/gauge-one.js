// 仪表盘配置导出项
export const gaugeOption = {
  type: "gauge",
  min:0,
  max: 1000,
  anchor: {
    show: true,
    showAbove: true,
    size: 16,
    itemStyle: {
      color: "#fff",
      borderColor: "#f53f3f",
      borderWidth: 4,
    },
  },
  pointer: {
    show: false,
    icon: "path://M2.9,0.7L2.9,0.7c1.4,0,2.6,1.2,2.6,2.6v115c0,1.4-1.2,2.6-2.6,2.6l0,0c-1.4,0-2.6-1.2-2.6-2.6V3.3C0.3,1.9,1.4,0.7,2.9,0.7z",
    width: 4,
    itemStyle:{color:'#f53f3f'},
    length: "65%",
    offsetCenter: [0, "8%"],
  },
  progress: {
    show: true,
    overlap: true,
    roundCap: true,
    clip: true,
    width: 12,
    itemStyle: {
      borderColor: "#fff",
      borderWidth: 2,
    },
  },
  axisTick: {
    distance: 4,
    lineStyle: { color: "#c9cdd4" },
  },
  axisLine: {
    roundCap: true,
    lineStyle: { width: 12, color: [[1, "#c9cdd4"]] },
  },
  axisLabel: { show: false },
  splitLine: {
    distance: 4,
    lineStyle: { color: "#c9cdd4" },
  },
  title: { show: false },
  detail: { 
    show: false,
    formatter: ['{detail_title|综合得分}','{detail_value|{value}}'].join('\n'),
    rich: {
        detail_title: {color:'#4e5969',fontSize:16,padding: [0, 10, 0, 10],},
        detail_value: {color:'#1D2129',fontSize:28,fontWeight:800}
    },
    offsetCenter: [0, '60%']
 },
  data: {},
};
