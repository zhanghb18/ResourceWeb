<template>
    <div class="login_page" @click="clickOverlay">
        <div class="login_box" ref="loginBox">
            <el-form :model="loginForm" :rules="loginRules" ref="loginForm"  style="text-align: center">
                <img src="../assets/logo.png" style="height: 60px;">

                <el-form-item prop="account" style="margin-top: 10px">
                    <el-input size="large" placeholder="账号" v-model="loginForm.account"></el-input>
                </el-form-item>

                <el-form-item prop="passWord" style="margin-top: 10px;">
                    <el-input size="large" type="password" placeholder="密码" v-model="loginForm.passWord"></el-input>
                </el-form-item>

                <el-form-item style="display: inline-block">
                    <el-button round type="primary" class="sizedBtn submitBtn" color="rgb(120, 70, 139)" @click="loginInComfirmed">登录</el-button>
                    <el-button round type="primary" class="sizedBtn resignBtn" color="#626aef">注册</el-button>
                    <el-button round type="primary" class="sizedBtn forgetBtn" color="#aaaaaa">忘记密码？</el-button>
                </el-form-item>
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
    height: 100vh;
    padding: 0;
    margin: 0;
    /* font-size: 16px; */
    background: radial-gradient(rgb(255,255,255,0.2), rgba(0,0,0,1));
    color: #fff;
    font-family: "Source Sans Pro";
    position: relative;
}

.login_box {
    width: 400px;
    height: 240px;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    margin: auto;
    border-radius: 20px; 
    padding: 40px 40px 60px 40px;
    box-shadow: -15px 15px 15px rgba(6, 17, 47, 0.7);
    background:rgb(255, 253, 255);
}

.sizedBtn {
    min-width: 100px;
    min-height: 40px;
}
</style>
