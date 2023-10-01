<template>
    <el-row class="bangu-detail-root">
      <user-header></user-header>
      <el-col :lg="{ span: 16, offset: 4 }" class="container">
        <el-row class="container-head">
          <img :src="imgUrl" class="background-img" :style="{'opacity': bgOpacity}">
          <el-col :span="7" class="left-col">
            <img :src="imgUrl" class="bangu-image">
          </el-col>
          <el-col :span="15" class="right-col">
            <p class="bangu-name">{{ name }}</p>
            <p class="bangu-info">{{ "放送日期：" + turnOverTime }}</p>
            <p class="bangu-info">{{ "放送起始：" + startTime }}</p>
            <p class="bangu-info">{{ '总集数：' + episodes }}</p>
            <p class="brief-info">
              简介：{{ displayInfo }}
              <span v-if="!moreInfoFlag && briefInfo.length > 150" class="more" @click="toggleMore">[更多]</span>
              <span v-if="moreInfoFlag" class="more" @click="toggleMore">[隐藏]</span>
            </p>
            <div class="taginfo">
              <p v-for="(tag, index) in tagInfo" :key="index" class="tag">{{ tag }}</p>
            </div>
            <div class="right-top-icons">
              <img src="@/assets/DramaList/follow.png" alt="follow" class="icon">
              <img src="@/assets/DramaList/star.png" alt="star" class="icon">
            </div>
          </el-col>
        </el-row>
        <el-row class="container-body">
          <el-col :span="7" class="left-col">
          </el-col>
          <el-col :span="15" class="right-col">
          </el-col>
        </el-row>
      </el-col>
    </el-row>
  </template>

  <script>
  import UserHeader from "../../components/UserHeader.vue";

  export default {
    components: {
      UserHeader,
    },
    data() {
      return {
        bgOpacity: 0.15,
        imgUrl: '',
        name: "久保同学不放过我",
        turnOverTime: "星期二",
        startTime: "2023年1月23日",
        episodes: 12,
        briefInfo: "懒坑小子张后斌，他是一个大sb，脑子不好爱睡觉，同时还是大虚比，哈哈哈哈哈哈，嘻嘻嘻嘻嘻嘻，你能把我怎么样，我是你爹你是屁，懒坑小子张后斌，他是一个大sb，脑子不好爱睡觉，同时还是大虚比，哈哈哈哈哈哈，嘻嘻嘻嘻嘻嘻，你能把我怎么样，我是你爹你是屁，懒坑小子张后斌，他是一个大sb，脑子不好爱睡觉，同时还是大虚比，哈哈哈哈哈哈，嘻嘻嘻嘻嘻嘻，你能把我怎么样，我是你爹你是屁，懒坑小子张后斌，他是一个大sb，脑子不好爱睡觉，同时还是大虚比，哈哈哈哈哈哈，嘻嘻嘻嘻嘻嘻，你能把我怎么样，我是你爹你是屁",
        moreInfoFlag: false,
        tagInfo: ['# 老张是狗', '# 如来', '# 老张真是狗？','# 贺启爬坏','# 贺启爬没jj','# 矛头','# 毛字','# 呃呃','#啦啦啦'],
      };
    },
    computed: {
      displayInfo() {
        return this.moreInfoFlag ? this.briefInfo : this.briefInfo.substring(0, 150) + "...";
      },
    },
    methods: {
      toggleMore() {
        this.moreInfoFlag = !this.moreInfoFlag;
      },
    },
  };
  </script>
  
  <style scoped>
  .bangu-detail-root {
    background-color: #fcf2ff;
    min-width: 1200px;
    font-size: 16px;
    z-index: 0;
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
    height: auto;
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
  .more {
    color: #3e97ff;
    cursor: pointer;
  }

  .taginfo {
    margin-top: 20px; /* 设置元素区域与简介区域之间的间隔 */
    display: flex;
    flex-wrap: wrap;
    gap: 10px; /* 设置元素之间的间隔 */
  }

  .tag {
    background-color: #8557A7;
    font-size: 15px;
    padding: 5px 12px;
    color: white;
    border-radius: 15px;
    margin: 0px 0px 0px 0px;
  }
  .right-top-icons {
  position: absolute;
  top: 55px;
  right: 55px;
  display: flex;
  }

  .icon {
    width: 45px;
    height: 45px;
    margin-left: 10px;
  }
  </style>
  