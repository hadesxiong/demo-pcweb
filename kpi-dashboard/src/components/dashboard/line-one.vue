<template>
    <div class="bg_white d_flex p_20 fd_c gap_20 br_4 w_p100 h_p100">
        <div class="d_flex jc_sb">
            <div class="d_flex gap_20 fai_c jc_fs">
                <div class="d_iflex font_16 fw_500 fc_l1 lh_20">{{ db_data.db_title }}</div>
                <div class="d_iflex br_4" :class="db_data.db_tag.tag_class"> {{ db_data.db_tag.tag_name }} </div>
            </div>
            <div class="d_flex fai_c jc_fe gap_16">
                <a-dropdown>
                    <a class="d_flex fai_c gap_8 fc_brand6">
                        {{ choose_org }}
                        <icon-down size="14" class="d_flex fai_c" fill="#165fdd"></icon-down>
                    </a>
                    <template #overlay>
                        <a-menu>
                            <div v-for="(item, index) in org_filter" :key="index">
                                <a-sub-menu v-if="item.children" :key="item.org_key" :title="item.org_name">
                                    <a-menu-item v-for="sub_item in item.children" :key="sub_item.org_key"
                                        @click="chooseOrg(sub_item)">{{
                                            sub_item.org_name }}</a-menu-item>
                                </a-sub-menu>
                                <a-menu-item v-else @click="chooseOrg(item)">{{ item.org_name }}</a-menu-item>
                            </div>
                        </a-menu>
                    </template>
                </a-dropdown>
                <a-range-picker picker="month" :bordered="false" class="custom_dp" :allowClear="false"
                    v-model:value="date_value">
                    <template #suffixIcon>
                        <icon-down size="14" class="d_flex fai_c" fill="#165fdd"></icon-down>
                    </template>
                    <template #separator>
                        <icon-minus size="14" class="d_flex fai_c" fill="#165fdd"></icon-minus>
                    </template>
                </a-range-picker>
            </div>
        </div>
        <div class="d_flex jc_sb">
            <a-radio-group v-model:value="chosen_value" button-style="solid">
                <a-radio-button value="enterprise">企金</a-radio-button>
                <a-radio-button value="retial">零售</a-radio-button>
            </a-radio-group>
            <div class="d_iflex fai_c lh_20 fc_l3 gap_16 lh_32">
                <div class="d_iflex gap_12 fai_c">
                    <div class="blue_dot"></div>
                    一般性存款
                </div>
                <div class="d_iflex gap_12 fai_c">
                    <div class="purple_dot"></div>
                    低成本存款
                </div>
            </div>
        </div>
        <div class="d_flex jc_c fai_c w_p100 h_p100">
            <div class="d_flex jc_sb fai_c  w_p100 h_p100">
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
    border-start-start-radius: 0px;
    border-end-start-radius: 0px;
}

.ant-radio-button-wrapper:last-child {
    border-start-end-radius: 0px;
    border-end-end-radius: 0px;
}

.ant-radio-button-wrapper:not(:first-child)::before {
    width: 0px;
}

.ant-radio-button-wrapper-checked {
    border-start-start-radius: 2px !important;
    border-end-start-radius: 2px !important;
    background-color: #fff !important;
    color: #165dff !important;
    border: 1px solid #f2f3f5 !important;
    font-weight: 700;
}

.blue_dot {
    width: 10px;
    height: 10px;
    border-radius: 10px;
    background-color: #165DFF;
    border: 2px solid #BEDAFF;
}

.purple_dot {
    width: 10px;
    height: 10px;
    border-radius: 10px;
    background-color: #722ED1;
    border: 2px solid #F5E8FF;
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
import { defineComponent, ref } from 'vue';
import { Down, Minus } from '@icon-park/vue-next';
import { Dropdown, Menu, SubMenu, MenuItem, RangePicker, RadioGroup, RadioButton } from 'ant-design-vue';
import { echartsResize } from '@/utils/echartsResize.js';

import * as echarts from 'echarts/lib/echarts.js';
import 'echarts/lib/component/tooltip';
import 'echarts/lib/component/grid';
import 'echarts/lib/chart/line';

export default defineComponent({
    name: "LineOne",
    components: {
        'icon-down': Down,
        'icon-minus': Minus,
        'a-dropdown': Dropdown,
        'a-menu': Menu,
        'a-sub-menu': SubMenu,
        'a-menu-item': MenuItem,
        'a-range-picker': RangePicker,
        'a-radio-group': RadioGroup,
        'a-radio-button': RadioButton
    },
    props: {
        id: {
            type: String,
            default: "db_line"
        },
        db_data: {
            type: Object
        },
        org_filter: { type: Object },
        cur_org: { type: String },
        cur_date: { type: Array }
    },
    data() {
        return {
            db_width: "100%",
            db_height: "100%"
        };
    },
    setup(props) {
        const chosen_value = ref('enterprise');
        return {
            chosen_value,
            date_value: ref(props.cur_date),
            selectedKeys: ref([]),
            choose_org: ref(props.cur_org)
        }
    },
    mounted() {
        this.drawLine();
    },
    methods: {
        drawLine() {
            let myChart = echarts.init(document.getElementById(this.id));
            let myChart_option = this.db_data.db_option;
            // console.log(myChart_option);
            myChart_option.series[0].areaStyle.color = new echarts.graphic.LinearGradient(0.5, 0, 0.5, 1, [
                { offset: 0, color: "rgba(100, 162, 255, 0.12)" },
                { offset: 1, color: 'rgba(52, 105, 255, 0.01)' }
            ]);
            myChart_option.series[1].areaStyle.color = new echarts.graphic.LinearGradient(0.5, 0, 0.5, 1, [
                { offset: 0, color: 'rgba(131, 100, 255, 0.12)' },
                { offset: 1, color: 'rgba(80, 52, 255, 0.01)' }
            ]);
            myChart_option.xAxis.axisLabel.formatter = function (value, index) {
                if (index === 0) {
                    return '{start|' + value + '}';
                } else if (index == myChart_option.xAxis.data.length - 1) {
                    return '{end|' + value + '}';
                } else {
                    return value;
                }
            }
            myChart.setOption(myChart_option);
            // 添加自适应
            window.addEventListener('resize', function () {
                myChart.resize();
            });
            echartsResize(document.getElementById(this.id), myChart);
        },
        handlePickerClose(status) {
            if (!status) {
                console.log(this.date_value)
            }
        },
        chooseOrg(item) {
            this.selectedKeys.push(item.org_key);
            this.choose_org = item.org_name;
        }
    }
});

</script>