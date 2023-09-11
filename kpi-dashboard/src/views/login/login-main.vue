<template>
    <a-layout>
        <a-layout-content>
            <div class="bg_white w_p100 h_p100 d_flex">
                <div class="left_con h_p100 d_flex fd_c">
                    <div class="h_32 d_flex fai_c">
                        <img src="../../assets/logo.png" class="c-logo_icon mr_16">
                        <div class="fc_l5 fw_500 font_20">业绩展示系统</div>
                    </div>
                </div>
                <div class="right_con d_flex fd_c fai_c jc_c">
                    <div class="right_main d_flex fd_c fai_fs gap_20">
                        <div class="font_24 fw_500 mb_16 lh_32 w_p100 ta_l fc_l1"><span class="fc_l2 mr_8">欢迎登陆</span>业绩展示系统
                        </div>
                        <div class="d_flex fd_c gap_20 w_p100">
                            <a-input v-model:value="user_name" placeholder="请输入用户名" size="large" :bordered="false" class="bg_l3 br_2">
                                <template #prefix>
                                    <icon-park type="UserPositioning" fill="#4E5969" size="16"
                                        class="c-func_icon"></icon-park>
                                </template>
                            </a-input>
                            <a-input-password v-model:value="password" placeholder="请输入密码" size="large" :bordered="false" class="bg_l3 br_2">
                                <template #prefix>
                                    <icon-park type="Lock" fill="#4E5969" size="16" class="c-func_icon"></icon-park>
                                </template>
                            </a-input-password>
                        </div>
                        <div class="d_flex fai_c jc_sb lh_32 w_p100">
                            <a-checkbox>记住密码</a-checkbox>
                            <a class="fc_brand6">忘记密码</a>
                        </div>
                        <div class="w_p100 h_32 lh_32">
                            <a-button type="primary" class="bg_brand6 w_p100 h_38 font_16 fw_500" @click="userLogin(user_name,password)">登陆</a-button>
                        </div>
                    </div>
                </div>
            </div>
        </a-layout-content>
    </a-layout>
</template>

<style>
@import url('../../assets/style/common.css');
@import url('../../assets/style/colorset.css');
@import url('../../assets/style/overwrite.css');
</style>

<style scoped>
.ant-layout-content {
    padding: 0px !important;
    height: 100vh;
}

.left_con {
    width: 550px;
    padding: 40px;
    /* background: linear-gradient(163.85deg, #1d2129 0%, #00308f 100%); */
    background: url('../../assets/index.webp');
    background-size: cover
}

.right_con {
    width: calc(100% - 550px);
    height: 100%;
    padding: 40px;
    background: linear-gradient(163.85deg, rgba(174, 198, 222, 0.2) 0%, #ffffff 20%);
}

.right_main {
    width: 320px;
}

.c-logo_icon {
    width: 40px;
    height: 40px;
}

.c-logo_index {
    width: 320px;
    height: auto;
}

.c-func_icon {
    display: flex !important;
    align-items: center;
    justify-content: center;
    margin-right: 8px;
}

:where(.css-dev-only-do-not-override-eq3tly).ant-input-affix-wrapper:not(.ant-input-affix-wrapper-disabled):hover {
    background-color: #f2f3f5;
}

:where(.css-dev-only-do-not-override-eq3tly).ant-btn-primary:not(:disabled):hover {
    background-color: rgba(22, 93, 255, 0.8);
}

:where(.css-dev-only-do-not-override-eq3tly).ant-checkbox-checked .ant-checkbox-inner {
    background-color: #165dff !important;
    border-color: #165dff !important;
}
</style>

<script>
import { defineComponent,ref } from 'vue';
import { IconPark } from "@icon-park/vue-next/es/all";
import axios from 'axios';
import { useRouter } from 'vue-router';

export default defineComponent({
    name: 'LoginMain',
    components: {
        'icon-park': IconPark
    },
    setup() {
        return {
            user_name:ref(''),
            password: ref(''),
            router:useRouter()
        }
    },
    methods: {
        async userLogin(user,pw) {
            const user_data = {notes:user,pw:pw}
            const login_res = await axios.post('http://localhost:3000/api/auth/userLogin',user_data,{ withCredentials: true })
            localStorage.setItem('refresh',login_res['headers'].get('authorization'))
            localStorage.setItem('access',login_res['headers'].get('x-refresh-token'))
            if (login_res.data.code == 0) {
                this.router.push('/dashboard-main')
            }
        }
    }
})

</script>