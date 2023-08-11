<template>
    <div class="d_flex w_p100 fd_c bg_white p_20 gap_20">
        <div class="d_flex fd_r lh_30 gap_20 h_30">
            <div class="fc_l3 filter_title ta_l">查看方式</div>
            <div class="d_flex">
                <a-radio-group v-model:value="default_org" button-style="solid" class="d_flex gap_12 h_30">
                    <a-radio-button class="br_100 of_h tover_ell" v-for="(item,index) in filter_data.org_filter" :key="index" :value="item.value">{{ item.label }}</a-radio-button>
                </a-radio-group>
            </div>
        </div>
        <div class="d_flex fd_r lh_30 gap_20">
            <div class="fc_l3 filter_title ta_l">指标分类</div>
            <div class="d_flex">
                <custom-multi v-if="filter_data.enterprise_filter.index_class" :custom_options="filter_data.enterprise_filter.index_class"></custom-multi>
            </div>
        </div>
    </div>
</template>

<style scoped>
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
  height: 30px;
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
.filter_title {
    width: 80px;
}

</style>

<script>
import { defineComponent, ref } from 'vue';
import CustomMulti from './custom-multi.vue';

export default defineComponent({
    name:"TableFilter",
    components:{
        'custom-multi':CustomMulti
    },
    props:{
        filter_data:{
            type:Array
        },

    },
    data() {
        return {}
    },
    setup() {
        const default_org = ref('qyzxzh');
        return {
            default_org,
        }
    },
    mounted() {},
    methods:{
        execLabelList(index_list) {
            console.log(index_list);
        }
    }
});
</script>