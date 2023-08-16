<template>
    <div class="d_flex fd_c bd_4 bg_white w_p100 h_p100">
        <div class="d_flex jc_sb">
            <div class="d_flex">
                <div class="d_iflex font_16 fw_500 fc_l1 lh_20 m_20">{{ db_data.db_title }}</div>
                <div class="d_iflex br_4" :class="db_data.db_tag.tag_class">{{ db_data.db_tag.tag_name }}</div>
            </div>
            <div class="data_filter"></div>
        </div>
        <div class="d_flex fai_fs pl_20 pr_20 pb_4 pt_4">
            <a-radio-group v-model:value="chosen_value" button-style="solid">
                <a-radio-button value="enterprise">企金</a-radio-button>
                <a-radio-button value="retial">零售</a-radio-button>
            </a-radio-group>
        </div>
        <div class="d_flex jc_c fai_c pl_20 pr_20 pb_10 pt_10  w_p100 h_p100">
            <div class="d_flex jc_sb fai_c">
                <div :style="{ height: db_height, width: db_width }" :id="id"></div>
            </div>
        </div>
    </div>
</template>

<style scoped>

.ant-radio-group {
    border: 2px solid #f2f3f5;
    border-radius: 4px;
}
.ant-radio-button-wrapper {
    color: #4E5969;
    background-color: #F2F3F5;
    border: 1px solid #f2f3f5;
    height: 32px;
}
.ant-radio-button-wrapper:first-child {
    border-inline-start: 1px solid #f2f3f5;
    border-start-start-radius:0px;
    border-end-start-radius:0px;
}
.ant-radio-button-wrapper:last-child {
    border-start-end-radius:0px;
    border-end-end-radius:0px;
}
.ant-radio-button-wrapper:not(:first-child)::before {
    width: 0px;
}
.ant-radio-button-wrapper-checked {
    border-start-start-radius:2px !important;
    border-end-start-radius:2px !important;
    background-color: #fff !important;
    color: #165dff !important;
    border: 1px solid #f2f3f5 !important;
    font-weight: 700;
}

</style>

<script>
import { defineComponent, ref } from 'vue';

let echarts = require("echarts/lib/echarts")
require("echarts/lib/chart/bar")
require("echarts/lib/component/tooltip")
require("echarts/lib/component/grid")

export default defineComponent({
    name: "DashboardBar2",
    props: {
        id: {
            type: String,
            default: "rank_bar"
        },
        db_data: {
            type:Object
        }
    },
    data() {
        return {
            db_width:"100%",
            db_height: "100%"
        };
    },
    setup() {
        const chosen_value = ref('enterprise');
        return {
            chosen_value
        }
    },
    mounted() {
        this.drawLine();
    },
    methods: {
        drawLine() {
            // console.log(this.id);
            let myChart = echarts.init(document.getElementById(this.id));
            myChart.setOption(this.db_data.db_option);
            //添加自适应
            window.addEventListener('resize', function () {
                myChart.resize();
            })
        }
    }
})
</script>