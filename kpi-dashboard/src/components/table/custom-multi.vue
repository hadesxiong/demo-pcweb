<template>
    <div class="d_flex gap_20 lh_30">
        <div class="custom-checkbox d_flex fai_c br_100 pil_15 cursor_p" v-for="option in options" :key="option.value"
            :class="{ 'selected': isSelected(option.value) }" @click="toggleOption(option.value)">
            <span class="checkbox-label">{{ option.label }}</span>
            <span class="close-icon" v-if="isSelected(option.value)" @click="deselectOption(option.value)">
                <icon-park type="Close" size="12" class="d_flex"></icon-park>
            </span>
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

.custom-checkbox .checkbox-label {
    margin-right: 8px;
}

.custom-checkbox .close-icon {
    cursor: pointer;
}
</style>
  
<script>
import { defineComponent } from "vue";
import { IconPark } from "@icon-park/vue-next/es/all";

export default defineComponent({

    name: 'CustomMulti',
    components: {
        'icon-park': IconPark,
    },
    props: {
        custom_options: {
            type: Array
        }
    },
    data() {
        return {
            options: [
                { label: '全部', value: 'all' },
                { label: '选项1', value: 'option1' },
                { label: '选项2', value: 'option2' },
                { label: '选项3', value: 'option3' },
                { label: '选项4', value: 'option4' },
            ],
            selectedOptions: [],
        };
    },
    methods: {
        isSelected(optionValue) {
            return this.selectedOptions.includes(optionValue);
        },
        // toggleOption(optionValue) {
        //     if (this.isSelected(optionValue)) {
        //         this.deselectOption(optionValue);
        //     } else {
        //         this.selectedOptions.push(optionValue);
        //     }
        // },
        toggleOption(optionValue) {
            if (this.isSelected(optionValue)) {
                this.deselectOption(optionValue);
            } else {
                if (optionValue === 'all') {
                    this.selectedOptions = [];
                } else {
                    this.deselectOption('all');
                }
                this.selectedOptions.push(optionValue);
            }
        },
        deselectOption(optionValue) {
            this.selectedOptions = this.selectedOptions.filter(value => value !== optionValue);
        },
    },
});
</script>