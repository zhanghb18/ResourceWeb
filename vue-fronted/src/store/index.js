//使用Vuex进行状态管理
import { createStore } from 'vuex'

//登录状态管理
const tokenOptions = {
    // namespaced: true, //目前还没弄懂命名空间，先注释掉
    state: {
        token: "",
    },
    getters: {
        //计算属性，当token有值时，用户已经登录
        userLoginStatus(state) {
            return state.token.length > 0;
        }
    },
    mutations: {
        updateToken(state) {
            state.token = sessionStorage.getItem("token");
        },
    },
    actions: {
    },
}

export default new createStore({
    modules: {
        tokenAbout: tokenOptions,
    }
});
