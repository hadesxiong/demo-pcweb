<template>
    <div class="w_p100 bg_white br_4 d_flex fd_c minw_p100 h_p100">
        <div class="h_60 d_flex jc_sb pl_20 pr_20 pt_16 pb_16 fai_c bb_w1c2_so">
            <div class="d_iflex gap_12 fai_c lh_30">
                <div>
                    <a-button class="bak_btn" @click="goBack">
                        <template #icon>
                            <icon-left size="16" class="btn_icon bak_icon" theme="outline"></icon-left>
                        </template>
                    </a-button>
                </div>
                <div class="font_18 fw_500">{{ detail_info.index_name }}</div>
                <div>
                    <a-tag :class="detail_info.tag_class">{{ detail_info.class_name }}</a-tag>
                </div>
                <a-divider type="vertical" style="height: 18px; border-color: #E5E6EB; top: 0;"></a-divider>
                <div class="fc_l3">
                    数据月份: {{ detail_info.date.slice(0,7) }}
                </div>
                <div class="fc_l3">
                    查看方式: {{ detail_info.view_method }}
                </div>
            </div>
            <div>
                <a-button class="br_2 fai_c d_flex fc_l5 bg_brand6">
                    <template #icon>
                        <icon-download size="14" class="btn_icon"></icon-download>
                    </template>
                    导出</a-button>
            </div>
        </div>
        <div class="m_20 of_a h_p100">
            <a-table :columns="detail_data.table_column" :data-source="detail_data.table_data" :pagination="false"
                :scroll="{ y: true }" :expandIconColumnIndex="1" :expandIconAsCell="false" :indentSize="0"
                class="b_w1c2_so br_2">
                <template #innerExpand="{ record }">
                    <span v-if="record.children">
                        <!-- <a @click="toggleExpand(record)">展开</a> -->
                    </span>
                </template>
                <template #bodyCell="{ column, record }">
                    <template v-if="column.dataIndex === 'data_operation'">
                        <div class="fc_brand6 d_iflex gap_8">
                            <a id="history_btn" @click="showHistoryData(record)">查看历史</a>
                            <!-- <a id="belong_btn">查看下属机构</a> -->
                        </div>
                    </template>
                </template>
            </a-table>
        </div>
        <div class="d_flex fai_c jc_fe p_20">
            <a-pagination :current="page_obj.current" :total="page_obj.total" :pageSize="page_obj.pageSize"
                @change="handlePageChange"></a-pagination>
        </div>
        <a-drawer :width="850" :visible="draw_visible" @close="onClose" :closable="false">
            <template #title>
                <div class="d_flex gap_12 fai_c">
                    <div class="font_16 fc_l1 fw_500">历史数据</div>
                    <a-divider type="vertical"></a-divider>
                    <div class="font_14 fc_l3 fw_normal">徐汇区域中心支行</div>
                    <div class="font_14 fc_l3 fw_normal">营业净收入</div>
                </div>
            </template>
            <template #extra>
                <a-button class="bak_btn" @click="onClose">
                    <template #icon>
                        <icon-close size="14" class="btn_icon bak_icon" theme="outline"></icon-close>
                    </template>
                </a-button>
            </template>
            <div class="d_flex fd_c w_p100 gap_8">
                <div class="d_iflex fai_c lh_20 fc_l3 gap_16 lh_32">
                    <div class="d_iflex gap_12 fai_c">
                        <div class="blue_dot"></div>
                        期末数
                    </div>
                    <div class="d_iflex gap_12 fai_c">
                        <div class="purple_dot"></div>
                        计划完成率
                    </div>
                </div>
                <div :style="{ height: line_height, width: line_width }" id="line_con"></div>
                <a-divider></a-divider>
                <div class="ofx_a font_13 fw_400 b_w1c2_so br_4">
                    <a-table :columns="history_table.table_column" :data-source="history_table.table_data"
                        :pagination="false">

                    </a-table>
                </div>
            </div>
            <template #footer>
                <div class="d_flex jc_fe pt_10 pb_10">
                    <a-button type="primary" @click="onClose" class="br_2 fai_c d_flex fc_l5 bg_brand6 mr_8">
                        <template #icon>
                            <icon-download size="14" class="btn_icon"></icon-download>
                        </template>
                        导出
                    </a-button>
                </div>
            </template>
        </a-drawer>
    </div>
</template>

<style>
@import url('@/assets/style/common.css');
@import url('@/assets/style/colorset.css');
@import url('@/assets/style/overwrite.css');

.btn_icon {
    margin-right: 8px;
    height: 14px;
    line-height: 1px;
}

.bak_btn {
    width: 16px !important;
    border: none;
}

.bak_icon {
    display: block !important;
    margin: 0 auto;
}

.blue_dot {
    width: 6px;
    height: 6px;
    border-radius: 10px;
    background-color: #165DFF;
    border: 2px solid #BEDAFF;
}

.purple_dot {
    width: 6px;
    height: 6px;
    border-radius: 10px;
    background-color: #722ED1;
    border: 2px solid #F5E8FF;
}
</style>

<script>
import { defineComponent, ref } from 'vue';
import { Left, Download, Close } from '@icon-park/vue-next';
import { Button, Divider, Tag, Table, Pagination, Drawer } from 'ant-design-vue';
import axios from 'axios';
import { useRoute } from 'vue-router';
import { Base64 } from 'js-base64';

import * as echarts from 'echarts/lib/echarts.js';
import 'echarts/lib/component/tooltip';
import 'echarts/lib/component/grid';
import 'echarts/lib/chart/line';

export default defineComponent({
    name: 'RankDetail',
    components: {
        'icon-left': Left,
        'icon-download': Download,
        'icon-close': Close,
        'a-button': Button,
        'a-divider': Divider,
        'a-tag': Tag,
        'a-table': Table,
        'a-pagination': Pagination,
        'a-drawer': Drawer,
    },
    data() {
        return {
            id: 'line_con',
            line_width: '780px',
            line_height: "320px",
            detail_data: {},
            draw_visible: false,
            history_table: {}
        }
    },
    setup() {
        const route = useRoute();
        const rank_id = route.params.rank_id;
        const detail_info = JSON.parse(Base64.decode(rank_id))
        console.log(detail_info)
        return {
            detail_info,
            page_obj: ref({
                current: 1,
                pageSize: 10,
                total: 100
            })
        }
    },
    mounted() {
        this.getRankDetailData();
    },
    methods: {
        async getRankDetailData() {
            const detail_res = await axios.get('/demo/rank/rank-detail.json');
            // console.log(detail_res.data);
            this.detail_data = detail_res.data;
            // console.log(this.detail_data);
        },
        async showDrawer() {
            this.draw_visible = true;
        },
        async showHistoryData(record) {

            console.log(record)

            this.draw_visible = true;
            const history_data = await axios.get('/demo/rank/history-data.json');
            // console.log(history_data.data);
            this.history_table = history_data.data.table_data;
            // console.log(this.history_table);
            this.line_data = history_data.data.echarts_data
            let myChart = echarts.init(document.getElementById(this.id));
            let myChart_option = this.line_data;
            myChart_option.series[0].areaStyle.color = new echarts.graphic.LinearGradient(0.5, 0, 0.5, 1, [
                { offset: 0, color: "rgba(100, 162, 255, 0.12)" },
                { offset: 1, color: 'rgba(52, 105, 255, 0.01)' }
            ]);
            myChart_option.series[1].areaStyle.color = new echarts.graphic.LinearGradient(0.5, 0, 0.5, 1, [
                { offset: 0, color: 'rgba(131, 100, 255, 0.12)' },
                { offset: 1, color: 'rgba(80, 52, 255, 0.01)' }
            ])
            myChart_option.xAxis.axisLabel.formatter = function (value, index) {
                if (index === 0) {
                    return '{start|' + value + '}';
                } else if (index == myChart_option.xAxis.data.length - 1) {
                    return '{end|' + value + '}';
                } else {
                    return value;
                }
            };
            myChart.setOption(myChart_option);
            // 添加自适应
            window.addEventListener('resize', function () {
                myChart.resize();
            })

        },
        onClose() {
            this.draw_visible = false;
        },
        goBack() {
            this.$router.go(-1)
        },
        handlePageChange(page) {
            console.log(page)
            this.page_obj.current = page
        }
    }

});

</script>