<template>
  <div class="login_page" @click="clickOverlay">
    <div class="login_box" ref="loginBox">
      <el-row class="logo_row">
        <img class="logo_img" src="../assets/logo.png" />
        <span class="logo_text">文字LOGO</span>
        <el-icon
          :size="30"
          :class="{ close_icon: true, close_icon_over: isOverIcon }"
          @mouseover="this.isOverIcon = true"
          @mouseout="this.isOverIcon = false"
          @click="this.$emit('closeForm')"
          ><Close
        /></el-icon>
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
            <span class="text">邮箱</span>
          </div>
        </el-col>
        <el-col :span="18">
          <input v-model="loginForm.mails" />
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
      </el-row>

      <div style="border: 1px solid #ccc"></div>

      <el-row class="input_row">
        <el-col :span="3">
          <div class="text_container">
            <!-- TODO:目前长度设置有点问题，四个字过长了，先这么用 -->
            <span class="text">确认密</span>
          </div>
        </el-col>
        <el-col :span="18">
          <input type="password" v-model="loginForm.passWordCfm" />
        </el-col>
      </el-row>

      <div style="border: 1px solid #ccc"></div>

      <el-row class="button_row">
        <el-col :span="12">
          <el-button
            type="plain"
            class="size_btn"
            style="float: left"
            @click="registerComfirmed"
            >确认注册</el-button
          >
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
export default {
  name: "RegisterForm",
  data: function () {
    return {
      isOverIcon: false,
      loginForm: {
        account: "",
        mails: "",
        passWord: "",
        passWordCfm: "",
      },
      loginRules: {
        account: [{ required: true, message: "请输入账号", trigger: "blur" }],
        passWord: [{ required: true, message: "请输入密码", trigger: "blur" }],
      },
    };
  },
  methods: {
    registerComfirmed() {
      // TODO: 按下确认注册按钮后触发的的函数，建议从这里联系后端
    },
    clickOverlay(e) {
      let isClickInside = this.$refs.loginBox.contains(e.target);
      console.log(isClickInside);
      if (!isClickInside) {
        this.$emit("closeForm");
      }
    },
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
  height: 539px; /* 430-37-54 */
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

.close_icon {
  position: relative;
  top: 15px;
  left: 372px;
}

.close_icon_over {
  color: purple;
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

.size_btn {
  height: 100%;
  width: 90%;
  border-radius: 12px;
  font-size: 20px;
}
</style>
