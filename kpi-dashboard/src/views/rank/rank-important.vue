<template>
    <div class="w_p100 h_p100 bg_white">
        <div class="d_flex jc_sb pt_20 pl_20 pr_20">
            <div class="d_flex">
                <a-radio-group v-model:value="default_line" button-style="solid" class="d_flex gap_12">
                    <a-radio-button value="all" class="br_100 of_h tover_ell">全部</a-radio-button>
                    <a-radio-button value="enterprise" class="br_100 of_h tover_ell">企金指标</a-radio-button>
                    <a-radio-button value="retail" class="br_100 of_h tover_ell">零售指标</a-radio-button>
                    <a-radio-button value="bank" class="br_100 of_h tover_ell">同业指标</a-radio-button>
                    <a-radio-button value="other" class="br_100 of_h tover_ell">其他指标</a-radio-button>
                </a-radio-group>
            </div>
            <div class="d_flex gap_20">
                <a-dropdown class="v-input_style">
                    <a>全部分类<a-icon style="dropdown_icon" type="down"></a-icon></a>
                    <a-menu>
                        <a-menu-item>1st menu item</a-menu-item>
                        <a-menu-item>2nd menu item</a-menu-item>
                        <a-menu-item>3rd menu item</a-menu-item>
                    </a-menu>
                </a-dropdown>
                <a-dropdown class="v-input_style">
                    <a>全部分类<a-icon style="dropdown_icon" type="down"></a-icon></a>
                    <a-menu>
                        <a-menu-item>1st menu item</a-menu-item>
                        <a-menu-item>2nd menu item</a-menu-item>
                        <a-menu-item>3rd menu item</a-menu-item>
                    </a-menu>
                </a-dropdown>
                <a-dropdown class="v-input_style">
                    <a>全部分类<a-icon style="dropdown_icon" type="down"></a-icon></a>
                    <a-menu>
                        <a-menu-item>1st menu item</a-menu-item>
                        <a-menu-item>2nd menu item</a-menu-item>
                        <a-menu-item>3rd menu item</a-menu-item>
                    </a-menu>
                </a-dropdown>
            </div>
        </div>
        <div class="p_20">
            <a-row>
            </a-row>
            <rank-main v-if="rank_list" :rank_list="rank_list"></rank-main>
        </div>
    </div>
</template>

<style scoped>
@import url('../../assets/style/common.css');
@import url('../../assets/style/colorset.css');
@import url('../../assets/style/overwrite.css');

/* 覆盖部分 */

/* radio部分 */
.ant-radio-group-solid .ant-radio-button-wrapper-checked:not(.ant-radio-button-wrapper-disabled):hover {
  color: #165dff;
  background-color: #f2f3f5;
}

.ant-radio-button-wrapper:last-child {
  border-start-end-radius: 100px;
  border-end-end-radius: 100px;
}

.ant-radio-button-wrapper:first-child {
  border-inline-start: 0;
  border-start-start-radius: 100px;
  border-end-start-radius: 100px;
}

.ant-radio-button-wrapper {
  border: none;
}
.ant-radio-button-wrapper:not(:first-child)::before {
  width: 0;
  inset-block-start: 0;
  inset-block-end: 0;
  padding-block: 0;
  background-color: transparent;
}
.ant-radio-button-wrapper:not(:first-child)::before {
  color: #165dff;
  background-color: #f2f3f5;
  border-color: transparent;
}
.ant-radio-group-solid .ant-radio-button-wrapper-checked:not(.ant-radio-button-wrapper-disabled) {
  background-color: #f2f3f5;
  color: #165dff;
  border-color: transparent;
  font-weight: 500;
}

.v-input_style {
    background-color: #f2f3f5;
    width: 180px;
    min-width: 100px;
    border-radius: 0.125rem;
    display: block;
    height: 2rem;
    text-align: left;
    padding: 0.3125rem 0.75rem;
    color: #1D2129;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

/* 表格覆写部分 */

.ant-table-wrapper .ant-table {
    font-size: 13px;
}

</style>

<script>
import { defineComponent, ref } from 'vue';
import RankMain from '../../components/rank/rank-main';
import axios from 'axios';

export default defineComponent({
    name: 'rank-important',
    components: {
        'rank-main': RankMain
    },
    data() {
        return {
            rank_list: []
        }
    },
    setup() {
        const default_line = ref('all');
        return {
            default_line
        }
    },
    mounted() {
        this.getRankData();
    },
    methods: {
        async getRankData() {
            const rank_res = await axios.get('http://localhost:8080/demo/rank/rank-important.json');
            // console.log(rank_res);
            this.rank_list = rank_res.data;
            // console.log(this.rank_list)
        }
    }
});

</script>