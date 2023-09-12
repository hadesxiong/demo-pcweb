// 用于供别的业务逻辑进行token刷新时调用

export async function refreshToken() {
    const refresh_token = localStorage.getItem('refresh')
    console.log(refresh_token)
}