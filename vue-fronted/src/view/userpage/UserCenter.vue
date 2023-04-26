<template>
  <user-header></user-header>
  <!-- 页面模板 -->
  <el-row>
    <el-col :span="24">
      <div class="background">
        <!-- 背景图片 -->
        <img src="https://placekitten.com/800/600" alt="background" />
      </div>
      <el-row>
        <el-col :sm="24" :md="3" :offset="5">
          <div class="avatar">
            <!-- 头像 -->
            <img src="https://placekitten.com/200/200" alt="avatar" />
          </div>
        </el-col>
        <el-col :sm="24" :md="4">
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
        <el-col :sm="24" :md="3" :offset="4">
          <div class="settings">
            <!-- 账号设置 -->
            <p>账号设置</p>
          </div>
        </el-col>
      </el-row>
    </el-col>
  </el-row>
  <el-row class="profile-wrapper">
    <el-col :span="24">
      <div class="table">
        <!-- 表格区域 -->
      </div>
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
};
</script>

<style scoped>
/* 样式表 */
.background {
  position: relative;
  width: 62.5%; 
  height: 23.15%; 
  top: 0%;
  left: 18.75%;
  overflow: hidden;
}

.background img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.avatar {
  position: relative;
  bottom: 130px;
  width: 240px;
  height: 240px;
  border-radius: 50%;
  overflow: hidden;
}

.avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.profile {
  position: relative;
  margin-left: 35px;
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
  width: 172px;
}

.settings p{
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
</style>
