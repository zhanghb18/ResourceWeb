<template>
    <div class="login_page" @click="clickOverlay">
        <div class="login_box" ref="loginBox">
            <h4>登录</h4>

            <el-form :model="loginForm" :rules="loginRules" ref="loginForm">
                <el-form-item label="" prop="account" style="margin-top: 10px">
                    <el-input class="inps" placeholder="账号" v-model="loginForm.account"></el-input>
                </el-form-item>

                <el-form-item label="" prop="passWord" style="margin-top: 10px">
                    <el-input class="inps" type="password" placeholder="密码" v-model="loginForm.passWord"></el-input>
                </el-form-item>

                <el-form-item style="margin-top: 55px;justify-content: center;">
                    <!-- <el-button type="primary" round class="submitBtn" @click="submitForm">登录 -->
                    <el-button type="primary" round class="submitBtn" @click="loginInComfirmed">登录</el-button>
                </el-form-item>

                <div class="unlogin">
                    <router-link :to="{ path: '/forgetpwd' }"> 忘记密码? </router-link>
                    |
                    <router-link :to="{ path: '/register' }">
                        <a href="register.vue" target="_blank">注册新账号</a>
                    </router-link>
                </div>
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
    height: 280px;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    margin: auto;
    padding: 50px 40px 40px 40px;
    box-shadow: -15px 15px 15px rgba(6, 17, 47, 0.7);
    background:rgb(23, 50, 114);
}

.inps input {
    border: none;
    color: #fff;
    background-color: transparent;
    font-size: 12px;
}

.submitBtn {
    background-color: transparent;
    color: #39f;
    width: 200px;
}
</style>