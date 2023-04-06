/**
 * 用户接口列表
 */

import base from './base'; // 导入接口域名列表
import axios from "@/utils/http"; // 导入http中创建的axios实例

const user = {
    //用户注册
    UserRegister(params) {
        return axios.post(`${base.baseURL}/user/register`, params);
    }
}

export default user;