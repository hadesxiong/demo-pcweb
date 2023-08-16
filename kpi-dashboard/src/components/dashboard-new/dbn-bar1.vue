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
                <div :style="{ height: db_height, width: db_width }" :id="id"></div>
            </div>
        </div>
    </div>
</template>

<style></style>

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
            id: {
                type: String,
                default: "retail-income"
            },
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
                let myChart = echarts.init(document.getElementById(this.id));
                myChart.setOption(this.bar_data.db_option);
                // 添加自适应
                document.getElementById(this.id).addEventListener('resize', function () {
                    myChart.resize();
                })
            }
        }
    }
) 
</script>