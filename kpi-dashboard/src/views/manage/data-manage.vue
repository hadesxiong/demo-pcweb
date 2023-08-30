<template>
    <div class="d_flex fd_c gap_20 h_p100">
        <div class="d_flex p_20 bg_white fd_r gap_20 fai_c jc_sb">
            <div class="d_flex gap_20">
                <a-dropdown
                    class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180">
                    <a>{{ selected_class.value }}<icon-park type="Down" class="lh_1" fill="#86909C"></icon-park></a>
                    <template #overlay>
                        <a-menu>
                            <a-menu-item v-for="item in class_data" :key="item.key"
                                @click="chooseMenuItem(item, 'selected_class')">{{ item.value }}</a-menu-item>
                        </a-menu>
                    </template>
                </a-dropdown>
                <a-dropdown
                    class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180">
                    <a>{{ selected_line.value }}<icon-park type="Down" class="lh_1" fill="#86909C"></icon-park></a>
                    <template #overlay>
                        <a-menu>
                            <a-menu-item v-for="item in line_data" :key="item.key"
                                @click="chooseMenuItem(item, 'selected_line')">{{ item.value }}</a-menu-item>
                        </a-menu>
                    </template>
                </a-dropdown>
                <a-dropdown
                    class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_280 b_n">
                    <a-range-picker picker="date" :placeholder="['起始日期', '截止日期']" format="YYYY-MM-DD" :value="date_value"
                        :mode="['date', 'date']" @panelChange="handlePannelChange" @openChange="handleChange"
                        @change="datesChange" :allowClear="false">
                        <template #separator>
                            <icon-park type="RightSmall" fill="#86909C" size="14"></icon-park>
                        </template>
                        <template #suffixIcon>
                            <icon-park type="CalendarThirty" fill="#86909C" size="14"></icon-park>
                        </template>
                    </a-range-picker>
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
                            <icon-park type="Upload" size="14" class="mr_8 lh_1"></icon-park>
                        </template>
                        导入
                    </a-button>
                </div>
            </div>

        </div>
        <div class="p_20 bg_white h_p100 d_flex fd_c gap_20">
            <div class="of_a h_p100">
                <a-table :columns="upload_data.table_columns" :data-source="upload_data.table_data" :pagination="false"
                    class="b_w1c2_so br_4">
                    <template #bodyCell="{ column, record }">
                        <template v-if="column.dataIndex === 'operation'">
                            <div class="fc_brand6 d_iflex gap_8">
                                <!-- <router-link to="/data-manage/data-detail" class="fc_brand6 font_14">查看详情</router-link> -->
                                <router-link :to="{ name: 'data-detail', params: { data_id: record.upload_num } }"
                                    class="fc_brand6 font_14">查看详情</router-link>
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
        <a-modal v-model:open='modal_visible' width="auto" title="导入数据" :closable="false" centered>
            <div class="d_flex fai_c pt_20 pb_10 jc_sb">
                <div class="d_flex fd_r fai_c jc_sb gap_20">
                    <div class="d_flex fai_c gap_16">
                        <div class="fc_l2 font_14 minw_60">条线分类</div>
                        <a-dropdown
                            class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180">
                            <a-input :value="update_line.value" class="w_240">
                                <template #suffix>
                                    <icon-park type="Down" class="lh_1" fill="#86909C"></icon-park>
                                </template>
                            </a-input>
                            <template #overlay>
                                <a-menu>
                                    <a-menu-item v-for="item in line_data" :key="item.key"
                                        @click="chooseMenuItem(item, 'update_line')">{{ item.value }}</a-menu-item>
                                </a-menu>
                            </template>
                        </a-dropdown>
                    </div>
                    <div class="d_flex fai_c gap_16">
                        <div class="fc_l2 font_14 minw_60">通报月份</div>
                        <a-date-picker picker="month" class="w_240" :allowClear="false" format="YYYY-MM" :value="file_date"
                            @change="dateChange"></a-date-picker>
                    </div>
                </div>
            </div>
            <div class="d_flex fai_c pt_20 pb_20 jc_fs">
                <div class="d_flex fd_r fai_c jc_sb gap_20">
                    <div class="d_flex fai_c gap_16">
                        <div class="fc_l2 font_14 minw_60">导入文件</div>
                        <file-input></file-input>
                    </div>
                    <div class="d_flex fai_c gap_16">
                        <a class="fc_brand6 font_14">下载模版</a>
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
</style>

<style scoped>
.ant-btn-default:not(:disabled):hover {
    border-color: #165dff;
    color: #165dff;
}

.ant-btn .ant-btn-default {
    border-radius: 2px !important;
}
</style>

<script>
import { defineComponent, ref } from 'vue';
import { IconPark } from '@icon-park/vue-next/es/all';
import axios from 'axios';
import { RouterLink } from 'vue-router';
import FileInput from '../../components/other/file-input.vue';

import dayjs from 'dayjs';
import 'dayjs/locale/zh-cn';
import locale from 'ant-design-vue/es/date-picker/locale/zh_CN';

dayjs.locale('zh-cn');

export default defineComponent({
    name: "DataManage",
    components: {
        'icon-park': IconPark,
        'router-link': RouterLink,
        'file-input': FileInput
    },
    setup() {
        return {
            locale,
            upload_data: ref({}),
            modal_visible: ref(false),
            inputValue: ref(''),
            class_data: ref([]),
            selected_class: ref({ key: 'all', value: '全部分类' }),
            line_data: ref([]),
            selected_line: ref({ key: 'all', value: '全部指标' }),
            page_obj: ref({ current: 1, pageSize: 10, total: 100 }),
            date_value: ref([dayjs().add(-1, 'month'), dayjs()]),
            file_date: ref(dayjs()),
            update_line: ref({ key: 'all', value: '全部指标' })
        }
    },
    mounted() {
        this.getUploadList();
        this.getFilterData();
    },
    methods: {
        async getFilterData() {
            const filter_res = await axios.get('/demo/filter/normal_filter.json');
            this.class_data = filter_res.data.class_data;
            this.line_data = filter_res.data.line_data;
        },
        async getUploadList() {
            const upload_res = await axios.get('/demo/manage/data-manage.json');
            this.upload_data = upload_res.data;
            // console.log(this.upload_data)
        },
        showModal() {
            this.modal_visible = true;
        },
        cancelUpload() {
            this.modal_visible= false;
        },
        confirmUpload() {
            this.modal_visible = false;
        },
        handlePageChange(page) {
            console.log(page)
            this.page_obj.current = page
        },
        handlePannelChange(value, mode) {
            console.log(value, mode)
            this.date_value = value;
        },
        handleChange(status) {
            console.log(status);
        },
        datesChange(dates) {
            console.log(dates);
            this.date_value = dates;
        },
        dateChange(date) {
            console.log(date);
            this.file_date = date;
        },
        chooseMenuItem(item, target) {
            this[target] = item
        },
        resetSearch() {
            this.selected_class = { key: 'all', value: '全部分类' };
            this.selected_line = { key: 'all', value: '全部指标' };
            this.date_value = [dayjs().add(-1, 'month'), dayjs()]
        },
        confirmSearch() {
            console.log(this.selected_class, this.selected_line, this.date_value)
        }
    }
});

</script>