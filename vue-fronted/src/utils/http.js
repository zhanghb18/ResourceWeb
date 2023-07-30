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

/** 
 * 请求拦截器 
 * 每次请求前，如果存在token则在请求头中携带token 
 */ 
instance.interceptors.request.use(    
    config => {      
        if(config.url !== "/user/login"){  // 判断请求是否是登录接口
            config.headers.token = localStorage.getItem("token"); // 如果不是登录接口，就给请求头里面设置token
        }
        return config;
    },    
    error => {
        return Promise.error(error)
    }
)

export default instance;
