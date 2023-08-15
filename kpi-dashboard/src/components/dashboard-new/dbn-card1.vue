<template>
    <div class="bg_white d_flex p_20 fd_c gap_20 br_4">
        <div class="d_flex fd_r jc_sb">
            <div class="d_flex gap_20 fai_c jc_fs">
                <div class="font_16 fw_500 fc_l1">{{ retailCustomer_data.db_title }}</div>
                <div :class="retailCustomer_data.tag_class" class="br_4">{{retailCustomer_data.tag_name}}</div>
            </div>
            <div class="filter"></div>
        </div>
        <div>
            <a-row :gutter="['20']">
                <a-col :span="6" v-for="(item,index) in retailCustomer_data.card_data" :key="index">
                    <div class="bg_l1 d_flex fd_c p_16 gap_10">
                        <div class="d_flex jc_fs fc_l2 font_14">{{ item.card_title }}</div>
                        <div class="d_flex jc_sb fai_b">
                            <div class="fw_700 font_14 fc_l1 d_flex fai_b gap_8 lh_30 h_30">
                                <div class="font_18">{{ item.value_current }}</div>
                                {{ item.value_unit }}
                            </div>
                            <div class="d_flex gap_4 fc_l3">
                                较上期
                                <div :class="item.value_status === 0 ? 'compare_plus' : 'compare_minus'" class="ml_4 fw_700">{{item.value_compare}}</div>
                            </div>
                        </div>
                    </div>
                </a-col>
            </a-row>
        </div>
    </div>
</template>

<style>
</style>

<script>
import {defineComponent} from 'vue';

export default defineComponent({
    name:'DBNCard1',
    props:{
        retailCustomer_data:{
            type:Object
        }
    }
});

</script>