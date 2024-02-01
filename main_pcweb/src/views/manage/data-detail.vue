<template>
    <div class="w_p100 bg_white br_4 d_flex fd_c minw_p100 h_p100">
        <div class="h_60 d_flex jc_sb pl_20 pr_20 pt_20 pb_20 fai_c bb_w1c2_so">
            <div class="d_iflex gap_12 fai_c lh_30">
                <div>
                    <a-button class="bak_btn" @click="goBack"><template #icon><icon-left size="16" class="btn_icon bak_icon" theme="outline"></icon-left></template></a-button>
                </div>
                <div class="font_18 fw_500">{{ data_id }}</div>
                <div><a-tag :class="detail_data.tag_class">{{ detail_data.info.class_name }}数据</a-tag></div>
                <a-divider type="vertical" style="height: 18px; border-color: #E5E6EB; top: 0;"></a-divider>
                <div class="fc_l3 d_flex"><div class="fc_l2">{{ detail_data.info.record_dt }}</div></div>
                <div class="fc_l3 d_flex gap_4">由<div class="fc_l2">{{ detail_data.info.user_name }}</div></div>
                <div class="fc_l3 d_flex gap_4">
                    于<div class="fc_l2">{{ detail_data.info.record_update_time }}</div>导入
                </div>
                <div v-if="detail_data.now_status" class="d_flex gap_8 fai_c">
                    <div class="green_dot"></div>
                    <div class="fc_success6 fw_500">当前数据已发布</div>
                </div>
                <div v-else class="d_flex gap_8 fai_c">
                    <div class="red_dot"></div>
                    <div class="fc_danger6 fw_500">当前数据未发布</div>
                </div>
            </div>
            <div class="d_flex gap_20">
                <a-upload :show-upload-list="false" :before-upload="beforeUpload" :on-success="onSuccess" v-model="upload_file">
                    <a-button class="br_2 fai_c d_flex fc_l5 bg_warn6">
                        <template #icon>
                            <icon-upload size="14" class="btn_icon"></icon-upload>
                        </template>
                        上传</a-button>
                </a-upload>
                <a-button class="br_2 fai_c d_flex fc_l5 bg_brand6">
                    <template #icon>
                        <icon-send size="14" class="btn_icon"></icon-send>
                    </template>
                    发布</a-button>
            </div>
        </div>
        <div class=" d_flex fd_c m_20 br4 of_a h_p100 ">
            <a-spin :spinning="spin_status" size="large" :delay="100" tip="数据加载中">
                <a-tabs v-model:activeKey="active_tab" tab-position="top" class="h_p100">
                <a-tab-pane key="data_table" tab="数据详情" class="h_p100 d_flex fd_c gap_20">
                    <div class="ofy_h h_p100" id="data_table">
                        <a-table :columns="detail_data.title" :data-source="detail_data.index"
                            :pagination="false" class="b_w1c2_so br_4"></a-table>
                    </div>
                </a-tab-pane>
                <a-tab-pane key="data_history" tab="历史记录" class="h_p100 d_flex fd_c gap_20">
                    <div class="ofy_h h_p100 fg_1" id="data_history">
                        <a-table :columns="histroy_data.title" :data-source="histroy_data.index"
                            :pagination="false" class="b_w1c2_so br_4" :scroll="table_scroll">
                            <template #bodyCell="{ record, column, text }">
                                <template v-if="record.detail_active == 1 && column.dataIndex == 'detail_update'">
                                    <div class="d_iflex gap_16 fai_c">
                                        {{ text }}
                                        <div class="fc_brand6 fw_500">
                                            #当前发布版本
                                        </div>
                                    </div>
                                </template>
                                <template v-if="column.dataIndex == 'detail_update_fileName'">
                                    <div class="d_iflex fai_c jc_sb w_p60">
                                        <a :href="record.files_link" class="fc_brand6">{{ text }}</a>
                                        <a :href="record.files_link"><icon-download fill="#165fdd" class="d_flex"></icon-download></a>
                                    </div>
                                </template>
                            </template>

                        </a-table>
                    </div>
                </a-tab-pane>
            </a-tabs> 
            </a-spin>

        </div>
    </div>
</template>

<style>
@import url('@/assets/style/common.css');
@import url('@/assets/style/colorset.css');
@import url('@/assets/style/overwrite.css');
</style>

<style scoped>
.btn_icon {
    margin-right: 8px;
    height: 14px;
    line-height: 1px;
}

.bak_btn {
    width: 16px !important;
}

.bak_icon {
    display: block !important;
    margin: 0 auto;
}

.green_dot {
    width: 10px;
    height: 10px;
    border-radius: 10px;
    background-color: #00b42a;
    border: 2px solid #e8ffea;
}

.red_dot {
    width: 10px;
    height: 10px;
    border-radius: 10px;
    background-color: #f53f3f;
    border: 2px solid #ffece8;
}

.ant-tabs .ant-tabs-content {
    height: 100% !important;
}
.ant-tag {
    line-height: 24px;
    margin-inline-end: 0px;
}
</style>

<script>
import { defineComponent, ref } from 'vue';
import { Left, Upload as IconUpload, Send, Download } from '@icon-park/vue-next';
import { Button, Tag, Upload, Tabs, TabPane, Table, Divider, Spin } from 'ant-design-vue';

import { api } from '@/utils/commonApi.js';
import { tableScrollYResize } from '@/utils/tableScrollYResize.js';
import { detailTableHead } from '@/assets/config/data-detail.js';
import { recordClassMap } from '@/assets/config/tag-map.js';
import { useRoute } from 'vue-router';

const myApi = api();

export default defineComponent({
    name: "DataDetail",
    components: {
        'icon-left': Left,
        'icon-upload': IconUpload,
        'icon-send': Send,
        'icon-download': Download,
        'a-button': Button,
        'a-tag': Tag,
        'a-upload': Upload,
        'a-tabs': Tabs,
        'a-tab-pane': TabPane,
        'a-table': Table,
        'a-divider': Divider,
        'a-spin': Spin
    },
    setup() {
        const route = useRoute();
        
        return {
            data_id: ref(route.params.data_id),
            active_tab: ref('data_table'),
            detail_data: ref({
                info:ref({}),
                detail:ref([]),
                title:ref([]),
            }),
            histroy_data: ref({
                title: ref(detailTableHead),
                index: ref([])
            }),
            tag_map:ref(recordClassMap),
            table_scroll: ref({ y: 550 }),
            is_mounted: ref(false),
            upload_file: ref(),
            spin_status: ref(false)
        }
    },
    mounted() {
        this.getUploadDetail();
        // window.addEventListener('resize',()=>{
        //     tableScrollYResize('detail_con',this.table_scroll)
        // });
        window.addEventListener('resize',()=>{
            tableScrollYResize(this.active_tab,this.table_scroll)
        });
    },
    methods: {
        goBack() {
            this.$router.go(-1)
        },
        async beforeUpload(file) {
            // loading启动
            this.spin_status = true;
            // 在上传之前的处理逻辑，例如限制文件类型和大小
            // 返回 false 可以取消上传
            this.upload_file = file

            const upload_form = new FormData();
            upload_form.append('class',this.detail_data.info.record_class)
            upload_form.append('date',this.detail_data.info.record_date)
            upload_form.append('user',localStorage.getItem('notes_id'))
            upload_form.append('file',file)

            const post_headers = {'Content-Type': 'multipart/form-data'}
            const upload_res = await myApi.post('/api/upload/createUpload',upload_form,{headers:post_headers})
            console.log(upload_res)

            // loding结束
            this.spin_status = false;
        },
        onSuccess(file) {
            // 上传成功后的处理逻辑
            console.log(file)
        },
        // 获取明细
        async getUploadDetail() {
            // Loading 启动
            this.spin_status = true;
            // 主逻辑
            const detail_list = await myApi.get('/api/upload/getUploadDetail',{params:{record:this.data_id}});
            this.detail_data.info = detail_list.data.data.info
            this.detail_data.title = detail_list.data.data.title
            this.detail_data.index = detail_list.data.data.index
            this.histroy_data.index = detail_list.data.data.detail
            this.detail_data.tag_class = this.tag_map[detail_list.data.data.info.record_class].tag_class;
            // loading结束
            this.spin_status = false
        }
    }
});

</script>