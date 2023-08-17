<template>
    <div class="d_flex fd_c bd_4 bg_white w_p100 h_p100">
        <div class="d_flex jc_sb">
            <div class="d_flex">
                <div class="d_iflex font_16 fw_500 fc_l1 lh_20 m_20">{{ bar_data.db_title }}</div>
                <div class="d_iflex br_4" :class="bar_data.db_tag.tag_class">{{ bar_data.db_tag.tag_name }}</div>
            </div>
            <div class="c-data_filter"></div>
        </div>
        <div class="d_flex jc_c fai_c pl_20 pr_20 pb_20 w_p100 h_p100">
            <div class="d_flex jc_sb fai_c w_p100 h_p100">
                <div :style="{ height: db_height, width: db_width }" :id="bar_data.db_id"></div>
            </div>
        </div>
        <!-- 如果有示例 -->
        <div class="d_flex jc_c fai_c gap_32 mb_20 h_20 lh_20">
            <div class="d_flex fai_c gap_10" v-for="(item,index) in bar_data.db_option.series" :key="index">
                <div class="dot" :class="`eg_${index+1}`" ></div>
                <div class="fc_l3">{{ bar_data.db_title }} - {{ item.name }}</div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.dot {
    width: 10px;
    height: 10px;
    border-radius: 10px;
}
.eg_1 {
    background-color: #246eff;
}
.eg_2 {
    background-color: #00B2FF;
}
.eg_3 {
    background-color: #81E2FF;
}
</style>

<script>
let echarts = require("echarts/lib/echarts");
require("echarts/lib/chart/bar");
require("echarts/lib/component/tooltip");
require("echarts/lib/component/grid");

import { defineComponent } from "vue";


export default defineComponent(
    {
        name: "DashboardBar",
        props: {
            bar_data: {
                type: Object,
            },
        },
        data() {
            return {
                db_height: '250px',
                db_width: '100%'
            };
        },
        mounted() {
            this.drawLine();
        },
        methods: {
            async drawLine() {
                // console.log(this.id);
                let myChart = echarts.init(document.getElementById(this.bar_data.db_id));
                myChart.setOption(this.bar_data.db_option);
                // 添加自适应
                window.addEventListener('resize', function () {
                    myChart.resize();
                })
            }
        }
    }
) 
</script>