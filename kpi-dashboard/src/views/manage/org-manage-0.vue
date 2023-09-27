<template>
    <div class="d_flex fd_c gap_20 h_p100">
        <div class="d_flex p_20 bg_white fd_r gap_20 fai_c jc_sb">
            <div class="d_flex gap_20">
                <a-dropdown
                    class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180">
                    <a>
                        {{ search_orgGroup.value }}
                        <icon-down class="lh_1" fill="#86909C"></icon-down>
                    </a>
                    <template #overlay>
                        <a-menu>
                            <a-menu-item v-for="item in org_group" :key="item.key"
                                @click="chooseMenuItem(item, 'search_orgGroup')">{{ item.value }}</a-menu-item>
                        </a-menu>
                    </template>
                </a-dropdown>
                <a-dropdown
                    class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180">
                    <a>
                        {{ search_orgLevel.value }}
                        <icon-down class="lh_1" fill="#86909C"></icon-down>
                    </a>
                    <template #overlay>
                        <a-menu>
                            <a-menu-item v-for="item in org_level" :key="item.key"
                                @click="chooseMenuItem(item, 'search_orgLevel')">{{ item.value }}</a-menu-item>
                        </a-menu>
                    </template>
                </a-dropdown>
                <a-input placeholder="输入导入人信息或者导入编号进行搜索"
                    class="w_360 fai_c bg_l2 br_2  ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 b_n">
                    <template #suffix>
                        <icon-search size="14" class="mr_8 lh_1"></icon-search>
                    </template>
                </a-input>
            </div>
            <div class="d_flex gap_20 fai_c">
                <a-divider type="vertical" style="height: 18px; border-color: #E5E6EB; top: 0;"></a-divider>
                <div class="d_flex gap_20">
                    <a-button type="default" class="br_2 fai_c d_flex fc_l2 bg_l2 b_n" @click="resetSearch">
                        <template #icon>
                            <icon-redo size="14" class="mr_8 lh_1"></icon-redo>
                        </template>
                        重置
                    </a-button>
                    <a-button type="primary" class="br_2 fai_c d_flex fc_l5 bg_brand6" @click="confirmSearch">
                        <template #icon>
                            <icon-search size="14" class="mr_8 lh_1"></icon-search>
                        </template>
                        查询
                    </a-button>
                    <a-button type="primary" class="br_2 fai_c d_flex fc_l5 bg_brand6" @click="showModal">
                        <template #icon>
                            <icon-add size="14" class="mr_8 lh_1"></icon-add>
                        </template>
                        新增
                    </a-button>
                </div>
            </div>
        </div>
        <div class="p_20 bg_white h_p100 d_flex fd_c gap_20">
            <div class="of_a fg_1">
                <a-table :columns="table_data.table_columns" :data-source="table_data.table_data" :pagination="false"
                    class="b_w1c2_so br_2">
                    <template #bodyCell="{ column, text, record }">
                        <template
                            v-if="['org_num', 'org_name', 'org_group', 'org_level', 'lead_org'].includes(column.dataIndex)">
                            <div class="input-container">
                                <a-input v-if="editableData[record.key]"
                                    v-model:value="editableData[record.key][column.dataIndex]" class="input-wrapper">
                                </a-input>
                                <template v-else>{{ text }}</template>
                            </div>
                        </template>
                        <template v-else-if="column.dataIndex === 'org_operation'">
                            <div>
                                <span v-if="editableData[record.key]" class="d_iflex gap_8 font_13">
                                    <a @click="save(record.key)">保存</a>
                                    <a-popconfirm title="Sure to cancel?" @confirm="cancel(record.key)">
                                        <a>取消</a>
                                    </a-popconfirm>
                                </span>
                                <span v-else>
                                    <a @click="edit(record.key)">编辑</a>
                                </span>
                            </div>
                        </template>
                    </template>
                </a-table>
            </div>
            <div class="d_flex fai_c jc_fe">
                <a-pagination :current="page_obj.current" :total="page_obj.total" :pageSize="page_obj.pageSize"
                    @change="handlePageChange"></a-pagination>
            </div>
        </div>
    </div>
    <div class="modalCon" ref="modal">
        <a-modal v-model:open='modal_visible' width="auto" title="新增机构" centered :closable="false">
            <div class="d_flex fai_c pt_20 pb_10 jc_sb">
                <div class="d_flex fd_r fai_c jc_sb gap_20 w_p100">
                    <div class="d_flex fai_c gap_16">
                        <div class="fc_l2 font_14 minw_60">机构编号</div>
                        <a-dropdown
                            class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180">
                            <a-input :value="org_num" class="w_240">
                                <template #suffix></template>
                            </a-input>
                        </a-dropdown>
                    </div>
                    <div class="d_flex fai_c gap_16">
                        <div class="fc_l2 font_14 minw_60">机构名称</div>
                        <a-dropdown
                            class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180">
                            <a-input :value="org_name" class="w_240">
                                <template #suffix></template>
                            </a-input>
                        </a-dropdown>
                    </div>
                </div>
            </div>
            <div class="d_flex fai_c pt_20 pb_10 jc_sb">
                <div class="d_flex fd_r fai_c jc_sb gap_20 w_p100">
                    <div class="d_flex fai_c gap_16">
                        <div class="fc_l2 font_14 minw_60">机构分组</div>
                        <a-dropdown
                            class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180">
                            <a-input :value="add_orgGroup.value" class="w_240">
                                <template #suffix>
                                    <icon-down class="lh_1" fill="#86909C"></icon-down>
                                </template>
                            </a-input>
                            <template #overlay>
                                <a-menu>
                                    <a-menu-item v-for="item in org_group.filter((a) => { return a.key != 'all' })"
                                        :key="item.key" @click="chooseMenuItem(item, 'add_orgGroup')">{{ item.value
                                        }}</a-menu-item>
                                </a-menu>
                            </template>
                        </a-dropdown>
                    </div>
                    <div class="d_flex fai_c gap_16">
                        <div class="fc_l2 font_14 minw_60">机构层级</div>
                        <a-dropdown
                            class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180">
                            <a-input :value="add_orgLevel.value" class="w_240">
                                <template #suffix>
                                    <icon-down class="lh_1" fill="#86909C"></icon-down>
                                </template>
                            </a-input>
                            <template #overlay>
                                <a-menu>
                                    <a-menu-item v-for="item in org_level.filter((a) => { return a.key != 'all' })"
                                        :key="item.key" @click="chooseMenuItem(item, 'add_orgLevel')">{{ item.value
                                        }}</a-menu-item>
                                </a-menu>
                            </template>
                        </a-dropdown>
                    </div>
                </div>
            </div>
            <div class="d_flex fai_c pt_20 pb_20 jc_sb">
                <div class="d_flex fd_r fai_c jc_sb gap_20 w_p100">
                    <div class="d_flex fai_c gap_16">
                        <div class="fc_l2 font_14 minw_60">上级机构</div>
                        <a-dropdown
                            class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180">
                            <a-input :value="lead_org.value" class="w_240">
                                <template #suffix>
                                    <icon-down class="lh_1" fill="#86909C"></icon-down>
                                </template>
                            </a-input>

                            <template #overlay>
                                <a-menu>
                                    <a-menu-item>上海分行</a-menu-item>
                                    <a-menu-item>其他区域中心支行</a-menu-item>
                                </a-menu>
                            </template>
                        </a-dropdown>
                    </div>
                    <div class="d_flex fai_c gap_16 jc_sb">
                        <div class="fc_l2 font_14 minw_60">负责人</div>
                        <a-dropdown
                            class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180">
                            <a-input :value="org_manager" class="w_240">
                                <template #suffix></template>
                            </a-input>
                        </a-dropdown>
                    </div>
                </div>
            </div>
            <template #footer>
                <div class="d_flex jc_fe gap_8">
                    <a-button type="default" class="br_2 fai_c d_flex fc_l2 bg_l2 b_n" @click="cancelUpload">
                        <template #icon>
                            <icon-close size="14" class="mr_8 lh_1"></icon-close>
                        </template>
                        取消
                    </a-button>
                    <a-button type="primary" class="br_2 fai_c d_flex fc_l5 bg_brand6" @click="confirmUpload">
                        <template #icon>
                            <icon-check size="14" class="mr_8 lh_1"></icon-check>
                        </template>
                        提交
                    </a-button>
                </div>
            </template>
        </a-modal>
    </div>
</template>

<style>
@import url('@/assets/style/common.css');
@import url('@/assets/style/colorset.css');
@import url('@/assets/style/overwrite.css');
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
.input-container {
    max-width: 100%;
    display: flex;
    align-items: center;
    height: 20px;
    line-height: 20px;
    font-size: 13px;
}
.input-container .ant-input {
    width: 100%;
}
.input-container .input-wrapper {
    max-width: 100%;
    overflow: hidden;
    font-size: 13px;
    width: 100%;
}
.input-container .select-wrapper {
    height: 20px;
    line-height: 20px;
    align-items: center;
    font-size: 13px;
    display: flex;
    width: 100%;
}
.input-container .select-wrapper div.ant-select-selector {
    height: 30px;
    line-height: 30px;
    /* background-color: transparent; */
    padding-left: 8px;
    padding-right: 24px;
}
.input-container .select-wrapper div.ant-select-selector span {
    font-size: 13px;
    line-height: 30px;
}
.input-container .select-wrapper div.ant-select-selector span.ant-select-selection-search input {
    font-size: 13px;
    line-height: 20px;
    height: 20px;
}
.input-container .ant-select-single .ant-select-selector span.ant-select-selection-search {
    inset-inline-start: 8px;
    inset-inline-end: 8px
}
.input-container .ant-select-single .ant-select-selector span.ant-select-selection-item {
    height: 30px;
}
.disabled_link {
    pointer-events: none;
    cursor: not-allowed;
    color: #C9CDD4;
}
</style>

<script>
import { defineComponent, reactive, ref } from 'vue';
import { Down, Search, Redo, AddFour, Close, Check } from '@icon-park/vue-next';
import { Dropdown, Menu, MenuItem, Input, Divider, Button, Table, Popconfirm, Pagination, Modal } from 'ant-design-vue';
import axios from 'axios';
import { cloneDeep } from 'lodash-es'

export default defineComponent({
    name: "OrgManage",
    components: {
        'icon-down': Down,
        'icon-search': Search,
        'icon-redo': Redo,
        'icon-add': AddFour,
        'icon-close': Close,
        'icon-check': Check,
        'a-dropdown': Dropdown,
        'a-menu': Menu,
        'a-menu-item': MenuItem,
        'a-input': Input,
        'a-divider': Divider,
        'a-button': Button,
        'a-table': Table,
        'a-pagination': Pagination,
        'a-modal': Modal,
        'a-popconfirm': Popconfirm,
    },
    setup() {
        const table_data = ref({});
        const dataSource = ref(table_data);
        const modal_visible = ref(false);
        const editableData = reactive({});
        return {
            table_data,
            editableData,
            dataSource,
            modal_visible,
            page_obj: ref({
                current: 1,
                pageSize: 10,
                total: 100
            }),
            search_orgGroup: ref({ key: 'all', value: '全部分组' }),
            org_group: ref([]),
            search_orgLevel: ref({ key: 'all', value: '全部层级' }),
            org_level: ref([]),
            add_orgGroup: ref({ key: 'qyzxzh', value: '区域中心支行' }),
            add_orgLevel: ref({ key: '04', value: '四级机构' }),
            lead_org: ref({ key: '3100001', value: '上海分行' }),
            org_num: ref(),
            org_name: ref(''),
            org_manager: ref('')
        }
    },
    mounted() {
        this.getOrgData();
        this.getFilterData();
    },
    methods: {
        async getOrgData() {
            const org_res = await axios.get('/demo/manage/org-manage.json');
            this.table_data = org_res.data
        },
        async getFilterData() {
            const filter_res = await axios.get('/demo/filter/normal_filter.json');
            this.org_group = filter_res.data.org_group;
            this.org_level = filter_res.data.org_level;
        },
        edit(key) {
            // console.log(this.dataSource.table_data,key)
            this.editableData[key] = cloneDeep(this.dataSource.table_data.filter(item => key === item.key)[0]);
        },
        save(key) {
            Object.assign(this.dataSource.table_data.filter(item => key === item.key)[0], this.editableData[key]);
            delete this.editableData[key];
        },
        cancel(key) {
            delete this.editableData[key];
        },
        showModal() {
            this.modal_visible = true;
        },
        cancelUpload() {
            this.modal_visible = false;
        },
        confirmUpload() {
            this.modal_visible = false;
        },
        handlePageChange(page) {
            console.log(page)
            this.page_obj.current = page
        },
        chooseMenuItem(item, target) {
            this[target] = item
        },
        resetSearch() {
            this.search_orgGroup = { key: 'all', value: '全部分组' };
            this.search_orgLevel = { key: 'all', value: '全部层级' };
        },
        confirmSearch() {
            console.log(this.search_orgGroup, this.search_orgLevel)
        }
    }
});

</script>