<template>
    <div class="c-data_con d_flex fd_c bd_4 bg_white">
        <div class="d_flex jc_sb">
            <div class="d_flex jc_sb">
                <div class="d_iflex gap_10 font_16 fw_500 fc_l1 lh_20 m_20">机构画像</div>
            </div>
            <div class="c-data_filter"></div>
        </div>
        <div class="d_flex jc_c fai_c pl_20 pr_20 pb_20">
            <div class="d_flex jc_sb fai_c">
                <div :style="{ height: radar_height, width: radar_width }" :id="id"></div>
            </div>
        </div>
    </div>
</template>

<style>

</style>

<script>
let echarts = require("echarts/lib/echarts")
require("echarts/lib/chart/radar")
require("echarts/lib/component/tooltip")
require("echarts/lib/component/grid")

export default {
    name: "DashboardRadar",
    props: {
        id: {
            type: String,
            default: "score_2"
        },
        db_data:{
            type:Object
        }
    },
    data() {
        return {
            radar_height:"200px",
            radar_width:"446px"
        };
    },
    mounted() {
        this.drawLine();
    },
    methods: {
        drawLine() {
            // console.log(this.id);
            let myChart = echarts.init(document.getElementById(this.id));
            myChart.setOption(this.db_data.db_option);
        }
    }
}

</script>