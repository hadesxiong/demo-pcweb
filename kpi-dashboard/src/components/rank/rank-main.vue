<template>
    <div class="d_flex fwrap_w" style="padding: 0px !important;">
        <a-row :gutter="[20, 20]" :wrap="true" justify="start">
            <a-col :md="24" :lg="24" :xl="12" :xxl="8" :xxxl="6" v-for="item in rank_list" :key="item.rank_id">
                <div class="d_flex fd_c bg_white br_4 c-rank_con p_20 b_w1c2_so">
                    <div class="d_flex jc_sb w_p100 lh_20 fai_b">
                        <div class="d_iflex gap_12 fai_c">
                            <div class="font_14 fw_500">{{ item.rank_info.data_title }}</div>
                            <div v-for="(tag_item, index) in item.rank_info.data_tag" :key="index">
                                <a-tag :class="tag_item.tag_class">{{ tag_item.tag_title }}</a-tag>
                            </div>
                            <div class="fc_l3">
                                数据更新于{{ item.rank_info.data_update }}
                            </div>
                        </div>
                        <div>
                            <div class="fc_brand6">
                                <router-link to="/rank-important/rank-detail" class="more_btn">查看全部</router-link>
                            </div>
                        </div>
                    </div>
                    <div class="w_p100 mt_20">
                        <a-table :columns="item.rank_column" :data-source="item.rank_data" :pagination="false"></a-table>
                    </div>
                </div>

            </a-col>
        </a-row>
    </div>
</template>

<style>
</style>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
    name: "RankMain",
    props: {
        rank_list: {
            type: Array
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