<template>
    <div class="bg_white d_flex p_20 fd_c gap_20 br_4 w_p100 h_p100">
        <div class="d_flex fd_r jc_sb">
            <div class="d_flex gap_20 fai_c jc_fs">
                <div class="font_16 fw_500 fc_l1">{{ bar_data.db_title }}</div>
                <div :class="bar_data.tag_class" class="br_4">{{ bar_data.tag_name }}</div>
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
                <a-date-picker picker="month" :bordered="false" class="custom_dp" :allowClear="false">
                    <template #suffixIcon>
                        <icon-park type="Down" size="14" class="d_flex fai_c" fill="#165fdd"></icon-park>
                    </template>
                </a-date-picker>
            </div>
        </div>
        <div class="d_flex jc_c fai_c w_p100 h_p100">
            <div class="d_flex jc_sb fai_c w_p100">
                <div :style="{ height: db_height, width: db_width }" :id="db_id" class="w_p100 h_p100"></div>
            </div>
        </div>
    </div>
</template>

<style>
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
import { defineComponent } from 'vue';
import { IconPark } from '@icon-park/vue-next/es/all';

import { echartsResize } from '@/utils/echartsResize.js';

let echarts = require("echarts/lib/echarts")
require("echarts/lib/chart/bar")
require("echarts/lib/component/tooltip")
require("echarts/lib/component/grid")
export default defineComponent({
    name: "DBNBar2",
    components: {
        'icon-park': IconPark,
    },
    props: {
        db_id: {
            type: String
        },
        bar_data: {
            type: Object
        }
    },
    data() {
        return {
            db_width: "100%",
            db_height: "100%"
        };
    },
    setup() { },
    mounted() {
        this.drawLine();
    },
    methods: {
        drawLine() {
            // console.log(this.id);
            let myChart = echarts.init(document.getElementById(this.db_id));
            myChart.setOption(this.bar_data.db_option);
            //添加自适应
            // window.addEventListener('resize', function () {
            //     myChart.resize();
            // })
            document.getElementById(this.db_id).addEventListener('resize', function () {
                myChart.resize();
            });
            echartsResize(document.getElementById(this.db_id), myChart);
        }
    }
})
</script>