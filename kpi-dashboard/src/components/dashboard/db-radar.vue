<template>
    <div class="c-data_con">
        <div class="c-data_head">
            <div class="c-head_left">
                <div class="c-data_title">机构画像</div>
            </div>
            <div class="c-data_filter"></div>
        </div>
        <div class="c-data_body">
            <div class="c-data_main">
                <div :style="{ height: height, width: width }" :id="id"></div>
            </div>
        </div>
    </div>
</template>

<style>
@import url('../../assets/style/dashboard.css');
@import url('../../assets/style/colorset.css');
</style>

<script>
let echarts = require("echarts/lib/echarts")
require("echarts/lib/chart/radar")
require("echarts/lib/component/tooltip")
require("echarts/lib/component/grid")

export default {
    name: "DashboardRadar",
    props: {
        height: {
            type: String,
            default: "12.875rem",
        },
        width: {
            type: String,
            default: "27.875rem",
        },
        id: {
            type: String,
            default: "score_2"
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
                tooltip: {},
                radar: {
                    center: ['50%', '55%'],
                    radius: '75%',
                    name: {
                        show:true,
                        textStyle: {
                            color: '#999',
                            borderRadius: 4,
                            fontSize:"0.875rem",
                            padding: [1, 6],
                        }
                    },
                    indicator: [
                        { name: '财务效益', max: 200 },
                        { name: '客户建设', max: 300 },
                        { name: '转型发展', max: 200 },
                        { name: '社会责任', max: 180 },
                        { name: '风险合规', max: 200 },
                    ]
                },
                series: [{
                    name: '机构画像',
                    type: 'radar',
                    // areaStyle: {normal: {}},
                    data: [
                        {
                            value: [170, 60, 123, 150, 120],
                            symbol:'circle',
                            symbolSize: 4,
                            itemStyle:{
                                color:"#249EFF",
                            },
                            // name: '预算分配（Allocated Budget）'
                            areaStyle:{
                                color:'rgba(36, 158, 255, 0.40)'
                            },
                            lineStyle:{
                                color: '#249EFF'
                            }
                        }
                    ]
                }]
            });
        }
    }
}

</script>