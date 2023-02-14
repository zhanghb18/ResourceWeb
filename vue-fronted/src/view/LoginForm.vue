<template>
        <div class="login_page" @click="clickOverlay">
            <div class="login_box" ref="loginBox">
                <h4></h4>
                <el-col :span="6" ><img src="assets/LOGO.png" style="width: 42px;height: 20px;"></el-col>
                <el-form :model="loginForm" :rules="loginRules" ref="loginForm">
    
                    <el-form-item label="" prop="account" style="margin-top: 10px">
                        
                        
                            <input  class="inps" placeholder="账号" v-model="loginForm.account" style="width: 405px">
                        
                    </el-form-item>
    
                    <el-form-item label="" prop="passWord" style="width: 300px; margin-right: 10px;">
                        <el-upload>
                            <input class="inps" type="password" placeholder="密码" v-model="loginForm.passWord" style="width: 350px" >
                            <input class="Forget" type="password" placeholder="忘记密码" v-model="loginForm.passWord" style="width: 55px" >
                    
    
                        </el-upload>
                        
                    </el-form-item>
    
                    <el-form-item >
                        
    
                    
                    <el-upload>
    
                        
                        <el-button type="primary" round class="resign" @click="loginInComfirmed">注册</el-button>
                        <el-button type="primary" round class="submitBtn" @click="loginInComfirmed">登录</el-button>
                    </el-upload>
                        
    
                        
                        
                    </el-form-item>
    
    <!--
                    <div class="unlogin">
                        <router-link :to="{ path: '/forgetpwd' }"> 忘记密码? </router-link>
                        |
                        <router-link :to="{ path: '/register' }">
    
                            <a href="register.vue" target="_blank">注册新账号</a>
                        </router-link>
                    </div>-->
                </el-form>
            </div>
        </div>
    </template>
    
<script>
// import { mapMutations } from "vuex";

export default {
    name: "LoginForm",
    data: function () {
        return {
            loginForm: {
                account: "",
                passWord: "",
            },
            loginRules: {
                account: [{ required: true, message: "请输入账号", trigger: "blur" }],
                passWord: [{ required: true, message: "请输入密码", trigger: "blur" }],
            },
        };
    },
    methods: {
        loginInComfirmed(){
            this.$emit("loginInComfirmed")
        },
        clickOverlay(e){
            let isClickInside = this.$refs.loginBox.contains(e.target)
            console.log(isClickInside)
            if(!isClickInside){
                this.$emit("clickOutside")
            }
        }
        // ...mapMutations(["changeLogin"]),
        // submitForm() {
        //     const userAccount = this.loginForm.account;
        //     const userPassword = this.loginForm.passWord;
        //     if (!userAccount) {
        //         return this.$message({
        //             type: "error",
        //             message: "账号不能为空！",
        //         });
        //     }
        //     if (!userPassword) {
        //         return this.$message({
        //             type: "error",
        //             message: "密码不能为空！",
        //         });
        //     }
        //     console.log("用户输入的账号为：", userAccount);
        //     console.log("用户输入的密码为：", userPassword);

        // },
    },
};
</script>

<style>
.login_page {
    width: 100vw;
    padding: 0;
    margin: 0;
    height: 100vh;
    font-size: 16px;
    background: radial-gradient(rgb(255,255,255,0.2), rgba(0,0,0,1));
    color: #fff;
    font-family: "Source Sans Pro";
    position: relative;
}

.login_box {
    width: 400px;
    height: 180px;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    margin: auto;
    border-radius: 20px; 
    padding: 50px 40px 40px 40px;
    box-shadow: -15px 15px 15px rgba(6, 17, 47, 0.7);
    background:rgb(255, 253, 255);
}

.inps{

border-bottom: 1px solid #dbdbdb;  
border-top:0px;  
border-left:0px;  
border-right:0px;  
text-align: justify;
}

.Forget {
    border-bottom: 1px solid #dbdbdb;  
border-top:0px;  
border-left:0px;  
border-right:0px;  
    text-align: justify;
}


.submitBtn {
    background-color: transparent;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    color: rgb(255, 255, 255);
    background-color: rgb(120, 70, 139);
    height:40px;
    width: 200px;
}
.resign {
    background-color: transparent;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    color: rgb(0, 0, 0);
    background-color: rgb(255, 255, 255);
    height:40px;
    width: 200px;
}
</style>
