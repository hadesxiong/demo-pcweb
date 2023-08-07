<template>
    <div class="data_con">
        <div class="data_head">
            <div class="head_left">
                <div class="data_title">AUM日均</div>
                <div class="data_label label_orange">转型与质量发展</div>
            </div>
            <div class="data_filter"></div>
        </div>
        <div class="btn_switch flex-align-fs">
            <a-radio-group default-value="company" button-style="solid">
                <a-radio-button value="company">企金</a-radio-button>
                <a-radio-button value="retial">零售</a-radio-button>
            </a-radio-group>
        </div>
        <div class="data_body">
            <div class="data_main">
                <div :style="{ height: height, width: width }" :id="id"></div>
            </div>
        </div>
    </div>
</template>

<style>
@import url('../../assets/style/dashboard.css');
@import url('../../assets/style/colorset.css');

.btn_switch {
    display: flex;
    margin-left: 1.25rem;
}
</style>

<script>
let echarts = require("echarts/lib/echarts")
require("echarts/lib/chart/bar")
require("echarts/lib/component/tooltip")
require("echarts/lib/component/grid")

export default {
    name: "dashboard_bar",
    props: {
        height: {
            type: String,
            default: "100%"
        },
        width: {
            type: String,
            default: "30rem"
        },
        id: {
            type: String,
            default: "rank_bar"
        }
    },
    data() {
        return {};
    },
    mounted() {
        this.drawLine();
    },
    methods: {
        drawLine() {
            console.log(this.id);
            let myChart = echarts.init(document.getElementById(this.id));

            myChart.setOption({
                tooltip: {
                    // trigger: 'axis',
                    // axisPointer: {
                    // Use axis to trigger tooltip
                    // type: 'shadow' // 'shadow' as default; can also be 'line' or 'shadow'
                    // }
                },
                grid: {
                    left: '0%',
                    right: '4%',
                    bottom: '3%',
                    width: '100%',
                    height: '100%',
                    containLabel: true
                },
                yAxis: {
                    type: 'value',
                    max: function (value) {
                        return value.max + 0.25 * value.max;
                    },
                    splitLine: {
                        lineStyle: {
                            color: ["#E5E8EF"],
                            type: "dashed"
                        }
                    }
                },
                xAxis: {
                    type: 'category',
                    axisLine: {
                        lineStyle: {
                            color: ["#E5E8EF"],
                            type: "dashed"
                        }
                    },
                    axisLabel: {
                        margin: 12,
                    },
                    axisTick: {
                        alignWithLabel: true,
                        lineStyle: {
                            color: "#86909C"
                        }
                    },
                    data: ['2023.01', '2023.02', '2023.03', '2023.04', '2023.05', '2023.06']
                },
                series: [
                    {
                        name: '企金条线',
                        type: 'bar',
                        stack: 'total',
                        barWidth: 28,
                        label: {
                            show: false
                        },
                        emphasis: {
                            focus: 'none'
                        },
                        itemStyle: {
                            color: '#246EFF'
                        },
                        data: [320, 302, 301, 334, 390, 330]
                    },
                    {
                        name: '零售条线',
                        type: 'bar',
                        stack: 'total',
                        label: {
                            show: false
                        },
                        emphasis: {
                            focus: 'none'
                        },
                        itemStyle: {
                            color: '#00B2FF'
                        },
                        data: [120, 132, 101, 134, 90, 230]
                    },
                    {
                        name: '同业条线',
                        type: 'bar',
                        stack: 'total',
                        label: {
                            show: false
                        },
                        emphasis: {
                            focus: 'none'
                        },
                        itemStyle: {
                            color: '#81E2FF',
                            borderRadius: [4, 4, 0, 0]
                        },
                        data: [220, 182, 191, 234, 290, 330]
                    }
                ]

            });
            //添加自适应
            window.addEventListener('resize', function () {
                myChart.resize();
            })
        }
    }
}
</script>