<template>
    <div class="mr_16 d_flex gap_8 lh_30 fai_b">
        <span>🌞🌞🌞</span>
        <span class="fc_l2">你好,</span>
        <span class="fc_brand6">{{ user_name }}</span>
        <span class="fc_l2">Long May the Sun Shine.</span>
        <span>🌞🌞🌞</span>
    </div>
    <div class="d_flex fai_c">
        <a-avatar shape="circle" size="medium" :style="{backgroundColor:user_color,fontWeight:500}">{{ user_name.substring(0,1) }}</a-avatar>
    </div>
</template>

<style>
@import url('@/assets/style/common.css');
</style>

<script>
import { defineComponent, ref } from 'vue';
import { Avatar } from 'ant-design-vue';

export default defineComponent({
    name:'HeaderOther',
    components: {
        'a-avatar': Avatar,
    },
    setup() {
        const user_name = localStorage.getItem('name_1')
        return {
            user_name,
            user_color: ref('#165DFF')
        };
    }
});

</script>