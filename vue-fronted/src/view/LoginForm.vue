<template>
    <div class="login_page" @click="clickOverlay">
        <div class="login_box" ref="loginBox">
            <div class="logo_img_box">
                <img class="logo_img" src="./assets/LOGO.png">
            </div>

            <el-row class="input_row">
                <el-col :span="3">
                    <p class="text">账号</p>
                </el-col>
                <el-col :span="16">
                    <input v-model="loginForm.account">
                </el-col>
            </el-row>

            <div style="border:1px solid #CCC;"></div>

            <el-row class="input_row">
                <el-col :span="3">
                    <p class="text">密码</p>
                </el-col>
                <el-col :span="16">
                    <input type="password" v-model="loginForm.passWord">
                </el-col>
                <el-col :span="5" style="margin: auto;">
                    <el-button :type="'primary'" text>忘记密码？</el-button>
                </el-col>
            </el-row>

            <div style="border:1px solid #CCC"></div>

            <el-row class="button_row">
                <el-col :span="12">
                    <el-button type="plain" class="sizedBtn" style="float: left;" @click="loginInComfirmed">注册</el-button>
                </el-col>
                <el-col :span="12">
                    <el-button type="plain" class="sizedBtn" color="rgb(120, 70, 139)" style="float: right;"
                        @click="loginInComfirmed">登录</el-button>
                </el-col>
            </el-row>
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
        loginInComfirmed() {
            this.$emit("loginInComfirmed")
        },
        clickOverlay(e) {
            let isClickInside = this.$refs.loginBox.contains(e.target)
            console.log(isClickInside)
            if (!isClickInside) {
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

<style scoped>
.login_page {
    width: 100vw;
    height: 100vh;
    background: radial-gradient(rgb(255, 255, 255, 0.2), rgba(0, 0, 0, 1));
    display: flex;
}

.login_box {
    width: 400px;
    height: 260px;
    margin: auto;
    border-radius: 20px;
    padding: 20px 40px 40px 40px;
    box-shadow: -15px 15px 15px rgba(6, 17, 47, 0.7);
    background: rgb(255, 255, 255);
}

.logo_img_box {
    height: 30%;
}

.logo_img {
    float: left;
    height: 100%;
    left: -6%;
    position: relative;
}

.input_row {
    margin-bottom: 20px;
    height: 30px;
}


.text {
    color: black;
    font-size: 15px;
}

input {
    outline-style: none;
    box-sizing: content-box;
    width: 80%;
    height: 100%;
    border: none;
    padding: 0px 20px;
    font-size: 15px;
}

.button_row {
    margin-top: 30px;
}

.sizedBtn {
    min-width: 180px;
    min-height: 40px;
    border-radius: 12px;
}
</style>
