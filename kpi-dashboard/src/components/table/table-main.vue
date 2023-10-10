<template>
    <div class="w_p100 h_p100 bg_white p_20 d_flex fd_c gap_20 fg_1">
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
        <div class="ofy_h fg_1 h_p100" id="table_con">
            <a-spin :spinning="spin_status" size="large" :delay="100" tip="数据加载中">
                <div class="fg_1">
                    <a-table :columns="table_data.table_columns" :data-source="table_data.table_data" :expandIconColumnIndex="1" :pagination="false"
                        :expandIconAsCell="false" :indentSize="26" @expand="expandRows" :expandedRowKeys="expand_keys" @expandedRowsChange="expandRowsChange" class="br_2 b_w1c2_so" :scroll="table_scroll" :bordered="false">
                        <template #customFilterIcon>
                            <icon-filter size='14' fill="#C9CDD4" theme="filled" class="d_flex"></icon-filter>
                        </template>
                        <template #bodyCell="{record,column,text}">
                            <div v-if="record['detail_date'] && column.dataIndex == 'detail_date'">
                                {{ text.substr(0,7) }}
                            </div>
                        </template>
                    </a-table>
                </div>

            </a-spin>
        </div>
        <div class="d_flex fai_c jc_fe">
            <a-pagination :current="page_data.current" :total="page_data.total" :pageSize="page_data.pageSize" :pageSizeOptions="page_data.sizeOptions" @change="changePage" @showSizeChange="changeSizeOptions"></a-pagination>
        </div>
    </div>
</template>

<style scoped>

.ant-picker {
  border: 1px solid var(--color-fill-2);
}
.ant-picker:hover, .ant-picker-focused {
  border-color: none;
  background-color: #fff;
}
.ant-picker-input-active {
  background-color: var(--color-fill-2);
}
.ant-table-cell {
  white-space: nowrap;
}

</style>

<script>
import { defineComponent, ref, watch } from 'vue';
import { RightSmall, CalendarThirty, Download, Filter } from '@icon-park/vue-next';
import { RangePicker, Button, Table, Pagination, Spin } from 'ant-design-vue';

import dayjs from 'dayjs';
import 'dayjs/locale/zh-cn';
import locale from 'ant-design-vue/es/date-picker/locale/zh_CN';

import { tableScrollYResize } from '@/utils/tableScrollYResize.js';

dayjs.locale('zh-cn');

export default defineComponent({
    name: 'TableMain',
    props: {
        table_data: {type: Object},
        spin_status: {type: Boolean,default:false},
        clean_expand: {type: Boolean,default: false},
        page_data: {type:Object, default: ()=>{return {
            current:1,
            pageSize:10,
            total:100,
            sizeOptions:['10','20','30']
        }}}
    },
    components: {
        'icon-right': RightSmall,
        'icon-calendar': CalendarThirty,
        'icon-download': Download,
        'icon-filter': Filter,
        'a-range-picker': RangePicker,
        'a-button': Button,
        'a-table': Table,
        'a-pagination': Pagination,
        'a-spin': Spin
    },
    setup(props) {
        console.log(props.table_data)
        const w_table_data = ref(props.table_data)
        const page_obj = ref(props.page_data)
        const expand_keys = ref([])
        const need_expand = ref(props.clean_expand)
        watch(need_expand,()=>{
            console.log(need_expand)
            if (need_expand.value == true) {expand_keys.value = []}
        })
        return {
            locale,
            expand_keys,
            table_id: ref(),
            pannel_mode: ref(['month', 'month']),
            date_value: ref([dayjs().add(-5,'month'),dayjs().add(-5,'month')]),
            w_table_data,
            table_scroll: ref({ x:100,y:360 }),
            page_obj
        }
    },
    mounted() {
        // this.w_table_data = this.$props.table_data;
        // console.log(this.w_table_data)
        // this.page_obj = this.$props.page_data
        // console.log(this.page_obj)
        // this.expand_keys = this.$props.expand
        window.addEventListener('resize',tableScrollYResize('table_con',this.table_scroll));
    },
    methods: {
        handlePannelChange(value, mode) {
            this.date_value = value;
            this.pannel_mode = [mode[0] === 'date' ? 'month' : mode[0], mode[1] === 'date' ? 'month' : mode[1]];
        },
        handleChange(status) {
            if(!status) {
                const [startDate,endDate] = this.date_value;
                this.$emit('getDateRange',{date_range:[
                    startDate.startOf('month').format('YYYY-MM-DD'),
                    endDate.endOf('month').format('YYYY-MM-DD')
                ]})
            }
        },
        expandRows(expanded,record) {
            if (expanded) {
                this.expand_keys.push(record.key)
                this.$emit('getChildOptions',{date:record.detail_date,parent:record.detail_belong,key:record.key})
            } else {
                this.expand_keys.splice(this.expand_keys.indexOf(record.key),1)
            }
        },
        expandRowsChange(expandedRows) {
            console.log(expandedRows)
        },
        changePage(page) {
            // console.log(page)
            this.page_obj.current= page
            this.$emit('getPageOptions',{page:page,size:this.page_obj.pageSize})
        },
        changeSizeOptions(_,size) {
            // console.log(size)
            this.page_obj.pageSize = size;
            this.$nextTick(()=>{
                this.page_obj.current = 1
                this.$emit('getPageOptions',{page:this.page_obj.current,size:size})
            })
        },
    }
});

</script>   