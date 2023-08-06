<template>
    <div class="data_con">
        <div class="data_head">
            <div class="data_title">{{ title }}</div>
            <div class="data_filter"></div>
        </div>
        <div class="data_body">
            <div class="data_main">
                <div :style="{ height: db_height, width: db_width }" :id="id"></div>
            </div>
        </div>
    </div>
</template>

<style>
@import url('../../assets/style/dashboard.css');
@import url('../../assets/style/colorset.css');
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
            id: {
                type: String,
                default: "retail-income"
            },
            option_data: {
                type: Object,
            },
            title: {
                type: String,
            }
        },
        data() {
            return {
                db_height: '13rem',
                db_width: '33rem'
            };
        },
        mounted() {
            this.drawLine();
        },
        methods: {
            async drawLine() {
                // console.log(this.id);
                let myChart = echarts.init(document.getElementById(this.id));
                myChart.setOption(this.option_data)
            }
        }
    }
) 
</script>