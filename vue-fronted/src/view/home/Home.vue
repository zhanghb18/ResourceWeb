<template>
    <div class="home" :style="{opacity: opa}" @mousewheel="handleScroll($event)">
        <div id="search_form" class="s_form">
            <div id="serchr_form_header" class="s_form_header">
                <el-row>
                    <el-col :span="6">
                        <img 
                        id="logo_img" 
                        class="logo_img_style" 
                        src="../../assets/logo.png"
                        style="border-radius:50%;background-color: white;height: 150px;">
                    </el-col>
                    <el-col :span="18">
                        <div style="font-size:80px;padding-left: 20px;">文字logo</div>
                    </el-col>
                </el-row>
            </div>
            <div id="search_content" class="s_content">
                <el-row>
                    <el-col :span="20">
                        <input type="text" class="search_input">
                    </el-col>
                    <el-col :span="4">
                        <img
                        src="../../assets/logo.png"
                        style="border-radius:50%;background-color: white;height: 42px;">
                    </el-col>
                </el-row>
            </div>
            <div class="s_tailer">
                <el-row>
                    <el-col :span="6"><img src="../assets/注册.png" style="border-radius:50%;background-color: white;width: 42px;height: 42px;object-fit: contain;"></el-col>
                    <el-col :span="6"><img src="../assets/登录.png" style="border-radius:50%;background-color: white;width: 42px;height: 42px;object-fit: contain;" @click="gotoLogin"></el-col>
                    <el-col :span="6"><img src="../assets/打赏.png" style="border-radius:50%;background-color: white;width: 42px;height: 42px;object-fit: contain;"></el-col>
                    <el-col :span="6"><img src="../assets/联系我们.png" style="border-radius:50%;background-color: white;width: 42px;height: 42px;object-fit: contain;"></el-col>
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

export default {
    name: "Home",
    components:{
        LoginForm
    },
    data(){
        return{
            opa: 1,
            isLogin: false
        }
    },
    methods: {
        gotoLogin(){
            this.isLogin = true
        },
        loginInComfirmed(){
            this.isLogin = false
        },
        clickOutside(e){
            this.isLogin = false
        },
        handleScroll(e) {
            var scrollY = e.deltaY;
            if (scrollY > 0){
                this.opa = 0.5;
            }
            else{
                this.opa = 1;
            }
        }
    },
}
</script>

<style scoped>
.home{
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
    background-size : cover; 
    background-attachment: fixed;
    background-repeat:no-repeat; 
    overflow: scroll;
    position:absolute;
    z-index: 1;
}
.s_form{
    width: 30%;
    margin: auto;
    padding-top: 200px;
}
.s_form_header{
    margin: auto;
    padding-bottom: 30px;
    padding-left: 20px;
    padding-right: 20px;
}
.s_content{
    padding-bottom: 30px;
}
.search_input{
    width: 100%;
    height: 40px;
    border-radius: 15px;
    border: none;
    box-shadow: none;
    /* outline-color: #4e6ef2; */
    outline-color: none;
}
/* .search_input:focus{
    border-color: #4e6ef2 !important;
    opacity: 1;
}
.search_input:hover{
    border-color: #a7aab5 ;
} */
.login_form{
    position:absolute;
    z-index: 2;
}
.login-form-transition-enter-active, .login-form-transition-leave-active{
    transition: opacity 0.5s
}
.login-form-transition-enter-from, .login-form-transition-leave-to{
    opacity: 0
}
</style>