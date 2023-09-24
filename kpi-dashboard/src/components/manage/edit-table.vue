<template>
    <div class="ofy_h fg_1" id="table_con">
        <a-spin :spinning="spin_status" size="large" :delay="100" tip="数据加载中">
            <a-table :columns="columns" :data-source="data" :scroll="table_scroll" :pagination="false">
                <template #bodyCell="column,text,record">
                    <template v-for="item in editIndex" :key="item.key">
                        <div v-if="item.type==='input'" class="input-container d_flex fai_c font_13 h_20 lh_20 maxw_p100">
                            <a-input v-if="editableData[record.key]" class="input-wrapper maxw_p100 of_h font_13 w_p100"
                                v-model:value="editableData[record.key][column.dataIndex]">
                            </a-input>
                            <template v-else>{{ text }}</template>
                        </div>
                        <div v-else-if="item.type==='select'" class="input-container d_flex fai_c font_13 h_20 lh_20 maxw_p100">
                            <a-select v-if="editableData[record.key]" class="select-wrapper d_flex fai_c font_13 h_20 lh_20 maxw_p100">
                                <template #suffixIcon>
                                    <icon-down size="16" fill="#86909C" class="d_flex fai_c"></icon-down>
                                </template>
                                <a-select-option
                                    v-for="sub_item in item.option_list.filter((a) => { return a.ref_code != 0 })"
                                    :key="sub_item.ref_code" :value="sub_item.ref_name">{{ sub_item.ref_name }}</a-select-option>
                            </a-select>
                        </div>
                        <div v-else-if="item.type==='search'" class="input-container d_flex fai_c font_13 h_20 lh_20 maxw_p100">
                            <search-input v-if="editableData[record.key]"></search-input>
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
</style>

<style scoped>
.input-container input {
    height: 30px;
    background-color: #f2f3f5;
    border: none;
    color: #4e5969;
    border-radius: 2px;
    padding-left: 8px;
}

.input-container input:focus {
    color: #C9CDD4;
}

/* .input-container {
    max-width: 100%;
    display: flex;
    align-items: center;
    height: 20px;
    line-height: 20px;
    font-size: 13px;
} */

.input-container .ant-input {
    width: 100%;
}

/* .input-container .input-wrapper {
    max-width: 100%;
    overflow: hidden;
    font-size: 13px;
    width: 100%;
} */

/* .input-container .select-wrapper {
    height: 20px;
    line-height: 20px;
    align-items: center;
    font-size: 13px;
    display: flex;
    width: 100%;
} */

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

/* .input-container .select-wrapper div.ant-select-selector span.ant-select-selection-search input {
    font-size: 13px;
    line-height: 20px;
    height: 20px;
} */

.input-container .ant-select-single .ant-select-selector span.ant-select-selection-search {
    inset-inline-start: 8px;
    inset-inline-end: 8px
}

/* .input-container .ant-select-single .ant-select-selector span.ant-select-selection-item {
    height: 30px;
} */

.disabled_link {
    pointer-events: none;
    cursor: not-allowed;
    color: #C9CDD4;
}
</style>


<script>
import { defineComponent, ref, toRefs } from 'vue';
import { Table, Spin, Input, Select, SelectOption } from 'ant-design-vue';
import { Down } from '@icon-park/vue-next';
import { cloneDeep } from 'lodash-es';

import SearchInput from '@/components/other/search-input.vue';
import { tableScrollYResize } from '@/utils/tableScrollYResize.vue';
import { valueFindKey } from '@/utils/valueFindKey';

export default defineComponent({
    name: 'EditTable',
    components: {
        'a-spin': Spin,
        'a-table': Table,
        'a-input': Input,
        'a-select': Select,
        'a-select-option': SelectOption,
        'search-input': SearchInput,
        'icon-down': Down
    },
    props: {
        'table_obj': {type:Object},
    },
    setup(props) {
        const { columns, data, editIndex, editMap } = toRefs(props.table_obj)
        return {
            spin_status: ref(false),
            columns: columns.value,
            data: data.value,
            editIndex: editIndex.value,
            table_scroll: ref({y:0}),
            editableData: ref({}),
            editMap: editMap.value,
        }
    },
    mounted() {
        window.addEventListener('resize',tableScrollYResize('table_con',this.table_scroll));
    },
    methods: {
        editTable(key) {
            this.editableData[key] = cloneDeep(this.user_list.filter(item => key === item.key)[0]);
            // console.log(this.editableData[key])
        },
        cancelTable(key) {
            delete this.editableData[key];
        },
        saveTable(key) {
            // 文本直接赋值
            Object.assign(this.data.filter(item => key === item.key)[0],this.editableData[key]);
            // 结合editMap匹配对应的码值
            this.editMap.forEach(function(each) {
                console.log(each);
                this.data.filter(item => key === item.key)[0][each.code_target] = valueFindKey(each.range,each.name_target,'ref_name','ref_code')
            })
            // 搜索项
            
            console.log(this.user_list.filter(item => key === item.key)[0])
        }
    }
})
</script>