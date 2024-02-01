<template>
    <div class="d_flex gap_20 lh_30 fwrap_w">
        <div class="custom-checkbox d_flex fai_c br_100 pil_15 cursor_p" v-for="option in custom_options"
            :key="option.value" :class="{ 'selected': isSelected(option.value) }" @click="toggleOption(option.value)">
            <span class="checkbox-label">{{ option.label }}</span>
            <!-- <span class="close-icon" v-if="isSelected(option.value) && option.value != 'all'"
                @click="deselectOption(option.value)">
                <icon-park type="Close" size="12" class="d_flex"></icon-park>
            </span> -->
        </div>
    </div>
</template>
  
<style scoped>
.custom-checkbox {
    cursor: pointer;
}

.custom-checkbox.selected {
    background-color: #f2f3f5;
    color: var(--brand-1-6);
    font-weight: 500;
}

.custom-checkbox .close-icon {
    margin-left: 8px;
    cursor: pointer;
}
</style>
  
<script>
import { defineComponent } from "vue";

// 方法

export default defineComponent({

    name: 'CustomMulti',
    components: {},
    props: {
        custom_options: {type: Array},
        option_type:{type:String}
    },
    data() {
        return {
            selectedOptions: [],
        };
    },
    watch: {
        custom_options(newOptions) {
            // 传入的newOptions要做map
            const newOptionsValue = newOptions.map((x)=>(x.value));
            this.selectedOptions = this.selectedOptions.filter(option => newOptionsValue.includes(option));
            // 补偿机制,如果长度为0，添加all
            if(this.selectedOptions.length == 0) {
                this.selectedOptions.push('all')
            }
        }
    },
    setup() {
        // console.log(props)
    },
    mounted() {
        // 默认选择全部选项
        this.toggleOption('all');
    },
    methods: {
        isSelected(optionValue) {
            return this.selectedOptions.includes(optionValue);
        },
        toggleOption(optionValue) {
            // console.log(optionValue)
            if (this.isSelected(optionValue) && optionValue != 'all') {
                this.deselectOption(optionValue);
            } else {
                if (optionValue == 'all') {
                    this.selectedOptions = [];
                } else {
                    this.deselectOption('all');
                }
                this.selectedOptions.push(optionValue);
            }
            // 补偿机制:如果selectOptions为空，那么选择全部
            if (this.selectedOptions.length == 0) {
                this.selectedOptions.push('all')
            }
            this.$emit('getSelectedOptions', {class:this.option_type,list:this.selectedOptions});
        },
        deselectOption(optionValue) {
            this.selectedOptions = this.selectedOptions.filter(value => value !== optionValue);
        },
    },
});
</script>