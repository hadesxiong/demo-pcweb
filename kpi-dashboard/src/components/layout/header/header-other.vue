<template>
    <div class="func_con mr_16">
        <a-button shape="circle" class="func_btn">
            <template #icon><icon-park type="Remind" class="func_icon" size="12"></icon-park></template>
        </a-button>
    </div>
    <div class="avatar_con">
        <a-avatar shape="circle" size="medium" :style="{backgroundColor:userColor,fontWeight:500}">{{ userName }}</a-avatar>
    </div>
</template>

<style>
@import url('../../../assets/style/common.css');

.avatar_con,.func_con {
    display: flex;
    align-items: center;
}
.func_btn {
    background-color: #F2F3F5;
    border-color: transparent;
    color: #4E5969;
    font-weight: 500;
}
.func_icon {
    display: flex !important;
    align-items: center;
    justify-content: center;
}
</style>

<script>
import { defineComponent } from 'vue';
import { IconPark } from "@icon-park/vue-next/es/all";

export default defineComponent({
    name:'HeaderOther',
    components: {
        IconPark
    },
    data(){
        // 测试数据
        this.userName = 'N';
        this.userColor = '#165DFF' ;
        return {};
    },
    setup() {
        return {};
    }
});

</script>