<template>
    <a-collapse :bordered="false" :activeKey="activePannel">
        <template #expandIcon="{ isActive }">
            <caret-right-outlined :rotate="isActive ? 90 : 0" />
        </template>
        <a-collapse-panel key="enterprise">
            <template #header>
                <div class="d_flex fai_c gap_16">
                    <div class="fc_l2 font_16 fw_500">企金指标</div>
                    <div class="fc_l3 font_14">共24个</div>
                </div>
            </template>
            <div style="padding: 0px !important;">
                <a-row :gutter="[20, 20]" :wrap="true" justify="start">
                    <a-col :md="24" :lg="24" :xl="12" :xxl="8" :xxxl="6" v-for="item in rank_list" :key="item.rank_id">
                        <div class="d_flex fd_c bg_white br_4 c-rank_con p_20 b_w1c2_so">
                            <div class="d_flex jc_sb w_p100 lh_20 fai_b ws_no ">
                                <div class="d_iflex gap_12 fai_c ta_l">
                                    <div class="font_14 fw_500 tover_ell of_h">{{ item.rank_info.data_title }}</div>
                                    <div v-for="(tag_item, index) in item.rank_info.data_tag" :key="index">
                                        <a-tag :class="tag_item.tag_class">{{ tag_item.tag_title }}</a-tag>
                                    </div>
                                    <!-- <div class="fc_l3">
                                        数据更新于{{ item.rank_info.data_update }}
                                    </div> -->
                                </div>
                                <div>
                                    <div class="fc_brand6">
                                        <!-- <router-link to="/rank-important/rank-detail" class="more_btn">查看全部</router-link> -->
                                        <router-link :to="{name:'rank-detail',params:{rank_id:item.rank_id}}" class="more_btn">查看全部</router-link>
                                    </div>
                                </div>
                            </div>
                            <div class="w_p100 mt_20">
                                <a-table :columns="item.rank_column" :data-source="item.rank_data"
                                    :pagination="false"></a-table>
                            </div>
                        </div>
                    </a-col>
                </a-row>
            </div>
        </a-collapse-panel>
    </a-collapse>
</template>

<style>
:where(.css-dev-only-do-not-override-eq3tly).ant-collapse .ant-collapse-content>.ant-collapse-content-box {
    padding-left: 0;
    padding-right: 0;
}

:where(.css-dev-only-do-not-override-eq3tly).ant-collapse-borderless>.ant-collapse-item>.ant-collapse-content>.ant-collapse-content-box {
    padding-top: 20px;
}

:where(.css-dev-only-do-not-override-eq3tly).ant-collapse-borderless {
    background-color: transparent;
}

:where(.css-dev-only-do-not-override-eq3tly).ant-collapse-borderless>.ant-collapse-item .ant-collapse-header {
    background-color: #f2f3f5;
    border-radius: 2px;
}
:where(.css-dev-only-do-not-override-eq3tly).ant-collapse>.ant-collapse-item >.ant-collapse-header {
    align-items: center;
}
</style>

<script>
import { defineComponent, ref } from 'vue';
// import { IconPark } from '@icon-park/vue-next/es/all';
import { CaretRightOutlined } from '@ant-design/icons-vue';

export default defineComponent({
    name: "RankMain",
    components: {
        // 'icon-park': IconPark
        "caret-right-outlined": CaretRightOutlined
    },
    props: {
        rank_list: {
            type: Array
        }
    },
    data() {
        return {};
    },
    setup() {
        return {
            expandIconPosition: ref('right'),
            activePannel:ref('enterprise')
        };
    }
});

</script>