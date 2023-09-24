// 封装axios方法
import axios from 'axios';

function createApiInstance() {
    const api = axios.create({
        baseURL: process.env.VUE_APP_BASE_URL
    });
    api.defaults.headers.common['Authorization'] = localStorage.getItem('access');
    return api;
}

export function api() {
    return createApiInstance();
}