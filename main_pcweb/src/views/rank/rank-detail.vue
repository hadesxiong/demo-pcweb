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
                    数据月份: {{ detail_info.date.slice(0,4) }}.{{ detail_info.date.slice(5,7) }}
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
        <div class="m_20 of_a h_p100" id="table_con">
            <a-spin :spinning="rank_spin" size="large" :delay="100" tip="数据加载中">
                <a-table :columns="detail_table.column" :data-source="detail_table.data" :pagination="false"
                    :scroll="rank_scroll" :expandIconColumnIndex="1" :expandIconAsCell="false" :indentSize="26"
                    @expand="expandRows" class="b_w1c2_so br_2">
                    <template #innerExpand="{ record }">
                        <span v-if="record.children">
                            <!-- <a @click="toggleExpand(record)">展开</a> -->
                        </span>
                    </template>
                    <template #bodyCell="{ column, record, text }">
                        <template v-if="column.dataIndex === 'operation'">
                            <div class="fc_brand6 d_iflex gap_8">
                                <a id="history_btn" @click="showHistoryData(record)">查看历史</a>
                            </div>
                        </template>
                        <template v-if="column.dataIndex.indexOf('value') != -1">
                            <span v-if="column.dataIndex.indexOf('_rate')!=-1" :class="{fc_danger6:text<0,fw_700:text<0}">{{ processNumber(text) }}%</span>
                            <span v-else :class="{fc_danger6:text<0,fw_700:text<0}">{{ processNumber(text) }}</span>
                        </template>
                    </template>
                </a-table>
            </a-spin>
        </div>
        <a-drawer :width="850" :visible="draw_visible" @close="onClose" :closable="false" :destroyOnClose="false">
            <template #title>
                <div class="d_flex gap_8 fai_c">
                    <div class="font_16 fc_l1 fw_500">{{histroy_table.org_name}}</div>
                    <div class="font_16 fc_l3 fw_normal">{{detail_info.index_name}}</div>
                </div>
            </template>
            <template #extra>
                <a-button class="bak_btn" @click="onClose">
                    <template #icon>
                        <icon-close size="14" class="btn_icon bak_icon" theme="outline"></icon-close>
                    </template>
                </a-button>
            </template>
            <div class="d_flex fd_c w_p100 gap_4">
                <div class="d_iflex fai_c lh_20 fc_l3 gap_16 lh_32 mb_8">
                    <div class="d_iflex gap_12 fai_c">
                        <div class="blue_dot"></div>
                        期末数
                    </div>
                    <div class="d_iflex gap_12 fai_c">
                        <div class="purple_dot"></div>
                        计划数
                    </div>
                </div>
                <div :style="{ height: line_height, width: line_width }" id="line_con"></div>
                <a-divider style="margin: 16px 0;"></a-divider>
                <div class="ofx_a font_13 fw_400 b_w1c2_so br_4">
                    <a-spin :spinning="draw_spin" size="large" :delay="100" tip="数据加载中">
                        <a-table :columns="histroy_table.column" :data-source="histroy_table.data" :pagination="false">
                            <template #bodyCell="{ column,text }">
                                <template v-if="column.dataIndex === 'detail_date'">
                                    {{ text.slice(0,4) }}.{{text.slice(5,7)}}
                                </template>
                                <template v-if="column.dataIndex.indexOf('value') != -1">
                                    <span v-if="column.dataIndex.indexOf('_rate')!=-1" :class="{fc_danger6:text<0,fw_700:text<0}">{{ processNumber(text) }}%</span>
                                    <span v-else :class="{fc_danger6:text<0,fw_700:text<0}">{{ processNumber(text) }}</span>
                                </template>
                            </template>
                        </a-table>
                    </a-spin>
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
import { Button, Divider, Tag, Table, Drawer, Spin } from 'ant-design-vue';

import { useRoute } from 'vue-router';
import { Base64 } from 'js-base64';
import { cloneDeep } from 'lodash-es';

import { api } from '@/utils/commonApi.js';
import { tableScrollYResize } from '@/utils/tableScrollYResize.js';
import { detailTableHeadMap, histroyTableHeadMap, histroyEchartsConf } from '@/assets/config/rank-detail.js';
import { processNumber } from '@/utils/processNumber.js';

import * as echarts from 'echarts/lib/echarts.js';
import 'echarts/lib/component/tooltip';
import 'echarts/lib/component/grid';
import 'echarts/lib/chart/line';

const myApi = api();

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
        'a-drawer': Drawer,
        'a-spin': Spin
    },
    data() {
        return {
            id: 'line_con',
            line_width: '802px',
            line_height: "340px",
            detail_data: {},
            draw_visible: false,
            history_table: {}
        }
    },
    setup() {
        const route = useRoute();
        const rank_id = route.params.rank_id;
        const detail_info = JSON.parse(Base64.decode(rank_id))
        return {
            detail_info,
            rank_spin: ref(false),
            draw_spin: ref(false),
            rank_scroll: ref({y:500}),
            detail_table: ref({
                column: ref(detailTableHeadMap),
                data: ref([]),
            }),
            histroy_table: ref({
                column: ref(histroyTableHeadMap),
                data: ref([]),
                cache: ref({}),
                org_name: ref('')
            }),
            echarts_data: ref(histroyEchartsConf),
            myChart:ref()
        }
    },
    mounted() {
        this.getRankDetailData('single',this.detail_info.group,'detail_table','rank_spin');
        window.addEventListener('resize',tableScrollYResize('table_con',this.rank_scroll));
    },
    methods: {
        async getRankDetailData(type,target,data_ref,spin) {
            this[spin] = true;
            const get_params = {
                index: this.detail_info.index_num,
                date: this.detail_info.date,
                type: type,
                target: target
            }
            const rank_res = await myApi.get('/api/rank/getSingleRank',{params:get_params})
            // console.log(rank_res)
            if (type == 'belong') {
                const parent_data = this[data_ref]['data'].find(item => item.detail_belong == target);
                parent_data['children'] = rank_res.data.data;
            } else if(type == 'histroy') {
                this[data_ref]['cache'][target] = rank_res.data.data
            } else if(type == 'single') {
                this[data_ref]['data'] = rank_res.data.data
                this[data_ref]['data'] = this[data_ref]['data'].map((item, index) => { return { ...item, key: (index+1).toString() } });
            }
            this[spin] = false
            // console.log(this[data_ref])
        },
        async showHistoryData(record) {
            this.draw_visible = true;
            this.histroy_table.org_name = cloneDeep(record.org_name)
            // console.log(record)
            // 判断是否已经有了histroy数据
            if (!this.histroy_table.cache[record.detail_belong]) {
                await this.getRankDetailData('histroy',record.detail_belong,'histroy_table','draw_spin')
            }
            this.histroy_table.data = cloneDeep(this.histroy_table.cache[record.detail_belong])

            // 处理echarts_data
            this.echarts_data.xAxis.data = this.histroy_table.data.map(item=> (item.detail_date.slice(0,4)+'.'+item.detail_date.slice(5,7)))
            this.echarts_data.series[0].data = this.histroy_table.data.map(item=> item.value_tm_done)
            this.echarts_data.series[1].data = this.histroy_table.data.map(item=> item.value_ty_plan)

            this.myChart = echarts.init(document.getElementById(this.id));
            let myChart_option = this.echarts_data;
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
            this.myChart.setOption(myChart_option);
            // 添加自适应
            window.addEventListener('resize', function () {
                this.myChart.resize();
            })

        },
        onClose() {
            this.draw_visible = false;
            // 重置数据
            this.myChart.dispose();
            this.histroy_table.data = []
        },
        goBack() {
            this.$router.go(-1)
        },
        expandRows(expanded,record) {
            if (expanded && record.children.length == 0) {
                this.getRankDetailData('belong',record.detail_belong,'detail_table','rank_spin')
            }
        },
        processNumber
    }

});

</script>