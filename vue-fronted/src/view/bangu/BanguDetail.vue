<template>
  <el-row class="bangu-detail-root">
    <user-header></user-header>
    <el-col :lg="{ span: 16, offset: 4 }" class="container">
        <el-row class="container-head">
          <img :src = imgURL class="background-img" :style="{'opacity': bgOpacity}">
          <el-col :span = 7 class="left-col">
            <img :src = imgURL class="bangu-image">
          </el-col>
          <el-col :span = 15 class="right-col">
            <p class="bangu-name">{{ banguName }}</p>
            <p class="bangu-info">{{ "放送日期：" + turnOverTime }}</p>
            <p class="bangu-info">{{ "放送起始：" +startTime }}</p>
            <p class="bangu-info">{{ '总集数：' + totalNum }}</p>
            <p class="brief-info">{{ '简介：' +briefInfo }}</p>
          </el-col>
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
        imgURL: 'https://s3-alpha-sig.figma.com/img/c0ef/6f30/db825b75e4a7ed38777131fded749f57?Expires=1687737600&Signature=AjcP1ZaOqnIDNEIAM72zk~bX0FXD8ViYPARIc6MZ1twNgNHwjzweeid6TwVxc8GqEXsdMpHRSFKSOWwYd3Lr~DulVkGx870TZESRemLuftYWU3tv9Lp-rdmEXxNYvZgTNehiIuvKd7grRHa1NDTnRH65~Bx7xVvztTvnpQO8Of1SVdu6Xwv6oan5K1iuv6mwIf3AK5xlXd08etkpVD2dNrBXGpI6LQczFFuY3JS7kwGHiU3gyz3w167hNdmhVG77eb0gRrJ8zfpoDwrLaNn6zi2RYPOZftkGdMmq0CNNfCIwyj5sbSRYZdEJAigkDa3CxCfSKA~dnCt3txGcH~zcsA__&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4', // 这里填写你的背景图片地址
        banguName: "久保同学不放过我",
        turnOverTime: "星期二",
        startTime: "2023年1月23日",
        totalNum: 12,
        briefInfo: "懒坑小子张后斌，他是一个大sb，脑子不好爱睡觉，同时还是大虚比，哈哈哈哈哈哈，嘻嘻嘻嘻嘻嘻，你能把我怎么样，我是你爹你是屁",
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
  .background-img {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    z-index: -1;
  }
  .left-col{
    margin-top: 46px;
    margin-left: 1.25vw;
    margin-right: 1.25vw;
  }
  .right-col{
    margin-top: 50px;
    margin-right: 1.25vw;
  }
  .bangu-image{
    height: 31.6vh;
    width: 12.5vw;
    min-height: 342px;
    min-width: 241px;
    box-shadow: 0 0 0 2.5px rgba(102, 51, 153, 0.5);
  }
  .container-head {
    /* background-color: red; */
    min-height: 520px;
  }

  .bangu-name {
  font-size: 40px;
  text-align: left;
  margin: 0px 0px 19px 0px;
}

  .bangu-info{
    font-size: 20px;
    margin: 0px 0px 0px 0px;
    text-align: left;
  }
  .brief-info{
    font-size: 20px;
    margin: 19px 0px 0px 0px;
    text-align: left;
  }
  </style>
  