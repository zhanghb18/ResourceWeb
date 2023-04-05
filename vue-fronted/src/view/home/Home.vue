<template>


    <div class="background" @mousewheel="handleScroll($event)">
        <div class="Home_head" >
            <div id="serchr_form_header" :class="{ s_form_header: true }">
                        <el-row>
                            <el-col :span="4">
                                <div :class="{ Logo_circle: true ,'comp_go': compgo}" v-bind:style="{fontSize: fontSize + 'px' ,width: Width_C+'px', height:Height_C+'px'}"  >
                                     <!-- 绑定动画，同时修改大小 -->
                                    <img src="../../assets/logo.png" v-bind:style="{width: Width_P + '%', height:Height_P+ '%'}">
                                </div>
                            </el-col>
                            <el-col :span="20">
                                <div :class="{ logo: true, 'comp_logo_go': complogogo }" v-bind:style="{fontSize: fontSize + 'px'}">文字LOGO</div>
                                <!-- 绑定动画 -->
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
        </div>
        <transition v-on:before-enter="beforeEnter"
    v-on:enter="enter" name="home-transition" mode="out-in">
            <div class="home" v-if="isHome">
                <div id="search_form" class="s_form">
  
                    <div class="s_tailer">
                        <el-row justify="center">
                            <el-col :span="5">
                                <IconCircle :imgSrc="require('../../assets/home/注册.png')" text="注册"></IconCircle>
                            </el-col>
                            <el-col :span="5">
                                <IconCircle :imgSrc="require('../../assets/home/登录.png')" text="登录" @click="gotoLogin()">
                                </IconCircle>
                            </el-col>
                            <el-col :span="5">
                                <IconCircle :imgSrc="require('../../assets/home/联系我们.png')" text="联系"></IconCircle>
                            </el-col>
                            <el-col :span="5">
                                <IconCircle :imgSrc="require('../../assets/home/打赏.png')" text="打赏"></IconCircle>
                            </el-col>
                        </el-row>
                    </div>
                </div>

            </div>
            <div v-else class="DownPage"  >
                <div>
                    <AcgPage></AcgPage>
                </div>
            </div>
        </transition>
        <transition name="login-form-transition">
            <div class="login_form" v-if="isLogin">
                <LoginForm @loginInComfirmed="loginInComfirmed" @closeForm="closeLoginForm"></LoginForm>
            </div>
        </transition>
    </div>
</template>

<script>
import LoginForm from "../LoginForm.vue";

import IconCircle from "./IconCircle.vue";
import AcgPage from "../acgpage/AcgPage.vue"

export default {
    name: "Home",
    components: {
        LoginForm,
        IconCircle,
        AcgPage,
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
            fontSize:50,
            
        }
    },
    methods: {
        gotoLogin() {
            this.isLogin = true
        },
        loginInComfirmed() {
            this.isLogin = false
        },
        closeLoginForm(e) {
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
                        //修改bool值以开启动画
                        const that = this;
                        setTimeout(function(){ that.isHome = false; }, 10);
                        //设置在滚动1.5s后切换页面，用于保证前面的动画完成
                    
                    this.Width_C/=2
                    this.Width_P/=2
                    this.Height_C/=2
                    this.Height_P/=2
                    this.fontSize/=2
                    }

                }
                else if (e.deltaY < 0){
                    if (!this.isHome){
                        this.compgo=false

                        this.compsearchgo=false
                        this.complogogo=false
                    this.isHome = true
                    this.Width_C*=2
                    this.Width_P*=2
                    this.Height_C*=2
                    this.Height_P*=2
                    this.fontSize*=2}

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
.Home_head{
    background: url("../../assets/home/background.jpg");
    min-height: 50%;
}
.home {
    background: url("../../assets/home/background.jpg");
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
    animation:  comp_go 1.5s;
}

.comp_search_go{
    animation:  comp_search_go 1.5s;
}

.comp_logo_go{
    animation:  comp_logo_go 1.5s;
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
.home-transition-leave-to{
    opacity: 0;
    top: -10%;
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

/*以下为动画*/

@keyframes comp_go {
    to{
        transform:translateX(-600px)

    }
}

@keyframes comp_logo_go {
    to{
        transform:translateX(-700px)

    }
}

@keyframes comp_search_go {
    to{

    }
}

</style>