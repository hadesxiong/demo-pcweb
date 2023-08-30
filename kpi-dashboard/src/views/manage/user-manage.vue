<template>
    <div class="d_flex fd_c gap_20 h_p100">
        <div class="d_flex p_20 bg_white fd_r gap_20 fai_c jc_sb">
            <div class="d_flex gap_20">
                <a-dropdown
                    class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180">
                    <a>{{ search_orgGroup.value }}<icon-park type="Down" class="lh_1" fill="#86909C"></icon-park></a>
                    <template #overlay>
                        <a-menu>
                            <a-menu-item v-for="item in org_group" :key="item.key"
                                @click="chooseMenuItem(item, 'search_orgGroup')">{{ item.value }}</a-menu-item>
                        </a-menu>
                    </template>
                </a-dropdown>
                <a-dropdown
                    class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180">
                    <a>{{ search_charater.value }}<icon-park type="Down" class="lh_1" fill="#86909C"></icon-park></a>
                    <template #overlay>
                        <a-menu>
                            <a-menu-item v-for="item in charater_group" :key="item.key"
                                @click="chooseMenuItem(item, 'search_charater')">{{ item.value }}</a-menu-item>
                        </a-menu>
                    </template>
                </a-dropdown>
                <a-dropdown
                    class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180">
                    <a>{{ search_line.value }}<icon-park type="Down" class="lh_1" fill="#86909C"></icon-park></a>
                    <template #overlay>
                        <a-menu>
                            <a-menu-item v-for="item in line_more" :key="item.key"
                                @click="chooseMenuItem(item, 'search_line')">{{ item.value }}</a-menu-item>
                        </a-menu>
                    </template>
                </a-dropdown>
                <a-input placeholder="输入导入人信息或者导入编号进行搜索"
                    class="w_360 fai_c bg_l2 br_2  ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 b_n">
                    <template #suffix>
                        <icon-park type="Search" size="14" class="mr_8 lh_1"></icon-park>
                    </template>
                </a-input>
            </div>
            <div class="d_flex gap_20 fai_c">
                <a-divider type="vertical" style="height: 18px; border-color: #E5E6EB; top: 0;"></a-divider>
                <div class="d_flex gap_20">
                    <a-button type="default" class="br_2 fai_c d_flex fc_l2 bg_l2 b_n" @click="resetSearch">
                        <template #icon>
                            <icon-park type="Redo" size="14" class="mr_8 lh_1"></icon-park>
                        </template>
                        重置
                    </a-button>
                    <a-button type="primary" class="br_2 fai_c d_flex fc_l5 bg_brand6" @click="confirmSearch">
                        <template #icon>
                            <icon-park type="Search" size="14" class="mr_8 lh_1"></icon-park>
                        </template>
                        查询
                    </a-button>
                    <a-button type="primary" class="br_2 fai_c d_flex fc_l5 bg_brand6" @click="showModal">
                        <template #icon>
                            <icon-park type="AddFour" size="14" class="mr_8 lh_1"></icon-park>
                        </template>
                        新增
                    </a-button>
                </div>
            </div>

        </div>
        <div class="p_20 bg_white h_p100 d_flex fd_c gap_20">
            <div class="of_a fg_1">
                <a-table :columns="table_data.table_columns" :data-source="table_data.table_data" class="b_w1c2_so br_4"
                    :pagination="false">
                    <template #bodyCell="{ column, text, record }">
                        <template
                            v-if="['user_notesid', 'user_name', 'user_character', 'user_class', 'user_org'].includes(column.dataIndex)">
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
        <a-modal v-model:open='modal_visible' width="auto" title="新增用户" centered :closable="false">
            <div class="d_flex fai_c pt_20 pb_10 jc_sb">
                <div class="d_flex fd_r fai_c jc_sb gap_20 w_p100">
                    <div class="d_flex fai_c gap_16">
                        <div class="fc_l2 font_14 minw_60">新增方式</div>
                        <a-radio-group v-model:value="create_type">
                            <a-radio :value="1">单条新增</a-radio>
                            <a-radio :value="2">批量新增</a-radio>
                        </a-radio-group>
                    </div>
                </div>
            </div>
            <div v-if="create_type == 1" class="single_create">
                <div class="d_flex fai_c pt_20 pb_10 jc_sb">
                    <div class="d_flex fd_r fai_c jc_sb gap_20 w_p100">
                        <div class="d_flex fai_c gap_16">
                            <div class="fc_l2 font_14 minw_60">NotesID</div>
                            <a-dropdown
                                class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180">
                                <a-input :value="user_notesid" class="w_240">
                                    <template #suffix></template>
                                </a-input>
                            </a-dropdown>
                        </div>
                        <div class="d_flex fai_c gap_16">
                            <div class="fc_l2 font_14 minw_60">用户名称</div>
                            <a-dropdown
                                class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180">
                                <a-input :value="user_name" class="w_240">
                                    <template #suffix></template>
                                </a-input>
                            </a-dropdown>
                        </div>
                    </div>
                </div>
                <div class="d_flex fai_c pt_20 pb_10 jc_sb">
                    <div class="d_flex fd_r fai_c jc_sb gap_20 w_p100">
                        <div class="d_flex fai_c gap_16">
                            <div class="fc_l2 font_14 minw_60">用户角色</div>
                            <a-dropdown
                                class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180">
                                <a-input :value="add_charater.value" class="w_240">
                                    <template #suffix>
                                        <icon-park type="Down" class="lh_1" fill="#86909C"></icon-park>
                                    </template>
                                </a-input>
                                <template #overlay>
                                    <a-menu>
                                        <a-menu-item v-for="item in charater_group.filter((a) => { return a.key != 'all' })"
                                            :key="item.key" @click="chooseMenuItem(item, 'add_charater')">{{ item.value
                                            }}</a-menu-item>
                                    </a-menu>
                                </template>
                            </a-dropdown>
                        </div>
                        <div class="d_flex fai_c gap_16">
                            <div class="fc_l2 font_14 minw_60">归属条线</div>
                            <a-dropdown
                                class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180">
                                <a-input :value="add_line.value" class="w_240">
                                    <template #suffix>
                                        <icon-park type="Down" class="lh_1" fill="#86909C"></icon-park>
                                    </template>
                                </a-input>
                                <template #overlay>
                                    <a-menu>
                                        <a-menu-item v-for="item in line_more.filter((a) => { return a.key != 'all' })"
                                            :key="item.key" @click="chooseMenuItem(item, 'add_line')">{{ item.value
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
                            <div class="fc_l2 font_14 minw_60">归属机构</div>
                            <a-dropdown
                                class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180">
                                <a-input :value="belong_org.value" class="w_240">
                                    上海分行
                                    <template #suffix>
                                        <icon-park type="Down" class="lh_1" fill="#86909C"></icon-park>
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
                            <div class="fc_l2 font_14 minw_60">直属上级</div>
                            <a-dropdown
                                class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180">
                                <a-input :value="lead_manager.value" class="w_240">
                                    <template #suffix></template>
                                </a-input>
                            </a-dropdown>
                        </div>
                    </div>
                </div>
            </div>
            <div v-if="create_type == 2" class="multi_create">
                <div class="d_flex fai_c pt_20 pb_20 jc_fs">
                    <div class="d_flex fd_r fai_c jc_sb gap_20">
                        <div class="d_flex fai_c gap_16">
                            <div class="fc_l2 font_14 minw_60">导入文件</div>
                            <file-input></file-input>
                        </div>
                        <div class="d_flex fai_c gap_16" style="width:316px">
                            <a class="fc_brand6 font_14">下载模版</a>
                        </div>
                    </div>
                </div>
            </div>
            <template #footer>
                <div class="d_flex jc_fe gap_8">
                    <a-button type="default" class="br_2 fai_c d_flex fc_l2 bg_l2 b_n" @click="cancelUpload">
                        <template #icon>
                            <icon-park type="Close" size="14" class="mr_8 lh_1"></icon-park>
                        </template>
                        取消
                    </a-button>
                    <a-button type="primary" class="br_2 fai_c d_flex fc_l5 bg_brand6" @click="confirmUpload">
                        <template #icon>
                            <icon-park type="Check" size="14" class="mr_8 lh_1"></icon-park>
                        </template>
                        提交
                    </a-button>
                </div>
            </template>
        </a-modal>
    </div>
</template>

<style>
@import url('../../assets/style/common.css');
@import url('../../assets/style/colorset.css');
@import url('../../assets/style/overwrite.css');

.input-container {
    max-width: 100%;
    overflow: hidden;
}

.input-container .ant-input {
    width: 100%;
}

.input-container .input-wrapper {
    max-width: 100%;
    overflow: hidden;
    font-size: 13px;
}

.input-container .input-wrapper .input-component {
    width: 100%;
}
</style>

<style scoped>
:where(.css-dev-only-do-not-override-eq3tly).ant-input {
    padding: 0px !important;
    height: 100% !important;
    background-color: transparent;
    border: none;
    color: #C9CDD4;
    border-radius: 0px;
}

:where(.css-dev-only-do-not-override-eq3tly).ant-input:focus {
    color: #165dff;
}
</style>

<script>
import { defineComponent, reactive, ref } from 'vue';
import { IconPark } from '@icon-park/vue-next/es/all';
import axios from 'axios';
import { cloneDeep } from 'lodash-es'

import FileInput from '../../components/other/file-input.vue';

export default defineComponent({
    name: "OrgManage",
    components: {
        'icon-park': IconPark,
        'file-input': FileInput
    },
    setup() {
        const table_data = ref({});
        const dataSource = ref(table_data);
        const modal_visible = ref(false);
        const create_type = ref(1)
        const editableData = reactive({});
        return {
            table_data,
            editableData,
            dataSource,
            modal_visible,
            create_type,
            page_obj: ref({
                current: 1,
                pageSize: 10,
                total: 100
            }),
            org_group: ref([]),
            charater_group: ref([]),
            line_more: ref([]),
            search_orgGroup: ref({ key: 'all', value: '全部分组' }),
            search_charater: ref({ key: 'all', value: '全部角色' }),
            search_line: ref({ key: 'all', value: '全部序列' }),
            add_charater: ref({ key: '00', value: '超级管理员' }),
            add_line: ref({ key: 'enterprise', value: '企金序列' }),
            belong_org: ref({ key: '3100001', value: '上海分行' }),
            lead_manager: ref({ key: '101203', value: '真汉子比尔曼' }),
            user_notesid: ref(),
            user_name: ref()
        }
    },
    mounted() {
        this.getOrgData();
        this.getFilterData();
    },
    methods: {
        async getOrgData() {
            const user_res = await axios.get('/demo/manage/user-manage.json');
            this.table_data = user_res.data
        },
        async getFilterData() {
            const filter_res = await axios.get('/demo/filter/normal_filter.json');
            this.org_group = filter_res.data.org_group;
            this.charater_group = filter_res.data.charater_gourp;
            this.line_more = filter_res.data.line_more;
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
            this.search_charater = { key: 'all', value: '全部角色' };
            this.search_line = { key: 'all', value: '全部序列' };
        },
        confirmSearch() {
            console.log(this.search_orgGroup, this.search_charater,this.search_line)
        }
    }
});

</script>