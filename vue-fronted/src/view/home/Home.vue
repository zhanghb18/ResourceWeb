<template>
    <div class="background" @mousewheel="handleScroll($event)">
        <transition name="home-transition">
            <div class="home" v-if="isHome">
                <div id="search_form" class="s_form">
                    <div id="serchr_form_header" class="s_form_header">
                        <el-row>
                            <el-col :span="4">
                                <div class="Logo_circle">
                                    <img src="../../assets/logo.png">
                                </div>
                            </el-col>
                            <el-col :span="20">
                                <div class="logo">文字LOGO</div>
                            </el-col>
                        </el-row>
                    </div>
                    <div id="search_content" class="s_content">
                        <el-row>
                            <el-col :span="22">
                                <div style="display: flex; align-items: center; padding-right: 10px;">
                                    <input type="text" class="search_input" v-model="searchText" placeholder="请输入关键字"
                                        @focus="clearPlaceholder">
                                </div>
                            </el-col>
                            <el-col :span="2">
                                <div class="search_circle">
                                    <img src="../../assets/logo.png">
                                </div>
                            </el-col>
                        </el-row>
                    </div>
                    <div class="s_tailer">
                        <el-row justify="center">
                            <el-col :span="5">
                                <IconCircle :imgSrc="require('../assets/注册.png')" text="注册"></IconCircle>
                            </el-col>
                            <el-col :span="5">
                                <IconCircle :imgSrc="require('../assets/登录.png')" text="登录" @click="gotoLogin()">
                                </IconCircle>
                            </el-col>
                            <el-col :span="5">
                                <IconCircle :imgSrc="require('../assets/联系我们.png')" text="联系"></IconCircle>
                            </el-col>
                            <el-col :span="5">
                                <IconCircle :imgSrc="require('../assets/打赏.png')" text="打赏"></IconCircle>
                            </el-col>
                        </el-row>
                    </div>
                </div>
            </div>
        </transition>
        <transition name="login-form-transition">
            <div class="login_form" v-if="isLogin">
                <LoginForm @loginInComfirmed="loginInComfirmed" @clickOutside="clickOutside"></LoginForm>
            </div>
        </transition>
    </div>
</template>

<script>
import LoginForm from "../LoginForm.vue";
import IconCircle from "./IconCircle.vue";

export default {
    name: "Home",
    components: {
        LoginForm,
        IconCircle,
    },
    data() {
        return {
            isHome: true,
            isLogin: false,
            searchText: '',
            isOnIcon: false,
        }
    },
    methods: {
        gotoLogin() {
            this.isLogin = true
        },
        loginInComfirmed() {
            this.isLogin = false
        },
        clickOutside(e) {
            this.isLogin = false
        },
        clearPlaceholder() {
            this.searchText = '';
        },
        handleScroll(e) {
            //TODO: 存在BUG，home的背景会在移动完成后才发生透明度突变
            var scrollY = e.deltaY;
            if (!this.isLogin) {
                if (scrollY > 0) {
                    this.isHome = false
                }
                else {
                    this.isHome = true
                }
            }
        }
    },
}
</script>

<style scoped>
@import '../../assets/font/font.css';

.background {
    min-height: 100%;
    min-width: 100%;
}

.home {
    background: url("../assets/background.jpg");
    /* background-position: center center;
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-size: cover;
    width:100%;
    height:100%;
    position:fixed; */
    /* background-size:100% 100%; */
    min-height: 100%;
    min-width: 100%;
    background-size: cover;
    background-attachment: fixed;
    background-repeat: no-repeat;
    position: absolute;
    z-index: 1;
}

.s_form {
    width: 30%;
    margin: auto;
    padding-top: 200px;
}

.s_form_header {
    margin: auto;
    padding-bottom: 30px;
    padding-left: 20px;
    padding-right: 20px;
}

.s_content {
    padding-bottom: 30px;
}

.search_input {
    box-sizing: border-box;
    width: 100%;
    height: 40px;
    border-radius: 5px;
    border: none;
    box-shadow: none;
    padding: 5px 20px;
    font-size: 15px;
    outline-color: none;
}

.search_input:focus {
    border-color: #409eff;
    box-shadow:
        inset 0 -3em 3em #f2f2f2,
        0.3em 0.3em 1em rgba(155, 155, 155, 0.3);
    outline: 0px;
}

.search_input::placeholder {
    color: #999;
    font-size: 15px;
    padding-left: 0px;
}

.Logo_circle {
    width: 125px;
    height: 125px;
    border-radius: 50%;
    background-color: #fff;
    display: flex;
    justify-content: center;
    align-items: center;
}

.Logo_circle img {
    width: 60%;
    height: 60%;
    object-fit: contain;
}

.logo {
    font-size: 50px;
    padding-left: 10px;
    padding-top: 35px;
    letter-spacing: 6px;
    font-family: 'DOUYU', cursive;
    color: white;
}

.search_circle {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background-color: #fff;
    display: flex;
    justify-content: center;
    align-items: center;
    line-height: 30px;
}

.search_circle img {
    width: 60%;
    height: 60%;
    object-fit: contain;
}
.home-transition-enter-active, .home-transition-leave-active{
    transition: all 0.5s;
}
.home-transition-enter-from, .home-transition-leave-to{
    opacity: 0;
    top: -100%;
}
.home-transition-enter-to, .home-transition-leave-from{
    opacity: 1;
    top: 0%;
}
/* .search_input:focus{
    border-color: #4e6ef2 !important;
    opacity: 1;
}
.search_input:hover{
    border-color: #a7aab5 ;
} */
.login_form {
    position: absolute;
    z-index: 2;
}

.login-form-transition-enter-active,
.login-form-transition-leave-active {
    transition: opacity 0.5s
}

.login-form-transition-enter-from,
.login-form-transition-leave-to {
    opacity: 0
}
</style>