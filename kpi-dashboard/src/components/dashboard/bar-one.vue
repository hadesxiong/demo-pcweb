<template>
    <div class="bg_white d_flex p_20 fd_c gap_20 br_4 w_p100 h_p100">
        <div class="d_flex jc_sb">
            <div class="d_flex gap_20 fai_c jc_fs">
                <div class="d_iflex font_16 fw_500 fc_l1 lh_20 ">{{ bar_conf[db_index]['bar_title'] }}</div>
                <div class="d_iflex br_4" :class="bar_conf[db_index]['tag_class']">{{ bar_conf[db_index]['tag_name'] }}</div>
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
                                <a-sub-menu v-if="item.children" :key="item.org_key" :title="item.org_name">
                                    <a-menu-item v-for="sub_item in item.children" :key="sub_item.org_key" @click="chooseOrg(sub_item)">
                                        {{ sub_item.org_name }}
                                    </a-menu-item>
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
        <div class="d_flex jc_c fai_c w_p100 h_p100">
            <div class="d_flex jc_sb fai_c w_p100 h_p100">
                <a-skeleton v-if="!db_data.data" :active="true" :paragraph="{ rows: 6, width:'100%' }"></a-skeleton>
                <div :style="{ height: db_height, width: db_width }">
                    <a-spin :spinning="loading_status" :delay="100" tip="数据加载中...">
                        <div :style="{ height: db_height, width: db_width }" :id="db_index"></div>
                    </a-spin>
                </div>
            </div>
        </div>
        <!-- 如果有示例 -->
        <div class="d_flex jc_c fai_c gap_32 h_20 lh_20">
            <div class="d_flex fai_c gap_10" v-for="(item,index) in bar_options['series']" :key="index">
                <div class="dot" :class="`eg_${index + 1}`"></div>
                <div class="fc_l3">{{ item.name }}</div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.dot {
    width: 10px;
    height: 10px;
    border-radius: 10px;
}

.eg_1 {
    background-color: #246eff;
}

.eg_2 {
    background-color: #00B2FF;
}

.eg_3 {
    background-color: #81E2FF;
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
import { defineComponent, ref, watch } from "vue";
import { Down, } from '@icon-park/vue-next';
import { Dropdown, Menu, SubMenu, MenuItem, DatePicker, Spin, Skeleton } from 'ant-design-vue';

import { vBarConfMap, vBarConfOptions } from "@/assets/config/dashboard-main.js";

import { echartsResize } from '@/utils/echartsResize.js';
import { iterateMonths} from '@/utils/iterateMonths.js';

import * as echarts from 'echarts/lib/echarts.js';
import 'echarts/lib/chart/bar';
import 'echarts/lib/component/tooltip';
import 'echarts/lib/component/grid';

import dayjs from 'dayjs';
import 'dayjs/locale/zh-cn';
import locale from 'ant-design-vue/es/date-picker/locale/zh_CN';

import { cloneDeep } from "lodash-es";

dayjs.locale('zh-cn');

export default defineComponent(
    {
        name: "BarOne",
        components: {
            'icon-down': Down,
            'a-dropdown': Dropdown,
            'a-menu': Menu,
            'a-sub-menu': SubMenu,
            'a-menu-item': MenuItem,
            'a-date-picker': DatePicker,
            'a-spin': Spin,
            'a-skeleton': Skeleton
        },
        props: {
            bar_data: { type: Object },
            org_filter: { type: Object },
            db_index: {type: String}
        },
        data() {
            return {
                db_height: '250px',
            };
        },
        setup(props) {
            const db_width = ref('0%');
            const loading_status = ref(false);
            const choose_org = ref({
                org_num: localStorage.getItem('org_num'),
                org_name: localStorage.getItem('org_name')
            });
            const db_data = ref(props.bar_data);
            const bar_options = ref(cloneDeep(vBarConfOptions));
            const bar_conf = ref(vBarConfMap);
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

                echart_options.series[0]['data'] = db_data.value['data'][bar_conf.value[props.db_index]['map_list'][0]]
                echart_options.series[1]['data'] = db_data.value['data'][bar_conf.value[props.db_index]['map_list'][1]]
                echart_options.series[2]['data'] = db_data.value['data'][bar_conf.value[props.db_index]['map_list'][2]]

                echart_obj = echarts.init(document.getElementById(echart_con))
                echart_obj.setOption(echart_options)

                window.addEventListener('resize',function(){echart_obj.resize()}, {passive: true})
                echartsResize(document.getElementById(echart_con),echart_obj)
            }

            watch(props,()=>{
                db_data.value = props.bar_data

                loading_status.value = true
                if(db_data.value['data'] && document.getElementById(props.db_index)) {
                    if(myChart.value) {
                        myChart.value.dispose()
                        myChart.value = null;
                    }
                    db_width.value = '100%'
                    initChart(myChart,bar_options.value,props.db_index)
                }

                loading_status.value = false
            },{ immediate: true })

            return {
                locale,
                loading_status,
                db_data,
                bar_conf,
                date_value: ref(dayjs().add(-1, 'month').endOf('month')),
                selectedKeys: ref([]),
                choose_org,
                bar_options,
                myChart,
                search_form,
                db_width
            }
        },
        mounted() {},
        methods: {
            handlePickerClose(status) {
                if (!status) {
                    console.log(this.date_value)
                    this.search_form.date = [
                        this.date_value.add(-5,'month').startOf('month').format('YYYY-MM-DD'),
                        this.date_value.add(0,'month').endOf('month').format('YYYY-MM-DD')
                    ]
                    this.loading_status = true;
                    this.$emit('getDBFilters',this.search_form)
                }
            },
            chooseOrg(item) {
                this.selectedKeys.push(item);
                this.choose_org = item;
                this.search_form.org = item.org_num;
                this.loading_status = true;
                this.$emit('getDBFilters',this.search_form)
            },
            disabledDate(current) {
                return current && current > dayjs().add(-1, 'month').endOf('month')
            }
        }
    }
) 
</script>