<template>
    <div class="d_flex fd_c gap_20 h_p100">
        <div class="d_flex p_20 bg_white fd_r gap_20 fai_c jc_sb">
            <a-row>
                <a-col><menu-input v-if="data_loaded" :cp_data="character_option"></menu-input></a-col>
                <a-col><menu-input v-if="data_loaded" :cp_data="org_option"></menu-input></a-col>
                <a-col><menu-input v-if="data_loaded" :cp_data="line_option"></menu-input></a-col>
            </a-row>
        </div>
    </div>
</template>

<style>
@import url('@/assets/style/common.css');
@import url('@/assets/style/colorset.css');
@import url('@/assets/style/overwrite.css');
</style>

<script>
import { defineComponent, ref } from 'vue';
import { Col, Row } from 'ant-design-vue';

import MenuInput from '@/components/other/menu-input.vue';
// import SearchInput from '@/components/other/search-input.vue';
// import EditTable from '@/components/manage/edit-table.vue';

import { api } from '@/utils/commonApi.js';

const myApi = api();

export default defineComponent({
    name: 'CustomManage',
    components: {
        'menu-input': MenuInput,
        // 'search-input': SearchInput,
        'a-col': Col,
        'a-row': Row,
        // 'a-button': Button
    },
    data() {
        return {
            character_option: ref({}),
            org_option: ref({}),
            line_option: ref({}),
            data_loaded: ref(false)
        }
    },
    setup() {
        return {}
    },
    created() {
        myApi.get('/api/other/getFilter',{params: {type:'ubg.uc.og'}}).then(
            (response) => {
                this.character_option = {
                    menu_data: response.data.data.user_character,
                    menu_key: {code:'ref_code',label:'ref_name'}
                }
                this.org_option = {
                    menu_data: response.data.data.org_group,
                    menu_key: {code:'ref_code',label:'ref_name'}
                }
                this.line_option = {
                    menu_data: response.data.data.user_belong_group,
                    menu_key: {code:'ref_code',label:'ref_name'}
                }
                this.data_loaded = true;
            }
        )
    },
    methods: {
    }
})
</script>