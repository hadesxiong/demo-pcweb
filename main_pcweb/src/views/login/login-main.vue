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
                        <div class="d_flex fd_c w_p100">
                            <a-form :model="formContent" ref="formObj">
                                <a-form-item :rules="[{ required: true, trigger:'blur', message: '用户名不能为空' }]" name="username" class="ta_l">
                                    <a-input v-model:value="formContent.username" placeholder="请输入用户名" size="large" :bordered="false" class="bg_l3 br_2" name="username" autocomplete="username">
                                        <template #prefix>
                                            <icon-user fill="#4E5969" size="16" class="c-func_icon"></icon-user>
                                        </template>
                                    </a-input> 
                                </a-form-item>
                                <a-form-item :rules="[{ required: true, trigger:'blur', message: '密码不能为空' }]" name="password" class="ta_l">
                                    <a-input-password v-model:value="formContent.password" placeholder="请输入密码" size="large" :bordered="false" class="bg_l3 br_2" name="password" autocomplete="current-password">
                                        <template #prefix>
                                            <icon-lock fill="#4E5969" size="16" class="c-func_icon"></icon-lock>
                                        </template>
                                    </a-input-password>
                                </a-form-item>
                            </a-form>
                        </div>
                        <div class="d_flex fai_c jc_sb lh_32 w_p100" style="margin-top: -20px;">
                            <a-checkbox v-model:checked="pw_store">记住密码</a-checkbox>
                            <a class="fc_brand6" @click="forgetPassword">忘记密码</a>
                        </div>
                        <div class="w_p100 h_32 lh_32">
                            <a-button type="primary" class="bg_brand6 w_p100 h_38 font_16 fw_500" @click="checkForm">登陆</a-button>
                        </div>
                    </div>
                </div>
            </div>
        </a-layout-content>
    </a-layout>
</template>

<style>
@import url('@/assets/style/common.css');
@import url('@/assets/style/colorset.css');
@import url('@/assets/style/overwrite.css');
</style>

<style scoped>
.ant-layout-content {
    padding: 0px !important;
    height: 100vh;
}

.left_con {
    width: 550px;
    padding: 40px;
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

.ant-input-affix-wrapper:not(.ant-input-affix-wrapper-disabled):hover {
    background-color: #f2f3f5;
}

.ant-btn-primary:not(:disabled):hover {
    background-color: rgba(22, 93, 255, 0.8);
}

.ant-checkbox-checked .ant-checkbox-inner {
    background-color: #165dff !important;
    border-color: #165dff !important;
}

</style>

<script>
import { defineComponent,reactive,ref } from 'vue';
import { UserPositioning, Lock } from '@icon-park/vue-next';
import { Layout, LayoutContent, Input, InputPassword, Checkbox, Button, Form, FormItem, message } from 'ant-design-vue';

import axios from 'axios';
import { api } from '@/utils/commonApi.js';
import { useRouter } from 'vue-router';
import CryptoJS from 'crypto-js';

// const myApi = api();
const login_api = axios.create({
    baseURL: process.env.VUE_APP_BASE_URL
})

export default defineComponent({
    name: 'LoginMain',
    components: {
        'icon-user': UserPositioning,
        'icon-lock': Lock,
        'a-layout': Layout,
        'a-layout-content': LayoutContent,
        'a-form': Form,
        'a-form-item': FormItem,
        'a-input': Input,
        'a-input-password': InputPassword,
        'a-checkbox': Checkbox,
        'a-button': Button
    },
    data() {
        return {
            key:process.env.VUE_APP_ENCRYPTED_KEY,
            iv:process.env.VUE_APP_ENCRYPTED_IV
        }
    },
    setup() {
        return {
            formContent: reactive({
                username: '',
                password: '',
            }),
            btnLoading: ref(false),
            router:useRouter(),
            pw_store: ref(false)
        }
    },
    methods: {
        async userLogin(user,pw) {
            // 密码加密
            const encrypted_pw = CryptoJS.enc.Utf8.parse(pw)
            const encrypted_key = CryptoJS.enc.Utf8.parse(this.key)
            const encrypted_iv = CryptoJS.enc.Utf8.parse(this.iv)
            const encrypted_data = CryptoJS.AES.encrypt(encrypted_pw,encrypted_key,{iv:encrypted_iv }).toString();
            const user_data = {notes:user,pw:encrypted_data}

            const login_res = await login_api.post('/api/auth/userLogin',user_data,{ withCredentials: true })
            // 处理结果
            if (login_res.data.code == 100) {
                // console.log(login_res)
                localStorage.setItem('refresh',login_res['headers'].get('x-refresh-token'));
                localStorage.setItem('access',login_res['headers'].get('authorization'));
                localStorage.setItem('notes_id',this.formContent.username);
            } else {
                console.log(login_res.data)
            }
            return login_res.data
        },
        async getUserInfo(notes_id) {
            const tempApi = api();
            const user_res = await tempApi.get('/api/auth/getUserInfo',{params:{user:notes_id}});
            if (user_res.data.code == 200) {
                localStorage.setItem('user_name',user_res.data.data.name_1);
                localStorage.setItem('org_num',user_res.data.data.org_num);
                localStorage.setItem('user_character',user_res.data.data.character);
                localStorage.setItem('org_name',user_res.data.data.org_name)
            } else {
                console.log(user_res.data)
            }
            return user_res.data;
        },
        async checkForm() {
            const check_res = await this.$refs.formObj.validate()
            message.loading({
                content:'正在登陆,请稍后...',
                duration:0,
                class:'msg_loading'
            });
            if (check_res) {
                const login_res = await this.userLogin(this.formContent.username,this.formContent.password);
                if (login_res.code == 100) {
                    await this.getUserInfo(this.formContent.username);
                    message.destroy();
                    message.success({
                        content:'验证成功,正在跳转...',
                        duration: 1.5,
                        class:'msg_loading',
                        onClose: async ()=>{
                            this.$router.push('/dashboard-main')
                        }
                    })
                } else {
                    message.destroy();
                    message.error({
                        content:'验证失败,请检查用户名或者密码...',
                        duration: 3,
                        class:'msg_loading'
                    })
                }
            } else { 
                console.log('校验不通过.')
            }
        },
        forgetPassword() {
            message.warning({
                content:'该演示版本不提供密码重置逻辑',
                duration: 0,
                class:'msg_loading'
            })
        },
    }
})

</script>