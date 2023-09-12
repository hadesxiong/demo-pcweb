<template>
        <div class="w_p100 h_p100 bg_white d_flex fd_c">
            <div class="d_flex jc_sb pt_20 pl_20 pr_20 fs_0">
                <div class="d_flex">
                    <a-radio-group v-model:value="choose_line" button-style="solid" class="d_flex gap_12 h_30 lh_30"
                        @change="changeLine">
                        <a-radio-button v-for="item in line_data" :key="item.key" :value="item.key"
                            class="br_100 h_30 lh_30 of_h tover_ell">{{ item.value }}</a-radio-button>
                    </a-radio-group>
                </div>
                <div class="d_flex gap_20">
                    <a-dropdown
                        class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180">
                        <a>{{ choose_class.value }}<icon-park type="Down" class="lh_1" fill="#86909C"></icon-park></a>
                        <template #overlay>
                            <a-menu v-model:value="choose_class">
                                <a-menu-item v-for="item in class_data" :key="item.key"
                                    @click="chooseIndex(item, 'class')">{{ item.value }}</a-menu-item>
                            </a-menu>
                        </template>
                    </a-dropdown>
                    <a-dropdown
                        class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180">
                        <a>{{ choose_group.value }}<icon-park type="Down" class="lh_1" fill="#86909C"></icon-park></a>
                        <template #overlay>
                            <a-menu v-model:value="choose_group">
                                <a-menu-item v-for="item in group_data" :key="item.key"
                                    @click="chooseIndex(item, 'group')">{{ item.value }}</a-menu-item>
                            </a-menu>
                        </template>
                    </a-dropdown>
                    <a-dropdown
                        class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180">
                        <a-date-picker picker="month" :placeholder="'数据日期'" :allowClear="false" v-model:value="date_value">
                            <template #suffixIcon>
                                <icon-park type="CalendarThirty" fill="#86909C" size="14"></icon-park>
                            </template>
                        </a-date-picker>
                    </a-dropdown>
                </div>
            </div>
            <div class="mt_20 ml_20 mr_20 fg_1 ofy_a ofx_h">
                <rank-main v-if="rank_list" :rank_list="rank_list"></rank-main>
            </div>
        </div>
</template>

<style>
@import url('../../assets/style/common.css');
@import url('../../assets/style/colorset.css');
@import url('../../assets/style/overwrite.css');

/* 覆盖部分 */

/* radio部分 */
.ant-radio-group-solid .ant-radio-button-wrapper-checked:not(.ant-radio-button-wrapper-disabled):hover {
    color: #165dff;
    background-color: #f2f3f5;
}

.ant-radio-button-wrapper:last-child {
    border-start-end-radius: 100px;
    border-end-end-radius: 100px;
}

.ant-radio-button-wrapper:first-child {
    border-inline-start: 0;
    border-start-start-radius: 100px;
    border-end-start-radius: 100px;
}

.ant-radio-button-wrapper {
    border: none;
}

.ant-radio-button-wrapper:not(:first-child)::before {
    width: 0;
    inset-block-start: 0;
    inset-block-end: 0;
    padding-block: 0;
    background-color: transparent;
}

.ant-radio-button-wrapper:not(:first-child)::before {
    color: #165dff;
    background-color: #f2f3f5;
    border-color: transparent;
}

.ant-radio-group-solid .ant-radio-button-wrapper-checked:not(.ant-radio-button-wrapper-disabled) {
    background-color: #f2f3f5;
    color: #165dff;
    border-color: transparent;
    font-weight: 500;
}

.ant-picker-input input {
    text-align: left;
}

/* 表格覆写部分 */

.ant-table-wrapper .ant-table {
    font-size: 13px;
}

/* 下拉按钮部分 */
.ant-picker {
    background-color: var(--color-fill-2);
    border: none;
    border-radius: 2px;
}

.ant-picker-focused {
    box-shadow: none;
}

.ant-collapse .ant-collapse-content>.ant-collapse-content-box {
    padding-left: 0;
    padding-right: 0;
}

.ant-collapse-borderless>.ant-collapse-item>.ant-collapse-content>.ant-collapse-content-box {
    padding-top: 20px;
}

.ant-collapse-borderless {
    background-color: transparent;
}

.ant-collapse-borderless>.ant-collapse-item .ant-collapse-header {
    background-color: #f2f3f5;
}
</style>

<script>
import { defineComponent, ref } from 'vue';
import { IconPark } from "@icon-park/vue-next/es/all";
import RankMain from '@/components/rank/rank-main';
import axios from 'axios';

import dayjs from 'dayjs';
import 'dayjs/locale/zh-cn';
import locale from 'ant-design-vue/es/date-picker/locale/zh_CN';

dayjs.locale('zh-cn');

export default defineComponent({
    name: 'rank-important',
    components: {
        'rank-main': RankMain,
        'icon-park': IconPark,
    },
    data() {
        return {
            rank_list: [],
            line_data: [
                { key: "all", value: "全部指标" },
                { key: "enterprise", value: "企金指标" },
                { key: "retail", value: "零售指标" },
                { key: "bank", value: "同业指标" },
                { key: "other", value: "其他指标" },
            ],
            class_data: [
                { key: "all", value: "全部分类" },
                { key: "cwxy", value: "财务效益" },
                { key: "khjs", value: "客户建设" },
                { key: "zxfz", value: "转型与发展质量" },
                { key: "fxhg", value: "风险合规" },
                { key: "shzr", value: "社会责任" }
            ],
            group_data: [
                { key: "qyzxzh", value: "按区域中心支行查看" },
                { key: "ddzh", value: "按单点支行查看" },
                { key: "zlkhb", value: "按战略客户部查看" },
                { key: "fzjg", value: "按4级分支机构查看" }
            ]
        }
    },
    setup() {
        return {
            locale,
            choose_line: ref('all'),
            choose_class: ref({ key: "all", value: "全部分类" }),
            choose_group: ref({ key: "qyzxzh", value: "按区域中心支行查看" }),
            date_value: ref(dayjs())
        }
    },
    mounted() {
        this.getRankData();
    },
    methods: {
        async getRankData() {
            const rank_res = await axios.get('/demo/rank/rank-important.json');
            // console.log(rank_res);
            this.rank_list = rank_res.data;
            // console.log(this.rank_list)
        },
        chooseIndex(item, section) {
            console.log(item, section);
            if (section == 'class') {
                this.choose_class = item;
            } else if (section == 'group') {
                this.choose_group = item;
            }
        },
        changeLine(e) {
            console.log(e.target.value);
            this.choose_line = e.target.value
        }
    }
});

</script>