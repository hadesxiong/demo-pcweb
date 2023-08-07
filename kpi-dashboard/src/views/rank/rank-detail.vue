<template>
    <div class="v-rank_detail">
        <div class="v-detail_header">
            <div class="v-detail_header-left">
                <div>
                    <a-button class="bak_btn">
                        <template #icon>
                            <icon-park type="Left" size="16" class="btn_icon bak_icon" theme="outline"></icon-park>
                        </template>
                    </a-button>
                </div>
                <div class="v-detail-title">{{ detail_data.table_title }}</div>
                <div class="v-rank_tag">
                    <a-tag :class="detail_data.tag_class">{{ detail_data.tag_title }}</a-tag>
                </div>
                <a-divider type="vertical" style="height: 18px; border-color: #E5E6EB; top: 0;"></a-divider>
                <div class="v-rank_update">
                    数据更新于:{{ detail_data.table_update }}
                </div>
                <div class="v-rank_update">
                    查看方式:{{ detail_data.table_view }}
                </div>
            </div>
            <div class="v-detail_header-right">
                <a-button class="downbtn">
                    <template #icon>
                        <icon-park type="Download" size="14" class="btn_icon"></icon-park>
                    </template>
                    导出</a-button>
            </div>
        </div>
        <div class="v-rank_table">
            <a-table :columns="detail_data.table_column" :data-source="detail_data.table_data" :pagination=false :scroll="{y: 680}">
                <template #bodyCell="{ column }">
                    <template v-if="column.dataIndex === 'data_operation'">
                        <div class="operation_btn">
                            <a id="history_btn">查看历史</a>
                            <a id="belong_btn">查看下属机构</a>
                        </div>
                    </template>
                </template>

            </a-table>
        </div>
    </div>
</template>

<style>
@import url('../../assets/style/overwrite.css');
@import url('../../assets/style/colorset.css');
@import url('../../assets/style/common.css');

.v-rank_detail {
    width: 100%;
    height: auto;
    min-width: 100%;
    background-color: #fff;
    border-radius: 4px;
    display: flex;
    flex-direction: column;
}

.v-detail_header {
    display: flex;
    justify-content: space-between;
    padding: 20px 16px 16px 20px;
    border-bottom: 1px solid var(--color-border-2);
    align-items: center;
    height: 60px;
}

.v-detail_header-left {
    display: inline-flex;
    gap: 12px;
    align-items: center;
    line-height: 30px;
}

.v-detail-title {
    font-size: 18px;
    font-weight: 500;
}

.v-rank_update {
    color: var(--color-text-3);
}

.downbtn {
    background-color: var(--brand-1-6);
    color: var(--color-text-5);
    display: flex;
    align-items: center;
    border-radius: 2px;
}

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

.v-rank_table {
    margin: 20px;
    border: 1px solid var(--color-border-2);
    border-radius: 4px;
    overflow: auto;
    height: 100%;
}
.operation_btn {
    color: var(--brand-1-6);
    display: inline-flex;
    gap: 8px;
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
            detail_data: {}
        }
    },
    setup() {
        return {}
    },
    mounted() {
        this.getRankDetailData();
        console.log(this.detail_data)
    },
    methods: {
        async getRankDetailData() {
            const detail_res = await axios.get('http://localhost:8080/demo/rank/rank-detail.json');
            // console.log(detail_res.data);
            this.detail_data = detail_res.data;
            // console.log(this.detail_data);
        }
    }

});

</script>