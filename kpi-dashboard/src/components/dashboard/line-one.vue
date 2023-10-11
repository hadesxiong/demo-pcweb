<template>
    <div class="bg_white d_flex p_20 fd_c gap_20 br_4 w_p100 h_p100">
        <div class="d_flex jc_sb">
            <div class="d_flex gap_20 fai_c jc_fs">
                <div class="d_iflex font_16 fw_500 fc_l1 lh_20">{{ line_conf[db_index]['line_title'] }}</div>
                <div class="d_iflex br_4" :class="line_conf[db_index]['tag_class']"> {{ line_conf[db_index]['tag_name'] }} </div>
            </div>
            <div class="d_flex fai_c jc_fe gap_16">
                <a-dropdown>
                    <a class="d_flex fai_c gap_8 fc_brand6">
                        {{ choose_org.org_name }}
                        <icon-down size="14" class="d_flex fai_c" fill="#165fdd"></icon-down>
                    </a>
                    <template #overlay>
                        <a-menu>
                            <div v-for="(item, index) in org_filter" :key="index">
                                <a-sub-menu v-if="item.children" :key="item.org_num" :title="item.org_name">
                                    <a-menu-item v-for="sub_item in item.children" :key="sub_item.org_num"
                                        @click="chooseOrg(sub_item)">{{
                                            sub_item.org_name }}</a-menu-item>
                                </a-sub-menu>
                                <a-menu-item v-else @click="chooseOrg(item)">{{ item.org_name }}</a-menu-item>
                            </div>
                        </a-menu>
                    </template>
                </a-dropdown>
                <a-date-picker picker="month" :bordered="false" class="custom_dp" :allowClear="false"
                    v-model:value="date_value" @openChange="handlePickerClose" :locale="locale" :disabled-date="disabledDate">
                    <template #suffixIcon>
                        <icon-down size="14" class="d_flex fai_c" fill="#165fdd"></icon-down>
                    </template>
                </a-date-picker>
            </div>
        </div>
        <div class="d_flex jc_sb">
            <a-radio-group v-model:value="chosen_value" button-style="solid">
                <a-radio-button v-for="item in line_conf['change_map']" :key="item.key" :value="item.key">
                    {{ item.value }}
                </a-radio-button>
            </a-radio-group>
            <div class="d_iflex fai_c lh_20 fc_l3 gap_16 lh_32">
                <div class="d_iflex gap_12 fai_c" v-for="(item,index) in line_conf['series_name']" :key="index">
                    <div class="dot" :class="`eg_${index + 1}`"></div>
                    {{ item }}
                </div>
            </div>
        </div>
        <div class="d_flex jc_c fai_c w_p100 h_p100">
            <div class="d_flex jc_sb fai_c  w_p100 h_p100">
                <div :style="{ height: db_height, width: db_width }" :id="db_index"></div>
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
.dot {
    width: 10px;
    height: 10px;
    border-radius: 10px;
}
.eg_1 {
    background-color: #165DFF;
    border: 2px solid #BEDAFF;
}
.eg_2 {
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
import { defineComponent, ref, watch } from 'vue';
import { Down } from '@icon-park/vue-next';
import { Dropdown, Menu, SubMenu, MenuItem, DatePicker, RadioGroup, RadioButton } from 'ant-design-vue';
import { echartsResize } from '@/utils/echartsResize.js';
import { iterateMonths } from '@/utils/iterateMonths.js';

import { changeLineConfMap, changeLineConfOptions } from '@/assets/config/dashboard-main.js';

import { cloneDeep } from 'lodash-es';

import * as echarts from 'echarts/lib/echarts.js';
import 'echarts/lib/component/tooltip';
import 'echarts/lib/component/grid';
import 'echarts/lib/chart/line';

import dayjs from 'dayjs';
import 'dayjs/locale/zh-cn';
import locale from 'ant-design-vue/es/date-picker/locale/zh_CN';

dayjs.locale('zh-cn');

export default defineComponent({
    name: "LineOne",
    components: {
        'icon-down': Down,
        'a-dropdown': Dropdown,
        'a-menu': Menu,
        'a-sub-menu': SubMenu,
        'a-menu-item': MenuItem,
        'a-date-picker': DatePicker,
        'a-radio-group': RadioGroup,
        'a-radio-button': RadioButton
    },
    props: {
        id: {
            type: String,
            default: "db_line"
        },
        org_filter: { type: Object },
        line_data: {type: Object},
        db_index: {type:String}
    },
    data() {
        return {
            db_height: "100%"
        };
    },
    setup(props) {
        const chosen_value = ref('enterprise');
        const db_width = ref('0%');
        const loading_status = ref(false);
        const choose_org = ref({
            org_num: localStorage.getItem('org_num'),
            org_name: localStorage.getItem('org_name')
        });
        const db_data = ref(props.line_data);
        const line_options = ref(cloneDeep(changeLineConfOptions));
        const line_conf = ref(changeLineConfMap);
        const myChart = ref(null);
        const search_form = ref({
            mark: ref(props.db_index),
            date: ref([
            dayjs().add(-6,'month').startOf('month').format('YYYY-MM-DD'),
                    dayjs().add(-1,'month').endOf('month').format('YYYY-MM-DD')
            ]),
            org: ref(localStorage.getItem('org_num'))
        })

        const initChart = function(echart_obj,echart_options,echart_con) {
            echart_options.xAxis.data = [];
            iterateMonths(
                search_form.value.date[0],
                search_form.value.date[1],
                (date)=>{
                    echart_options.xAxis.data.push(date.format('YYYY-MM'))
            });

            echart_options.series[0]['name'] = line_conf.value[props.db_index]['series_name'][0]
            echart_options.series[1]['name'] = line_conf.value[props.db_index]['series_name'][1]

            echart_options.series[0]['data'] = db_data.value['data'][line_conf.value[props.db_index]['map_list'][chosen_value.value][0]]
            echart_options.series[1]['data'] = db_data.value['data'][line_conf.value[props.db_index]['map_list'][chosen_value.value][1]]

            echart_options.series[0]['areaStyle']['color'] = new echarts.graphic.LinearGradient(0.5, 0, 0.5, 1, [
                { offset: 0, color: "rgba(100, 162, 255, 0.12)" },
                { offset: 1, color: 'rgba(52, 105, 255, 0.01)' }
            ]);

            echart_options.series[1]['areaStyle']['color'] = new echarts.graphic.LinearGradient(0.5, 0, 0.5, 1, [
                { offset: 0, color: 'rgba(131, 100, 255, 0.12)' },
                { offset: 1, color: 'rgba(80, 52, 255, 0.01)' }
            ]);
            echart_options.xAxis.axisLabel.formatter = function(value,index) {
                if (index === 0) {
                    return '{start|' + value + '}';
                } else if (index == echart_options.xAxis.data.length - 1) {
                    return '{end|' + value + '}';
                } else {
                    return value;
                }
            }

            echart_obj = echarts.init(document.getElementById(echart_con))
            echart_obj.setOption(echart_options)

            window.addEventListener('resize',function(){echart_obj.resize()}, {passive: true})
            echartsResize(document.getElementById(echart_con),echart_obj)
        }

        watch(props,()=>{
            db_data.value = props.line_data;

            loading_status.value = true;
            if (db_data.value['data'] && document.getElementById(props.db_index)) {
                if (myChart.value) {
                    myChart.value.dispose();
                    myChart.value = null;
                }
                db_width.value = '100%';
                initChart(myChart,line_options.value,props.db_index)
            }

            loading_status.value = false
        },{immediate:true})

        return {
            chosen_value,
            locale,
            loading_status,
            db_data,
            line_conf,
            date_value: ref(dayjs().add(-1, 'month').endOf('month')),
            selectedKeys: ref([]),
            choose_org,
            line_options,
            myChart,
            search_form,
            db_width
        }
    },
    mounted() {
        // this.drawLine();
    },
    methods: {
        // drawLine() {
        //     let myChart = echarts.init(document.getElementById(this.id));
        //     let myChart_option = this.db_data.db_option;
        //     // console.log(myChart_option);
        //     myChart_option.series[0].areaStyle.color = new echarts.graphic.LinearGradient(0.5, 0, 0.5, 1, [
        //         { offset: 0, color: "rgba(100, 162, 255, 0.12)" },
        //         { offset: 1, color: 'rgba(52, 105, 255, 0.01)' }
        //     ]);
        //     myChart_option.series[1].areaStyle.color = new echarts.graphic.LinearGradient(0.5, 0, 0.5, 1, [
        //         { offset: 0, color: 'rgba(131, 100, 255, 0.12)' },
        //         { offset: 1, color: 'rgba(80, 52, 255, 0.01)' }
        //     ]);
        //     myChart_option.xAxis.axisLabel.formatter = function (value, index) {
        //         if (index === 0) {
        //             return '{start|' + value + '}';
        //         } else if (index == myChart_option.xAxis.data.length - 1) {
        //             return '{end|' + value + '}';
        //         } else {
        //             return value;
        //         }
        //     }
        //     myChart.setOption(myChart_option);
        //     // 添加自适应
        //     window.addEventListener('resize', function () {
        //         myChart.resize();
        //     }, { passive: true });
        //     echartsResize(document.getElementById(this.id), myChart);
        // },
        handlePickerClose(status) {
            if (!status) {
                console.log(this.date_value)
            }
        },
        chooseOrg(item) {
            this.selectedKeys.push(item.org_key);
            this.choose_org = item;
        },
        disabledDate(current) {
            return current && current > dayjs().add(-1, 'month').endOf('month')
        }
    }
});

</script>