<template>
    <div :style="{ height: db_height, width: db_width }" :id="db_index"></div>
</template>

<style></style>

<script>
import { defineComponent, ref, watch } from 'vue';
import { echartsResize } from '@/utils/echartsResize.js';

import { gaugeOption } from '@/assets/config/gauge-one.js';

import * as echarts from 'echarts/lib/echarts.js';
import 'echarts/lib/chart/gauge';
import 'echarts/lib/component/tooltip'

import { cloneDeep } from 'lodash-es'

export default defineComponent(
    {
        name: 'GaugeOne',
        props: {
            gauge_data: {type:Object},
            color_list: {type:Array},
            db_index: {type:String}
        },
        data() {
            return {
                db_height: '250px'
            }
        },
        setup(props) {
            const db_width = ref('auto')
            const db_data = ref(props.gauge_data);
            const color_style = ref(props.color_list)
            const myChart = ref(null);
            const initChart = function(echart_obj,echart_options,echart_con) {
                echart_obj = echarts.init(document.getElementById(echart_con))
                echart_obj.setOption(echart_options)

                window.addEventListener('resize',function(){echart_obj.resize()}, {passive: true})
                echartsResize(document.getElementById(echart_con),echart_obj)
            };
            watch(props,()=>{
                // db_data.value = props.gauge_data;
                db_data.value = props.gauge_data.map((item,index)=>{
                    const add_sum = props.gauge_data.slice(0, index + 1).reduce((accumulator, currentValue) => accumulator + currentValue.detail_value, 0);
                    return { ...item, add_sum };
                })          
                if (db_data.value.length > 0 && document.getElementById(props.db_index)) {
                    if(myChart.value) {
                        myChart.value.dispose();
                        myChart.value = null;
                    }
                    let gauge_option = {series:[]}
                    for (let i=0;i<db_data.value.length;i++) {
                        let add_option = cloneDeep(gaugeOption);
                        add_option.data = [{
                            name: db_data.value[i].index_name,
                            value: db_data.value[i].add_sum,
                            itemStyle: {color: color_style.value[i]}
                        }]
                        gauge_option.series.push(add_option)
                        if (i==db_data.value.length-1) {
                            add_option.pointer.show = true
                            add_option.detail.show = true
                        }
                    }
                    db_width.value = '250px'
                    initChart(myChart,gauge_option,props.db_index)
                    
                }
            },{ immediate: true })
            return {
                db_data,
                myChart,
                db_width
            }
        }
    }
)

</script>