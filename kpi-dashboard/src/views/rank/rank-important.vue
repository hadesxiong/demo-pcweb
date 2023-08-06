<template>
    <div class="v-rank_con">
        <div class="v-filter_con">
            <div class="v-filter_left">
                <a-radio-group v-model:value="default_line" button-style="solid" class="v-radio_group">
                    <a-radio-button value="all" class="v-radio_btn">全部</a-radio-button>
                    <a-radio-button value="enterprise" class="v-radio_btn">企金指标</a-radio-button>
                    <a-radio-button value="retail" class="v-radio_btn">零售指标</a-radio-button>
                    <a-radio-button value="bank" class="v-radio_btn">同业指标</a-radio-button>
                    <a-radio-button value="other" class="v-radio_btn">其他指标</a-radio-button>
                </a-radio-group>
            </div>
            <div class="v-filter_right">
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
        <div class="v-data_con">
            <rank-main v-if="rank_list" :rank_list="rank_list"></rank-main>
        </div>
    </div>
</template>

<style>
@import url('../../assets/style/colorset.css');
@import url('../../assets/style/overwrite.css');

.v-rank_con {
    width: 100%;
    height: 100%;
    background-color: #fff;
}

.v-filter_con {
    display: flex;
    padding: 20px 20px 0 20px;
    line-height: 0;
    justify-content: space-between;
}

.v-radio_group {
    display: flex;
    gap: 12px;
}

.v-radio_btn {
    border-radius: 100px;
    min-width: 50px;
    overflow: hidden;
    text-overflow: ellipsis;
}

.v-data_con {
    padding: 20px;
}
.v-filter_right {
    display: flex;
    gap: 20px;

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
            console.log(rank_res);
            this.rank_list = rank_res.data;
            console.log(this.rank_list)
        }
    }
});

</script>