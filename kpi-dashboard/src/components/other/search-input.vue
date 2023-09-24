<template>
    <div class="d_flex fai_c gap_16">
        <span class="fc_l2" v-if="need_label">{{ label_name }}</span>
        <a-dropdown class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l1 of_h tover_ell ws_no minw_100">
            <a-select class="d_flex w_p100 fai_c select_wrapper" 
                :show-arrow="false" show-search 
                @search="debounceSearch" 
                @change="emitSelectValue"
                v-model:value="search_result[res_value]" 
                :options="search_option">
                <template #notFoundContent v-if="in_fetching">
                    <a-spin size="small"></a-spin>
                </template>
            </a-select>
        </a-dropdown>
    </div>
</template>

<style>
@import url('@/assets/style/common.css');
</style>

<style scoped>
.select_wrapper div.ant-select-selector {
    padding-left: 8px;
    align-items: center;
}
</style>

<script>
import { defineComponent, ref, reactive, toRefs } from 'vue';
import { Dropdown, Select, Spin } from 'ant-design-vue';
import { debounce } from 'lodash-es';

import { api } from '@/utils/commonApi.js';

const myApi = api();

export default defineComponent({
    name: 'SearchInput',
    components: {
        'a-dropdown': Dropdown,
        'a-select': Select,
        'a-spin': Spin
    },
    props:{
        res_map: {type:Object},
        api_info: {type:Object},
        label_info: {
            type:Object,
            default: () => {return reactive({'need_label':false,'label_name':''})}
        }
    },
    setup(props) {
        const { need_label, label_name } = toRefs(props.label_info)
        const { key,value,label } = toRefs(props.res_map)
        const { url, params } = toRefs(props.api_info)
        return {
            in_fetching: ref(false),
            need_label: need_label.value,
            label_name: label_name.value,
            url: url.value,
            params: params.value,
            res_label: label.value,
            res_key: key.value,
            res_value: value.value,
            search_option: ref([]),
            search_result: ref({})
        }
    },
    methods: {
        debounceSearch: debounce(function(value) {
            this.in_fetching = true;
            if (value.length>=2) {
                myApi.get(this.url,{params:this.params}).then((response) => {
                    if (response.data.code == 200) {
                        this.search_option = response.data.data.map(obj=>({
                            label: obj[this.res_label],
                            key: obj[this.res_key],
                            value:obj[this.res_value]
                        }))
                    }
                    this.in_fetching = false;
                })
            }
        },750),
        emitSelectValue() {
            const emit_result = this.search_option.find(
                (option) => {
                    // console.log(option[this.res_value]); 
                    return option.value ===this.search_result[this.res_value]
            });
            this.$emit('search-select',{title:'title',data:emit_result});
            this.search_option = [];
        }
    }
})
</script>