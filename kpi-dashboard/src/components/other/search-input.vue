<template>
    <div class="d_flex fai_c gap_16 w_p100">
        <span class="fc_l2" v-if="need_label">{{ label_name }}</span>
        <a-dropdown class="d_flex jc_sb fai_c bg_l2 br_2 ta_l h_30 lh_30 fc_l1 of_h tover_ell ws_no minw_100">
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

.select_wrapper div.ant-select-selector {
    /* padding-left: 8px; */
    /* align-items: center; */
    font-size: 13px;
}
.ant-select-single .ant-select-selector .ant-select-selection-search {
    display: flex;
    align-items: center;
}
</style>

<script>
import { defineComponent, ref, reactive } from 'vue';
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
        target_title: {type:String},
        label_info: {
            type:Object,
            default: () => {return reactive({'need_label':false,'label_name':''})}
        }
    },
    setup(props) {
        return {
            in_fetching: ref(false),
            need_label: ref(props.label_info.need_label),
            label_name: ref(props.label_info.label_name),
            url: ref(props.api_info.url),
            params: ref(props.api_info.params),
            res_label: ref(props.res_map.label),
            res_key: ref(props.res_map.key),
            res_value: ref(props.res_map.value),
            search_option: ref([]),
            search_result: ref({}),
            data_title: ref(props.target_title)
        }
    },
    methods: {
        debounceSearch: debounce(function(value) {
            this.in_fetching = true;
            if (value.length>=2) {
                this.params.ext = value
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
                    console.log(option[this.res_value]); 
                    return option.value ===this.search_result[this.res_value]
            });
            this.$emit('search-select',{title:this.data_title,data:emit_result});
            this.search_option = [];
        }
    }
})
</script>