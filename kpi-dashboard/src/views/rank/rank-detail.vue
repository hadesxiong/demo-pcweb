<template>
    <div class="w_p100 bg_white br_4 d_flex fd_c minw_p100">
        <div class="h_60 d_flex jc_sb pl_20 pr_20 pt_16 pb_16 fai_c bb_w1c2_so">
            <div class="d_iflex gap_12 fai_c lh_30">
                <div>
                    <a-button class="bak_btn">
                        <template #icon>
                            <icon-park type="Left" size="16" class="btn_icon bak_icon" theme="outline"></icon-park>
                        </template>
                    </a-button>
                </div>
                <div class="font_18 fw_500">{{ detail_data.table_title }}</div>
                <div>
                    <a-tag :class="detail_data.tag_class">{{ detail_data.tag_title }}</a-tag>
                </div>
                <a-divider type="vertical" style="height: 18px; border-color: #E5E6EB; top: 0;"></a-divider>
                <div class="fc_l3">
                    数据更新于:{{ detail_data.table_update }}
                </div>
                <div class="fc_l3">
                    查看方式:{{ detail_data.table_view }}
                </div>
            </div>
            <div class="v-detail_header-right">
                <a-button class="br_2 fai_c d_flex fc_l5 bg_brand6 mr_8">
                    <template #icon>
                        <icon-park type="Download" size="14" class="btn_icon"></icon-park>
                    </template>
                    导出</a-button>
            </div>
        </div>
        <div class="m_20 b_w1c2_so br_4 of_a h_p100">
            <a-table :columns="detail_data.table_column" :data-source="detail_data.table_data" :pagination="false"
                :scroll="{ y: 680 }" :expandIconColumnIndex="1" :expandIconAsCell="false" :indentSize="0">
                <template #innerExpand="{ record }">
                    <span v-if="record.children">
                        <!-- <a @click="toggleExpand(record)">展开</a> -->
                    </span>
                </template>
                <template #bodyCell="{ column }">
                    <template v-if="column.dataIndex === 'data_operation'">
                        <div class="fc_brand6 d_iflex gap_8">
                            <a id="history_btn" @click="showDrawer">查看历史</a>
                            <!-- <a id="belong_btn">查看下属机构</a> -->
                        </div>
                    </template>
                </template>
            </a-table>
        </div>
        <a-drawer :width="500" title="Basic Drawer" :placement="right" :visible="draw_visible" @close="onClose"
            :closable="false">
            <template #extra>
                <a-button style="margin-right: 8px" @click="onClose">Cancel</a-button>
                <a-button type="primary" @click="onClose">Submit</a-button>
            </template>
            <p>Some contents...</p>
            <p>Some contents...</p>
            <p>Some contents...</p>
        </a-drawer>
    </div>
</template>

<style>
@import url('../../assets/style/overwrite.css');
@import url('../../assets/style/colorset.css');
@import url('../../assets/style/common.css');

.btn_icon {
    margin-right: 8px;
    height: 14px;
    line-height: 14px;
}

.bak_btn {
    width: 16px !important;
}

.bak_icon {
    display: block !important;
    margin: 0 auto;
}
</style>

<script>
import { defineComponent } from 'vue';
import { IconPark } from "@icon-park/vue-next/es/all";
import axios from 'axios';

export default defineComponent({
    name: 'RankDetail',
    components: {
        'icon-park': IconPark
    },
    data() {
        return {
            detail_data: {},
            draw_visible: false,
        }
    },
    setup() {
        return {}
    },
    mounted() {
        this.getRankDetailData();
        // console.log(this.detail_data)
    },
    methods: {
        async getRankDetailData() {
            const detail_res = await axios.get('http://localhost:8080/demo/rank/rank-detail.json');
            // console.log(detail_res.data);
            this.detail_data = detail_res.data;
            this.detail_data.table_column[0].customCell = (_, index) => { if (index === 0) { return { rowSpan: 12 } } else { return { rowSpan: 0 } } }
            // console.log(this.detail_data);
        },
        async showDrawer() {
            this.draw_visible = true;
        },
        onClose() {
            this.draw_visible = false;
        }
    }

});

</script>