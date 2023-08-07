<template>
    <div class="c-data_con">
        <div class="c-data_head">
            <div class="c-head_left">
                <div class="c-data_title">理财日均保有量</div>
                <div class="c-data_label label_orange">转型与质量发展</div>
            </div>
            <div class="c-data_filter"></div>
        </div>
        <div class="c-data_body">
            <div class="c-data_main">
                <div class="c-card_con width_410">
                    <div v-for="item in card_data" :key="item.data_title" class="c-card_main width_32p flex-align-fs gap-02">
                        <div class="c-card_title">{{ item.data_title }}</div>
                        <div class="c-card_data">
                            <div class="c-data_detail">
                                <span class="detail_num">{{ item.data_value }}</span>
                                {{ item.data_unit }}
                            </div>
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
</template>

<style>
@import url('../../assets/style/dashboard.css');
@import url('../../assets/style/common.css');
@import url('../../assets/style/overwrite.css');
@import url('../../assets/style/colorset.css');
.width_410 {
    min-width: var(--card-con-410);
}
.width_32p {
    width:32%;
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
    name: "dashboard_cardOne",
    props:{},
    data() {
        this.card_data = [
            {data_title:'企金理财日均保有量',data_unit:'万元',status:'1',data_value:'232,123',compare_value:'+12,309'},
            {data_title:'零售理财日均保有量',data_unit:'万元',status:'1',data_value:'2,123.98',compare_value:'+309.23'},
            {data_title:'同业理财日均保有量',data_unit:'万元',status:'2',data_value:'232,123',compare_value:'-12,309'},
        ]
        return {};
    },
    mounted() {},
    methods: {}
}

</script>