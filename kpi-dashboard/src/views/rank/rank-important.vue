<template>
        <div class="w_p100 h_p100 bg_white d_flex fd_c">
            <div class="d_flex jc_sb pt_20 pl_20 pr_20 fs_0">
                <div class="d_flex">
                    <a-radio-group v-model:value="active_line" button-style="solid" class="d_flex gap_12 h_30 lh_30"
                        @change="changeLine">
                        <a-radio-button v-for="item in line_data" :key="item.key" :value="item.key"
                            class="br_100 h_30 lh_30 of_h tover_ell">{{ item.value }}</a-radio-button>
                    </a-radio-group>
                </div>
                <div class="d_flex gap_20">
                    <a-dropdown
                        class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180">
                        <a>
                            {{ search_form.class.value }}
                            <icon-down class="lh_1" fill="#86909C"></icon-down>
                        </a>
                        <template #overlay>
                            <a-menu v-model:value="search_form.class">
                                <a-menu-item v-for="item in class_data" :key="item.key"
                                    @click="chooseIndex(item, 'class')">{{ item.value }}</a-menu-item>
                            </a-menu>
                        </template>
                    </a-dropdown>
                    <a-dropdown
                        class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180">
                        <a>
                            {{ search_form.group.value }}
                            <icon-down class="lh_1" fill="#86909C"></icon-down>
                        </a>
                        <template #overlay>
                            <a-menu v-model:value="search_form.group">
                                <a-menu-item v-for="item in group_data" :key="item.key"
                                    @click="chooseIndex(item, 'group')">{{ item.value }}</a-menu-item>
                            </a-menu>
                        </template>
                    </a-dropdown>
                    <a-dropdown
                        class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180">
                        <a-date-picker picker="month" :placeholder="'数据日期'" :allowClear="false" v-model:value="search_form.date" @change="changeDate">
                            <template #suffixIcon>
                                <icon-calendar fill="#86909C" size="14"></icon-calendar>
                            </template>
                        </a-date-picker>
                    </a-dropdown>
                </div>
            </div>
            <div class="d_flex fd_c h_p100 w_p100 jc_c" v-if="spin_status">
                <a-spin :spinning="spin_status" size="large" :delay="100" tip="数据加载中">
                </a-spin>
            </div>
            <div class="m_20 fg_1 ofy_a ofx_h" v-if="!spin_status">
                <rank-main v-if="rank_data" 
                :rank_data="rank_data" 
                :show_pannel="show_pannel"
                :active_pannel="active_pannel"
                :detail_params="detail_params"></rank-main>
            </div>
        </div>
</template>

<style>
@import url('@/assets/style/common.css');
@import url('@/assets/style/colorset.css');
@import url('@/assets/style/overwrite.css');

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
import { Down, CalendarThirty } from '@icon-park/vue-next';
import { RadioGroup, RadioButton, Dropdown, Menu, MenuItem, DatePicker, Spin } from 'ant-design-vue';

import RankMain from '@/components/rank/rank-main';
// import axios from 'axios';

import { api } from '@/utils/commonApi.js';
import { lineMap, classMap, groupMap, tagMap } from '@/assets/config/rank-important.js';

import { cloneDeep } from 'lodash-es';
import dayjs from 'dayjs';
import 'dayjs/locale/zh-cn';
// import locale from 'ant-design-vue/es/date-picker/locale/zh_CN';

const myApi = api();

export default defineComponent({
    name: 'rank-important',
    components: {
        'icon-down': Down,
        'icon-calendar': CalendarThirty,
        'a-radio-group': RadioGroup,
        'a-radio-button': RadioButton,
        'a-dropdown': Dropdown,
        'a-menu': Menu,
        'a-menu-item': MenuItem,
        'a-date-picker': DatePicker,
        'a-spin': Spin,
        'rank-main': RankMain,
    },
    data() {
        return {
            line_data: ref(lineMap),
            class_data: ref(classMap),
            group_data: ref(groupMap),
            tag_data: ref(tagMap)
        }
    },
    setup() {
        return {
            // locale,
            spin_status: ref(false),
            show_pannel: ref(false),
            active_pannel: ref('1'),
            raw_data: ref({
                column: ref([]),
                data: ref([]),
                title: ref([])
            }),
            rank_data: ref({
                column: ref([]),
                data: ref([]),
                title: ref([])
            }),
            search_form: ref({
                class: ref({key:0,value:'全部分类'}),
                group: ref({key:1,value:'按区域中心支行查看'}),
                date: ref(dayjs().endOf('month'))
            }),
            detail_params: ref({
                group: ref(),
                date: ref()
            }),
            active_line: ref(0)
        }
    },
    mounted() {
        this.getRankData();
    },
    methods: {
        async getRankData() {
            this.spin_status = true;
            const get_params = {
                class: this.search_form.class.key,
                group: this.search_form.group.key,
                date: this.search_form.date.format('YYYY-MM-DD'),
                page: 1
            }
            const rank_res = await myApi.get('/api/rank/getRank',{params:get_params})
            this.raw_data.column = rank_res.data.column
            this.raw_data.data = Object.values(rank_res.data.data)
            this.raw_data.title = Object.keys(rank_res.data.data).map(
                (item)=>{
                    return {
                        title:lineMap[Number(item)].value,
                        key:Number(item),
                        count: rank_res.data.data[Number(item)].length 
                    }})
            // 调用过滤方法进行展示
            this.mapLineData();
            // 根据active情况过滤
            this.spin_status = false;
            // 补充设置detail_params
            this.detail_params.group = cloneDeep(this.search_form.group)
            this.detail_params.date = cloneDeep(this.search_form.date.format('YYYY-MM-DD'))
        },
        chooseIndex(item, section) {
            // console.log(item, section);
            if (section == 'class') {
                this.search_form.class = item;
            } else if (section == 'group') {
                this.search_form.group = item;
            }
            console.log(this.search_form)
            this.getRankData()
        },
        changeLine(e) {
            this.active_line = e.target.value;
            // console.log(this.active_line);
            this.mapLineData();
        },
        mapLineData() {
            if (this.active_line == 0) {
                this.rank_data = cloneDeep(this.raw_data)
                // this.active_pannel = '1'
            } else {
                this.rank_data.column = cloneDeep(this.raw_data.column);
                this.rank_data.title = cloneDeep(this.raw_data.title.filter(item=>item.key === this.active_line))
                const target_index = this.raw_data.title.map(item=>item.key).indexOf(this.active_line)
                this.rank_data.data = [cloneDeep(this.raw_data.data[target_index])]
                this.active_pannel = String(this.active_line)
            }
        },
        changeDate(date) {
            this.search_form.date = date;
            this.getRankData();
        }
    }
});

</script>