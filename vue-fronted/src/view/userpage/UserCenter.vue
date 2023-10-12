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
                  <img class="container-avatar-img" :src=userInfo.userAvatar alt="avatar" />
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
                          <input type="text" v-model="userInfo.userSignature" @blur="changeSignature" />
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
              <el-dialog title="头像上传" v-model="cropperModel" width="950px">
                <cropper-image :Name="cropperName" @uploadImgSuccess="handleUploadSuccess" ref="child">
                </cropper-image>
              </el-dialog>
            </el-row>
          </el-col>
        </el-row>

        <el-row style="height: 20px; background-color: #fcf2ff;"></el-row> <!-- 分割区域 -->

        <el-row class="column_line"> <!-- 栏目选择行 -->
          <el-col :span="6">
            <el-button class="column_btn">
              <img :src="require('../../assets/DramaList/star.png')" alt="" class="star_icon_small">
              &emsp; 主页
            </el-button>
          </el-col>
          <el-col :span="6">
            <el-button class="column_btn">
              <img :src="require('../../assets/DramaList/star.png')" alt="" class="star_icon_small">
              &emsp; 收藏
            </el-button>
          </el-col>
          <el-col :span="6">
            <el-button class="column_btn">
              <img :src="require('../../assets/DramaList/star.png')" alt="" class="star_icon_small">
              &emsp; 追番
            </el-button>
          </el-col>
          <el-col :span="6">
            <el-button class="column_btn">
              <img :src="require('../../assets/DramaList/star.png')" alt="" class="star_icon_small">
              &emsp; 动态
            </el-button>
          </el-col>
        </el-row>

        <el-row> <!-- 我的收藏 -->
          <el-col :span="22" class="list_area">
            <div class="list_area_first_line">
              <img :src="require('../../assets/DramaList/star.png')" alt="" class="star_icon">
              <div class="label_name">
                我的收藏
              </div>
              <el-button class="watch_all_btn">
                查看全部
              </el-button>
            </div>
            
            <el-row class="card_row">
                <DramaCard :msg="sheet" v-for="sheet in userCollectSheet1"/>
            </el-row>
            <el-row class="card_row">
              <DramaCard :msg="sheet" v-for="sheet in userCollectSheet2"/>
            </el-row>
            <el-row>
              <div class="page-buttons">
                <el-button size="small" icon="CaretLeft" circle class="arrowBtn" @click="changePageCollect(currentPageCollect - 1)"/>
                <div class="page-input">
                  <input v-model.number="inputPageCollect" @keydown.enter="jumpToPageCollect" @blur="jumpToPageCollect" class="page-input-box" type="number">
                  <span class="total-pages">/ {{ totalPagesCollect }}</span>
                </div>
                <el-button size="small" icon="CaretRight" circle class="arrowBtn" @click="changePageCollect(currentPageCollect + 1)"/>
              </div>
            </el-row>
          </el-col>
        </el-row>

        <el-row> <!-- 我的追番 -->
          <el-col :span="22" class="list_area">
            <div class="list_area_first_line">
              <img :src="require('../../assets/DramaList/star.png')" alt="" class="star_icon">
              <div class="label_name">
                我的追番
              </div>
              <el-button class="watch_all_btn">
                查看全部
              </el-button>
            </div>
            
            <el-row class="card_row">
                <DramaCard :msg="sheet" v-for="sheet in userFollowSheet1"/>
            </el-row>
            <el-row class="card_row">
              <DramaCard :msg="sheet" v-for="sheet in userFollowSheet2"/>
            </el-row>
            <el-row>
              <div class="page-buttons">
                <el-button size="small" icon="CaretLeft" circle class="arrowBtn" @click="changePageFollow(currentPageFollow - 1)"/>
                <div class="page-input">
                  <input v-model.number="inputPageFollow" @keydown.enter="jumpToPageFollow" @blur="jumpToPageFollow" class="page-input-box" type="number">
                  <span class="total-pages">/ {{ totalPagesFollow }}</span>
                </div>
                <el-button size="small" icon="CaretRight" circle class="arrowBtn" @click="changePageFollow(currentPageFollow + 1)"/>
              </div>
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
import CropperImage from "../../components/CropperImage.vue";
import { alertBox } from "@/utils/alertBox.js";
import { CaretLeft, CaretRight } from "@element-plus/icons-vue";

export default {
  name: "UserCenter",
  components: {
    UserHeader,
    DramaCard,
    CropperImage,
    CaretLeft,
    CaretRight,
  },
  data() {
    return {
      isInputMode: false,
      userInfo: {
        userNickName: "张后斌", // 用户名
        userSignature: "我是懒坑小子张后斌", // 个人简介
      },
      currentPageCollect: 1,
      currentPageFollow: 1,
      inputPageCollect: 1,
      inputPageFollow: 1,
      userCollectSheet:[
        {
          title: "番剧 1",
          imgSrc: "https://www.themoviedb.org/t/p/original/mvolqXssikgLeUomc59cB2RkH1k.jpg",
          comments: 100,
          collects: 100,
        },],
      userFollowSheet: [
        {
          title: "番剧 1",
          imgSrc: "https://www.themoviedb.org/t/p/original/mvolqXssikgLeUomc59cB2RkH1k.jpg",
          comments: 100,
          collects: 100,
        },
        {
          title: "番 ailflef 剧 1",
          imgSrc: "https://www.themoviedb.org/t/p/original/mvolqXssikgLeUomc59cB2RkH1k.jpg",
          comments: 132,
          collects: 1124,
        },
        {
          title: "番剧 dawl1",
          imgSrc: "https://www.themoviedb.org/t/p/original/mvolqXssikgLeUomc59cB2RkH1k.jpg",
          comments: 34,
          collects: 12,
        },
        {
          title: "番剧 dawl1",
          imgSrc: "https://www.themoviedb.org/t/p/original/mvolqXssikgLeUomc59cB2RkH1k.jpg",
          comments: 34,
          collects: 12,
        },
        {
          title: "番剧 dawl1",
          imgSrc: "https://www.themoviedb.org/t/p/original/mvolqXssikgLeUomc59cB2RkH1k.jpg",
          comments: 34,
          collects: 12,
        },
        {
          title: "番剧 dawl1",
          imgSrc: "https://www.themoviedb.org/t/p/original/mvolqXssikgLeUomc59cB2RkH1k.jpg",
          comments: 34,
          collects: 12,
        },
        {
          title: "番剧 dawl1",
          imgSrc: "https://www.themoviedb.org/t/p/original/mvolqXssikgLeUomc59cB2RkH1k.jpg",
          comments: 34,
          collects: 12,
        },
        {
          title: "番剧 dawl1",
          imgSrc: "https://www.themoviedb.org/t/p/original/mvolqXssikgLeUomc59cB2RkH1k.jpg",
          comments: 34,
          collects: 12,
        },
        {
          title: "番剧 dawl1",
          imgSrc: "https://www.themoviedb.org/t/p/original/mvolqXssikgLeUomc59cB2RkH1k.jpg",
          comments: 34,
          collects: 12,
        },
      ],
      //裁切图片参数
      cropperModel: false,
      cropperName: '',
    };
  },
  methods: {
    goToUserInfo() {
      this.$router.push("/userinfo");
    },
    changeSignature() {
      // 提交新的 userSignature
      if (this.isInputMode) {
        var that = this;
        this.$api.user.changeUserInfo(this.userInfo)
          .then(function (response) {
            if (response.data.msg === "success") {
              alertBox("用户个性签名修改成功！", "success", that);
            } else {
              alertBox("用户个性签名修改失败！", "error", that);
            }
          })
          .catch(function (error) {
            alertBox("连接异常，请检查网络或稍后再试。", "error", that);
          });
      }
      this.isInputMode = !this.isInputMode;
      // console.log('失去焦点');
    },
    changeAvatar() {
      console.log("进入修改头像");
      this.cropperName = 'test';
      this.cropperModel = true;
    },
    handleUploadSuccess(data) {
      console.log("上传成功");
      console.log(data);
      this.cropperModel = false;
    },
    changePageCollect(page) {
      if (page >= 1 && page <= this.totalPagesCollect) {
        this.currentPageCollect = page;
        this.inputPageCollect = page;
      }
    },
    changePageFollow(page) {
      if (page >= 1 && page <= this.totalPagesFollow) {
        this.currentPageFollow = page;
        this.inputPageFollow = page;
      }
    },
    jumpToPageCollect() {
      const page = parseInt(this.inputPageCollect);
      if (page >= 1 && page <= this.totalPagesCollect) {
        this.currentPageCollect = page;
        this.inputPageCollect = page;
      } else if (page < 1) {
        this.currentPageCollect = 1;
        this.inputPageCollect = 1;
      } else if (page > this.totalPagesCollect) {
        this.currentPageCollect = this.totalPagesCollect;
        this.inputPageCollect = this.totalPagesCollect;
      }
    },
    jumpToPageFollow() {
      const page = parseInt(this.inputPageFollow);
      if (page >= 1 && page <= this.totalPagesFollow) {
        this.currentPageFollow = page;
        this.inputPageFollow = page;
      } else if (page < 1) {
        this.currentPageFollow = 1;
        this.inputPageFollow = 1;
      } else if (page > this.totalPagesFollow) {
        this.currentPageFollow = this.totalPagesFollow;
        this.inputPageFollow = this.totalPagesFollow;
      }
    },
  },
  created() {
    var that = this;
    this.$api.user.getUserInfo()
      .then(function (response) {
        if (response.data.msg === "success") {
          var statusCode = response.data.data.statusCode;
          if (statusCode == 1) {
            alertBox("获取用户信息失败，错误码：1", "error", that);
          } else {
            that.userInfo.userNickName = response.data.data.nickname;
            that.userInfo.userSignature = response.data.data.signature;
            that.userInfo.userAvatar = response.data.data.avatar;
            if (that.userInfo.userAvatar == "") {
              that.userInfo.userAvatar = "http://123.56.45.70/user_avatar/8c9d9dbcc7ab402f8d7f096afd9b2547.jpg"
            }
          }
        } else {
          alertBox("获取用户信息失败", "error", that);
        }
      })
      .catch(function (error) {
        alertBox("连接异常，请检查网络或稍后再试。", "error", that);
      });
  },
  computed:
  {
    totalPagesCollect () {
      return Math.ceil(this.userCollectSheet.length / 8);
    },
    totalPagesFollow () {
      return Math.ceil(this.userFollowSheet.length / 8);
    },
    userCollectSheet1 () {
      return this.userCollectSheet.slice((this.currentPageCollect - 1) * 8, this.currentPageCollect * 8 - 4);
    },
    userCollectSheet2 () {
      return this.userCollectSheet.slice(this.currentPageCollect * 8 - 4, this.currentPageCollect * 8);
    },
    userFollowSheet1 () {
      return this.userFollowSheet.slice((this.currentPageFollow - 1) * 8, this.currentPageFollow * 8 - 4);
    },
    userFollowSheet2 () {
      return this.userFollowSheet.slice(this.currentPageFollow * 8 - 4, this.currentPageFollow * 8);
    },
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
      position: relative;
      width: 240px;
      height: 240px;
      border-radius: 50%;
      overflow: hidden;
      /* margin-left: 50px; */
    }

    .overlay {
      position: absolute;
      // justify-content: center;
      top: 0;
      left: 50%;
      transform: translate(-50%, 0);
      width: 240px;
      height: 240px;
      border-radius: 50%;
      opacity: 0;
      background-color: rgba(0, 0, 0, 0.5);
      color: white;
      transition: opacity 0.3s ease;
      /* 添加过渡效果 */
      font-size: 16px;
      line-height: 240px;
    }

    // .overlay {
    //   position: absolute;
    //   top: 50%;
    //   left: 50%;
    //   transform: translate(-50%, -50%);
    //   background-color: rgba(0, 0, 0, 0.5);
    //   color: white;
    //   padding: 10px;
    //   font-size: 16px;
    //   border-radius: 5px;
    //   opacity: 0; /* 初始时隐藏覆盖层 */
    //   transition: opacity 0.3s ease; /* 添加过渡效果 */
    // }
    &:hover .overlay {
      opacity: 1;
      /* 鼠标悬停时显示覆盖层 */
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

.column_line {
  width: 100%;
  height: 81px;
  background-color: #ebebeb;
  :hover {
    background-color: #b8b8b8;
    border-radius: 10px;
  }
}

.column_btn {
  width: 100%;
  height: 100%;
  border-radius: 0;
  border-width: 0px;
  background-color: #fff;
  color: #000;
  font-size: 20px;
  font-weight: 400;
}

.star_icon_small {
  width: 20px;
  height: 20px;
  position: relative;
}

.list_area {
  margin: 0 auto;
  max-width: 1060px;
}

.list_area_first_line {
  display: flex;
  align-items: center;
  margin-top: 30px;
  margin-bottom: 20px;
}

.star_icon {
  width: 35px;
  height: 35px;
  position: relative;
  bottom: 5px;
}

.label_name {
  font-size: 30px;
  font-weight: 500;
  text-align: left;
  margin-left: 20px;
  width: 100%;
}

.watch_all_btn {
  border-radius: 25px;
  width: 250px;
  font-size: 16px;
}

.card_row {
  min-width: 900px;
  margin-top: 30px;
  display: -webkit-flex;
  display: flex;
  justify-content: space-between;
}

.page-buttons 
{
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 2px;
  gap: 5px;
  margin-top: 20px;
  margin-left: auto;
}

.page-input {
  display: flex;
  align-items: center;
  gap: 5px;
}

.page-input-box {
  width: 40px;
  height: 20px;
  text-align: center;
  font-size: 10px;
  border-radius: 5px;
  outline: none;
  border: none;
}

.page-input-box::-webkit-outer-spin-button,
.page-input-box::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

.total-pages {
  font-size: 12px;
}

.arrowBtn {
  width: 20px;
  height: 20px;
  color: #fff;
  background-color: #8557A7; /* 紫色 */
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.arrowBtn:hover {
  background-color: #662D91; /* 鼠标悬停时的紫色 */
}
</style>
