<template>
  <user-header></user-header>
  <!-- 页面模板 -->
  <el-row style="background-color: #FCF2FF">
    <el-col :span="12" :offset="6" class="container">
      <div class="container-header">
        <img src="https://placekitten.com/800/600" alt="background-image">
      </div>
      <el-row>
        <el-col :span="22" :offset="1" class="container-body">
          <el-row class="container-body-info">
            <el-col :span="6">
              <img class="container-avatar" src="https://placekitten.com/200/200" alt="avatar">
            </el-col>
            <el-col :span="13">
              <div class="profile">
                <div class="info">
                  <div class="name-bio">
                    <!-- 用户名和个人简介 -->
                    <h2>{{ username }}</h2>
                    <p>{{ bio }}</p>
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
          <el-row class="container-body-profile">
            <el-col :span="16">
              <div style="background-color: #ccc; height: 400px;"></div>
            </el-col>

            <el-col :span="5" :offset="3">
              <div style="background-color: #ccc; height: 400px;"></div>
            </el-col>
          </el-row>
        </el-col>
      </el-row>
    </el-col>
  </el-row>
</template>

<script>
import UserHeader from '../../components/UserHeader.vue';

export default {
  name: "ProfilePage",
  components: {
    UserHeader,
  },
  data() {
    return {
      username: "张后斌", // 用户名
      bio: "我是懒坑小子张后斌", // 个人简介
    };
  },
  methods: {
    goToUserInfo() {
      this.$router.push('/userinfo');
    }
  }
};
</script>

<style scoped>
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

.container-avatar {
  position: relative;
  bottom: 130px;
  width: 240px;
  height: 240px;
  border-radius: 50%;
  overflow: hidden;
  /* margin-left: 50px; */
}

.container-body-info {
  height: 100px;
}

.profile {
  position: relative;
  margin-left: 25px;
  margin-top: 20px;
}

.settings {
  margin-top: 30px;
  background: #662D91;
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
}

.info h2 {
  margin: 0;
  text-align: left;
  font-family: 'Source Han Sans CN';
  font-style: normal;
  font-weight: 400;
  font-size: 30px;
  line-height: 46px;
}

.info p {
  margin: 8px 0 0;
  font-family: 'Inter';
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
</style>