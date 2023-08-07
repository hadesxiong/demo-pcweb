<template>
    <div class="c-data_con">
        <div class="c-data_head">
            <div class="c-head_left">
                <div class="c-data_title">考核评分</div>
            </div>
            <div class="c-data_filter"></div>
        </div>
        <div class="c-data_body">
            <div class="c-data_main">
                <div :style="{ height: height, width: width }" :id="id" class="ml_20 mr_20"></div>
                <div class="c-card_con">
                    <div class="c-card_main">
                        <div class="c-card_title">企金指标得分</div>
                        <div class="c-card_data">
                            <div class="data_num"><span>100</span> / 200</div>
                            <div class="c-data_bar">
                                <div class="bar_value linear_blue"></div>
                            </div>
                        </div>
                    </div>
                    <div class="c-card_main">
                        <div class="c-card_title">零售指标得分</div>
                        <div class="c-card_data">
                            <div class="data_num"><span>100</span> / 200</div>
                            <div class="c-data_bar">
                                <div class="bar_value linear_red"></div>
                            </div>
                        </div>
                    </div>
                    <div class="c-card_main">
                        <div class="c-card_title">同业指标得分</div>
                        <div class="c-card_data">
                            <div class="data_num"><span>100</span> / 200</div>
                            <div class="c-data_bar">
                                <div class="bar_value linear_purple"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </div>

    </div>
</template>

<style>
/* 引入dashboard基本样式 */
@import url('../../assets/style/dashboard.css');
@import url('../../assets/style/colorset.css');
@import url('../../assets/style/common.css');


.data_num {
    color: #C9CDD4;
    font-size: 12px;
    line-height: 30px;
    letter-spacing: 0.5px;
    font-weight: 700;
}

.data_num span {
    font-size: 18px;
    color: #0F172A;
    line-height: 30px;
}

.c-data_bar {
    width: auto;
    height: 12px;
    background-color: #e5e6eb;
    flex-grow: 1;
    min-width: 100px;
}

.bar_value {
    border-radius: 0 4px 4px 0;
    width: 33%;
    height: 12px;
    flex-shrink: 0;
}

.linear_blue {
    background: linear-gradient(270deg, rgba(27, 85, 255, 0.50) 0%, #2563EB 100%);
}

.linear_red {
    background: linear-gradient(270deg, rgba(255, 110, 102, 0.50) 0%, #FF6E66 100%);
}

.linear_purple {
    background: linear-gradient(270deg, rgba(195, 76, 217, 0.52) 0%, #C34CD9 100%);
}
</style>

<script>
// 引入基本模板
let echarts = require("echarts/lib/echarts");
// 引入柱状图组件
//   require("echarts/lib/chart/bar");
require("echarts/lib/chart/pie")
// 引入提示框和title组件
require("echarts/lib/component/tooltip");
require("echarts/lib/component/title");
// 不引入这个会报错 xAxis "0" not found
require("echarts/lib/component/grid");
require("echarts/lib/component/graphic")

export default {
    name: "DashboardPie",
    props: {
        height: {
            type: String,
            default: "180px",
        },
        width: {
            type: String,
            default: "180px",
        },
        id: {
            type: String,
            default: "score_1",
        },
    },
    data() {
        return {};
    },
    mounted() {
        this.drawLine();
    },
    methods: {
        drawLine() {
            // 基于准备好的dom，初始化echarts实例
            console.log(this.id);
            let myChart = echarts.init(document.getElementById(this.id));
            // 绘制图表
            myChart.setOption({
                tooltip: {
                    trigger: 'item',
                    formatter: '{b}: {c}'
                },
                series: [
                    {
                        name: '指标得分',
                        hoverAnimation: false,
                        type: 'pie',
                        center: ['50%', '50%'],
                        radius: ['70%', '90%'],
                        avoidLabelOverlap: false,
                        label: {
                            show: false,
                            position: 'center'
                        },
                        emphasis: {
                            label: {
                                show: false,
                                fontSize: 20,
                                fontWeight: 'bold'
                            }
                        },
                        labelLine: {
                            show: false
                        },
                        data: [
                            { value: 100, name: '企金指标得分', itemStyle: { color: "#1B55FF" } },
                            { value: 100, name: '零售指标得分', itemStyle: { color: "#FF6E66" } },
                            { value: 100, name: '同业指标得分', itemStyle: { color: "#C34CD9" } },
                            { value: 300, tooltip: { show: false }, itemStyle: { color: '#F7F8FA' }, emphasis: { itemStyle: { color: '#F7F8FA' } } }
                        ],
                    }
                ],
                graphic: {
                    elements: [{
                        type: 'text',
                        style: {
                            text: '综合评分',
                            fontSize: '16px',
                            textAlign: 'center',
                            width: 'auto',
                            height: 'auto'
                        },
                        left: 'center',
                        top: '40%'
                    }, {
                        type: 'text',
                        style: {
                            text: '753',
                            fontSize: '22px',
                            fontWeight: 'bold',
                            textAlign: 'center',
                            width: 'auto',
                            height: 'auto'
                        },
                        left: 'center',
                        top: '55%'
                    }]
                }
            });
            //添加自适应
            window.addEventListener('resize', function () {
                myChart.resize();
            })
        },
    },
};
</script>
  