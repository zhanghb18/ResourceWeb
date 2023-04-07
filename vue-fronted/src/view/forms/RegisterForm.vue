<template>
  <div class="rgst_page" @click="clickOverlay">
    <div class="rgst_box" ref="loginBox">
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
        :message="message.mails"
        v-model="rgstForm.mails"
        @blur="checkEmail"
      ></InputCom>

      <InputCom
        text="密码"
        type="password"
        :message="message.password"
        v-model="rgstForm.passWord"
        @blur="checkPassword"
      ></InputCom>

      <InputCom
        text="确认密码"
        type="password"
        :message="message.passwordCfm"
        v-model="passWordCfm"
        @blur="checkPasswordCfm"
      ></InputCom>

      <InputCom
        text="验证码"
        btnText="发送验证码"
        :message="message.pin"
        v-model="rgstForm.pin"
        @click="sendPin"
        :btnDisable="btnDisable"
      ></InputCom>

      <el-row class="button_row">
        <el-col :span="6"></el-col>
        <el-col :span="12">
          <el-button
            type="plain"
            class="size_btn"
            color="rgb(120, 70, 139)"
            style="margin: auto"
            @click="registerComfirmed"
            >确认注册
          </el-button>
        </el-col>
        <el-col :span="6"></el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
import { alertBox } from "@/utils/alertBox.js";
import InputCom from "./InputCom.vue";
import { ConstantTypes } from "@vue/compiler-core";

export default {
  name: "RegisterForm",
  components: {
    InputCom,
  },
  data: function () {
    return {
      isOverIcon: false,
      rgstForm: {
        mails: "",
        passWord: "",
        pin: "",
      },
      passWordCfm: "",
      message: {
        mails: "",
        password: "",
        passwordCfm: "",
        pin: "",
      },
      btnDisable: false,
    };
  },
  methods: {
    registerComfirmed() {
      // 在前端检查输入
      this.checkEmail();
      this.checkPassword();
      this.checkPasswordCfm();
      this.checkPin();
      var flag = true;
      if (
        this.message.mails.length > 0 ||
        this.message.password.length > 0 ||
        this.message.passwordCfm.length > 0 ||
        this.message.pin.length > 0
      ) {
        flag = false;
      }

      if (!flag) {
        alertBox("请检查输入是否正确", "error", this);
        return;
      } else {
        // 发送注册请求
        var that = this;
        this.$api.user.UserRegister(this.rgstForm).then(function (response) {
          if (response.data.msg === "success") {
            alertBox("用户注册成功！", "success", that);
          } else {
            alertBox(response.data.data, "error", that, "用户注册失败!");
          }
        });
      }
    },
    clickOverlay(e) {
      let isClickInside = this.$refs.loginBox.contains(e.target);
      if (!isClickInside) {
        this.$emit("closeForm");
      }
    },
    checkEmail() {
      var box = /^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/;
      if (box.test(this.rgstForm.mails)) {
        this.message.mails = "";
      } else {
        this.message.mails = "邮箱格式不正确";
      }
    },
    checkPassword() {
      var box = /^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,20}$/;
      if (box.test(this.rgstForm.passWord)) {
        this.message.password = "";
      } else {
        this.message.password = "密码必须在6~20位之间，且包含数字和字母";
      }
      this.checkPasswordCfm();
    },
    checkPasswordCfm() {
      if (!this.passWordCfm.length == 0) {
        if (this.rgstForm.passWord === this.passWordCfm) {
          this.message.passwordCfm = "";
        } else {
          this.message.passwordCfm = "两次密码不一致";
        }
      }
    },
    checkPin() {
      var box = /^[0-9]{6}$/;
      if (box.test(this.rgstForm.pin)) {
        this.message.pin = "";
      } else {
        this.message.pin = "验证码格式不正确";
      }
    },
    sendPin() {
      var that = this;
      this.checkEmail();
      if (this.message.mails.length == 0) {
        this.$api.user.SendPin(this.rgstForm.mails).then(function (response) {
          if (response.data.msg === "success") {
            alertBox("验证码发送成功！", "success", that);
          } else {
            alertBox(response.data.data, "error", that, "验证码发送失败!");
          }
        });
      }
    },
  },
};
</script>

<style scoped>
@import "../../assets/font/font.css";

.rgst_page {
  width: 100vw;
  height: 100vh;
  background: radial-gradient(rgb(255, 255, 255, 0.2), rgba(0, 0, 0, 1));
  display: flex;
}

.rgst_box {
  min-width: 618px;
  min-height: 501px;
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
