<template>
    <div class="w_p100 h_p100 bg_white">
        <div class="d_flex jc_sb pt_20 pl_20 pr_20">
            <div class="d_flex">
                <a-radio-group v-model:value="default_line" button-style="solid" class="d_flex gap_12 h_30 lh_30">
                    <a-radio-button value="all" class="br_100 h_30 lh_30 of_h tover_ell">全部</a-radio-button>
                    <a-radio-button value="enterprise" class="br_100 h_30 lh_30 of_h tover_ell">企金指标</a-radio-button>
                    <a-radio-button value="retail" class="br_100 h_30 lh_30 of_h tover_ell">零售指标</a-radio-button>
                    <a-radio-button value="bank" class="br_100 h_30 lh_30 of_h tover_ell">同业指标</a-radio-button>
                    <a-radio-button value="other" class="br_100 h_30 lh_30 of_h tover_ell">其他指标</a-radio-button>
                </a-radio-group>
            </div>
            <div class="d_flex gap_20">
                <a-dropdown class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180" @click="handleClass">
                    <a>全部分类<icon-park type="Down" class="lh_1" fill="#86909C"></icon-park></a>
                    <template #overlay>
                        <a-menu>
                            <a-menu-item>全部分类</a-menu-item>
                            <a-menu-item>财务效益</a-menu-item>
                            <a-menu-item>客户建设</a-menu-item>
                            <a-menu-item>转型与质量发展</a-menu-item>
                            <a-menu-item>风险合规</a-menu-item>
                            <a-menu-item>社会责任</a-menu-item>
                        </a-menu>
                    </template>
                </a-dropdown>
                <a-dropdown class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180" @click="handleClass">
                    <a>按区域中心支行查看<icon-park type="Down" class="lh_1" fill="#86909C"></icon-park></a>
                    <template #overlay>
                        <a-menu>
                            <a-menu-item>按区域中心支行查看</a-menu-item>
                            <a-menu-item>按分支机构查看</a-menu-item>
                            <a-menu-item>按战略客户部查看</a-menu-item>
                            <a-menu-item>按单点支行查看</a-menu-item>
                        </a-menu>
                    </template>
                </a-dropdown>
                <a-dropdown class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180">
                    <a-date-picker picker="month" :placeholder="'数据日期'" :allowClear="false">
                        <template #suffixIcon>
                            <icon-park type="CalendarThirty" fill="#86909C" size="14"></icon-park>
                        </template>
                    </a-date-picker>
                </a-dropdown>
            </div>
        </div>
        <div class="mt_20 ml_20 mr_20">
            <rank-main v-if="rank_list" :rank_list="rank_list"></rank-main>
        </div>
    </div>
</template>

<style scoped>
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

:where(.css-dev-only-do-not-override-eq3tly).ant-collapse .ant-collapse-content>.ant-collapse-content-box {
    padding-left: 0;
    padding-right: 0;
}
:where(.css-dev-only-do-not-override-eq3tly).ant-collapse-borderless >.ant-collapse-item>.ant-collapse-content>.ant-collapse-content-box {
    padding-top: 20px;
}
:where(.css-dev-only-do-not-override-eq3tly).ant-collapse-borderless {
    background-color: transparent;
}
:where(.css-dev-only-do-not-override-eq3tly).ant-collapse-borderless >.ant-collapse-item .ant-collapse-header {
    background-color: #f2f3f5;
}

</style>

<script>
import { defineComponent, ref } from 'vue';
import { IconPark } from "@icon-park/vue-next/es/all";
import RankMain from '../../components/rank/rank-main';
import axios from 'axios';

export default defineComponent({
    name: 'rank-important',
    components: {
        'rank-main': RankMain,
        'icon-park': IconPark
    },
    data() {
        return {
            rank_list: []
        }
    },
    setup() {
        const default_line = ref('all');
        return {
            default_line
        }
    },
    mounted() {
        this.getRankData();
    },
    methods: {
        async getRankData() {
            const rank_res = await axios.get('http://localhost:8080/demo/rank/rank-important.json');
            // console.log(rank_res);
            this.rank_list = rank_res.data;
            // console.log(this.rank_list)
        },
        handleClass(e) {
            console.log(e)
        }
    }
});

</script>