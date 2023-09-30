<template>
    <div class="d_flex fd_c gap_20 h_p100 w_p100">
        <div class="d_flex p_20 bg_white gap_20 fai_c w_p100 jc_sb">
            <a-row :gutter="[20,20]" class="fwrap_n w_p100">
                <!-- <a-col :span="4"><menu-input :cp_data="index_option" @menu-select="handleMenuSelect"></menu-input></a-col> -->
                <a-col :span="4"><menu-input :cp_data="line_option" @menu-select="handleMenuSelect"></menu-input></a-col>
                <a-col :span="6">
                    <a-dropdown class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 b_n">
                        <a-range-picker picker="date" :placeholder="['起始日期', '截止日期']" format="YYYY-MM-DD"
                            :value="search_form.date_range" :mode="['date', 'date']" @panelChange="handlePannelChange"
                            @openChange="handleChange" @change="datesChange" :allowClear="false">
                            <template #separator>
                                <icon-right fill="#86909C" size="14"></icon-right>
                            </template>
                            <template #suffixIcon>
                                <icon-calender fill="#86909C" size="14"></icon-calender>
                            </template>
                        </a-range-picker>
                    </a-dropdown>
                </a-col>
                <a-col :span="8">                
                    <a-input v-model:value='search_form.key_word' placeholder="输入导入人信息或者导入编号进行搜索"
                        class="fai_c bg_l2 br_2  ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no b_n">
                        <template #suffix><icon-search size="14" class="mr_8 lh_1"></icon-search></template>
                    </a-input>
                </a-col>
            </a-row>
            <div class="d_flex gap_20 fai_c">
                <a-divider type="vertical" style="height: 18px; border-color: #E5E6EB; top: 0;"></a-divider>
                <a-button type="default" class="br_2 fai_c d_flex fc_l2 bg_l2 b_n" @click="resetSearch">
                    <template #icon><icon-redo size="14" class="mr_8 lh_1"></icon-redo></template>
                    重置
                </a-button>
                <a-button type="primary" class="br_2 fai_c d_flex fc_l5 bg_brand6" @click="confirmSearch">
                    <template #icon><icon-search size="14" class="mr_8 lh_1"></icon-search></template>
                    查询
                </a-button>
                <a-button type="primary" class="br_2 fai_c d_flex fc_l5 bg_brand6" @click="showModal">
                    <template #icon><icon-upload size="14" class="mr_8 lh_1"></icon-upload></template>
                    导入
                </a-button>
            </div>
        </div>
        <div class="d_flex p_20 bg_white gap_20 fd_c h_p100">
            <edit-table :table_obj="table_obj" :status="status" :editable="can_edit" @table-edit="handleTableEdit"></edit-table>
            <div class="d_flex fai_c jc_fe">
                <a-pagination :current="page_obj.current" :total="page_obj.total" :pageSize="page_obj.size"
                    :pageSizeOptions="page_obj.sizeOptions" @change="changePage"
                    @showSizeChange="changeSizeOptions"></a-pagination>
            </div>
        </div>   
    </div>
    <div class="modal_con">
        <modal-input :modal_obj="modal_obj" :visible="visible" @modal-confirm="handleModalConfirm"></modal-input>
    </div>
</template>

<style>
@import url('@/assets/style/common.css');
@import url('@/assets/style/colorset.css');
@import url('@/assets/style/overwrite.css');
</style>

<style scoped>
.ant-picker:hover, .ant-picker-focused {
    border-color: transparent;
}
</style>

<script>
import { defineComponent, ref } from 'vue';
import { Col, Row, Input, Divider, Button, Pagination, RangePicker, Dropdown, message } from 'ant-design-vue';
import { RightSmall, CalendarThirty, Redo, Search as SearchIcon, Upload as UploadIcon } from '@icon-park/vue-next';

import MenuInput from '@/components/other/menu-input.vue';
import ModalInput from '@/components/other/modal-input.vue';
import EditTable from '@/components/manage/edit-table.vue';

import dayjs from 'dayjs';
import 'dayjs/locale/zh-cn';
import locale from 'ant-design-vue/es/date-picker/locale/zh_CN';

import { api } from '@/utils/commonApi.js';
import { dataTableHead, dataImportModal, dataViewMap } from '@/assets/config/data-manage.js';

const myApi = api();

export default defineComponent({
    name:'DataManage',
    components: {
        'menu-input': MenuInput,
        'edit-table': EditTable,
        'modal-input': ModalInput,
        'a-col': Col,
        'a-row': Row,
        'a-input': Input,
        'a-divider': Divider,
        'a-button': Button,
        'a-pagination': Pagination,
        'a-range-picker': RangePicker,
        'a-dropdown': Dropdown,
        'icon-search': SearchIcon,
        'icon-redo': Redo,
        'icon-upload': UploadIcon,
        'icon-right': RightSmall,
        'icon-calender': CalendarThirty,
    },
    data() {return {}},
    setup() {
        return {
            locale,
            // index_option: ref({menu_data:[{ref_code:0,ref_name:'全部'}],menu_key:{code:'ref_code',label:'ref_name'},select_title:'index_option'}),
            line_option: ref({menu_data:[{ref_code:0,ref_name:'全部'}],menu_key:{code:'ref_code',label:'ref_name'},select_title:'line_option'}),
            search_form: ref({
                // index_option: {ref_code:0,ref_name:'全部'},
                line_option: {ref_code:0,ref_name:'全部'},
                date_range: ref([dayjs().add(-1, 'month'), dayjs()]),
                key_word:''
            }),
            page_obj:ref({current:1,size:15,total:100,sizeOptions:['15', '30', '60']}),
            table_obj: ref({
                columns: ref(dataTableHead),
                data: ref([]),
                editIndex: ref([]),
                editMap: ref([]),
                search_obj: ref({}),
                viewMap:ref(dataViewMap)
            }),
            status: ref(false),
            can_edit: ref(true),
            modal_obj: ref({title:'新增导入数据',data:ref(dataImportModal)}),
            visible: ref(false)
        }
    },
    mounted() {
        myApi.get('/api/other/getFilter',{params:{type:'bl'}}).then(
            (response) => {
                // this.index_option.menu_data = response.data.data.index_class.filter( item => item.ref_code <= 5),
                this.line_option.menu_data = response.data.data.belong_line
            }
        );
        this.getUploadList();
    },
    methods: {
        // 接收menuSelect带来的参数
        handleMenuSelect(value) {
            this.search_form[value.title] = value.data;
        },
        handleTableEdit(value) {
            console.log(value)
        },
        // 日期面板调整
        handlePannelChange(value, mode) {
            console.log(value, mode)
            this.date_value = value;
        },
        handleChange(status) {
            console.log(status);
        },
        datesChange(dates) {
            console.log(dates);
            this.search_form.date_range = dates;
        },
        // 重置查询条件
        resetSearch() {
            this.search_form = {
                index_option: {ref_code:0,ref_name:'全部'},
                line_option: {ref_code:0,ref_name:'全部'},
                key_word: ''
            }
        },
        // 展示新增表单
        showModal() {
            this.visible = true
        },
        // 提交查询
        confirmSearch() {
            // console.log(this.search_form);
            this.getUploadList();
        },
        // 翻页
        changePage(page) {
            this.page_obj.current = page
            this.getUploadList()
        },
        // 设定pageSize
        changeSizeOptions(_, size) {
            // 设定size，页数重置
            this.page_obj.size = size;
            this.$nextTick(()=>{
                this.page_obj.current = 1;
                this.getUploadList();
            })
        },
        handleModalConfirm(value) {
            if (value.type == 2) {
                const post_data = new FormData();
                post_data.append('class',value.data.class_name.ref_code);
                const new_date = dayjs(value.data.record_dt).endOf('month').format('YYYY-MM-DD')
                post_data.append('date',new_date);
                post_data.append('file',value.data.upload_file);
                post_data.append('user',localStorage.getItem('notes_id'))
                const post_headers = {'Content-Type': 'multipart/form-data'}
                message.loading({content:'正在上传数据...',duration:0,class:'msg_loading'});
                myApi.post('/api/upload/createUpload',post_data,{headers:post_headers}).then(
                    () => {
                        message.destroy();
                        message.success({content:'上传数据成功.',duration:1.5,class:'msg_loading',onClose:()=>{this.getUploadList()}})
                    }
                ).catch(
                    (response) => {
                        message.destroy();
                        message.error({content:`'上传失败,'${response.data.msg}`,duration:2,class:'msg_loading'})
                    }
                )
            }
            this.visible = !this.visible;
        },
        async getUploadList() {
            // loading开始
            this.status = true;
            // 主逻辑
            const get_params = {
                class: this.search_form.line_option.ref_code,
                start: dayjs(this.search_form.date_range[0]).format('YYYY-MM-DD'),
                end: dayjs(this.search_form.date_range[1]).format('YYYY-MM-DD'),
                key: this.search_form.key_word,
                client:0
                // date:
            }
            const upload_list = await myApi.get('/api/upload/getUploadList',{params:get_params})
            // 组装table_obj
            this.table_obj.data = upload_list.data.data;
            // 为data添加key
            if (this.table_obj.data) {
                this.table_obj.data = this.table_obj.data.map((item, index) => { return { ...item, key: index.toString() } });
                // 添加查看详情
                this.table_obj.data = this.table_obj.data.map((item) => {return {...item,view_more:'查看详情'}})
            }
            this.page_obj.total = upload_list.data.data_total
            // loading结束
            this.status = false;
        }
    }
})

</script>