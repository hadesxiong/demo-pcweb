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
                        上海分行
                        <icon-park type="Down" size="14" class="d_flex fai_c" fill="#165fdd"></icon-park>
                    </a>
                    <template #overlay>
                        <a-menu>
                            <a-menu-item>1st menu item</a-menu-item>
                            <a-menu-item>2nd menu item</a-menu-item>
                            <a-sub-menu key="sub1" title="sub menu">
                                <a-menu-item>3rd menu item</a-menu-item>
                                <a-menu-item>4th menu item</a-menu-item>
                            </a-sub-menu>
                            <a-sub-menu key="sub2" title="disabled sub menu" disabled>
                                <a-menu-item>5d menu item</a-menu-item>
                                <a-menu-item>6th menu item</a-menu-item>
                            </a-sub-menu>
                        </a-menu>
                    </template>
                </a-dropdown>
                <a-config-provider :locale="locale">
                    <a-date-picker picker="month" :bordered="false" class="custom_dp" :allowClear="false" v-model:value="date_value" @openChange="handlePickerClose">
                        <template #suffixIcon>
                            <icon-park type="Down" size="14" class="d_flex fai_c" fill="#165fdd"></icon-park>
                        </template>
                    </a-date-picker>
                </a-config-provider>

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

import dayjs from 'dayjs';
import 'dayjs/locale/zh-cn';
import locale from 'ant-design-vue/es/date-picker/locale/zh_CN';

dayjs.locale('zh-cn');

export default defineComponent({
    name: 'DBNCard1',
    components: {
        'icon-park': IconPark
    },
    props: {
        card_data: {
            type: Object
        }
    },
    setup() {
        return {
            locale,
            date_value: ref(dayjs())
        }
    },
    methods:{
        handlePickerClose(status) {
            if(!status) {
                console.log(this.date_value,this.date_value.format('YYYY-MM'))
            }
        }
    }
});

</script>