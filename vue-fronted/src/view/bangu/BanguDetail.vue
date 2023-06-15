<template>
  <el-row class="bangu-detail-root">
    <user-header></user-header>
    <el-col :lg="{ span: 16, offset: 4 }" class="container">
        <el-row class="container-head">
          <div :background-image = imgURL>
            <el-col :lg="{ span: 6 }" class="left-col">
              <img :src = imgURL class="bangu-image">
            </el-col>
            <el-col :lg="{ span: 16 }" class="right-col">
              <p>这是简介的内容</p>
            </el-col>
          </div>
        </el-row>
    </el-col>
  </el-row>
</template>
  
  <script>
  import UserHeader from "../../components/UserHeader.vue";
  
  export default {
    name: "BanguDetail",
    components: {
      UserHeader,
    },
    data() {
      return {
        bgOpacity: 0.15, // 背景图片透明度初始值为0.5
        imgURL: 'https://s3-alpha-sig.figma.com/img/c0ef/6f30/db825b75e4a7ed38777131fded749f57?Expires=1687737600&Signature=AjcP1ZaOqnIDNEIAM72zk~bX0FXD8ViYPARIc6MZ1twNgNHwjzweeid6TwVxc8GqEXsdMpHRSFKSOWwYd3Lr~DulVkGx870TZESRemLuftYWU3tv9Lp-rdmEXxNYvZgTNehiIuvKd7grRHa1NDTnRH65~Bx7xVvztTvnpQO8Of1SVdu6Xwv6oan5K1iuv6mwIf3AK5xlXd08etkpVD2dNrBXGpI6LQczFFuY3JS7kwGHiU3gyz3w167hNdmhVG77eb0gRrJ8zfpoDwrLaNn6zi2RYPOZftkGdMmq0CNNfCIwyj5sbSRYZdEJAigkDa3CxCfSKA~dnCt3txGcH~zcsA__&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4' // 这里填写你的背景图片地址
      };
    },
  };
  </script>
  
  <style scoped>
  .bangu-detail-root {
    background-color: #fcf2ff;
    min-width: 1200px;
    font-size: 16px;
    z-index: -2;
    /* height: auto; */
    /* overflow-x: scroll; */
  }
  
  .container {
    background-color: #ffffff;
    height: auto;
    z-index: -1;
    /* width: 100px; */
  }
  .left-col{

  }
  .right-col{

  }

  .bangu-image{
    height: 31.6vh;
    min-height: 342px;
    margin-top: 46px;
    margin-left: 1.25vw;
    margin-right: 1.25vw;
  }
  .container-head {
    /* background-color: red; */
    min-height: 520px;
  }
  .container-body-nav {
    /* background-color: red; */
    height: auto;
    /* margin: 22px 0 0 22px; */
    margin-top: 22px;
    margin-left: 1.25vw;
    margin-right: 1.25vw;
  }
  
  .container-body-content {
    /* background-color: green; */
    height: auto;
    margin-top: 22px;
    margin-right: 1.3vw;
    /* margin: 22px 22px 0 20px; */
  }
  
  .user-profile-nav {
    width: 100%;
    height: 432px;
    background-color: #fcf2ff;
    border-radius: 5px;
    float: left;
    /* display: inline-block; */
  }
  
  .user-profile-avatar {
    width: 100%;
    height: 132px;
    display: flex;
  }
  
  .user-profile-avatar>img {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    margin: 27px 18px 25px 35px;
  }
  
  .user-profile-avatar>span {
    margin: 52px 35px 0 0;
    white-space: nowrap;
    /* 禁止换行 */
    overflow: hidden;
    /* 控制文本溢出隐藏 */
    text-overflow: ellipsis;
    /* 使用省略号截断文本 */
  }
  
  .user-profile-setting {
    display: flex;
    cursor: pointer;
    justify-content: space-around;
    align-items: center;
    height: 100px;
  }
  
  .user-profile-setting.active {
    background-color: #c2abd3;
  }
  
  /* .user-profile-setting svg {
    margin: 30px 0 29px 49px;
  }
  
  .user-profile-setting span {
    margin-top: 38px;
    margin-left: 65px;
  } */
  
  .user-profile-body {
    width: 100%;
    height: 780px;
    /* margin: 22px 29px 0 23px; */
    background-color: #fcf2ff;
    border-radius: 5px;
    float: right;
    /* display: inline-block; */
  }
  
  .user-profile-body>span {
    line-height: 30.26px;
    width: 100px;
    height: 30px;
    margin-left: 30px;
    margin-top: 27px;
    margin-bottom: 27px;
    font-size: 25px;
    display: block;
  }
  
  .user-profile-body-item {
    display: flex;
    align-items: center;
    margin: 10px 0;
    height: 100px;
  }
  
  .user-profile-body-item img {
    width: 68px;
    height: 68px;
    border-radius: 50%;
    float: left;
  }
  
  .user-profile-body-item button {
    width: 50px;
    height: 22px;
    background-color: #fcf2ff;
    border: none;
    cursor: pointer;
  }
  
  .user-profile-body-item div {
    float: left;
  }
  </style>
  