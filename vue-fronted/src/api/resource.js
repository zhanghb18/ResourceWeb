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
    // 获取番剧列表
    getAnimeTable(params) {
        return axios.post(`${base.baseURL}/resource/getAnimeTable`, params);
    },
    // 获取番剧详情
    getBanguInfo(params) {
        return axios.post(`${base.baseURL}/bangu/getBanguInfo`, params);
    },
    getSingleResource(params) {
        return axios.post(`${base.baseURL}/bangu/getSingleResource`, params);
    },
    getResourceInfo(params) {
        return axios.post(`${base.baseURL}/bangu/getResourceInfo`, params);
    },
}

export default resource;