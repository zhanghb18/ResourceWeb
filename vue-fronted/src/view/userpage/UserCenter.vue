<template>
  <div>
    <user-header></user-header>
    <!-- 页面模板 -->
    <el-row style="background-color: #fcf2ff">
      <el-col :span="16" :offset="4" class="container">
        <div class="container-header">
          <img src="https://placekitten.com/800/600" alt="background-image" />
        </div>
        <el-row>
          <el-col :span="22" :offset="1" class="container-body">
            <el-row class="container-body-info">
              <el-col :span="6">
                <div class="container-avatar">
                  <img class="container-avatar-img" src="https://placekitten.com/200/200" alt="avatar" />
                  <div class="overlay" @click="changeAvatar">修改头像</div>
                </div>
              </el-col>
              <el-col :span="13">
                <div class="profile">
                  <div class="info">
                    <div class="name-bio">
                      <!-- 用户名和个人简介 -->
                      <h2>{{ userInfo.userNickName }}</h2>
                      <div>
                        <div v-if="isInputMode">
                          <input type="text" v-model="userInfo.userSignature"  @blur="changeSignature"/>
                        </div>
                        <div v-else>
                          {{ userInfo.userSignature }}
                          <svg class="icon" aria-hidden="true" @click="changeSignature()">
                            <use xlink:href="#icon-xiugai"></use>
                          </svg>
                        </div>
                      </div>
                      <!-- <p>{{ userInfo.userSignature }}</p> -->
                    </div>
                  </div>
                </div>
              </el-col>
              <el-col :span="5">
                <div class="settings" @click="goToUserInfo">
                  <!-- 账号设置 -->
                  <p>账号设置</p>
                </div>
              </el-col>
            </el-row>
            <!-- 分割线 -->
            <el-divider></el-divider>
            <!-- 番剧展示区域 -->
            <el-row>
              <el-col :span="22" class="list_area">
                <div class="menu">
                  <button :class="{ menu_btn: true, active_menu_btn: true }">我的片单</button>
                  <button :class="{ menu_btn: true, active_menu_btn: false }">我的追番</button>
                </div>
                <div class="card_area">
                  <!-- TODO: 如何处理片单为空的情况，如何处理片单数量超过 8 个的情况 -->
                  <DramaCard v-for="sheet in userSheetList" :msg="sheet" />
                </div>
              </el-col>
            </el-row>
          </el-col>
        </el-row>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import UserHeader from "../../components/UserHeader.vue";
import DramaCard from "../../components/DramaCard.vue";

export default {
  name: "ProfilePage",
  components: {
    UserHeader,
    DramaCard,
  },
  data() {
    return {
      isInputMode: false,
      userInfo: {
        userNickName: "张后斌", // 用户名
        userSignature: "我是懒坑小子张后斌", // 个人简介
      },
      userSheetList: [
        {
          name: "番剧 1",
          imgSrc: "https://www.themoviedb.org/t/p/original/mvolqXssikgLeUomc59cB2RkH1k.jpg",
          browseNum: 100,
          collectNum: 100,
        },
        {
          name: "番 ailflef 剧 1",
          imgSrc: "https://www.themoviedb.org/t/p/original/mvolqXssikgLeUomc59cB2RkH1k.jpg",
          browseNum: 132,
          collectNum: 1124,
        },
        {
          name: "番剧 dawl1",
          imgSrc: "https://www.themoviedb.org/t/p/original/mvolqXssikgLeUomc59cB2RkH1k.jpg",
          browseNum: 34,
          collectNum: 12,
        },
        {
          name: "番剧 dawl1",
          imgSrc: "https://www.themoviedb.org/t/p/original/mvolqXssikgLeUomc59cB2RkH1k.jpg",
          browseNum: 34,
          collectNum: 12,
        },
        {
          name: "番剧 dawl1",
          imgSrc: "https://www.themoviedb.org/t/p/original/mvolqXssikgLeUomc59cB2RkH1k.jpg",
          browseNum: 34,
          collectNum: 12,
        },
      ],
    };
  },
  methods: {
    goToUserInfo() {
      this.$router.push("/userinfo");
    },
    changeSignature() {
      this.isInputMode = !this.isInputMode;
      // console.log('失去焦点');
      // 提交新的 userSignature
    },
    changeAvatar() {
      console.log("改变头像");
    }
  },
  created() {
    var user_token = sessionStorage.getItem("token");
    var Data = {
      token: user_token,
    };
    var that = this;
    this.$api.user
      .getUserInfo(Data)
      .then(function (response) {
        if (response.data.msg === "success") {
          var statusCode = response.data.data.statusCode;
          if (statusCode == 1) {
            alertBox("获取用户信息失败，错误码：1", "error", that);
          } else {
            that.userInfo.userNickName = response.data.data.nickname;
            that.userInfo.userSignature = response.data.data.signature;
          }
        } else {
          alertBox("获取用户信息失败", "error", that);
        }
      })
      .catch(function (error) {
        alertBox("连接异常，请检查网络或稍后再试。", "error", that);
      });
  },
};
</script>

<style lang="less" scoped>
/* 样式表 */
.container {
  background-color: #fff;
  width: 62.5%;
  height: auto;
  min-height: 90vh;
}

.container-header {
  height: 250px;
  /* overflow: hidden; */
}

.container-header img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.container-body {
  background-color: #fff;
  /* height: 1000px; */
}

.container-body-info {
  height: 100px;
  margin-bottom: 50px;
  .container-avatar {
    position: relative;
    bottom: 130px;
    img {
      width: 240px;
      height: 240px;
      border-radius: 50%;
      overflow: hidden;
      /* margin-left: 50px; */
    }
    .overlay {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      background-color: rgba(0, 0, 0, 0.5);
      color: white;
      padding: 10px;
      font-size: 16px;
      border-radius: 5px;
      opacity: 0; /* 初始时隐藏覆盖层 */
      transition: opacity 0.3s ease; /* 添加过渡效果 */
    }
    &:hover .overlay {
      opacity: 1; /* 鼠标悬停时显示覆盖层 */
      cursor: pointer;
    }
  }
}

.profile {
  position: relative;
  margin-left: 25px;
  margin-top: 20px;
}

.settings {
  margin-top: 30px;
  background: #662d91;
  text-align: center;
  color: #fff;
  border-radius: 10px;
  padding: 6px;
  cursor: pointer;
}

.settings p {
  margin: 0;
  font-size: 20px;
  font-weight: 400;
  line-height: 32px;
}

.info {
  text-align: center;
}

.name-bio {
  margin-bottom: 20px;
  display: flex;
  flex-flow: column;
  div {
    text-align: left;
    display: flex;
    align-items: center;
    input {
      height: 20px;
      font-size: 16px;
    }
    svg {
      width: 20px;
      height: 20px;
    }
  }
}

.info h2 {
  margin: 0;
  text-align: left;
  font-family: "Source Han Sans CN";
  font-style: normal;
  font-weight: 400;
  font-size: 30px;
  line-height: 46px;
}

.info p {
  margin: 8px 0 0;
  font-family: "Inter";
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 25px;
  text-align: left;
}

.container-body-profile {
  /* background-color: #662D91; */
  margin-top: 50px;
  /* max-height: 100px; */
}

.list_area {
  margin: 0 auto;
}

.menu {
  display: flex;
}

.menu_btn {
  background-color: #fff;
  border: none;
  height: 36px;
  font-size: 20px;
  padding: 0 20px;
}

.menu_btn:hover {
  background-color: #f5f5f5;
}

.active_menu_btn {
  border-bottom: 2px solid #662d91;
}

.card_area {
  margin-top: 20px;
  text-align: left;
}

</style>
