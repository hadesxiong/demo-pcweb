<template>
    <div class="d_flex fai_c gap_16">
        <span class="fc_l2" v-if="need_label">{{ label_name }}</span>
        <a-dropdown class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100 fg_1">
            <a>
                {{item_choosen[item_label]}}
                <icon-down class="lh_1" fill="#86909C"></icon-down>
            </a>
            <template #overlay>
                <a-menu>
                    <a-menu-item v-for="item in item_list" :key="item[item_code]" @click="chooseMenuItem(item,'item_choosen')">
                        <span v-if="suffix_front">{{ suffix_label }}</span>
                        {{ item[item_label] }}
                        <span v-if="suffix_end">{{ suffix_label }}</span>
                    </a-menu-item>
                </a-menu>
            </template>
        </a-dropdown>
    </div>
</template>

<style>
@import url('@/assets/style/common.css');
@import url('@/assets/style/colorset.css');
@import url('@/assets/style/overwrite.css');
</style>

<script>
import { defineComponent, ref, reactive, watch } from 'vue';
import { Dropdown, Menu, MenuItem } from 'ant-design-vue';
import { Down } from '@icon-park/vue-next';

export default defineComponent({
    name: 'MenuInput',
    components:{
        'icon-down': Down,
        'a-dropdown': Dropdown,
        'a-menu': Menu,
        'a-menu-item': MenuItem,
    },
    props:{
        cp_data: {type: Object},
        cp_filter: {
            type: Array,
            default:() => {return []}
        },
        label_data: {
            type: Object,
            default:() => {return reactive({need_label:false,label_name:''})}
        },
        suffix_info: {
            type: Object,
            default:() => {return reactive({front:false,end:false,suffix:''})}
        }
    },
    setup(props) {
        // console.log(props)
        const item_list = ref(props.cp_data.menu_data.filter(a => !props.cp_filter.includes(a[props.cp_data.menu_key.code])));
        const item_choosen = ref(item_list.value[0]);

        watch(props, () => {
            item_list.value = props.cp_data.menu_data.filter(a => !props.cp_filter.includes(a[props.cp_data.menu_key.code]));
            item_choosen.value = item_list.value[0];
        }, { deep: true });

        return {
            item_list,
            item_code: ref(props.cp_data.menu_key.code),
            item_label: ref(props.cp_data.menu_key.label),
            item_choosen,
            need_label: ref(props.label_data.need_label),
            label_name: ref(props.label_data.label_name),
            suffix_front: ref(props.suffix_info.front),
            suffix_end: ref(props.suffix_info.end),
            suffix_label: ref(props.suffix_info.suffix),
            select_title: ref(props.cp_data.select_title),
        }
    },
    methods: {
        chooseMenuItem(item,target) {
            this[target] = item;
            this.$emit('menu-select',{'title':this.select_title,'data':item})
        }
    }
})
</script>