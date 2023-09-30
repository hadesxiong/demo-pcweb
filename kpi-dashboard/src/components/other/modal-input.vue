<template>
    <!-- <div class="h_p100"> -->
        <a-modal v-model:open="modal_visible" :width="660" :title="modal_title" centered :closable="false" :maskClosable="false">
            <div class="d_flex fai_c pt_20 jc_sb" v-if="group_info.need_show">
                <div class="d_flex fd_r fai_c jc_sb gap_20 w_p100">
                    <div class="d_flex fai_c gap_16">
                        <div class="fc_l2 font_14 minw_60">{{ group_info.label }}</div>
                        <a-radio-group v-model:value="radio_group" @change="changeRadio">
                            <a-radio v-for="item in group_info.data" :value="item.key" :key="item.key">{{ item.label }}</a-radio>
                        </a-radio-group>
                    </div>
                </div>
            </div>
            <a-row :gutter="[20,]" :wrap="true" justify="space-between" class="pt_30">
                <a-col :span="12" v-for="(item,index) in modal_data.form_list" :key="index" class="wp_100">
                    <div class="d_flex fai_c gap_16 w_p100 fg_1 pb_30" v-if="item.group===radio_group">
                        <div class="fc_l2 font_14 minw_60">{{ item.label }}</div>
                        <div v-if="item.type==='input'" class="d_flex fg_1">
                            <a-input v-model:value="form_data[item.dataIndex]"
                                class="d_flex jc_sb fai_c bg_l2 br_2 b_n ta_l h_30 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100">
                            </a-input>
                        </div>
                        <div v-else-if="item.type ==='select'" class="d_flex fg_1">
                            <menu-input :cp_data="{menu_data:item.option,menu_key:{code:'ref_code',label:'ref_name'},select_title:item.dataIndex}" class="w_p100" @menu-select="handleMenuSelect"></menu-input>
                        </div>
                        <div v-else-if="item.type==='search'" class="d_flex fg_1">
                            <search-input class="wp_100 font-14" :res_map="item.search_map.in" :api_info="item.search_func" :target_title="item.dataIndex" @search-select="handleSearchInput"></search-input>
                        </div>
                        <div v-else-if="item.type==='show-only'" class="d_flex fg_1">
                            <a-input v-model:value="form_data[item.dataIndex]" :disabled="true"
                                class="d_flex jc_sb fai_c bg_l2 br_2 b_n ta_l h_30 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100">
                            </a-input>
                        </div>
                        <div v-else-if="item.type==='file'" class="d_flex fg_1">
                            <file-input @file-upload="handleFileUpload" class="w_p100"></file-input>
                        </div>
                        <div v-else-if="item.type==='date-month'" class="d_flex fg_1">
                            <a-date-picker picker="month" class="w_a fg_1" :allowClear="false" format="YYYY-MM"
                                :value="form_data[item.dataIndex]" @change="dateChange(item.dataIndex,$event)" placeholder="请选择数据通报月份">
                            </a-date-picker>
                        </div>
                    </div>
                </a-col>
            </a-row>
            <template #footer>
                <div class="d_flex jc_fe gap_8">
                    <a-button type="default" class="br_2 fai_c d_flex fc_l2 bg_l2 b_n" @click="cancelModal">
                        <template #icon>
                            <icon-close size="14" class="mr_8 lh_1"></icon-close>
                        </template>
                        取消
                    </a-button>
                    <a-button type="primary" class="br_2 fai_c d_flex fc_l5 bg_brand6" @click="confirmModal">
                        <template #icon>
                            <icon-check size="14" class="mr_8 lh_1"></icon-check>
                        </template>
                        提交
                    </a-button>
                </div>
            </template>
        </a-modal>
    <!-- </div> -->
</template>

<style>
@import url('@/assets/style/common.css');
@import url('@/assets/style/colorset.css');
@import url('@/assets/style/overwrite.css');
</style>

<style scoped>
span {
    font-size: 14px !important;
}
.ant-picker:hover, .ant-picker-focused {
    border-color: transparent;
}
</style>

<script>
import { defineComponent, ref, watch } from 'vue';
import { Col, Row, Modal, RadioGroup, Radio, Input, Button, DatePicker, message } from 'ant-design-vue';
import { Close, Check } from '@icon-park/vue-next';

import MenuInput from '@/components/other/menu-input.vue';
import SearchInput from '@/components/other/search-input.vue';
import FileInput from '@/components/other/file-input.vue';

export default defineComponent({
    name: 'ModalInput',
    components: {
        'a-col': Col,
        'a-row': Row,
        'a-modal': Modal,
        'a-radio-group': RadioGroup,
        'a-radio': Radio,
        'a-input': Input,
        'a-button': Button,
        'a-date-picker': DatePicker,
        'menu-input': MenuInput,
        'search-input': SearchInput,
        'file-input': FileInput,
        'icon-close': Close,
        'icon-check': Check
    },
    props: {
        modal_obj: {type:Object,default:()=>{return {}}},
        visible: {type:Boolean,default: false}
    },
    setup(props) {

        const modal_visible = ref(props.visible);
        watch(props,()=>{modal_visible.value = props.visible});

        return {
            modal_visible,
            modal_title: ref(props.modal_obj.title),
            modal_data: ref(props.modal_obj.data),
            group_info: ref(props.modal_obj.data.group_info),
            radio_group: ref(props.modal_obj.data.group_info.data[0].key),
            form_data: ref({})
        }
    },
    mounted() {
        this.initFormData();
    },
    methods:{
        // 选项菜单获取初始值填入form_data
        initFormData() {
            this.modal_data.form_list.forEach((item)=>{
                if(item.type == 'select') {
                    this.form_data[item.dataIndex] = item.option[0]
                }
            })
        },
        // 切换radio时清除表单
        changeRadio() {
            this.form_data = {}
        },
        handleFileUpload(file) {
            this.form_data.upload_file = file;
        },
        handleMenuSelect(value) {
            this.form_data[value.title] = value.data;
        },
        handleSearchInput(value) {
            // 判断title有没有存在过，没有的话则保存用于遍历
            if(!(value.title in this.form_data)) {
                this.form_data[value.title] = value.data
            }
        },
        cancelModal() {
            this.$emit('modal-confirm',{type:1})
            Object.keys(this.form_data).forEach(key => delete this.form_data[key]);
            console.log(this.form_data)
        },
        confirmModal() {
            this.form_data.type = this.radio_group
            // 检查字段，如果不存在则无法提交
            const dataIndex_list = this.modal_data.form_list.filter(item => (item.group == this.radio_group && item.required)).map(item => item.dataIndex)
            if (dataIndex_list.every(field => field in this.form_data)) {
                this.$emit('modal-confirm',{type:2,data:this.form_data})
                Object.assign({},this.form_data)
            } else {
                console.log(dataIndex_list)
                message.error({content:'请检查录入参数',duration:2,class:'msg_loading'})
            }
            
        },
        dateChange(title,value) {
            this.form_data[title] = value
            console.log(this.form_data)
        }
    }
})

</script>