<template>
    <a-collapse :bordered="false" :activeKey="activePannel" accordion :ghost="true" @change="changePannel" class="d_flex fd_c gap_20">
        <template #expandIcon="{ isActive }">
            <caret-right-outlined :rotate="isActive ? 90 : 0" />
        </template>
        <template v-if="rank_data.title.length > 0">
            <a-collapse-panel v-for="(item,index) in rank_data.title" :key="item.key">
                <template #header>
                    <div class="d_flex fai_c gap_16" >
                        <div class="fc_l2 font_16 fw_500">{{ item.title }}</div>
                        <div class="fc_l3 font_14">共{{ item.count }}个指标</div>
                    </div>
                </template>
                <div style="padding: 0px !important;">
                    <a-row :gutter="[20, 20]" :wrap="true" justify="start">
                        <a-col :md="24" :lg="24" :xl="12" :xxl="8" :xxxl="6" v-for="sub_item in rank_data.data[index]" :key="sub_item.index_num">
                            <div class="d_flex fd_c bg_white br_4 c-rank_con p_20 b_w1c2_so">
                                <div class="d_flex jc_sb w_p100 lh_20 fai_b ws_no ">
                                    <div class="d_iflex gap_12 fai_c ta_l">
                                        <div class="font_14 fw_500 tover_ell of_h">{{ sub_item.index_name }}</div>
                                        <div>
                                            <a-tag :class="tag_map[sub_item.index_class-1]['tag']">{{ sub_item.class_name}}</a-tag>
                                        </div>
                                        <!-- <div class="fc_l3">
                                            数据更新于{{ item.rank_info.data_update }}
                                        </div> -->
                                    </div>
                                    <div>
                                        <div class="fc_brand6">
                                            <router-link 
                                            :to="{
                                                name:'rank-detail',
                                                params:{rank_id:encodeQuery({
                                                    index_num: sub_item.index_num,
                                                    index_name:sub_item.index_name,
                                                    date: detail_form.date,
                                                    view_method: detail_form.group.value,
                                                    group: detail_form.group.key,
                                                    tag_class: tag_map[sub_item.index_class-1]['tag'],
                                                    class_name: sub_item.class_name
                                                })}}" 
                                            class="more_btn">查看全部</router-link>
                                        </div>
                                    </div>
                                </div>
                                <div class="w_p100 mt_20">
                                    <a-table :columns="rank_data.column" :data-source="sub_item.detail_list"
                                        :pagination="false">
                                        <template #bodyCell="{column,index}">
                                            <div v-if="column.dataIndex == 'rank_sort'" class="d_flex gap_4 jc_sb">
                                                <div>{{ index+1 }}</div>
                                                <div v-if="index == 0" class="d_flex fai_c jc_c">
                                                    <img src="../../assets/gold.png" alt="" class="rank_icon">
                                                </div>
                                                <div v-if="index == 1" class="d_flex fai_c jc_c">
                                                    <img src="../../assets/silver.png" alt="" class="rank_icon">
                                                </div>
                                                <div v-if="index == 2" class="d_flex fai_c jc_c">
                                                    <img src="../../assets/copper.png" alt="" class="rank_icon">
                                                </div>
                                            </div>
                                        </template>
                                    </a-table>
                                </div>
                            </div>
                        </a-col>
                    </a-row>
                </div>
            </a-collapse-panel>
        </template>
        <template v-else>
            <div class="d_flex fd_c w_p100 h_p100 fai_c jc_c" style="margin-top: 200px;">
                <a-empty :image-style="{height: '100%'}"></a-empty>
            </div>
        </template>
    </a-collapse>
</template>

<style>
.ant-collapse .ant-collapse-content>.ant-collapse-content-box {
    padding-left: 0;
    padding-right: 0;
}

.ant-collapse-borderless>.ant-collapse-item>.ant-collapse-content>.ant-collapse-content-box {
    padding-top: 20px;
}

.ant-collapse-borderless {
    background-color: transparent;
}

.ant-collapse-borderless>.ant-collapse-item .ant-collapse-header {
    background-color: #f2f3f5;
    border-radius: 2px;
}
.ant-collapse>.ant-collapse-item >.ant-collapse-header {
    align-items: center;
}
.ant-table-tbody > tr:last-child td {
  border-bottom: none !important;
}
.rank_icon {
    width: 18px;
}
</style>

<script>
import { defineComponent, ref, watch } from 'vue';
import { CaretRightOutlined } from '@ant-design/icons-vue';
import { Collapse, CollapsePanel, Row, Col, Tag, Table, Empty } from 'ant-design-vue';

import { tagMap } from '@/assets/config/rank-important.js'

import { Base64 } from 'js-base64';

export default defineComponent({
    name: "RankMain",
    components: {
        "caret-right-outlined": CaretRightOutlined,
        'a-collapse': Collapse,
        'a-collapse-panel': CollapsePanel,
        'a-row': Row,
        'a-col': Col,
        'a-tag': Tag,
        'a-table': Table,
        'a-empty': Empty
    },
    props: {
        rank_data: {type: Object},
        show_pannel: {type: Boolean,default:false},
        active_pannel: {type: String ,default:'1'},
        detail_params: {type: Object}
    },
    data() {
        return {};
    },
    setup(props) {
        const activePannel = ref(props.active_pannel);
        const detail_form = ref(props.detail_params)
        // console.log(detail_form)
        watch(props,()=>{
            activePannel.value = props.active_pannel
            detail_form.value = props.detail_params
        })
        return {
            expandIconPosition: ref('right'),
            activePannel,
            detail_form,
            tag_map: ref(tagMap),
        };
    },
    methods: {
        changePannel(key) {
            this.activePannel = key
        },
        encodeQuery(query) {
            return Base64.encode(JSON.stringify(query));
        }
    }
});

</script>