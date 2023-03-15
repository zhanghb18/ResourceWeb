<template>
    <div class="home">
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
                        <IconCircle imgSrc="../assets/注册.png" text="注册"></IconCircle>
                    </el-col>
                    <el-col :span="5">
                        <div class="icon_circle" @mouseover="iconMouseOver(2)" @mouseout="iconMouseOut(2)"
                            @click="gotoLogin">
                            <img src="../assets/登录.png">
                            <div class="tooltip" style="display: none;">登录</div>
                        </div>
                    </el-col>
                    <el-col :span="5">
                        <div class="icon_circle" @mouseover="iconMouseOver(3)" @mouseout="iconMouseOut(3)">
                            <img src="../assets/联系我们.png">
                            <div class="tooltip" style="display: none;">联系</div>
                        </div>
                    </el-col>
                    <el-col :span="5">
                        <div class="icon_circle" @mouseover="iconMouseOver(4)" @mouseout="iconMouseOut(4)">
                            <img src="../assets/打赏.png">
                            <div class="tooltip" style="display: none;">打赏</div>
                        </div>
                    </el-col>
                </el-row>
            </div>
        </div>
    </div>
    <transition name="login-form-transition">
        <div class="login_form" v-if="isLogin">
            <LoginForm @loginInComfirmed="loginInComfirmed" @clickOutside="clickOutside"></LoginForm>
        </div>
    </transition>
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
        // 鼠标移入事件
        iconMouseOver(index) {
            const iconCircle = document.getElementsByClassName('icon_circle')[index - 1];
            const tooltip = iconCircle.querySelector('.tooltip');
            // tooltip.style.display = 'inline';
            this.isOnIcon = true;
            // 移动图标和新图标的位置
            iconCircle.style.transform = 'scale(1.2) translateX(-10px)';
            // 添加过渡动画
            iconCircle.style.transition = 'transform 0.3s';
        },
        iconMouseOut(index) {
            const iconCircle = document.getElementsByClassName('icon_circle')[index - 1];
            const tooltip = iconCircle.querySelector('.tooltip');
            // 隐藏新图标
            // tooltip.style.display = 'none';
            this.isOnIcon = false
            iconCircle.style.transform = 'scale(1) translateX(0)';
            // 移除过渡动画
            iconCircle.style.transition = 'none';
        },
    }
}
</script>

<style scoped>
@import '../../assets/font/font.css';

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
    border-radius: 15px;
    border: none;
    box-shadow: none;
    padding: 5px 20px;
    font-size: 15px;
    outline-color: none;
}

.search_input:focus {
    border-color: #409eff;
    box-shadow:
        inset 0 -3em 3em rgba(168, 167, 167, 0.1),
        0 0 0 2px rgb(255, 255, 255),
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
    padding-left: 30px;
    font-family: 'DOUYU', cursive;
    font-style: italic;
    font-weight: bold;
    color: white;
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

.icon_circle {
    position: relative;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background-color: #fff;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    z-index: 2;
}

.icon_circle img {
    width: 60%;
    height: 60%;
    object-fit: contain;
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