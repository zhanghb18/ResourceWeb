<template>
  <div class="TotalPage" style="height:100%">
  <div v-if="ishead" :class="{ acghead: true }">
    <Acghead></Acghead>
  </div>
  <div class="background" @mousewheel="handleScroll($event)"
         v-bind:style="{
        minHeight:back_height+'%',
      }">
    <div
      class="home"
      v-bind:style="{
        opacity: HomeOpacity,
        minHeight:back_height+'%',
      }"
    >
      <div id="search_form" class="s_form">
        <div
          v-if="Logocircle"
          id="serchr_form_header"
          :class="{ s_form_header: true }"
        >
          <el-row>
            <el-col :span="2">
              <div
                :class="{ Logo_circle: true, comp_go: compgo , comp_go2: compgo2}"
                v-bind:style="{
                  width: Width_C + 'px',
                  height: Height_C + 'px',
                  '--ToCsslogoY' : ToCsslogoY + '%',
                  '--ToCsslogoX' : ToCsslogoX + '%',
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
              <div
                :class="{ logo: true, 
                  comp_logo_go: complogogo , 
                  comp_logo_goacg: complogogo2}"
                :style="{ fontSize: font_size + 'px' ,  '--ToCsscomplogoX' : ToCsscomplogoX + '%','--ToCsscomplogoY' : ToCsscomplogoY + '%'}"
              >
                某次元
              </div>
              <!-- 绑定动画 -->
            </el-col>
          </el-row>
        </div>
        <div
          id="search_content"
          :class="{ s_content: true, comp_search_go: compsearchgo , comp_search_go2: compsearchgo2}"
          :style="{  '--ToCsssearchX' : ToCsssearchX + '%',
                    '--ToCsssearchY' : ToCsssearchY + '%'}"
        >
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
                  v-bind:style="{
                    width: Width_Search + 'px',
                  }"
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
        <button
          v-if="!AcgPagein"
          @click="gotoAcgpage()"
          class="Change_component"
          style="background-image"
        >
          <img :src="require('../../assets/home/切换箭头.png')" />
        </button>
      </div>
    </div>
    <!-- Acg界面-->
    <div v-if="AcgPagein" :class="{ DownPage: true, AcgPage_in: AcgPagein }" style="height:88%">
      <AcgPage></AcgPage>
    </div>
    <!-- 注册界面（暂无动画） -->
    <transition name="login-form-transition">
      <div class="register_form" v-if="isRegister">
        <RegisterForm @closeForm="closeRegisterForm"></RegisterForm>
      </div>
    </transition>
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
</div>
</template>

<script>
import RegisterForm from "../forms/RegisterForm.vue";
import LoginForm from "../forms/LoginForm.vue";
import IconCircle from "./IconCircle.vue";
import AcgPage from "../acgpage/AcgPage.vue";
import Acghead from "../acgpage/Head.vue";

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
      back_height:100,
      compgo: false,
      compsearchgo: false,
      complogogo: false,
      compgo2: false,
      compsearchgo2: false,
      complogogo2: false,
      isHome: true,
      AcgPagein: false,
      isRegister: false,
      isLogin: false,
      Logocircle: true,
      logo: true,
      searchText: "",
      isOnIcon: false,
      Width_C: 164,
      Height_C: 164,
      Width_P: 60,
      Height_P: 60,
      ACGbottom: -100,
      HomeOpacity: 1,
      ishead: false,
      font_size: 80,
      Width_Search:636,
      ToCsslogoY:-1320,
      ToCsslogoX:-455,
      ToCsscomplogoY:-168,
      ToCsscomplogoX:-372,
      ToCsssearchY:-242,
      ToCsssearchX:8,
      scale:1,
    };
  },
  mounted() {
    window.addEventListener('resize', this.handleResize);
    this.handleResize();
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.handleResize);
  },
  methods: {
    handleResize() {
      const width = window.innerWidth;
      const height = window.innerHeight;
      const ratio = Math.min(width / 1920, height / 1080);
      this.scale = ratio.toFixed(2);
    },
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
    gotoAcgpage() {
      if (!this.isLogin) {
        if (this.isHome) {
          //修改bool值以开启动画
          this.ToCsslogoY/=this.scale,
          this.ToCsslogoX/=this.scale,
          this.ToCsscomplogoY/=this.scale,
          this.ToCsscomplogoX/=this.scale,
          this.ToCsssearchY/=this.scale,
          this.ToCsssearchX/=this.scale,
          this.Width_C /= 3;
          this.Width_P /= 3;
          this.Height_C /= 3;
          this.Height_P /= 3;
          this.font_size /= 3.5;
          this.isHome = false;
          this.Width_Search -=62;
          const that1 = this;
          setTimeout(function () {
            that1.compgo2 = true;
            that1.compsearchgo2 = true;
            that1.complogogo2 = true;

          }, 10);
          //设置在滚动1.5s后切换页面，用于保证前面的动画完成
          this.back_height/=1.25;
          this.ACGbottom += 175;
          this.AcgPagein = true;
          const that = this;
          setTimeout(function () {
            that.Logocircle = false;
            that.HomeOpacity = 0;
            that.ishead = true;
          }, 1500);
        }
      } else if (e.deltaY < 0) {
        if (!this.isHome) {
          /*
          this.compgo = false;
          this.Logocircle = true;
          this.logo = true;
          this.compsearchgo = false;
          this.complogogo = false;
          this.AcgPagein = false;
          this.HomeOpacity = 1;
          this.ishead = false;
          this.isHome = true;
          this.Width_C *= 3;
          this.Width_P *= 3;
          this.Height_C *= 3;
          this.Height_P *= 3;
          this.font_size *= 3.5;
          */
        }
      }
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
            this.font_size /= 3.5;
            this.isHome = false;
            this.Width_Search -=62;
            const that1 = this;
            setTimeout(function () {
              that1.compgo = true;
              that1.compsearchgo = true;
              that1.complogogo = true;
            }, 10);
            //设置在滚动1.5s后切换页面，用于保证前面的动画完成
            this.ACGbottom += 175;
            this.AcgPagein = true;
            this.back_height/=1.25;
            const that = this;
            setTimeout(function () {
              that.Logocircle = false;
              that.HomeOpacity = 0;
              that.ishead = true;
            }, 1500);
          }
        } else if (!this.isHome) {
          /*
          this.compgo = false;
          this.Logocircle = true;
          this.logo = true;
          this.compsearchgo = false;
          this.complogogo = false;
          this.AcgPagein = false;
          this.HomeOpacity = 1;
          this.ishead = false;
          this.isHome = true;
          this.Width_C *= 3;
          this.Width_P *= 3;
          this.Height_C *= 3;
          this.Height_P *= 3;
          this.font_size *= 3.5;
          */
        }
      }
    },
  },
};
</script>

<style scoped>
@import "../../assets/font/font.css";

:root {
  --main-percent: -1320%;
}

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
.DownPage {
  position: absolute;
  width: 100%;
  bottom: 0%;
  z-index: 3;
}
.s_form {
  width: 650px;
  margin: auto;
  padding-top: 258px;
}

.comp_go {
  animation: comp_go 2.2s;
}

.comp_search_go {
  animation: comp_search_go 1.8s;
}

.comp_logo_go {
  animation: comp_logo_go 2.2s;
}
.AcgPage_in {
  animation: AcgPage_in 1.5s;
}

.comp_go2 {
  animation: comp_go2 1.8s;
}
.comp_search_go2 {
  animation: comp_search_go2 1.8s;
}

.comp_logo_goacg {
  animation: comp_logo_goacg 1.8s;
}
.AcgPage_in2 {
  animation: AcgPage_in2 1.5s;
}
.s_form_header {
  margin: auto;
  padding-left: 20px;
  padding-right: 20px;
}

.s_content {
  padding-bottom: 0px;
}

.search_input {
  /* 搜索框样式 */
  box-sizing: border-box;
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

.Change_component {
  background-color: transparent;
  border: none;
  cursor: pointer;
  margin-top: 150px;
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

.DownPage-transition-enter-to,
.home-transition-leave-from {
  bottom: 50%;
}

.DownPage-transition-enter-from {
  bottom: -50%;
}
/*以下为动画*/


@keyframes comp_go {
  to {
    transform: translateX(var(--ToCsslogoY))  translateY(var(--ToCsslogoX));
  }
}
@keyframes comp_logo_go {
  to {
    transform: translateX(var(--ToCsscomplogoY)) translateY(var(--ToCsscomplogoX));
  }
}
@keyframes comp_search_go {
  to {
    transform: translateX(var(--ToCsssearchX))  translateY(var(--ToCsssearchY));
  }
}

@keyframes comp_logo_goacg {
  to {
    transform: translateX(var(--ToCsscomplogoY)) translateY(var(--ToCsscomplogoX));
  }
}

@keyframes comp_go2 {
  to {
    transform: translateX(var(--ToCsslogoY))  translateY(var(--ToCsslogoX));
  }
}
@keyframes comp_search_go2 {
  to {
    transform: translateX(var(--ToCsssearchX))  translateY(var(--ToCsssearchY));
  }
}

@keyframes AcgPage_in {
  from {
    bottom: -50%;
  }
  to {
    bottom: 00%;
  }
}
</style>
