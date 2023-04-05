import router from '../router';
import axios from 'axios';
import api from '@/api'
import {getQueryVariable} from './getQueryVariable.js'

/** 
 * 跳转404页面，页面丢失
 */
const toNotFound = () => {
    console.log('to404')
    router.push({
        path: '/404',        
        query: {
            single: getQueryVariable('single'),
            token: getQueryVariable('token')
        }
    });
}

// 创建axios实例
var instance = axios.create({
    timeout: 5 * 60 * 1000,
});
// var instance = axios.create({ timeout: 10000 * 12 });
// 设置post请求头
instance.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
instance.defaults.timeout = 5 * 60 * 1000;

export default instance;
