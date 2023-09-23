<template>
    <div class="d_flex fai_c gap_16">
        <span class="fc_l2" v-if="need_label">{{ label_name }}</span>
        <a-dropdown class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h pl_12 pr_12 tover_ell ws_no minw_100">
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
import { defineComponent, ref, reactive, toRefs } from 'vue';
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

        const {menu_data,menu_key}  = toRefs(props.cp_data)
        const {need_label,label_name} = toRefs(props.label_data)
        const {front,end,suffix} = toRefs(props.suffix_info)
        
        const item_list = menu_data.value.filter((a) => !props.cp_filter.includes(a[menu_key.value.code]))
        return {
            'item_list': ref(item_list),
            'item_code': ref(menu_key.value.code),
            'item_label': ref(menu_key.value.label),
            'item_choosen': ref(item_list[0]),
            'need_label': ref(need_label),
            'label_name': ref(label_name),
            'suffix_front': ref(front.value),
            'suffix_end': ref(end.value),
            'suffix_label': ref(suffix.value)
        }
    },
    methods: {
        chooseMenuItem(item,target) {
            this[target] = item;
            this.$emit('menu-select',{'title':'title','data':item})
        }
    }
})
</script>