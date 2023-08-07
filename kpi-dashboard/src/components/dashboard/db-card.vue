<template>
    <div class="c-data_con">
        <div class="c-data_head">
            <div class="c-head_left">
                <div class="c-data_title">客户建设情况</div>
                <div class="c-data_label c-label_purple">客户建设</div>
            </div>

            <div class="c-data_filter"></div>
        </div>
        <div class="c-data_body">
            <div class="c-data_main">
                <div class="c-card_con width_360">
                    <div v-for="item in card_data" :key="item.data_title" class="c-card_main width_48p gap-06">
                        <div class="c-card_title">{{ item.data_title }}</div>
                        <div class="c-card_data">
                            <div class="data_detail">
                                <span class="detail_num">{{ item.data_value }}</span>
                                {{ item.data_unit }}
                            </div>
                            <div class="data_compare compare_detail">
                                较上期
                                <span :class="item.status == '1'? 'compare_plus' : 'compare_minus'">{{item.compare_value}}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style>
@import url('../../assets/style/dashboard.css');
@import url('../../assets/style/common.css');
@import url('../../assets/style/overwrite.css');
@import url('../../assets/style/colorset.css');

.width_360 {
    max-width: var(--card-con-360);
}
.width_48p {
    width:48%;
}
.data_detail {
    font-size:0.75rem;
    line-height: 1.875rem;
    display: flex;
    align-items:flex-end;
    align-self: stretch;
}
.detail_num {
    font-size: 1.125rem;
    color: "#0f172a";
    font-weight: 700;
    line-height: 1.875rem;
    letter-spacing: 0.0125rem;
    margin-right: 0.25rem;
}
.data_compare {
    font-size:0.75rem;
    line-height: 1.375rem;
}
.compare_detail span{
    margin-left: 0.25rem;
}

</style>

<script>


export default {
    name: "DashboardCard1",
    props:{},
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