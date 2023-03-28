<template>
    <div class="background" @mousewheel="handleScroll($event)">
        <transition v-on:before-enter="beforeEnter"
    v-on:enter="enter" name="home-transition" mode="out-in">
            <div class="home" v-if="isHome">
                <div id="search_form" class="s_form">
                    <div id="serchr_form_header" :class="{ s_form_header: true, 'comp_go': compgo }">
                        <el-row>
                            <el-col :span="4">
                                <div class="Logo_circle" v-bind:style="{width: Width_C+'px', height:Height_C+'px'}">
                                    <img src="../../assets/logo.png" v-bind:style="{width: Width_P + '%', height:Height_P+ '%'}">
                                </div>
                            </el-col>
                            <el-col :span="20">
                                <div :class="{ logo: true, 'comp_logo_go': complogogo }">文字LOGO</div>
                            </el-col>
                        </el-row>
                    </div>
                    <div id="search_content" class="s_content">
                        <el-row>
                            <el-col :span="22">
                                <div style="display: flex; align-items: center; padding-right: 10px;">
                                    <input type="text" :class="{ search_input: true, 'comp_search_go': compsearchgo }" v-model="searchText" placeholder="请输入关键字"
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
            <div v-if="!isHome" class="DownPage"  >
                    <div id="serchr_form_header" class="s_form_header">
                        <el-row>
                            <el-col :span="4">
                                <div class="Logo_circle" v-bind:style="{width: Width_C+'px', height:Height_C+'px'}">
                                    <img src="../../assets/logo.png" v-bind:style="{width: Width_P+ '%', height:Height_P+ '%'}">
                                </div>
                            </el-col>
                            <el-col :span="4">
                                <div class="logo2">文字LOGO</div>
                            </el-col>
                        </el-row>
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
            compgo:false,
            compsearchgo:false,
            complogogo:false,
            isHome: true,
            
            isLogin: false,
            searchText: '',
            isOnIcon: false,
            Width_C:125,
            Height_C:125,
            Width_P:60,
            Height_P:60,
            
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
            
            var scrollY = e.deltaY;
            if (!this.isLogin) {
                if (scrollY > 0) {
                    
                    if (this.isHome){
                        this.compgo=true

                        this.compsearchgo=true
                        this.complogogo=true
                        const that = this;
                        setTimeout(function(){ that.isHome = false; }, 300);
                    
                    this.Width_C/=2
                    this.Width_P/=2
                    this.Height_C/=2
                    this.Height_P/=2
                    }

                }
                else if (e.deltaY < 0){
                    if (!this.isHome){
                    this.isHome = true
                    this.Width_C*=2
                    this.Width_P*=2
                    this.Height_C*=2
                    this.Height_P*=2}

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

.comp_go{
    animation:  comp_go 1s;
}

.comp_search_go{
    animation:  comp_search_go 1s;
}

.comp_logo_go{
    animation:  comp_logo_go 1s;
}
.s_form_header {
    
    margin: auto;
    padding-bottom: 30px;
    padding-left: 20px;
    padding-right: 20px;
}

.logo-active{
    animation:  comp_go 1s;
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
    border-radius: 50%;
    background-color: #fff;
    display: flex;
    justify-content: center;
    align-items: center;
}

.Logo_circle img {

    object-fit: contain;
}

.logo {
    font-size: 50px;
    padding-left: 10px;
    padding-top: 35px;
    letter-spacing: 6px;
    font-family: 'DOUYU', cursive;
    color: black;
}

.logo2 {
    position: absolute; /* 设置绝对定位 */
    top: 20px; /* 距离顶部为0 */
    left: 45px; /* 距离左边为0 */
    font-size: 20px;
    font-family: 'DOUYU', cursive;
    color: black;
}

.tooltip {
    display: inline;
    position: absolute;
    top: 20%;
    left: 70%;
    width: 60px;
    border-radius: 50px;
    padding: 5px;
    background-color: #794B9C;
    color: #fff;
    z-index: -2;
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
    transition: all 1s;
}
.home-transition-leave-to{
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

.login-form-transition-enter-active{
    transition: opacity 0.5s 
}
.login-form-transition-leave-active {
    transition: opacity 0.5s 
}

.login-form-transition-enter-from{
    opacity: 0
}

.login-form-transition-leave-to {
    opacity: 0
}


@keyframes comp_go {
    to{
        transform:translateX(-80%)
        translateY(-90%)
    }
}

@keyframes comp_logo_go {
    to{
        transform:translateX(-70%)
        translateY(-90%)
    }
}

@keyframes comp_search_go {
    to{
        transform:translateY(-90%)
    }
}

</style>