<template>
    <div class="d_flex fd_c gap_10 bg_l1 minw_250 fai_fs p_16 fg_1" :id="db_data.index_num">
        <div class="fc_l2 font_14">{{ db_data.index_name }}</div>
        <div class="d_flex w_p100 gap_8 fai_b">
            <div class="d_ib va_bl">
                <span class="font_18 fw_700">{{ db_data.detail_value }}</span>
                <span class="font_12 fc_l4 ml_4">/</span>
                <span class="font_12 fc_l4 ml_4 fw_700">200</span>
            </div>
            <div class="w_a fg_1 po_r">
                <div :class="['po_a', 'h_12', 'fill_' + color_style]" :style="{width: db_data.rate}"></div>
                <div class="bg_l3 h_12 fg_1"></div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.fill_blue {
    border-radius: 0px 4px 4px 0px;
    background: linear-gradient(270deg, rgba(27, 85, 255, 0.50) 0%, #2563EB 100%);
}
.fill_red {
    border-radius: 0px 4px 4px 0px;
    background: linear-gradient(270deg, rgba(255, 110, 102, 0.50) 0%, #FF6E66 100%);
}
.fill_pink {
    border-radius: 0px 4px 4px 0px;
    background: linear-gradient(270deg, rgba(195, 76, 217, 0.52) 0%, #C34CD9 100%);
}
.fill_yellow {
    border-radius: 0px 4px 4px 0px;
    background: linear-gradient(270deg, rgba(247, 186, 30, 0.50) 0%, #F7BA1E 100%);
}
.fill_green {
    border-radius: 0px 4px 4px 0px;
    background: linear-gradient(270deg, rgba(30, 247, 52, 0.50) 0%, #1EF734 100%);
}
</style>

<script>
import {defineComponent, ref } from 'vue';

export default defineComponent(
    {
        name:'StepOne',
        props: {
            step_data: {type: Object},
            color: {type:String,default:'blue'}
        },
        setup(props) {
            const db_data = ref(props.step_data)
            // const db_data = origin_data.value.map(obj=>{return {...obj,ratio:obj.detail_value/200}})
            db_data.value.rate = (db_data.value.detail_value/200 *100).toFixed(0).toString()+'%'
            const color_style = ref(props.color)
            return {
                db_data,
                color_style
            }
        }
    }
)
</script>