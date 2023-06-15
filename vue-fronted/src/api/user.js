/**
 * 用户接口列表
 */

import base from './base'; // 导入接口域名列表
import axios from "@/utils/http"; // 导入http中创建的axios实例

const user = {
    // 发送验证码
    SendPin(params) {
        return axios.post(`${base.baseURL}/user/sendPin`, params);
    },
    // 用户注册
    UserRegister(params) {
        return axios.post(`${base.baseURL}/user/register`, params);
    },
    // 用户登录
    UserLogin(params) {
        return axios.post(`${base.baseURL}/user/login`, params);
    },
    // 获取用户信息
    getUserInfo(params) {
        return axios.post(`${base.baseURL}/user/getUserInfo`, params)
    }
}

export default user;