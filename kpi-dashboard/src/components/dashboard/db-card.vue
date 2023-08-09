<template>
    <div class="d_flex fd_c bd_4 bg_white">
        <div class="d_flex jc_sb">
            <div class="d_flex">
                <div class="d_iflex font_16 fw_500 fc_l1 lh_20 m_20">{{ db_data.db_title }}</div>
                <div class="d_iflex br_4" :class="db_data.db_tag.tag_class">{{ db_data.db_tag.tag_name }}</div>
            </div>
            <div class="c-data_filter"></div>
        </div>
        <div class="cd_flex jc_c fai_c pl_20 pr_20 pb_20">
            <div class="d_flex jc_sb fai_c">
                <div class="d_flex fwrap_w jc_fs gap_16 fs_0 dbcard-card_con">
                    <div v-for="(item,index) in db_data.db_other.card_data" :key="index" class="d_flex br_4 fd_c p_16 gap_4 jc_c fai_fs db-card_bgc dbcard-card_limit">
                        <div class="font_14 fw_400 lh_22 ta_l fc_l2">{{ item.card_title }}</div>
                        <div class="d_flex fai_b jc_sb gap_12 w_p100">
                            <div class="font_14 fw_700 lh_30 mr_4">
                                <span class="font_18 fc_l1 mr_4">{{ item.value_current }}</span>
                                {{ item.value_unit }}
                            </div>
                            <div class="font_12 fc_l2 lh_20">
                                较上期
                                <span :class="item.value_status === 0 ? 'compare_plus' : 'compare_minus'" class="ml_4 fw_700">{{item.value_compare}}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style>

.dbcard-card_con {
    flex-basis: 600px;
}

.dbcard-card_limit {
    width: 260px;
}


</style>

<script>


export default {
    name: "DashboardCard1",
    props:{
        db_data:{
            type:Object
        }
    },
    data() {
        this.card_data = [
            {data_title:'企金动户数',data_unit:'户',status:'1',data_value:'232,123',compare_value:'+12,309'},
            {data_title:'折算后价值客户数',data_unit:'户',status:'1',data_value:'2,123.98',compare_value:'+309.23'},
            {data_title:'零售客户总数',data_unit:'户',status:'1',data_value:'232,123',compare_value:'+12,309'},
            {data_title:'零售贵宾客户数',data_unit:'户',status:'2',data_value:'58,946',compare_value:'-3,029'},
            {data_title:'私行客户数',data_unit:'户',status:'2',data_value:'9,728',compare_value:'-329'},
            {data_title:'新获取有效代发个人客户数',data_unit:'户',status:'1',data_value:'232,123',compare_value:'+12,309'},
        ]
        return {};
    },
    mounted() {},
    methods: {}
}

</script>