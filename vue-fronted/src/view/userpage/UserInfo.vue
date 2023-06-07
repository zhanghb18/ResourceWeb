<template>
  <el-row class="user-info-root">
    <user-header></user-header>
    <el-col :lg="{ span: 16, offset: 4 }" class="container">
      <div class="container-header">
        <img src="https://placekitten.com/800/600" alt="background" class="header-image" />
      </div>
      <el-row class="container-body">
        <el-col :span="8" class="container-body-nav">
          <div class="user-profile-nav">
            <div class="user-profile-avatar">
              <img src="https://placekitten.com/200/200" alt="avatar" />
              <span>叫我 zizi 就好了</span>
            </div>
          </div>
        </el-col>

        <el-col :span="16" class="container-body-content">
          <div class="user-profile-body">
            <span>资料设置</span>
            <div class="user-profile-body-line">
              <div style="background-color: #662d91; width: 20%; height: 8px"></div>
            </div>
            <div class="user-profile-body-item">
              <span>头像</span>
              <img src="https://placekitten.com/200/200" alt="avatar" />
              <button>修改</button>
            </div>
          </div>
        </el-col>
      </el-row>
    </el-col>
  </el-row>
</template>

<script>
import UserHeader from "../../components/UserHeader.vue";

export default {
  name: "UserInfo",
  components: {
    UserHeader,
  },
  data() {
    return {
      activeOption: "option1",
    };
  },
  methods: {
    toggleActive1() {
      this.activeOption = "option1";
    },
    toggleActive2() {
      this.activeOption = "option2";
    },
    toggleActive3() {
      this.activeOption = "option3";
    },
  },
};
</script>

<style scoped>
.user-info-root {
  background-color: #fcf2ff;
  min-width: 1200px;
  /* height: auto; */
  /* overflow-x: scroll; */
}
.container {
  background-color: #ffffff;
  height: auto;
  min-height: 90vh;
  /* width: 100px; */
}

.header-image {
  height: 121px;
  width: 100%;
  object-fit: cover;
}

.container-body-nav {
  /* background-color: red; */
  height: auto;
}

.container-body-content {
  /* background-color: green; */
  height: auto;
}

.user-profile-nav {
  /* width: 300px; */
  height: 432px;
  background-color: #fcf2ff;
  margin-left: 24px;
  margin-top: 22px;
  border-radius: 5px;
  float: left;
  /* display: inline-block; */
}

.user-profile-avatar {
  width: 100%;
  height: 132px;
  display: flex;
}

.user-profile-avatar > img {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  margin: 27px 18px 25px 35px;
}

.user-profile-avatar > span {
  margin: 52px 35px 0 0;
}

.user-profile-body {
  width: 100%;
  height: 780px;
  margin: 22px 29px 0 23px;
  background-color: #fcf2ff;
  float: right;
  /* display: inline-block; */
}

.user-profile-body > span {
  line-height: 30.26px;
  width: 100px;
  height: 30px;
  margin-left: 30px;
  margin-top: 27px;
  margin-bottom: 27px;
  font-size: 25px;
  display: block;
}
</style>
