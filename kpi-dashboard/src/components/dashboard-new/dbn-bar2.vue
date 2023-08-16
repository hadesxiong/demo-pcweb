<template>
    <div class="bg_white d_flex p_20 fd_c gap_20 br_4 w_p100 h_p100">
        <div class="d_flex fd_r jc_sb">
            <div class="d_flex gap_20 fai_c jc_fs">
                <div class="font_16 fw_500 fc_l1">{{ bar_data.db_title }}</div>
                <div :class="bar_data.tag_class" class="br_4">{{ bar_data.tag_name }}</div>
            </div>
            <div class="filter"></div>
        </div>
        <div class="d_flex jc_c fai_c w_p100 h_p100">
            <div class="d_flex jc_sb fai_c w_p100">
                <div :style="{ height: db_height, width: db_width }" :id="db_id" class="w_p100 h_p100"></div>
            </div>
        </div>
    </div>
</template>

<script>
import { defineComponent } from 'vue';
let echarts = require("echarts/lib/echarts")
require("echarts/lib/chart/bar")
require("echarts/lib/component/tooltip")
require("echarts/lib/component/grid")
export default defineComponent({
    name: "DBNBar2",
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
            document.getElementById(this.db_id).addEventListener('resize',function(){
                myChart.resize();
            })
        }
    }
})
</script>