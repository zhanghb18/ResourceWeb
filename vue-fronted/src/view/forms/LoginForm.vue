<template>
  <div class="login_page" @click="clickOverlay">
    <div class="login_box" ref="loginBox">
      <el-row class="logo_row">
        <img class="logo_img" src="../../assets/logo.png" />
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

      <InputCom
        text="账号"
        type="account"
        btnText=""
        :message="message.account"
        v-model="loginForm.account"
      ></InputCom>

      <InputCom
        text="密码"
        type="password"
        btnText="忘记密码？"
        :message="message.password"
        v-model="loginForm.passWord"
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
            @click="loginInComfirmed"
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

export default {
  name: "LoginForm",
  components: {
    InputCom,
  },
  data () {
    return {
      isOverIcon: false,
      loginForm: {
        account: "",
        passWord: "",
      },
      loginRules: {
        account: [{ 
          required: true,
          message: "请输入账号",
          trigger: "blur"
        }],
        passWord: [{ 
          required: true,
          message: "请输入密码",
          trigger: "blur"
        }],
      },
      message: {
        account: "账号不存在！（测试用）",
        password: "",
      },
    };
  },
  // computed: {
  //   message () {
  //     if (this.loginForm.passWord.length <= 6)
  //       return "密码长度过短！密码为 6-20 位数字字母组合"
  //     else if (this.loginForm.passWord.length > 20)
  //       return "密码长度过长！密码为 6-20 位数字字母组合"
  //     else
  //       return ""
  //   }
  // },
  methods: {
    updateMessagePassword() {
      if (this.loginForm.passWord.length <= 6) {
        this.message.password = "密码长度过短！密码为 6-20 位数字字母组合"
      } 
      else if (this.loginForm.passWord.length > 20)
        this.message.password = "密码长度过长！密码为 6-20 位数字字母组合"
      else
        this.message.password = ""
    },
    loginInComfirmed() {
      // TODO: 按下登录按钮后触发的函数
      this.$emit("loginInComfirmed");
    },
    clickOverlay(e) {
      let isClickInside = this.$refs.loginBox.contains(e.target);
      console.log(isClickInside);
      if (!isClickInside) {
        this.$emit("closeForm");
      }
    },

  },
  mounted() {
    this.$watch('loginForm.passWord', () => {
      this.updateMessagePassword()
    })
  }
};
</script>

<style lang="less" scoped>
@import "../../assets/font/font.css";

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
  left: 372px;
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
