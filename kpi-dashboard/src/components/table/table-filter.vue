<template>
    <div class="d_flex w_p100 fd_c bg_white p_20 gap_20"  :class="label_collaspe ? 'normal_height' : 'collapse_height'">
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
                <a-button type="primary" class="br_2 fai_c d_flex fc_l5 bg_brand6">
                    <template #icon>
                        <icon-park type="Find" size="14" class="mr_8 lh_1"></icon-park>
                    </template>
                    查询
                </a-button>
            </div>
        </div>
        <div class="d_flex fd_r lh_30 gap_20 fai_fs jc_sb">
            <di v class="d_flex fd_r gap_20">
                <div class="fc_l3 filter_title ta_l">指标分类</div>
                <div class="d_flex">
                    <custom-multi v-if="filter_data.index_class" :custom_options="filter_data.index_class"
                        @getSelectedOptions="execIndexList"></custom-multi>
                </div>
            </di>
            <div>
                <a-button v-if="label_collaspe" type="text" class="br_2 fai_c d_flex fc_brand6"
                    style="width:auto;padding: 4px 15px;" @click="toggleIndex">
                    <template #icon>
                        <icon-park type="DoubleUp" size="14" class="mr_8 lh_1"></icon-park>
                        收起
                    </template>
                </a-button>
                <a-button v-else type="text" class="br_2 fai_c d_flex fc_brand6" style="width:auto;padding: 4px 15px;"
                    @click="toggleIndex">
                    <template #icon>
                        <icon-park type="DoubleDown" size="14" class="mr_8 lh_1"></icon-park>
                        展开
                    </template>
                </a-button>
            </div>
        </div>
        <div class="d_flex fd_r lh_30 gap_20 fai_fs jc_sb">
            <div class="d_flex fd_r gap_20">
                <div class="fc_l3 filter_title ta_l">指标名称</div>
                <div class="d_flex">
                    <custom-multi v-if="selectedIndexList" :custom_options="selectedIndexList"></custom-multi>
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
import { defineComponent, ref } from 'vue';
import CustomMulti from './custom-multi.vue';
import { IconPark } from "@icon-park/vue-next/es/all";

export default defineComponent({
    name: "TableFilter",
    components: {
        'custom-multi': CustomMulti,
        'icon-park': IconPark
    },
    props: {
        filter_data: {
            type: Object
        },

    },
    data() {
        return {
            selectedIndexList: []
        }
    },
    setup() {
        const default_org = ref('qyzxzh');
        const label_collaspe = ref(false);
        return {
            default_org,
            label_collaspe
        }
    },
    mounted() { },
    methods: {
        execIndexList(selected_class) {

            // 处理逻辑
            // 1.selected_class每次选择过一次全部后，需要清空一次selectedIndexList的选中状态
            // 2.每次优先添加全部选项
            // 3.然后按照选中的指标分类逐步完成添加

            let target_data = [];
            this.selectedIndexList = target_data
            if (selected_class.includes('all') || selected_class.length == 0) {
                this.filter_data.index_list.forEach(function (each_class) {
                    each_class.label_list.forEach(function (each_label) {
                        target_data.push(each_label);
                    })
                });
            } else {
                // console.log('222');
                target_data.push({ "label": "全部", "value": "all" });
                // console.log(this.filter_data.index_list,selected_class)
                this.filter_data.index_list.filter(function (each_class) {
                    if (selected_class.includes(each_class.class)) {
                        // console.log(each_class.label_list)
                        target_data = target_data.concat(each_class.label_list)
                    }
                });
            }
            this.selectedIndexList = target_data;
        },
        toggleIndex() {
            this.label_collaspe = !this.label_collaspe;
        }
    }
});
</script>