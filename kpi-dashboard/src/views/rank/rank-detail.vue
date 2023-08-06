<template>
    <div class="v-rank_detail">
        <div class="v-detail_header">
            <div class="v-detail_header-left">
                <div >
                    <a-button class="bak_btn">
                        <template #icon>
                            <icon-park type="Left" size="16" class="btn_icon" theme="outline"></icon-park>
                        </template>
                    </a-button>
                </div>
                <div class="v-detail-title">营业净收入</div>
                <div class="v-rank_tag">
                    <a-tag class="tag_magenta">财务效益</a-tag>
                </div>
                <div class="v-rank_update">
                    数据更新于:2023.12
                </div>
                <div class="v-rank_update">
                    查看方式:按区域中心支行查看
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

        </div>
    </div>
</template>

<style>
@import url('../../assets/style/overwrite.css');
@import url('../../assets/style/colorset.css');
@import url('../../assets/style/common.css');

.v-rank_detail {
    width: 100%;
    height: 100%;
    background-color: #fff;
    border-radius: 4px;
}
.v-detail_header {
    display: flex;
    justify-content: space-between;
    padding: 20px 16px 16px 20px;
    border-bottom: 1px solid var(--color-border-2);
    align-items: baseline;
}
.v-detail_header-left {
    display: inline-flex;
    gap: 12px;
    align-items: baseline;
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
    vertical-align: middle;
    width: 16px !important;
}

</style>

<script>
import { defineComponent } from 'vue';
import { IconPark } from "@icon-park/vue-next/es/all";

export default defineComponent({
    name: 'RankDetail',
    components:{
        'icon-park':IconPark
    }

});

</script>