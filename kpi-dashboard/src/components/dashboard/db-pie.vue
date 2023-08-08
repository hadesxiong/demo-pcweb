<template>
    <div class="d_flex fd_c bd_4 bg_white">
        <div class="d_flex jc_sb">
            <div class="d_flex jc_sb">
                <div class="c-data_title d_iflex gap_10 font_16 fw_500 fc_l1 lh_20 m_20">{{db_data.db_title}}</div>
            </div>
            <div class="c-data_filter"></div>
        </div>
        <div class="d_flex jc_c fai_c w_p100 pl_20 pr_20 pb_20">
            <div class="d_flex jc_sb mt_20 fai_c">
                <div :style="{ height: pie_height, width: pie_width }" :id="id" class="mr_20"></div>
                <div class="d_flex fwrap_w jc_fs gap_16 fs_0">
                    <div class="d_flex br_4 fd_c p_16 gap_10 jc_c card_bgc"  v-for="(item,index) in db_data.db_other.card_data" :key="index">
                        <div class="font_14 fw_400 lh_22 ta_l fc_l2">{{item.card_title}}</div>
                        <div class="d_flex fai_b jc_sb gap_12">
                            <div class="fc_l4 lh_30 font_12 fw_700"><span class="font_18 fc_l1">{{item.value_current}}</span> / {{ item.value_max }}</div>
                            <div class="c-data_bar fg_1 bg_l3">
                                <div class="bar_value br_tr4 br_br4 fs_0" :class="item.class" :style="{width: item.value_rate}"></div>
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
@import url('../../assets/style/colorset.css');
@import url('../../assets/style/common.css');

.card_bgc {
    background: #f7f8fa;
}
.c-data_bar {
    width: auto;
    height: 12px;
    min-width: 100px;
}
.bar_value {
    width: 33%;
    height: 12px;
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
        id: {
            type: String,
            default: "score_1",
        },
        db_data: {
            type:Object,
        },
        // title:{
        //     type:String,
        //     default:"看到这个说明接口失效了"
        // }
    },
    data() {
        return {
            pie_height: '174px',
            pie_width:'174px'
        };
    },
    mounted() {
        this.drawLine();
    },
    methods: {
        drawLine() {
            // 基于准备好的dom，初始化echarts实例
            let myChart = echarts.init(document.getElementById(this.id));
            // 绘制图表

            myChart.setOption(this.db_data.db_option)
            //添加自适应
            window.addEventListener('resize', function () {
                myChart.resize();
            })
        },
    },
};
</script>
  