<template>
  <div class="header">
    <div class="logo" @click="this.$router.push('/')">
      <div class="Logo_circle">
        <img src="../assets/logo.png" alt="logo" />
      </div>
      <p>某次元</p>
    </div>
    <div class="user">
      <router-link to="/userinfo">个人中心</router-link>
      <a href="#">观看历史</a>

      <el-popover
        placement="bottom"
        :width="150"
        trigger="hover"
      >
        <template #reference>
        <el-avatar :src="this.$store.getters.getAvatar"></el-avatar>
        </template>
        <el-button class="logoutBtn" @click="loginOut">退出登录</el-button>
      </el-popover>
    </div>
  </div>
</template>

<script>
export default {
  name: "UserHeader",
  methods: {
    loginOut() {
      localStorage.removeItem("token");
      localStorage.removeItem("avatar");
      this.$store.commit("updateToken");
      this.$store.commit("updateAvatar");
      this.$router.push("/");
    },
  },
};
</script>

<style scoped>
.header {
  width: 100%;
  height: 100px;
  background: url("../assets/acgpage/headbackground.png");
  background-size: fill;
  background-attachment: fixed;
  display: flex;
  justify-content: space-between;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.logo {
  /* logo 样式 */
  display: flex;
  align-items: flex-start;
  margin-left: 40px;
  margin-top: 30px;
  cursor: pointer;
}

.Logo_circle {
  width: 46px;
  height: 46px;
  border-radius: 50%;
  background-color: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-right: 10px;
}

.Logo_circle img {
  width: 60%;
  height: 60%;
  object-fit: contain;
}

.logo p {
  /* logo 文字样式 */
  font-size: 20px;
  margin-top: 12px;
  font-family: "DOUYU", cursive;
  color: white;
}

.user {
  /* 用户登录注册样式 */
  display: flex;
  align-items: flex-start;
  margin-top: 30px;
}

.user a {
  /* 用户登录注册链接样式 */
  font-size: 16px;
  margin-right: 20px;
  margin-top: 12px;
  text-decoration: none;
  color: #000;
}

.el-avatar {
  margin-right: 40px;
}

.logoutBtn {
  width: 100%;
  margin-top: 10px;
  margin-bottom: 10px;
  background-color: #fff;
  color: #000;
  border: none;
  border-radius: 0;
  font-size: 16px;
}
</style>