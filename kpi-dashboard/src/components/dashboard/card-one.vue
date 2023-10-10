<template>
    <div class="bg_white d_flex p_20 fd_c gap_20 br_4">
        <div class="d_flex fd_r jc_sb">
            <div class="d_flex gap_20 fai_c jc_fs">
                <div class="font_16 fw_500 fc_l1">{{ db_data.title }}</div>
                <div :class="card_conf[db_mark]['tag_class']" class="br_4">{{ card_conf[db_mark]['tag_name'] }}</div>
            </div>
            <div class="d_flex fai_c jc_fe gap_16">
                <a-dropdown>
                    <a class="d_flex fai_c gap_8 fc_brand6">
                        {{ choose_org.org_name }}
                        <icon-down size="14" class="d_flex fai_c" fill="#165fdd"></icon-down>
                    </a>
                    <template #overlay>
                        <a-menu v-model:selectedKeys="selectedKeys">
                            <div v-for="(item, index) in org_filter" :key="index">
                                <a-sub-menu v-if="item.children" :key="item.org_num" :title="item.org_name">
                                    <a-menu-item v-for="sub_item in item.children" :key="sub_item.org_num" @click="chooseOrg(sub_item)">{{
                                        sub_item.org_name }}</a-menu-item>
                                </a-sub-menu>
                                <a-menu-item v-else @click="chooseOrg(item)">{{ item.org_name }}</a-menu-item>
                            </div>
                        </a-menu>
                    </template>
                </a-dropdown>
                <a-date-picker picker="month" :bordered="false" class="custom_dp" :allowClear="false"
                    v-model:value="date_value[1]" @openChange="handlePickerClose" locale={locale}>
                    <template #suffixIcon>
                        <icon-down size="14" class="d_flex fai_c" fill="#165fdd"></icon-down>
                    </template>
                </a-date-picker>
            </div>
        </div>
        <div>
            <a-row :gutter="['20', '20']">
                <a-col :span="card_conf[db_mark]['card_col']" v-for="(item, index) in db_data.data" :key="index">
                    <div class="bg_l1 d_flex fd_c p_16 gap_10">
                        <div class="d_flex jc_fs fc_l2 font_14">{{ item.index_name }}</div>
                        <div class="d_flex jc_sb fai_b">
                            <div class="fw_700 font_14 fc_l1 d_flex fai_b gap_8 lh_30 h_30">
                                <div class="font_18">{{ item.value_current }}</div>
                                {{ item.value_unit }}
                            </div>
                            <div class="d_flex gap_4 fc_l3">
                                较上期
                                <div :class="item.value_status === 0 ? 'compare_plus' : 'compare_minus'"
                                    class="ml_4 fw_700 d_iflex fai_c jc_c">
                                    <span v-if="item.value_status === 1">+</span>
                                    {{ item.value_compare }}
                                </div>
                            </div>
                        </div>
                    </div>
                </a-col>
            </a-row>
        </div>
    </div>
</template>

<style scoped>
.custom_dp {
    padding-left: 0px;
    padding-right: 0px;
}
.custom_dp input {
    color: #165fdd !important;
    width: 55px !important;
}
.custom_dp span {
    padding-left: 0px !important;
    padding-right: 0px !important;
}
</style>

<script>
import { defineComponent, ref, watch } from 'vue';
import { Down } from '@icon-park/vue-next';
import { Dropdown, Menu, SubMenu, MenuItem, DatePicker, Row, Col } from 'ant-design-vue';

import { cardConfMap } from '@/assets/config/dashboard-main.js';

import dayjs from 'dayjs';
import 'dayjs/locale/zh-cn';
import locale from 'ant-design-vue/es/date-picker/locale/zh_CN';

dayjs.locale('zh-cn');

export default defineComponent({
    name: 'CardOne',
    components: {
        'icon-down': Down,
        'a-dropdown': Dropdown,
        'a-menu': Menu,
        'a-sub-menu': SubMenu,
        'a-menu-item': MenuItem,
        'a-date-picker': DatePicker,
        'a-row': Row,
        'a-col': Col,
    },
    props: {
        card_data: { type: Object },
        org_filter: { type: Object },
        cur_org: { type: Object },
        cur_date: { type: Array },
        db_index: {type: String}
    },
    setup(props) {
        const db_mark = ref(props.db_index);
        const choose_org = ref(props.cur_org);
        const db_data = ref(props.card_data)
        const date_value = ref(props.cur_date)
        watch(props,()=>{
            date_value.value = props.cur_date;
            choose_org.value = props.cur_org;
            db_data.value = props.card_data;
        })
        return {
            locale,
            date_value,
            db_data,
            card_conf: ref(cardConfMap),
            selectedKeys: ref([]),
            choose_org,
            db_mark,
            search_form: ref({
                mark: ref(db_mark),
                date: ref(date_value),
                org: ref(choose_org)
            })
        }
    },
    methods: {
        handlePickerClose(status) {
            if (!status) {
                // console.log(this.date_value[0])
                this.search_form.date = [
                    this.date_value[0].startOf('month').format('YYYY-MM-DD'),
                    this.date_value[1].endOf('month').format('YYYY-MM-DD')
                ]
                this.$emit('getDBFilters',this.search_form)
            }
        },
        chooseOrg(item) {
            
            this.selectedKeys.push(item);
            this.choose_org = item;
            this.search_form.org = item.org_num
            this.$emit('getDBFilters',this.search_form)
        }
    }
});

</script>