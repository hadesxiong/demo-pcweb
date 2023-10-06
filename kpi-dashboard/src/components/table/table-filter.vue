<template>
    <div class="d_flex w_p100 fd_c bg_white p_20 gap_20 fs_0 minh_120" :class="label_collaspe ? 'normal_height' : 'collapse_height'">
        <div class="d_flex fd_r lh_30 gap_20 h_30 fai_c jc_sb">
            <div class="d_flex fd_r gap_20">
                <div class="fc_l3 filter_title ta_l">查看方式</div>
                <div class="d_flex">
                    <a-radio-group v-model:value="default_org" button-style="solid" class="d_flex gap_12 h_30">
                        <a-radio-button class="br_100 of_h tover_ell" v-for="(item, index) in filter_data.org_filter"
                            :key="index" :value="item.value">{{ item.label }}</a-radio-button>
                    </a-radio-group>
                </div>
            </div>
            <div>
                <a-button type="primary" class="br_2 fai_c d_flex fc_l5 bg_brand6" @click="handleSearch(default_org,filterIndexClass,filterIndexList)">
                    <template #icon>
                        <icon-find size="14" class="mr_8 lh_1"></icon-find>
                    </template>
                    查询
                </a-button>
            </div>
        </div>
        <div class="d_flex fd_r lh_30 gap_20 h_30 fai_c jc_sb">
            <div class="d_flex fd_r gap_20">
                <div class="fc_l3 filter_title ta_l">指标分类</div>
                <div class="d_flex">
                    <custom-multi v-if="filter_data.index_class" :custom_options="filter_data.index_class"
                        :option_type="'class'" @getSelectedOptions="execIndexList" key="class"></custom-multi>
                </div>
            </div>
            <div>
                <a-button v-if="label_collaspe" type="text" class="br_2 fai_c d_flex fc_brand6"
                    style="width:auto;padding: 4px 15px;" @click="toggleIndex">
                    <template #icon>
                        <icon-doubleUp size="14" class="mr_8 lh_1"></icon-doubleUp>
                        收起
                    </template>
                </a-button>
                <a-button v-else type="text" class="br_2 fai_c d_flex fc_brand6" style="width:auto;padding: 4px 15px;"
                    @click="toggleIndex">
                    <template #icon>
                        <icon-doubleDown size="14" class="mr_8 lh_1"></icon-doubleDown>
                        展开
                    </template>
                </a-button>
            </div>
        </div>
        <div class="d_flex fd_r lh_30 gap_20 fai_fs jc_sb">
            <div class="d_flex fd_r gap_20">
                <div class="fc_l3 filter_title ta_l">指标名称</div>
                <div class="d_flex">
                    <custom-multi v-if="selectedIndexList" :custom_options="selectedIndexList"
                        :option_type="'index'" @getSelectedOptions="execIndexList" key="index"></custom-multi>
                </div>
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
    min-width: 80px;
}

.collapse_height {
    height: 120px;
    overflow: hidden;
}

.normal_height {
    height: auto;
}
</style>

<script>
import { defineComponent, ref, watch } from 'vue';
import { Find, DoubleUp, DoubleDown } from '@icon-park/vue-next';
import { RadioGroup, RadioButton, Button } from 'ant-design-vue';

import CustomMulti from './custom-multi.vue';

export default defineComponent({
    name: "TableFilter",
    components: {
        'icon-find': Find,
        'icon-doubleUp': DoubleUp,
        'icon-doubleDown': DoubleDown,
        'a-radio-group': RadioGroup,
        'a-radio-button': RadioButton,
        'a-button': Button,
        'custom-multi': CustomMulti,
    },
    props: {
        filter_data: {
            type: Object
        },
    },
    data() {
        return {}
    },
    setup(props) {
        // console.log(props.filter_data)
        const selectedIndexList = ref()
        const filterIndexClass = ref()
        watch(props, () => {
            selectedIndexList.value = props.filter_data['index_list'].map(item=>item.label_list).flat()
            filterIndexClass.value = props.filter_data['index_class'].filter(item => item.value != 'all').map(item=>item.value)
            // console.log(filterIndexClass)
        }, { deep: true });
        return {
            default_org: ref(1),
            label_collaspe: ref(false),
            selectedIndexList,
            filterIndexClass,
            filterIndexList: ref([])
        }
    },
    mounted() {},
    methods: {
        execIndexList(selected_object) {

            // 处理逻辑(指标拉平)
            // 1.selected_object每次选择过一次全部后，需要清空一次selectedIndexList的选中状态
            // 2.每次优先添加全部选项
            // 3.然后按照选中的指标分类逐步完成添加

            if (selected_object.class == 'class') {
                let target_data = [];
                this.selectedIndexList = target_data
                if (selected_object.list.includes('all') || selected_object.list.length == 0) {
                    this.filter_data.index_list.forEach(function (each_class) {
                        each_class.label_list.forEach(function (each_label) {
                            target_data.push(each_label);
                        })
                    });
                    this.filterIndexClass = this.filter_data.index_class.filter(item=>item.value!='all').map(item=>item.value)
                } else {
                    target_data.push({ "label": "全部", "value": "all" });
                    this.filter_data.index_list.filter(function (each_class) {
                        if (selected_object.list.includes(each_class.class)) {
                            // console.log(each_class.label_list)
                            target_data = target_data.concat(each_class.label_list)
                        }
                    });
                    this.filterIndexClass = selected_object.list
                }
                this.selectedIndexList = target_data;
            } else if (selected_object.class=='index') {
                this.filterIndexList = selected_object.list;
            }
        },
        toggleIndex() {
            this.label_collaspe = !this.label_collaspe;
        },
        handleSearch(org_list,class_list,index_list) {
            // 检查并处理index_list
            let index_result = []
            if (index_list.includes('all') || index_list.length == 0) {
                console.log('all')
                console.log(class_list)
                index_result = class_list.flatMap(each_class => {
                    const obj = this.filter_data.index_list.find(item => item.class == each_class);
                    return obj? obj.label_list:[]
                }).map(item=>item.value)
                console.log(index_result)
            } else {
                index_result = index_list
                console.log(index_result)
            }
            this.$emit('getFilterOptions',{'org':org_list,'class':class_list,'index':index_result})
        }
    }
});
</script>