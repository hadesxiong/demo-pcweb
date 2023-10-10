<template>
    <div class="mr_16 d_flex gap_8 lh_30 fai_b">
        <span>🌞🌞🌞</span>
        <span class="fc_l2">你好,</span>
        <span class="fc_brand6">{{ name_1 }}</span>
        <span class="fc_l2">Long May the Sun Shine.</span>
        <span>🌞🌞🌞</span>
    </div>
    <a-popover placement="bottomRight" arrow-point-at-center>
        <template #content>
            <a @click="userLogout" class="fc_brand6">退出登陆</a>
        </template>
        <div class="d_flex fai_c">
            <a-avatar shape="circle" size="medium" :style="{backgroundColor:user_color,fontWeight:500}">{{ name_1.slice(0,1) }}</a-avatar>
        </div>
    </a-popover>
</template>

<style>
@import url('@/assets/style/common.css');
</style>

<script>
import { defineComponent, ref } from 'vue';
import { Avatar, Popover } from 'ant-design-vue';

export default defineComponent({
    name:'HeaderOther',
    components: {
        'a-avatar': Avatar,
        'a-popover': Popover
    },
    props: {
        user_name: {type:String,default:'User'}
    },
    setup(props) {
        return {
            user_color: ref('#165DFF'),
            name_1: ref(props.user_name)
        };
    },
    methods: {
        userLogout() {
            localStorage.clear();
            location.reload();
        }
    }
});

</script>