//使用Vuex进行状态管理
import { createStore } from 'vuex'

//登录状态管理
const tokenOptions = {
    // namespaced: true, //目前还没弄懂命名空间，先注释掉
    state: {
        token: "",
        avatar: "",
    },
    getters: {
        //计算属性，当token有值时，用户已经登录
        userLoginStatus(state) {
            if (state.token){
                return state.token.length > 0;
            }
            else{
                return false;
            }
        },
        //计算属性，获取用户头像
        getAvatar(state) {
            if (state.avatar){
                return state.avatar;
            }
            else{
                return "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png";
            }
        },
    },
    mutations: {
        updateAll(state) {
            state.token = localStorage.getItem("token");
            state.avatar = localStorage.getItem("avatar");
        },
        updateToken(state) {
            state.token = localStorage.getItem("token");
        },
        updateAvatar(state) {
            state.avatar = localStorage.getItem("avatar");
        }
    },
    actions: {
    },
}

export default new createStore({
    modules: {
        tokenAbout: tokenOptions,
    }
});
