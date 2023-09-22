<template>
    <div class="d_flex fd_c gap_20 h_p100">
        <div class="d_flex p_20 bg_white fd_r gap_20 fai_c jc_sb">
            <div class="d_flex gap_20">
                <a-dropdown
                    class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180">
                    <a>
                        {{ search_orgGroup.ref_name }}
                        <icon-down class="lh_1" fill="#86909C"></icon-down>
                    </a>
                    <template #overlay>
                        <a-menu>
                            <a-menu-item v-for="item in org_group.filter((a) => { return a.ref_code != 5 })" :key="item.ref_code"
                                @click="chooseMenuItem(item, 'search_orgGroup')">{{ item.ref_name }}</a-menu-item>
                        </a-menu>
                    </template>
                </a-dropdown>
                <a-dropdown
                    class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180">
                    <a>
                        {{ search_charater.ref_name }}
                        <icon-down class="lh_1" fill="#86909C"></icon-down>
                    </a>
                    <template #overlay>
                        <a-menu>
                            <a-menu-item v-for="item in character_group" :key="item.ref_code"
                                @click="chooseMenuItem(item, 'search_charater')">{{ item.ref_name }}</a-menu-item>
                        </a-menu>
                    </template>
                </a-dropdown>
                <a-dropdown
                    class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180">
                    <a>
                        {{ search_line.ref_name }}条线
                        <icon-down class="lh_1" fill="#86909C"></icon-down>
                    </a>
                    <template #overlay>
                        <a-menu>
                            <a-menu-item v-for="item in group_group" :key="item.ref_code"
                                @click="chooseMenuItem(item, 'search_line')">{{ item.ref_name }}条线</a-menu-item>
                        </a-menu>
                    </template>
                </a-dropdown>
                <a-input v-model:value='search_keyword' placeholder="输入导入人信息或者导入编号进行搜索"
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
        <div class="p_20 bg_white h_p100 d_flex fd_c gap_20 ofy_h">
            <div class="ofy_h fg_1" id="user_table">
                <a-spin :spinning="spin_status" size="large" :delay="100" tip="数据加载中...">
                    <a-table :columns="table_header" :data-source="user_list" class="b_w1c2_so br_4" :pagination="false"
                        :scroll="table_scroll">
                        <template #bodyCell="{ column, text, record }">
                            <template v-if="column.dataIndex === 'user_name'">
                                <div class="input-container">
                                    <a-input v-if="editableData[record.key]"
                                        v-model:value="editableData[record.key][column.dataIndex]" class="input-wrapper">
                                    </a-input>
                                    <template v-else>{{ text }}</template>
                                </div>
                            </template>
                            <template v-else-if="column.dataIndex === 'character_name'">
                                <div class="input-container">
                                    <a-select v-if="editableData[record.key]"
                                        v-model:value="editableData[record.key][column.dataIndex]" class="select-wrapper">
                                        <template #suffixIcon>
                                            <icon-down size="16" fill="#86909C" class="d_flex fai_c"></icon-down>
                                        </template>
                                        <a-select-option
                                            v-for="item in character_group.filter((a) => { return a.ref_code != 0 })"
                                            :key="item.ref_code" :value="item.ref_name">{{ item.ref_name }}</a-select-option>
                                    </a-select>
                                    <template v-else>{{ text }}</template>
                                </div>
                            </template>
                            <template v-else-if="column.dataIndex === 'group_name'">
                                <div class="input-container">
                                    <a-select v-if="editableData[record.key]"
                                        v-model:value="editableData[record.key][column.dataIndex]" class="select-wrapper">
                                        <template #suffixIcon>
                                            <icon-down size="16" fill="#86909C" class="d_flex fai_c"></icon-down>
                                        </template>
                                        <a-select-option
                                            v-for="item in group_group.filter((a) => { return a.ref_code != 0 })"
                                            :key="item.ref_code"
                                            :value="item.ref_name">{{ item.ref_name }}条线</a-select-option>
                                    </a-select>
                                    <template v-else>{{ text }}条线</template>
                                </div>
                            </template>
                            <template v-else-if="column.dataIndex === 'org_name'">
                                <div class="input-container">
                                    <a-select v-if="editableData[record.key]" class="select-wrapper"
                                        v-model:value="editableData[record.key][column.dataIndex]" :show-arrow="false"
                                        :options="org_searchRes" show-search @search="debounceSearch">
                                        <template #notFoundContent v-if="org_fetching">
                                            <a-spin size="small"></a-spin>
                                        </template>
                                    </a-select>
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
                                        <a @click="editTable(record.key)" :class="{ 'disabled_link': !can_edit }">编辑</a>
                                    </span>
                                </div>
                            </template>
                        </template>
                    </a-table>
                </a-spin>
            </div>
            <div class="d_flex fai_c jc_fe">
                <a-pagination :current="page_obj.current" :total="page_obj.total" :pageSize="page_obj.pageSize"
                    :pageSizeOptions="page_obj.sizeOptions" @change="changePage"
                    @showSizeChange="changeSizeOptions"></a-pagination>
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
                                <a-input v-model:value="user_notesid" class="w_240">
                                    <template #suffix></template>
                                </a-input>
                            </a-dropdown>
                        </div>
                        <div class="d_flex fai_c gap_16">
                            <div class="fc_l2 font_14 minw_60">用户名称</div>
                            <a-dropdown
                                class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180">
                                <a-input v-model:value="user_name" class="w_240">
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
                                <a-input v-model:value="add_charater.ref_name" class="w_240">
                                    <template #suffix>
                                        <!-- <icon-park type="Down" class="lh_1" fill="#86909C"></icon-park> -->
                                        <icon-down class="lh_1" fill="#86909C"></icon-down>
                                    </template>
                                </a-input>
                                <template #overlay>
                                    <a-menu>
                                        <a-menu-item
                                            v-for="item in character_group.filter((a) => { return a.ref_code != 0 })"
                                            :key="item.ref_code" @click="chooseMenuItem(item, 'add_charater')">{{
                                                item.ref_name
                                            }}</a-menu-item>
                                    </a-menu>
                                </template>
                            </a-dropdown>
                        </div>
                        <div class="d_flex fai_c gap_16">
                            <div class="fc_l2 font_14 minw_60">归属条线</div>
                            <a-dropdown
                                class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180">
                                <a-input v-model:value="add_line.ref_name" class="w_240">
                                    <template #suffix>
                                        <!-- <icon-park type="Down" class="lh_1" fill="#86909C"></icon-park> -->
                                        <icon-down size="16" class="lh_1" fill="#86909C"></icon-down>
                                    </template>
                                </a-input>
                                <template #overlay>
                                    <a-menu>
                                        <a-menu-item v-for="item in group_group.filter((a) => { return a.ref_code != 0 })"
                                            :key="item.ref_code" @click="chooseMenuItem(item, 'add_line')">{{ item.ref_name
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
                                class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pr_12 tover_ell ws_no minw_100 w_180">
                                <a-select class="select-wrapper w_240" v-model:value="belong_org.value" :show-arrow="false"
                                    :options="org_searchRes" show-search @search="debounceSearch" placeholder="请输入机构名称进行搜索">
                                    <template #notFoundContent v-if="org_fetching">
                                        <a-spin size="small"></a-spin>
                                    </template>
                                </a-select>
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
                            <file-input @file-upload="handleFileUpload"></file-input>
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
                            <!-- <icon-park type="Close" size="14" class="mr_8 lh_1"></icon-park> -->
                            <icon-close size="14" class="mr_8 lh_1"></icon-close>
                        </template>
                        取消
                    </a-button>
                    <a-button type="primary" class="br_2 fai_c d_flex fc_l5 bg_brand6" @click="confirmUpload">
                        <template #icon>
                            <!-- <icon-park type="Check" size="14" class="mr_8 lh_1"></icon-park> -->
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
import { defineComponent, ref, reactive } from 'vue';
import { Down, Search, Redo, AddFour, Close, Check } from '@icon-park/vue-next';
import { Dropdown, Menu, MenuItem, Input, Divider, Button, Table, Popconfirm, Pagination, Modal, Radio, RadioGroup, Spin, Select, SelectOption, message } from 'ant-design-vue';
import { cloneDeep, debounce } from 'lodash-es'

import axios from 'axios';
import FileInput from '@/components/other/file-input.vue';
import { tableScrollYResize } from '@/utils/tableScrollYResize';
import { userTableHead } from '@/utils/commonTableHeader';
import { valueFindKey } from '@/utils/valueFindKey'

const api = axios.create({
    baseURL: process.env.VUE_APP_BASE_URL
})

export default defineComponent({
    name: "OrgManage",
    components: {
        'icon-down': Down, 'icon-search': Search, 'icon-redo': Redo, 'icon-add': AddFour, 'icon-close': Close, 'icon-check': Check,
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
        'a-radio': Radio,
        'a-radio-group': RadioGroup,
        'a-spin': Spin,
        'a-select': Select,
        'a-select-option': SelectOption,
        'file-input': FileInput,
    },
    data() {
        return { filter_list: 'ubg.uc.og' }
    },
    setup() {
        return {
            table_header: ref(userTableHead),
            user_list: ref([]),
            editableData: reactive({}),
            modal_visible: ref(false),
            create_type: ref(1),
            page_obj: ref({
                current: 1,
                pageSize: 15,
                total: 100,
                sizeOptions: ['15', '30', '60']
            }),
            table_scroll: ref({ y: 0 }),
            search_orgGroup: ref({ ref_code: 0, ref_name: '全部分组' }),
            search_charater: ref({ ref_code: 0, ref_name: '全部角色' }),
            search_line: ref({ ref_code: 0, ref_name: '全部' }),
            search_keyword: ref(''),
            add_charater: ref({}),
            add_line: ref({}),
            belong_org: ref({ key: '2100001', value: '上海分行' }),
            lead_manager: ref({ key: '', value: '' }),
            user_notesid: ref(),
            user_name: ref(),
            spin_status: ref(true),
            org_searchRes: ref([]),
            org_fetching: ref(false),
            can_edit: ref(true),
            upload_file: ref({})
        }
    },
    mounted() {
        this.getFilterData(this.filter_list);
        this.getUserList()
        window.addEventListener('resize', tableScrollYResize('user_table', this.table_scroll));
    },
    methods: {
        showModal() {
            this.modal_visible = true;
        },
        cancelUpload() {
            this.modal_visible = false;
        },
        confirmUpload() {

            // 根据type判断字段校验
            if (this.create_type == 1) {
                const error_list = [];
                // 参数校验
                try {
                    const post_data = {
                        'is_multi': false,
                        'update_data': {
                            'notes_id': this.user_notesid,
                            'user_name': this.user_name,
                            'user_belong_org': valueFindKey(this.org_searchRes,this.belong_org['value'],'label','key'),
                            'user_belong_group': this.add_line,
                            'user_character': this.add_charater
                        }
                    }
                    // 赋值遍历检查，简单版本
                    for (const key in post_data.update_data) {
                        if(!post_data.update_data[key]) {
                            throw new Error({'key':key,'msg':'赋值失败,请检查'})
                        }
                    }
                    // 提交修改
                    const post_headers = {
                        'Authorization': localStorage.getItem('access')
                    };
                    console.log(post_data);
                    message.loading({
                        content:'正在创建用户,请稍后...',
                        duration:0,
                        class: 'msg_loading'
                    })
                    api.post('/api/user/createUser',post_data,{headers:post_headers}).then(
                        (response) => {
                            console.log(response);
                            message.destroy();
                            message.success({
                                content: '用户创建完成',
                                duration: 1.5,
                                class: 'msg_loading',
                                onClose: () => {
                                    this.getUserList();
                                    this.modal_visible = false;
                                }
                            })
                        }
                    ).catch(
                        (response) => {
                            console.log(response);
                            message.destroy();
                            message.error({
                                content: `'用户创建失败,'${response.data.msg}`,
                                duration: 3,
                                class: 'msg_loading',
                                onClose: () => {
                                    this.modal_visible = false;
                                }
                            })
                        }
                    )

                } catch(error) {
                    error_list.push(error);
                }
                console.log(error_list)
            } else if (this.create_type == 2) {
                // 拼接表单
                const post_data = new FormData();
                post_data.append('is_multi',true);
                post_data.append('update_file',this.upload_file);

                const post_headers = {
                        'Authorization': localStorage.getItem('access'),
                        'Content-Type': 'multipart/form-data'
                    };
                
                message.loading({
                    content:'正在提交数据,请稍后...',
                    duration: 0,
                    class: 'msg_loading'
                })
                api.post('/api/user/createUser',post_data,{headers:post_headers}).then(
                    (response) => {
                        console.log(response);
                        message.destroy();
                        message.success({
                            content:'数据提交成功',
                            duration: 1.5,
                            class: 'msg_loading',
                            onClose: () => {
                                this.getUserList();
                                this.modal_visible = false;
                            }
                        })
                    }
                ).catch(
                    (response) => {
                        console.log(response);
                        message.destroy();
                        message.error({
                            content:'数据提交失败',
                            duration: 1.5,
                            class:'msg_loading',
                            onClose: () => {
                                this.modal_visible = false;
                            }
                        })
                    }
                )

            }
            

        },
        chooseMenuItem(item, target) {
            this[target] = item
        },
        // 重置查询条件
        resetSearch() {
            this.search_orgGroup = { ref_code: 0, ref_name: '全部分组' };
            this.search_charater = { ref_code: 0, ref_name: '全部角色' };
            this.search_line = { ref_code: 0, ref_name: '全部' };
            this.search_keyword = ''
        },
        // 提交查询
        confirmSearch() {
            console.log(this.search_orgGroup, this.search_charater, this.search_line);
            this.getUserList();
        },
        // 获取用户列表
        async getUserList() {
            this.spin_status = true;
            const get_params = {
                group: this.search_line.ref_code,
                character: this.search_charater.ref_code,
                org: this.search_orgGroup.ref_code,
                client: 0,
                page: this.page_obj.current,
                size: this.page_obj.pageSize,
                ext: this.search_keyword
            }
            const get_headers = {
                'Authorization': localStorage.getItem('access')
            }
            const user_list = await api('/api/user/getUserList', { params: get_params, headers: get_headers })
            this.user_list = user_list.data.data;
            // 添加key
            this.user_list = this.user_list.map((item, index) => { return { ...item, key: index.toString() } });
            this.page_obj.total = user_list.data.data_total
            this.spin_status = false
        },
        // 获取筛选项
        async getFilterData(ref_type) {
            const get_params = { type: ref_type }
            const get_headers = {
                'Authorization': localStorage.getItem('access')
            }
            const filter_data = await api('/api/other/getFilter', { params: get_params, headers: get_headers })
            if (filter_data.data.code == 0) {
                this.org_group = filter_data.data.data.org_group
                this.character_group = filter_data.data.data.user_character
                this.group_group = filter_data.data.data.user_belong_group
            }
            // 处理character_group/org_group的全部
            this.org_group.filter((a) => { return a.ref_code == 0 })[0]['ref_name'] = '全部分组'
            this.character_group.filter((a) => { return a.ref_code == 0 })[0]['ref_name'] = '全部角色'
        },
        // 设定pageSize
        changeSizeOptions(_, size) {
            // 设定size，页数重置
            this.page_obj.pageSize = size
            this.page_obj.current = 1
            // 更新数据
            this.getUserList()
        },
        // 翻页
        changePage(page) {
            this.page_obj.current = page
            this.getUserList()
        },
        // 编辑行数据
        editTable(key) {
            this.editableData[key] = cloneDeep(this.user_list.filter(item => key === item.key)[0]);
            // console.log(this.editableData[key])
        },
        // 机构搜索
        async orgSearch(keyword) {
            const get_params = {
                level: 0,
                group: 0,
                client: 0,
                size: 10,
                ext: keyword
            };
            const get_headers = {
                'Authorization': localStorage.getItem('access')
            };
            const org_searchRes = await api('/api/org/getOrgList', { params: get_params, headers: get_headers });
            // console.log(org_searchRes);
            return org_searchRes.data;
        },
        debounceSearch: debounce(function (value) {
            this.org_fetching = true;
            if (value.length >= 2) {
                this.orgSearch(value).then((response) => {
                    if (response.code == 200) {
                        this.org_searchRes = response.data.map(obj => ({
                            label: obj.org_name,
                            key: obj.org_num,
                            value: obj.org_name
                        }))
                    }
                    this.org_fetching = false
                })
            }
        }, 750),
        // 保存表格编辑
        save(key) {
            // 文本直接赋值
            Object.assign(this.user_list.filter(item => key === item.key)[0], this.editableData[key]);
            // 根据文本调整对应的码值
            this.user_list.filter(item => key === item.key)[0]['user_character'] = valueFindKey(this.character_group, this.editableData[key]['character_name'], 'ref_name', 'ref_code')
            this.user_list.filter(item => key === item.key)[0]['user_belong_group'] = valueFindKey(this.group_group, this.editableData[key]['group_name'], 'ref_name', 'ref_code')
            // 如果机构这里没有数据的话，说明没有发起过查询，就跳过了
            if (this.org_searchRes.length !== 0) {
                this.user_list.filter(item => key === item.key)[0]['user_belong_org'] = valueFindKey(this.org_searchRes, this.editableData[key]['org_name'], 'label', 'key');
                // 清空org_searchRes
                this.org_searchRes = []
            }
            delete this.editableData[key];
            console.log(this.user_list.filter(item => key === item.key)[0])
            // 提交修改
            const post_headers = {
                'Authorization': localStorage.getItem('access')
            };
            const post_data = {
                'user': this.user_list.filter(item => key === item.key)[0]['notes_id'],
                'type': 'update',
                'update_data': {
                    'user_name': this.user_list.filter(item => key === item.key)[0]['user_name'],
                    'user_character': this.user_list.filter(item => key === item.key)[0]['user_character'],
                    'user_belong_group': this.user_list.filter(item => key === item.key)[0]['user_belong_group'],
                    'user_belong_org': this.user_list.filter(item => key === item.key)[0]['user_belong_org']
                }
            };
            console.log(post_data);
            message.loading({
                content: '提交修改,请稍后...',
                duration: 0,
                class: 'msg_loading'
            });
            this.can_edit = false;
            api.post('/api/user/updateUser', post_data, { headers: post_headers }).then(
                (response) => {
                    console.log(response);
                    message.destroy();
                    message.success({
                        content: '修改完成',
                        duration: 1.5,
                        class: 'msg_loading',
                        onClose: () => {
                            this.getUserList();
                        }
                    })
                    this.can_edit = true
                }
            ).catch(
                () => {
                    message.destroy();
                    message.error({
                        content: '提交失败,请检查网络...',
                        duration: 3,
                        class: 'msg_loading',
                        onClose: () => {
                            this.can_edit = true;
                        }
                    })
                }
            )
        },
        // 取消表格编辑
        cancel(key) {
            delete this.editableData[key];
        },
        handleFileUpload(file) {
            this.upload_file = file;
        }
    }
});

</script>