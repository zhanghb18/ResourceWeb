<template>
  <div class="login_page" @click="clickOverlay">
    <div class="login_box" ref="loginBox">
      <el-row class="logo_row">
        <img class="logo_img" src="../assets/logo.png" />
        <span class="logo_text">文字LOGO</span>
      </el-row>

      <el-row class="input_row">
        <el-col :span="3">
          <div class="text_container">
            <span class="text">账号</span>
          </div>
        </el-col>
        <el-col :span="18">
          <input v-model="loginForm.account" />
        </el-col>
      </el-row>

      <div style="border: 1px solid #ccc"></div>

      <el-row class="input_row">
        <el-col :span="3">
          <div class="text_container">
            <span class="text">密码</span>
          </div>
        </el-col>
        <el-col :span="18">
          <input type="password" v-model="loginForm.passWord" />
        </el-col>
        <el-col :span="3" style="margin: auto">
          <el-button :type="'primary'" text large>忘记密码？</el-button>
        </el-col>
      </el-row>

      <div style="border: 1px solid #ccc"></div>

      <el-row class="button_row">
        <el-col :span="12">
          <el-button
            type="plain"
            class="size_btn"
            style="float: left"
            @click="loginInComfirmed"
            >注册</el-button
          >
        </el-col>
        <el-col :span="12">
          <el-button
            type="plain"
            class="size_btn"
            color="rgb(120, 70, 139)"
            style="float: right"
            @click="loginInComfirmed"
            >登录</el-button
          >
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
      this.$emit("loginInComfirmed");
    },
    clickOverlay(e) {
      let isClickInside = this.$refs.loginBox.contains(e.target);
      console.log(isClickInside);
      if (!isClickInside) {
        this.$emit("clickOutside");
      }
    },
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
@import "../assets/font/font.css";

.login_page {
  width: 100vw;
  height: 100vh;
  background: radial-gradient(rgb(255, 255, 255, 0.2), rgba(0, 0, 0, 1));
  display: flex;
}

.login_box {
  width: 618px; /* 750-66-66 */
  height: 339px; /* 430-37-54 */
  margin: auto;
  border-radius: 20px;
  padding: 37px 66px 54px 66px;
  box-shadow: 0px 0px 15px rgba(6, 17, 47, 0.7);
  background: rgb(255, 255, 255);
  scale: 1;
}

.logo_row {
  height: 60px;
  margin-bottom: 8px;
}

.logo_img {
  height: 60px;
  position: relative;
  left: -3%;
}

.logo_text {
  font-size: 30px;
  line-height: 60px;
  color: purple;
  font-family: "DOUYU", cursive;
}

.input_row {
  padding-top: 31px;
  height: 81px;
  font-size: 22px;
}

.text {
  line-height: 50px;
}

.text_container {
  color: black;
  font-size: 20px;
  justify-content: center;
  display: flex;
}

input {
  outline-style: none;
  box-sizing: content-box;
  width: 80%;
  height: 100%;
  border: none;
  padding: 0px 20px;
  font-size: 20px;
}

.button_row {
  margin-top: 52px;
  height: 56px;
}

.size d {
  height: 100%;
  width: 90%;
  border-radius: 12px;
  font-size: 20px;
}
</style>
