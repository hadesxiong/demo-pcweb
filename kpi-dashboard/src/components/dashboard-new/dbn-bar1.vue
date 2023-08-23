<template>
    <div class="bg_white d_flex p_20 fd_c gap_20 br_4 w_p100 h_p100">
        <div class="d_flex jc_sb">
            <div class="d_flex gap_20 fai_c jc_fs">
                <div class="d_iflex font_16 fw_500 fc_l1 lh_20 ">{{ bar_data.db_title }}</div>
                <div class="d_iflex br_4" :class="bar_data.db_tag.tag_class">{{ bar_data.db_tag.tag_name }}</div>
            </div>
            <div class="d_flex fai_c jc_fe gap_16">
                <a-dropdown>
                    <a class="d_flex fai_c gap_8 fc_brand6">
                        上海分行
                        <icon-park type="Down" size="14" class="d_flex fai_c" fill="#165fdd"></icon-park>
                    </a>
                    <template #overlay>
                        <a-menu>
                            <a-menu-item>1st menu item</a-menu-item>
                            <a-menu-item>2nd menu item</a-menu-item>
                            <a-sub-menu key="sub1" title="sub menu">
                                <a-menu-item>3rd menu item</a-menu-item>
                                <a-menu-item>4th menu item</a-menu-item>
                            </a-sub-menu>
                            <a-sub-menu key="sub2" title="disabled sub menu" disabled>
                                <a-menu-item>5d menu item</a-menu-item>
                                <a-menu-item>6th menu item</a-menu-item>
                            </a-sub-menu>
                        </a-menu>
                    </template>
                </a-dropdown>
                <a-range-picker picker="month" :bordered="false" class="custom_dp" :allowClear="false">
                    <template #suffixIcon>
                        <icon-park type="Down" size="14" class="d_flex fai_c" fill="#165fdd"></icon-park>
                    </template>
                    <template #separator>
                        <icon-park type="Minus" size="14" class="d_flex fai_c" fill="#165fdd"></icon-park>
                    </template>
                </a-range-picker>
            </div>
        </div>
        <div class="d_flex jc_c fai_c w_p100 h_p100">
            <div class="d_flex jc_sb fai_c w_p100 h_p100">
                <div :style="{ height: db_height, width: db_width }" :id="bar_data.db_id"></div>
            </div>
        </div>
        <!-- 如果有示例 -->
        <div class="d_flex jc_c fai_c gap_32 h_20 lh_20">
            <div class="d_flex fai_c gap_10" v-for="(item, index) in bar_data.db_option.series" :key="index">
                <div class="dot" :class="`eg_${index + 1}`"></div>
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
.custom_dp {
    padding-left: 0px;
    padding-right: 0px;
}
.custom_dp input {
    color: #165fdd !important;
    width: 55px !important;
}
.custom_dp span {
    padding-left: 0px !important;
    padding-right: 0px !important;
}
</style>

<script>
let echarts = require("echarts/lib/echarts");
require("echarts/lib/chart/bar");
require("echarts/lib/component/tooltip");
require("echarts/lib/component/grid");

import { defineComponent } from "vue";
import { IconPark } from '@icon-park/vue-next/es/all';

import { echartsResize } from '@/utils/echartsResize.js';


export default defineComponent(
    {
        name: "DashboardBar",
        components: {
            'icon-park': IconPark
        },
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
                });
                echartsResize(document.getElementById(this.bar_data.db_id), myChart);
            }
        }
    }
) 
</script>