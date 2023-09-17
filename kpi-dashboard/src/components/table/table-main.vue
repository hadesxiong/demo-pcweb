<template>
    <div class="w_p100 bg_white p_20 d_flex fd_c gap_20 fg_1">
        <div class="d_flex fd_c">
            <div class="d_flex fd_r jc_sb">
                <a-range-picker :placeholder="['起始月份', '截止月份']" format="YYYY-MM" :value="date_value" :mode='["month", "month"]'
                    @panelChange="handlePannelChange" @openChange="handleChange" :allowClear="false">
                    <template #separator>
                        <icon-right fill="#86909C"></icon-right>
                    </template>
                    <template #suffixIcon>
                        <icon-calendar fill="#86909C" size="14"></icon-calendar>
                    </template>
                </a-range-picker>
                <a-button type="primary" class="br_2 fai_c d_flex fc_l5 bg_brand6">
                    <template #icon>
                        <icon-download size="14" class="mr_8 lh_1"></icon-download>
                    </template>
                    下载
                </a-button>
            </div>
        </div>
        <div class="of_a h_p100">
            <a-table :columns="table_data.table_columns" :data-source="table_data.table_data" :expandIconColumnIndex="1" :pagination="false"
                :expandIconAsCell="false" :indentSize="0" expand="expandRows" class="b_w1c2_so br_2">
                <template #customFilterIcon>
                    <icon-filter size='14' fill="#C9CDD4" theme="filled" class="d_flex"></icon-filter>
                </template>
            </a-table>
        </div>
        <div class="d_flex fai_c jc_fe">
            <a-pagination :current="page_obj.current" :total="page_obj.total" :pageSize="page_obj.pageSize" @change="handlePageChange"></a-pagination>
        </div>
    </div>
</template>

<style scoped>

.ant-picker {
  border: 1px solid var(--color-fill-2);
}
:where(.css-dev-only-do-not-override-eq3tly).ant-picker:hover, :where(.css-dev-only-do-not-override-eq3tly).ant-picker-focused {
  border-color: none;
  background-color: #fff;
}
.ant-picker-input-active {
  background-color: var(--color-fill-2);
}

</style>

<script>
import { defineComponent, ref } from 'vue';
import { RightSmall, CalendarThirty, Download, Filter } from '@icon-park/vue-next';
import { RangePicker, Button, Table, Pagination } from 'ant-design-vue';

import dayjs from 'dayjs';
import 'dayjs/locale/zh-cn';
import locale from 'ant-design-vue/es/date-picker/locale/zh_CN';

dayjs.locale('zh-cn');

export default defineComponent({
    name: 'TableMain',
    props: {
        table_data: {
            type: Object
        }
    },
    components: {
        'icon-right': RightSmall,
        'icon-calendar': CalendarThirty,
        'icon-download': Download,
        'icon-filter': Filter,
        'a-range-picker': RangePicker,
        'a-button': Button,
        'a-table': Table,
        'a-pagination': Pagination
    },
    setup() {
        return {
            locale,
            pannel_mode: ref(['month', 'month']),
            date_value: ref([dayjs().add(-5,'month'),dayjs()]),
            w_table_data: ref({}),
            page_obj: ref({
                current:1,
                pageSize:10,
                total:100
            })
        }
    },
    mounted() {
        this.w_table_data = this.$props.table_data;
    },
    methods: {
        handlePannelChange(value, mode) {
            this.date_value = value;
            this.pannel_mode = [mode[0] === 'date' ? 'month' : mode[0], mode[1] === 'date' ? 'month' : mode[1]];
        },
        handleChange(status) {
            if(!status) {
                // console.log(this.date_value)
                this.$emit('getFilterOptions',{date_range:this.date_value})
            }
        },
        expandRows(expanded,record) {
            console.log(expanded,record)
        },
        handlePageChange(page) {
            console.log(page)
            this.page_obj.current= page
        }
    }
});

</script>   