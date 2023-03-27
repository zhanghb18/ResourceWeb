<template>
    <div class="head">
        <div class="logo">
            <img src="../../assets/logo.png" alt="logo" />
            <p>Logo Name</p>
        </div>
        <div id="search_content" class="s_content">
            <el-row>
                <el-col :span="22">
                    <div style="display: flex; align-items: center; padding-right: 10px;">
                        <input type="text" class="search_input" v-model="searchText" placeholder="请输入关键字"
                            @focus="clearPlaceholder">
                    </div>
                </el-col>
                <el-col :span="2">
                    <div class="search_circle">
                        <img src="../../assets/logo.png">
                    </div>
                </el-col>
            </el-row>
        </div>
        <div class="user">
            <a href="#">登录</a>
            <a href="#">注册</a>
            <el-avatar src="../../assets/logo.png" size="medium" class="avatar-circle"></el-avatar>
        </div>
    </div>
  </template>
  
  <style scoped>
  .head {
    background: url('../../assets/acgpage/headbackground.png');
    display: flex;
    background-size: fill;
    background-attachment: fixed;
    background-repeat: no-repeat;
    justify-content: space-between;
    height: 193px;
    width: 100%;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    padding: 0 50px;
  }
  
  .logo {
    display: flex;
    align-items: flex-start;
    margin-left: 40; 
    margin-top: 30px;
  }
  
  .logo img {
    height: 80px;
    margin-right: 20px;
  }
  
  .logo p {
    font-size: 24px;
    font-weight: bold;
  }
  
  .search_input {
    box-sizing: border-box;
    width: 100%;
    height: 40px;
    border-radius: 5px;
    border: none;
    box-shadow: none;
    padding: 5px 20px;
    font-size: 15px;
    outline-color: none;
    margin-top: 30px;
}

.search_input:focus {
    border-color: #409eff;
    box-shadow:
        inset 0 -3em 3em #f2f2f2,
        0.3em 0.3em 1em rgba(155, 155, 155, 0.3);
    outline: 0px;
}

.search_input::placeholder {
    color: #999;
    font-size: 15px;
    padding-left: 0px;
}
  
  .user {
    display: flex;
    align-items: flex-start;
    margin-right: 40px;
    margin-top: 30px;
  }
  
  .user a {
    font-size: 16px;
    margin-right: 20px;
    text-decoration: none;
    color: #000;
  }
  
  </style>
  