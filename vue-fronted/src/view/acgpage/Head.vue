<template>
  <!-- 头部组件 -->
  <div class="head">
      <!-- logo -->
      <div class="logo">
        <div class="Logo_circle">
          <img src="../../assets/logo.png" alt="logo" />
        </div>
          <p>文字LOGO</p>
      </div>
      <!-- 搜索框 -->
      <div id="search_content" class="s_content">
          <div style="display: flex;">
              <input type="text" class="search_input" placeholder="请输入关键字:">
              <button class="search_button">
                <img src="../../assets/acgpage/SearchLogo.png">
              </button>
          </div>
      </div>
      <!-- 用户登录注册 -->
      <div class="user">
          <a href="#">登录</a>
          <a href="#">注册</a>
          <el-avatar src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"></el-avatar>
      </div>
  </div>
</template>

<style scoped>
@import '../../assets/font/font.css';
.head {
  /* 头部背景 */
  background: url('../../assets/acgpage/headbackground.png');
  background-size: fill;
  background-attachment: fixed;
  display: flex;
  justify-content: space-between;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  width: 100%; 
  height: 192px;
}

.logo {
  /* logo样式 */
  display: flex;
  align-items: flex-start;
  margin-left: 40px; 
  margin-top: 30px;
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
  /* logo文字样式 */
  font-size: 20px;
  margin-top: 12px;
  font-family: 'DOUYU', cursive;
  color: white;
}

.search_input {
  /* 搜索框样式 */
  box-sizing: border-box;
  width: 574px;
  height: 46px;
  border-radius: 5px;
  border: none;
  box-shadow: none;
  padding: 5px 20px;
  font-size: 15px;
  outline-color: none;
  margin-top: 30px;
  display: flex;
  align-items: center;
}

.search_input:focus {
  /* 搜索框聚焦样式 */
  border-color: #409eff;
  box-shadow:
      inset 0 -3em 3em #f2f2f2,
      0.3em 0.3em 1em rgba(155, 155, 155, 0.3);
  outline: 0px;
}

.search_input::placeholder {
  /* 搜索框占位符样式 */
  color: #999;
  font-size: 15px;
  padding-left: 0px;
}
.search_button {
  /* 搜索按钮样式 */
  background-color: transparent;
  border: none;
  cursor: pointer;
  margin-top: 30px;
  margin-left: -48px;
}

.search_button img {
  /* 搜索按钮图片样式 */
  height: 26px;
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
.el-avatar{
  margin-right: 40px;
}

</style>
