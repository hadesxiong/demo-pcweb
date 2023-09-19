// 用于每个页面验证access_token

import jwtDecode from "jwt-decode";

export function checkAuth() {
    const ac_token = localStorage.getItem('access');
    if (ac_token) {
        try {
            const decoded_token = jwtDecode(ac_token);
            const exp_time = decoded_token.exp * 1000;
            const cur_time = Date.now();
    
            if (cur_time < exp_time) { return true }
        }
        catch(error) {
            console.log('fail to decode jwt token.',error);
        }
    }
    return false;
}