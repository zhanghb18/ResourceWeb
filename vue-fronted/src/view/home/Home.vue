<template>
  <div v-if="ishead" :class="{acghead:true }">
    <Acghead></Acghead>
  </div>
  <div class="background" @mousewheel="handleScroll($event)">
      <div class="home"  
      v-bind:style="{
                    opacity: HomeOpacity,
                  }">
        <div id="search_form" class="s_form">
          <div v-if="Logocircle" id="serchr_form_header" :class="{ s_form_header: true }">
            <el-row>
              <el-col :span="2">
                <div 
                  :class="{ Logo_circle: true , comp_go: compgo }" 
                  v-bind:style="{
                    width: Width_C + 'px',
                    height: Height_C + 'px',
                  }"
                >
                  <!-- 绑定动画，同时修改大小 -->
                  <img
                    src="../../assets/logo.png"
                    v-bind:style="{
                      width: Width_P + '%',
                      height: Height_P + '%',
                    }"
                  />
                </div>
              </el-col>
              <el-col :span="22">
                <div :class="{ logo: true, comp_logo_go: complogogo }"  :style="{ fontSize: font_size+'px' }" >
                  某次元
                </div>
                <!-- 绑定动画 -->
              </el-col>
            </el-row>
          </div>
          <div id="search_content" :class="{s_content:true, comp_search_go: compsearchgo}" >
            <el-row>
              <!-- 此处为原搜索框代码（按钮在框外） -->
              <!-- <el-col :span="22">
                    <div style="display: flex; align-items: center; padding-right: 10px;">
                        <input type="text" :class="{ search_input: true, 'comp_search_go': compsearchgo }" v-model="searchText" placeholder="请输入关键字"
                            @focus="clearPlaceholder">
                    </div>
                </el-col>
                <el-col :span="2">
                    <div class="search_circle">
                        <img src="../../assets/logo.png">
                    </div>
                </el-col> -->
              <el-col :span="22">
                <div style="display: flex">
                  <input
                    type="text"
                    class="search_input"
                    placeholder="搜索关键词:"
                  />
                  <button class="search_button">
                    <img src="../../assets/acgpage/SearchLogo.png" />
                  </button>
                </div>
              </el-col>
            </el-row>
          </div>
          <div v-if="!AcgPagein" class="s_tailer">
            <el-row justify="center">
              <el-col :span="5">
                <IconCircle
                  :imgSrc="require('../../assets/home/注册.png')"
                  text="注册"
                  @click="this.isRegister = !this.isRegister"
                ></IconCircle>
              </el-col>
              <el-col :span="5">
                <IconCircle
                  :imgSrc="require('../../assets/home/登录.png')"
                  text="登录"
                  @click="gotoLogin()"
                >
                </IconCircle>
              </el-col>
              <el-col :span="5">
                <IconCircle
                  :imgSrc="require('../../assets/home/联系我们.png')"
                  text="联系"
                ></IconCircle>
              </el-col>
              <el-col :span="5">
                <IconCircle
                  :imgSrc="require('../../assets/home/打赏.png')"
                  text="打赏"
                ></IconCircle>
              </el-col>
            </el-row>
          </div>
        </div>
      </div>
      <!-- 注册界面（暂无动画） -->
        <div v-if="AcgPagein" :class="{DownPage:true, AcgPage_in : AcgPagein,}">
          <AcgPage></AcgPage>
        </div>
    <!-- 注册界面（暂无动画） 
      <div class="register_form" v-if="isRegister">
        <RegisterForm
        @closeForm="closeRegisterForm"
        ></RegisterForm>
      </div>-->
    <!-- 登录界面 -->
    <transition name="login-form-transition">
      <div class="login_form" v-if="isLogin">
        <LoginForm
          @loginInComfirmed="loginInComfirmed"
          @gotoRegister="gotoRegister"
          @closeForm="closeLoginForm"
        ></LoginForm>
      </div>
    </transition>
  </div>
</template>

<script>
import RegisterForm from "../forms/RegisterForm.vue";
import LoginForm from "../forms/LoginForm.vue";
import IconCircle from "./IconCircle.vue";
import AcgPage from "../acgpage/AcgPage.vue";
import Acghead from "../acgpage/Head.vue"

export default {
  name: "Home",
  components: {
    RegisterForm,
    LoginForm,
    IconCircle,
    AcgPage,
    Acghead,
},
  data() {
    return {
      compgo: false,
      compsearchgo: false,
      complogogo: false,
      isHome: true,
      AcgPagein:false,
      isRegister: false,
      isLogin: false,
      Logocircle : true,
      logo:true,
      searchText: "",
      isOnIcon: false,
      Width_C: 164,
      Height_C: 164,
      Width_P: 60,
      Height_P: 60,
      ACGbottom:-100,
      HomeOpacity:1,
      ishead:false,
      font_size:80
    };
  },
  methods: {
    gotoRegister() {
      this.isRegister = true;
      this.isLogin = false;
    },
    gotoLogin() {
      this.isLogin = true;
      this.isRegister = false;
    },
    registerComfirmed() {
      this.isRegister = false;
    },
    loginInComfirmed() {
      this.isLogin = false;
    },
    closeRegisterForm() {
      this.isRegister = false;
    },
    closeLoginForm() {
      this.isLogin = false;
    },
    clearPlaceholder() {
      this.searchText = "";
    },
    handleScroll(e) {
      var scrollY = e.deltaY;
      if (!this.isLogin) {
        if (scrollY > 0) {
          if (this.isHome) {
            //修改bool值以开启动画

            this.Width_C /= 3;
            this.Width_P /= 3;
            this.Height_C /= 3;
            this.Height_P /= 3;
            this.font_size/=3.5;
            this.isHome = false;
            const that1 = this;
            setTimeout(function () {
              that1.compgo = true;
              that1.compsearchgo = true;
              that1.complogogo = true;
              
            }, 10);
            //设置在滚动1.5s后切换页面，用于保证前面的动画完成
            this.ACGbottom+=175;
            this.AcgPagein = true;
            const that = this;
            setTimeout(function () {
              that.Logocircle = false;
              that.HomeOpacity =0;
              that.ishead=true;
              
            }, 1500);
          }
        } else if (e.deltaY < 0) {
          if (!this.isHome) {
            this.compgo = false;
            this.Logocircle = true;
            this.logo = true;
            this.compsearchgo = false;
            this.complogogo = false;
            this.AcgPagein = false;
            this.HomeOpacity =1
            this.ishead=false;
            this.isHome = true;
            this.Width_C *= 3;
            this.Width_P *= 3;
            this.Height_C *= 3;
            this.Height_P *= 3;
            this.font_size*=3.5;
          }
        }
      }
    },
  },
};
</script>

<style scoped>
@import "../../assets/font/font.css";

.background {
  min-height: 100%;
  min-width: 100%;
}

.home {
  background: url("../../assets/home/background.jpg");
  min-height: 100%;
  min-width: 100%;
  background-size: cover;
  background-attachment: fixed;
  background-repeat: no-repeat;
  position: absolute;
  z-index: 1;
}
.DownPage{
  position:absolute;
  height: 82%; 
  width: 100%;
  bottom:0%;
  z-index:3;
}
.s_form {
  width: 650px;
  margin: auto;
  padding-top: 258px;
}

.comp_go {
  animation: comp_go 1.8s;
}

.comp_search_go {
  animation: comp_search_go 1.8s;
}

.comp_logo_go {
  animation: comp_logo_go 1.8s;
}
.AcgPage_in{
  animation: AcgPage_in 1.5s;
}
.s_form_header {
  margin: auto;
  padding-left: 20px;
  padding-right: 20px;
}

.s_content {
  padding-bottom:0px;
}

.search_input {
  /* 搜索框样式 */
  box-sizing: border-box;
  width: 636px;
  height: 51px;
  border-radius: 20px;
  border: none;
  box-shadow: none;
  padding: 5px 29px;
  font-size: 18px;
  outline-color: none;
  margin-top: 37px;
  margin-bottom: 58.5px;
  display: flex;
  align-items: center;
}

.search_input:focus {
  /* 搜索框聚焦样式 */
  border-color: #409eff;
  box-shadow: inset 0 -3em 3em #f2f2f2, 0.3em 0.3em 1em rgba(155, 155, 155, 0.3);
  outline: 0px;
}

.search_input::placeholder {
  /* 搜索框占位符样式 */
  color: #999;
  font-size: 18px;
  padding-left: 0px;
}
.search_button {
  /* 搜索按钮样式 */
  background-color: transparent;
  border: none;
  cursor: pointer;
  margin-top: 37px;
  margin-bottom: 58.5px;
  margin-left: -48px;
}

.search_button img {
  /* 搜索按钮图片样式 */
  height: 26px;
}
.Logo_circle {
  border-radius: 50%;
  background-color: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
}

.Logo_circle img {
  object-fit: contain;
}

.logo {
  padding-left: 45px;
  padding-top: 45px;
  letter-spacing: 6px;
  font-family: "DOUYU", cursive;
  color: white;
}

.logo2 {
  position: absolute; /* 设置绝对定位 */
  top: 20px; /* 距离顶部为0 */
  left: 45px; /* 距离左边为0 */
  font-size: 20px;
  font-family: "DOUYU", cursive;
  color: black;
}

.search_circle {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background-color: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
  line-height: 30px;
}

.search_circle img {
  width: 60%;
  height: 60%;
  object-fit: contain;
}
.home-transition-enter-active,
.home-transition-leave-active {
  transition: all 0s;
}
.home-transition-leave-to {
  opacity: 0;
  top: -50%;
}
.home-transition-enter-to,
.home-transition-leave-from {
  opacity: 1;
  top: 0%;
}

.register_form {
  position: absolute;
  z-index: 3;
}

.login_form {
  position: absolute;
  z-index: 2;
}

.login-form-transition-enter-active {
  transition: opacity 0.5s;
}
.login-form-transition-leave-active {
  transition: opacity 0.5s;
}

.login-form-transition-enter-from {
  opacity: 0;
}

.login-form-transition-leave-to {
  opacity: 0;
}
.DownPage-transition-enter-active,
.DownPage-transition-leave-active {
  transition: 1.5s;
}

.DownPage-transition-enter-to ,
.home-transition-leave-from{
  bottom: 50%;
}

.DownPage-transition-enter-from {
  bottom: -50%;
}
/*以下为动画*/

@keyframes comp_go {
  to {
    transform: translateX(-1448%) translateY(-390%);
  }
}

@keyframes comp_logo_go {
  to {
    transform: translateX(-183%) translateY(-328%);
  }
}

@keyframes comp_search_go {
  to {
    transform: translateY(-230%);
  }
}

@keyframes AcgPage_in{
  from{
    bottom:-50%;

  }
  to{
    bottom:00%;

  }
}
</style>
