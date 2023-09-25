<template>
    <div class="ofy_h fg_1" id="table_con">
        <a-spin :spinning="spin_status" size="large" :delay="100" tip="数据加载中">
            <a-table :columns="columns" :data-source="data" :scroll="table_scroll" :pagination="false" class="b_w1c2_so br_4">
                <template #bodyCell="{ column, text, record }">
                    <template v-for="item in editIndex" :key="item.column">
                        <div v-if="item.type==='input' && item.column === column.dataIndex" class="input-container d_flex fai_c font_13 h_20 lh_20 maxw_p100">
                            <a-input v-if="editableData[record.key]" class="input-wrapper maxw_p100 of_h font_13 w_p100"
                                v-model:value="editableData[record.key][column.dataIndex]">
                            </a-input>
                            <template v-else>{{ text }}</template>
                        </div>
                        <div v-else-if="item.type==='select' && item.column === column.dataIndex" class="input-container d_flex fai_c font_13 h_20 lh_20 maxw_p100">
                            <a-select v-model:value="editableData[record.key][column.dataIndex]"
                                v-if="editableData[record.key]" class="select-wrapper d_flex fai_c font_13 h_20 lh_20 maxw_p100 w_p100">
                                <template #suffixIcon>
                                    <icon-down size="16" fill="#86909C" class="d_flex fai_c"></icon-down>
                                </template>
                                <a-select-option
                                    v-for="sub_item in item.option_list.filter((a) => { return a.ref_code != 0 })"
                                    :key="sub_item.ref_code" :value="sub_item.ref_name">{{ sub_item.ref_name }}</a-select-option>
                            </a-select>
                            <template v-else>{{ text }}</template>
                        </div>
                        <div v-else-if="item.type==='search' && item.column === column.dataIndex" class="input-container d_flex fai_c font_13 h_20 lh_20 maxw_p100">
                            <search-input v-if="editableData[record.key]" :res_map="search_map[column.dataIndex]" :api_info="search_api" :target_title="column.dataIndex" @search-select="handleSearchInput"></search-input>
                            <template v-else>{{ text }}</template>
                        </div>
                    </template>
                    <template v-if="column.dataIndex === 'operation'">
                        <div>
                            <span v-if="editableData[record.key]" class="d_iflex gap_8 font_13">
                                <a @click="saveTable(record.key)">保存</a>
                                <a-popconfirm title="取消编辑?" @confirm="cancelTable(record.key)">
                                    <a>取消</a>
                                </a-popconfirm>
                            </span>
                            <span v-else>
                                <a @click="editTable(record.key)" :class="{ 'disabled_link': !can_edit }">编辑</a>
                            </span>
                        </div>
                    </template>
                </template>
            </a-table>
        </a-spin>
    </div>
</template>

<style>
@import url('@/assets/style/common.css');
@import url('@/assets/style/colorset.css');
@import url('@/assets/style/overwrite.css');

.input-container input {
    height: 30px;
    line-height: 30px;
    background-color: #f2f3f5;
    border: none;
    color: #4e5969;
    border-radius: 2px;
    padding-left: 8px;
    align-items: center;
}

.input-container input:focus {
    color: #C9CDD4;
}
.input-container .ant-input {
    width: 100%;
}
.input-container .select-wrapper div.ant-select-selector {
    height: 30px;
    line-height: 30px;
    padding-left: 8px;
    padding-right: 24px;
}
.input-container .select-wrapper div.ant-select-selector span {
    font-size: 13px;
    line-height: 30px;
}
.input-container .select-wrapper div.ant-select-selector span.ant-select-selection-item {
    font-size: 13px;
    line-height: 30px;
}
/* .input-container .ant-select-single .ant-select-selector span.ant-select-selection-search {
    inset-inline-start: 8px;
    inset-inline-end: 8px
} */
.disabled_link {
    pointer-events: none;
    cursor: not-allowed;
    color: #C9CDD4;
}
</style>

<script>
import { defineComponent, ref, watch } from 'vue';
import { Table, Input, Select, SelectOption, Popconfirm, Spin } from 'ant-design-vue';
import { Down } from '@icon-park/vue-next';
import { cloneDeep } from 'lodash-es';

import SearchInput from '@/components/other/search-input.vue';
import { tableScrollYResize } from '@/utils/tableScrollYResize.js';
import { valueFindKey } from '@/utils/valueFindKey.js';

export default defineComponent({
    name: 'EditTable',
    components: {
        'a-spin': Spin,
        'a-table': Table,
        'a-input': Input,
        'a-select': Select,
        'a-select-option': SelectOption,
        'a-popconfirm': Popconfirm,
        'search-input': SearchInput,
        'icon-down': Down
    },
    props: {
        'table_obj': {type:Object},
        'status': {type: Boolean,default:false}
    },
    setup(props) {
        const data = ref(props.table_obj.data);
        const spin_status = ref(props.status)

        watch(props, () => {
            spin_status.value = props.status
            data.value = props.table_obj.data;
        }, { deep: true });

        return {
            columns: ref(props.table_obj.columns),
            data,
            spin_status,
            editIndex: ref(props.table_obj.editIndex),
            table_scroll: ref({ y: 0 }),
            editableData: ref([]),
            editMap: ref(props.table_obj.editMap),
            search_map: ref(props.table_obj.search_obj.search_map),
            search_api: ref(props.table_obj.search_obj.search_api),
            search_res: ref({}),
            can_edit: ref(true)
        }
    },
    mounted() {
        window.addEventListener('resize',tableScrollYResize('table_con',this.table_scroll));
    },
    methods: {
        editTable(key) {
            this.editableData[key] = cloneDeep(this.data.filter(item => key === item.key)[0]);
            console.log(this.editableData[key])
        },
        cancelTable(key) {
            delete this.editableData[key];
        },
        saveTable(key) {
            // 抽出目标行
            let target_data = this.data.filter(item => key === item.key)[0]
            // let target_data = this.editableData[key]
            // 文本直接赋值
            Object.assign(this.data.filter(item => key === item.key)[0],this.editableData[key]);
            // 结合editMap匹配对应的码值
            this.editMap.forEach((each) => {
                target_data[each.code_target] = valueFindKey(each.range,target_data[each.name_target],'ref_name','ref_code')
            })
            // 结合search_map匹配对应的码值
            for (let key in this.search_res) {
                console.log(key);
                console.log(this.search_res[key],this.search_map[key])
                // target_data[]
                target_data[this.search_map[key]['key']] = this.search_res[key]['key']
            }
            // 保存
            console.log(this.data.filter(item => key === item.key)[0])
            delete this.editableData[key];
        },
        handleSearchInput(value) {
            console.log(value);
            // 判断title有没有存在过，没有的话则保存用于遍历
            if(!(value.title in this.search_res)) {
                this.search_res[value.title] = value.data
            }
            console.log(this.search_res)
            console.log(this.search_map)
        }
    }
})
</script>