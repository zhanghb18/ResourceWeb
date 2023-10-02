<template>
  <div class="login_page">
    <div class="login_box" ref="loginBox">
      <el-row class="logo_row">
        <img class="logo_img" src="../../assets/logo.png" />
        <span class="logo_text">某次元</span>
        <el-icon
          :size="30"
          :class="{ close_icon: true, close_icon_over: isOverIcon }"
          @mouseover="this.isOverIcon = true"
          @mouseout="this.isOverIcon = false"
          @click="this.$emit('closeForm')"
          ><Close
        /></el-icon>
      </el-row>

      <InputCom
        text="邮箱"
        :message="message.email"
        v-model="loginForm.email"
        @blur="checkEmail"
        v-bind:autocomplete="'off'"
      ></InputCom>

      <InputCom
        text="密码"
        type="password"
        btnText="忘记密码？"
        :message="message.password"
        v-model="loginForm.passWord"
        v-bind:autocomplete="'off'"
        @blur="checkPassword"
      ></InputCom>

      <el-row class="button_row">
        <el-col :span="12">
          <el-button
            type="plain"
            class="size_btn"
            style="float: left"
            @click="this.$emit('gotoRegister')"
            >注册
          </el-button>
        </el-col>
        <el-col :span="12">
          <el-button
            type="plain"
            class="size_btn"
            color="rgb(120, 70, 139)"
            style="float: right"
            @click="sendLoginRequest"
            >登录
          </el-button>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
// import { mapMutations } from "vuex";
import InputCom from "./InputCom.vue";
import { alertBox } from "@/utils/alertBox.js";

export default {
  name: "LoginForm",
  components: {
    InputCom,
  },
  data() {
    return {
      isOverIcon: false,
      loginForm: {
        email: "",
        passWord: "",
      },
      message: {
        email: "",
        password: "",
      },
    };
  },
  methods: {
    sendLoginRequest() {
      // 发送登录请求
      var that = this;
      this.$api.user.UserLogin(this.loginForm)
        .then(function (response) {
          if (response.data.msg === "success") {
            var statusCode = response.data.data.statusCode;
            if (statusCode == 0) {
              that.loginForm.email = "";
              that.loginForm.passWord = "";
              alertBox("登录成功！", "success", that);
              localStorage.setItem("token",response.data.data.token);
              localStorage.setItem("avatar",response.data.data.avatar);
              that.$store.commit("updateToken");
              that.$store.commit("updateAvatar");
              that.$emit("loginInComfirmed");
            } else if (statusCode == 1) {
              alertBox("邮箱不存在", "error", that);
            } else if (statusCode == 2) {
              alertBox("密码错误", "error", that);
            } else {
              alertBox("未知错误", "error", that);
            }
          } else {
            alertBox(response.data.data, "error", that, "登录请求发送失败");
          }
        })
        .catch(function (error) {
          alertBox("连接异常，请检查网络或稍后再试。", "error", that);
          that.btnDisable = false;
        });
    },
  },
};
</script>

<style lang="less" scoped>
@import "../../assets/font/font.css";

.login_page {
  width: 100vw;
  height: 100vh;
  background: radial-gradient(rgba(255, 255, 255, 0.2), rgba(0, 0, 0, 1));
  display: flex;
}

.login_box {
  min-width: 618px; /* 750-66-66 */
  min-height: 339px; /* 430-37-54 */
  margin: auto;
  border-radius: 20px;
  padding: 37px 66px 54px 66px;
  box-shadow: 0px 0px 15px rgba(6, 17, 47, 0.7);
  background: rgb(255, 255, 255);
  scale: 1;
}

.logo_row {
  height: 60px;
  margin-bottom: 39px;
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
  left: 428px;
}

.close_icon_over {
  color: purple;
}

.input_row {
  height: 50px;
}

.text {
  line-height: 50px;
  color: black;
  font-size: 20px;
  justify-content: center;
  display: flex;
}

.message_row {
  height: 31px;
}

.message_text {
  color: red;
  font-size: 14px;
  margin-left: 20px;
  line-height: 20px;
}

input {
  width: 100%;
  height: 100%;
  border: none;
  padding: 0px 20px;
  font-size: 20px;
  outline-style: none;
}

.button_row {
  margin-top: 21px;
  height: 56px;
}

.size_btn {
  height: 100%;
  width: 90%;
  border-radius: 12px;
  font-size: 20px;
}
</style>
