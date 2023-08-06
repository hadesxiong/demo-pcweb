<template>
    <div class="c-rank_list">
        <div class="c-rank_con" v-for="item in rank_list" :key="item.rank_id">
        <div class="c-rank_header">
            <div class="c-header_left">
                <div class="c-rank_title">{{ item.rank_info.data_title }}</div>
                <div class="c-rank_tag" v-for="(tag_item,index) in item.rank_info.data_tag" :key="index">
                    <a-tag :class="tag_item.tag_class">{{ tag_item.tag_title }}</a-tag>
                </div>
                <div class="c-rank_update">
                    数据更新于{{ item.rank_info.data_update }}
                </div>
            </div>
            <div class="c-header_right">
                <div class="more_btn">
                    <router-link to="/rank-important/rank-detail" class="more_btn">查看全部</router-link>
                </div>
            </div>
        </div>
        <div class="c-rank_main mt_20">
            <a-table :columns="item.rank_column" :data-source="item.rank_data" :pagination="false"></a-table>
        </div>
    </div>
    </div>
</template>

<style>
@import url('../../assets/style/colorset.css');
@import url('../../assets/style/common.css');
@import url('../../assets/style/overwrite.css');

.c-rank_list {
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
    align-items: stretch;
    flex-direction: row;
}

.c-rank_con {
    border-radius: 4px;
    border: 1px solid var(--color-border-2);
    background-color: #fff;
    width: auto;
    height: auto;
    display: flex;
    flex-direction: column;
    padding: 20px;
    /* max-width: calc(34% - 20px); */
    min-width: 520px;
    flex: 1 1 auto;
    /* flex-basis: calc(100% / 3); */
}

.c-rank_con:last-child {
    max-width: calc(50% - 10px);
}

.c-rank_header {
    display: flex;
    justify-content: space-between;
    width: 100%;
    line-height: 20px;
    font-size: 12px;
    align-items: baseline;
}

.c-header_left {
    display: inline-flex;
    gap: 12px;
    align-items: baseline;
}

.c-rank_title {
    font-size: 14px;
    font-weight: 500;
}

.c-rank_update {
    color: var(--color-text-3);
}

.more_btn {
    color: var(--brand-1-6);
}
.rank_main {
    width: 100%;
}

/* 表格覆写部分 */

.ant-table-wrapper .ant-table {
    font-size: 13px;
}

</style>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
    name: "RankMain",
    props:{
        rank_list:{
            type:Array
        }
    },
    data() {
        return {};
    },
    setup() {
        return {};
    }
});

</script>