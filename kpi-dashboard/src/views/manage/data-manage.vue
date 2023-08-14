<template>
    <div class="d_flex fd_c gap_20">
        <div class="d_flex p_20 bg_white fd_r gap_20 fai_c jc_sb">
            <div class="d_flex gap_20">
                <a-dropdown
                    class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180"
                    @click="handleClass">
                    <a>全部分类<icon-park type="Down" class="lh_1" fill="#86909C"></icon-park></a>
                    <template #overlay>
                        <a-menu>
                            <a-menu-item>全部分类</a-menu-item>
                            <a-menu-item>财务效益</a-menu-item>
                            <a-menu-item>客户建设</a-menu-item>
                            <a-menu-item>转型与质量发展</a-menu-item>
                            <a-menu-item>风险合规</a-menu-item>
                            <a-menu-item>社会责任</a-menu-item>
                        </a-menu>
                    </template>
                </a-dropdown>
                <a-dropdown
                    class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180"
                    @click="handleClass">
                    <a>全部数据<icon-park type="Down" class="lh_1" fill="#86909C"></icon-park></a>
                    <template #overlay>
                        <a-menu>
                            <a-menu-item>全部数据</a-menu-item>
                            <a-menu-item>企金数据</a-menu-item>
                            <a-menu-item>零售数据</a-menu-item>
                            <a-menu-item>同业数据</a-menu-item>
                            <a-menu-item>其他数据</a-menu-item>
                        </a-menu>
                    </template>
                </a-dropdown>
                <a-dropdown
                    class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_280 b_n">
                    <a-range-picker picker="date" :placeholder="['起始日期', '截止日期']" :allowClear="false">
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
                    <a-button type="default" class="br_2 fai_c d_flex fc_l2 bg_l2 b_n">
                        <template #icon>
                            <icon-park type="Redo" size="14" class="mr_8 lh_1"></icon-park>
                        </template>
                        重置
                    </a-button>
                    <a-button type="primary" class="br_2 fai_c d_flex fc_l5 bg_brand6">
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
        <div class="p_20 bg_white">
            <div class="b_w1c2_so br_4 of_a h_p100">
                <a-table :columns="upload_data.table_columns" :data-source="upload_data.table_data">
                    <template #bodyCell="{ column }">
                        <template v-if="column.dataIndex === 'operation'">
                            <div class="fc_brand6 d_iflex gap_8">
                                <router-link to="/data-manage/data-detail" class="fc_brand6 font_14">查看详情</router-link>
                            </div>
                        </template>
                    </template>
                </a-table>
            </div>
        </div>
    </div>
    <div class="modalCon" ref="modal">
        <a-modal v-model:open='modal_visible' width="auto" title="导入数据" @ok="confirmUpload" centered>
            <div class="d_flex fai_c pt_20 pb_10 jc_sb">
                <div class="d_flex fd_r fai_c jc_sb gap_20">
                    <div class="d_flex fai_c gap_16">
                        <div class="fc_l2 font_14 minw_60">数据分类</div>
                        <a-dropdown
                            class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180"
                            @click="handleClass">
                            <a-input v-model="inputValue" class="w_240">
                                全部分类
                                <template #suffix>
                                    <icon-park type="Down" class="lh_1" fill="#86909C"></icon-park>
                                </template>
                            </a-input>

                            <template #overlay>
                                <a-menu>
                                    <a-menu-item>全部分类</a-menu-item>
                                    <a-menu-item>财务效益</a-menu-item>
                                    <a-menu-item>客户建设</a-menu-item>
                                    <a-menu-item>转型与质量发展</a-menu-item>
                                    <a-menu-item>风险合规</a-menu-item>
                                    <a-menu-item>社会责任</a-menu-item>
                                </a-menu>
                            </template>
                        </a-dropdown>
                    </div>
                    <div class="d_flex fai_c gap_16">
                        <div class="fc_l2 font_14 minw_60">通报月份</div>
                        <a-date-picker picker="month" class="w_240" :allowClear="false">

                        </a-date-picker>
                    </div>
                </div>
            </div>
            <div class="d_flex fai_c pt_20 pb_20 jc_fs">
                <div class="d_flex fd_r fai_c jc_sb gap_20">
                    <div class="d_flex fai_c gap_16">
                        <div class="fc_l2 font_14 minw_60">导入文件</div>
                        <!-- <a-input placeholder="请上传导入文件"
                            class="b_n fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 w_180">

                        </a-input> -->
                        <file-input></file-input>
                    </div>
                    <div class="d_flex fai_c gap_16">
                        <a class="fc_brand6 font_14">下载模版</a>
                    </div>
                </div>
            </div>
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

export default defineComponent({
    name: "DataManage",
    components: {
        'icon-park': IconPark,
        'router-link': RouterLink,
        'file-input':FileInput
    },
    setup() {
        return {
            upload_data: ref({}),
            modal_visible: ref(false),
            inputValue: ref(''),
        }
    },
    mounted() {
        this.getUploadList();
    },
    methods: {
        async getUploadList() {
            const upload_res = await axios.get('http://localhost:8080/demo/manage/data-manage.json');
            this.upload_data = upload_res.data;
            // console.log(this.upload_data)
        },
        showModal() {
            this.modal_visible = true;
        },
        confirmUpload() {
            this.modal_visible = false;
        },
        handleClass(e) {
            console.log(e)
        }
    }
});

</script>