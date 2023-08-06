<template>
    <div class="c-logo_con">
        <img src="../../../assets/logo.png" class="c-logo_icon mt_16 mb_16 mr_16">
        <div class="c-logo_title">业绩展示系统</div>
    </div>
</template>

<style>
@import url('../../../assets/style/common.css');

.c-logo_con {
    display:flex;
}
.c-logo_icon {
    width: 30px;
    height: 30px;
}
.c-logo_title {
    font-size:18px;
    font-weight:500;
    color: #1D2129;
}
</style>
<script>
import { defineComponent } from 'vue';

export default defineComponent({
    name:'HeaderLogo',
    data(){
        return {}
    },
    setup(){}
});
</script>