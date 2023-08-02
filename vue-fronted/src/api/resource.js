/**
 * 番剧接口列表
 */

import base from './base'; // 导入接口域名列表
import axios from "@/utils/http"; // 导入http中创建的axios实例

const resource = {
    // 获取追番周历
    getAnimeCalendar(params) {
        return axios.post(`${base.baseURL}/resource/getAnimeCalendar`, params);
    },

}

export default resource;