<template>
    <div class="w_p100 bg_white br_4 d_flex fd_c minw_p100 h_p100">
        <div class="h_60 d_flex jc_sb pl_20 pr_20 pt_20 pb_20 fai_c bb_w1c2_so">
            <div class="d_iflex gap_12 fai_c lh_30">
                <div>
                    <a-button class="bak_btn" @click="goBack">
                        <template #icon>
                            <icon-park type="Left" size="16" class="btn_icon bak_icon" theme="outline"></icon-park>
                        </template>
                    </a-button>
                </div>
                <div class="font_18 fw_500">{{ detail_data.detail_id }}</div>
                <div>
                    <a-tag :class="detail_data.tag_class">{{ detail_data.tag_name }}</a-tag>
                </div>
                <a-divider type="vertical" style="height: 18px; border-color: #E5E6EB; top: 0;"></a-divider>
                <div class="fc_l3 d_flex">
                    <div class="fc_l2">{{ detail_data.data_month }}</div>数据
                </div>
                <div class="fc_l3 d_flex">
                    由<div class="fc_l2">{{ detail_data.exec_user }}</div>
                </div>
                <div class="fc_l3 d_flex">
                    于<div class="fc_l2">{{ detail_data.detail_update }}</div>导入
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
                <a-button class="br_2 fai_c d_flex fc_l5 bg_warn6">
                    <template #icon>
                        <icon-park type="Upload" size="14" class="btn_icon"></icon-park>
                    </template>
                    上传</a-button>
                <a-button class="br_2 fai_c d_flex fc_l5 bg_brand6">
                    <template #icon>
                        <icon-park type="Send" size="14" class="btn_icon"></icon-park>
                    </template>
                    发布</a-button>
            </div>
        </div>
        <div class=" d_flex fd_c m_20 br4 of_a h_p100 ">
            <a-tabs v-model:activeKey="active_tab" tab-position="top" class="h_p100">
                <a-tab-pane key="data_table" tab="数据详情" class="h_p100 d_flex fd_c gap_20">
                    <div class="of_a h_p100">
                        <a-table :columns="detail_data.table_columns" :data-source="detail_data.table_data"
                            :pagination="false" class="b_w1c2_so br_4"></a-table>
                    </div>
                    <div class="d_flex fai_c jc_fe">
                        <a-pagination :current="cur_page_obj.current" :total="cur_page_obj.total"
                            :pageSize="cur_page_obj.pageSize" @change="(page,pageSize) => handlePageChange(page, pageSize,'cur')"></a-pagination>
                    </div>
                </a-tab-pane>
                <a-tab-pane key="data_history" tab="历史记录" class="h_p100 d_flex fd_c gap_20">
                    <div class="of_a h_p100">
                        <a-table :columns="detail_data.history_columns" :data-source="detail_data.history_data"
                            :pagination="false" class="b_w1c2_so br_4">
                            <template #bodyCell="{ record, column, text }">
                                <template v-if="record.isthis_publish && column.dataIndex == 'exec_date'">
                                    <div class="d_iflex gap_16 fai_c">
                                        {{ text }}
                                        <div class="fc_brand6 fw_500">
                                            #当前发布版本
                                        </div>
                                    </div>
                                </template>
                                <template v-if="column.dataIndex == 'exec_files'">
                                    <div class="d_iflex fai_c jc_sb w_p100">
                                        <a :href="record.files_link">{{ text }}</a>
                                        <a :href="record.files_link"><icon-park type="Download"
                                                fill="#165fdd"></icon-park></a>
                                    </div>
                                </template>
                            </template>

                        </a-table>
                    </div>
                    <div class="d_flex fai_c jc_fe">
                        <a-pagination :current="his_page_obj.current" :total="his_page_obj.total"
                            :pageSize="his_page_obj.pageSize" @change="(page,pageSize) => handlePageChange(page, pageSize,'his')"></a-pagination>
                    </div>
                </a-tab-pane>
            </a-tabs>
        </div>
    </div>
</template>

<style>
@import url('../../assets/style/common.css');
@import url('../../assets/style/colorset.css');
@import url('../../assets/style/overwrite.css');
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

:where(.css-dev-only-do-not-override-eq3tly).ant-tabs .ant-tabs-content {
    height: 100% !important;
}

</style>

<script>
import { defineComponent, ref } from 'vue';
import { IconPark } from '@icon-park/vue-next/es/all';
import axios from 'axios';

export default defineComponent({
    name: "DataDetail",
    components: {
        'icon-park': IconPark
    },
    setup() {
        return {
            active_tab: ref('data_table'),
            detail_data: ref({}),
            cur_page_obj: ref({
                current: 1,
                pageSize: 10,
                total: 100
            }),
            his_page_obj: ref({
                current: 1,
                pageSize: 10,
                total: 100
            }),
        }
    },
    mounted() {
        this.getDataAll();
    },
    methods: {
        async getDataAll() {
            const dataAll_res = await axios.get('http://localhost:8080/demo/manage/data-detail.json')
            // console.log(dataAll_res.data);
            this.detail_data = dataAll_res.data
        },
        goBack() {
            this.$router.go(-1)
        },
        handlePageChange(page,pageSize,type) {
            if(type=='cur') {
                this.cur_page_obj.current = page
            } else if(type=='his') {
                this.his_page_obj.current = page
            }
        }
    }
});

</script>