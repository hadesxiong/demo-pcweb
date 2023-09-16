<template>
    <div class="c-func_con mr_16">
        <a-button shape="circle" class="c-func_btn">
            <template #icon>
                <icon-park type="Remind" class="c-func_icon" size="12"></icon-park>
            </template>
        </a-button>
    </div>
    <div class="c-avatar_con">
        <a-avatar shape="circle" size="medium" :style="{backgroundColor:userColor,fontWeight:500}">{{ userName }}</a-avatar>
    </div>
</template>

<style>
@import url('@/assets/style/common.css');

.c-avatar_con,.c-func_con {
    display: flex;
    align-items: center;
}
.c-func_btn {
    background-color: #F2F3F5;
    border-color: transparent;
    color: #4E5969;
    font-weight: 500;
}
.c-func_icon {
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
        'icon-park':IconPark
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