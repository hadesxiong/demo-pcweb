<template>
    <div class="bg_white d_flex p_20 fd_c gap_20 br_4">
        <div class="d_flex fd_r jc_sb">
            <div class="d_flex gap_20 fai_c jc_fs">
                <div class="font_16 fw_500 fc_l1">{{ card_data.db_title }}</div>
                <div :class="card_data.tag_class" class="br_4">{{ card_data.tag_name }}</div>
            </div>
            <div class="d_flex fai_c jc_fe gap_16">
                <a-dropdown>
                    <a class="d_flex fai_c gap_8 fc_brand6">
                        {{ choose_org }}
                        <icon-park type="Down" size="14" class="d_flex fai_c" fill="#165fdd"></icon-park>
                    </a>
                    <template #overlay>
                        <a-menu v-model:selectedKeys="selectedKeys">
                            <div v-for="(item, index) in org_filter" :key="index">
                                <a-sub-menu v-if="item.children" :key="item.org_key" :title="item.org_name">
                                    <a-menu-item v-for="sub_item in item.children" :key="sub_item.org_key" @click="chooseOrg(sub_item)">{{
                                        sub_item.org_name }}</a-menu-item>
                                </a-sub-menu>
                                <a-menu-item v-else @click="chooseOrg(item)">{{ item.org_name }}</a-menu-item>
                            </div>
                        </a-menu>
                    </template>
                </a-dropdown>
                <a-date-picker picker="month" :bordered="false" class="custom_dp" :allowClear="false"
                    v-model:value="date_value[1]" @openChange="handlePickerClose">
                    <template #suffixIcon>
                        <icon-park type="Down" size="14" class="d_flex fai_c" fill="#165fdd"></icon-park>
                    </template>
                </a-date-picker>
            </div>
        </div>
        <div>
            <a-row :gutter="['20', '20']">
                <a-col :span="card_data.card_col" v-for="(item, index) in card_data.card_data" :key="index">
                    <div class="bg_l1 d_flex fd_c p_16 gap_10">
                        <div class="d_flex jc_fs fc_l2 font_14">{{ item.card_title }}</div>
                        <div class="d_flex jc_sb fai_b">
                            <div class="fw_700 font_14 fc_l1 d_flex fai_b gap_8 lh_30 h_30">
                                <div class="font_18">{{ item.value_current }}</div>
                                {{ item.value_unit }}
                            </div>
                            <div class="d_flex gap_4 fc_l3">
                                较上期
                                <div :class="item.value_status === 0 ? 'compare_plus' : 'compare_minus'"
                                    class="ml_4 fw_700">{{ item.value_compare }}</div>
                            </div>
                        </div>
                    </div>
                </a-col>
            </a-row>
        </div>
    </div>
</template>

<style>
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
import { defineComponent, ref } from 'vue';
import { IconPark } from '@icon-park/vue-next/es/all';


export default defineComponent({
    name: 'DBNCard1',
    components: {
        'icon-park': IconPark
    },
    props: {
        card_data: { type: Object },
        org_filter: { type: Object },
        cur_org: { type: String },
        cur_date: { type: Array }
    },
    setup(props) {
        const date_value = ref(props.cur_date);
        return {
            date_value,
            selectedKeys: ref([]),
            choose_org:ref(props.cur_org)
        }
    },
    methods: {
        handlePickerClose(status) {
            if (!status) {
                console.log(this.date_value)
            }
        },
        chooseOrg(item) {
            this.selectedKeys.push(item.org_key);
            this.choose_org = item.org_name;
        }
    }
});

</script>