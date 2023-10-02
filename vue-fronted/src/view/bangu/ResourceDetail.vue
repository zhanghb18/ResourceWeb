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
            <div class="info-box">
              <p class="info-content"><span class="purple-bold">发布日期：</span>{{ releaseDate }}</p>
              <p class="info-content"><span class="purple-bold">资源大小：</span>{{ size }}</p>
              <p class="info-content"><span class="purple-bold">已下载：</span>{{ downflow }}</p>
            </div>
            <div class="button-group">
              <el-button type="primary" class="download-button">下载种子</el-button>
              <el-button type="primary" class="download-button">磁力链接</el-button>
            </div>
          </el-col>
          <el-col :span="15" class="right-col">
            <div class="right-bar">
              <div class = "left-part">
                <img src="@/assets/DramaList/return.png" alt="返回按钮" class="return-button" />
                <div class = "text" >{{ episodeTitle }}</div>
                <div class = "text" >{{ organization }}</div>
              </div>
              <div class = "right-part">
                <span v-if="UHD"><img src="@/assets/DramaList/UHD_white.png" alt="1080清晰度" class="resource-icon" /></span>
                <span v-if="HD"><img src="@/assets/DramaList/HD_white.png" alt="高清清晰度" class="resource-icon" /></span>
                <span v-if="inlineSub"><img src="@/assets/DramaList/inlineSub_white.png" alt="内嵌字幕" class="resource-icon" /></span>
                <span v-if="externalSub"><img src="@/assets/DramaList/externalSub_white.png" alt="外挂字幕" class="resource-icon" /></span>
                <span v-if="chs"><img src="@/assets/DramaList/chs_white.png" alt="简体" class="resource-icon" /></span>
                <span v-if="cht"><img src="@/assets/DramaList/cht_white.png" alt="繁体" class="resource-icon" /></span>
              </div>
            </div>
            <div class="resource-part">
              <!-- 图片 -->
              <img src="@/assets/BanGu/test.png" alt="本集封面图" class="resource-image" />
              <!-- 分割线 -->
              <hr class="divider" />
              <!-- 段落一 -->
              <pre class="custom-text">{{ customInfo1 }}</pre>
              <!-- 分割线 -->
              <hr class="divider" />
              <!-- 段落二 -->
              <pre class="custom-text">{{ customInfo2 }}</pre>
              <!-- 分割线 -->
              <hr class="divider" />
              <!-- 段落三 -->
              <pre class="custom-text">{{ customInfo3 }}</pre>
               <!-- 分割线 -->
              <hr class="divider" />
            </div>
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
        releaseDate: "2023.7.29",
        size: "729MB",
        downflow: "25",
        currentEpisode: "12",
        organization: "老张是狗汉化组",
        UHD: true,
        HD: false,
        inlineSub: true,
        externalSub: false,
        chs: true,
        cht: false,
        customInfo1: "喵萌奶茶屋招募以下职位的小伙伴！\n\
        1.翻译：没有证书要求，能正确听译一集动画即可\n\
        2.时轴：使用 Aegisub 准确拉轴对帧并设置合适的样式、字体、屏幕字\n\
        3.后期：懂时轴基础知识并使用 Vapoursynth 或 Avisynth 内嵌字幕，做种发布分流\n\
        4.压制：能独立写代码优化画质并使用 VapourSynth 或 AviSynth 压制 BDRip / DVDRip\n\
        5.特效：熟练应用特效代码制作合适的歌词特效\n\
        6.画师：画海报、字幕娘、表情包、LOGO 等\n\
        7.分流：捐献服务器盒子永久保种本组合集资源\n\
        欢迎热爱二次元热衷字幕制作的小伙伴加入！申请请加入 QQ 群：421320480\n\
        粉丝群：477659567\n",
        customInfo2:"奶茶屋所有最新的【外挂字幕】在这里，如果有对本组做过的番有兴趣的，欢迎来调 BD 轴！\n\
        本组发布的资源请以最新发布为准，最新的 TV 合集，最新的 BDRip 合集是最新修正的资源！\n\
        本组发布的外挂字幕请勿随意修改后发布至公网！\n\
        点击加入【奶茶分流小分队】，为自己喜爱的番奉献一份力量！\n",
        customInfo3:"从 2020 年 10 月新番起，本组发布的作品将去掉 Web 片源自带的片头！\n",
      };
    },
    computed: {
      displayInfo() {
        return this.moreInfoFlag ? this.briefInfo : this.briefInfo.substring(0, 150) + "...";
      },
      episodeTitle() {
        return "第 " + this.currentEpisode + " 话";
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
    display: flex;
    align-items: center;
    flex-direction: column;
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

  .info-box {
    background-color: #FCF2FF;
    position: relative;
    height: 10vh;
    width: 12.9vw;
    min-height: 111px;
    min-width: 249px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    border-radius: 15px;
    margin-bottom: 25px;
  }
  .info-content {
    font-size: 16px;
    margin:0px;
  }
  .purple-bold {
    color: #662D91;
    font-weight: bold;
  }
  .button-group {
    align-items: center;
    height: 10vh;
    width: 12.9vw;
    min-height: 111px;
    min-width: 249px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    background-color: #FCF2FF;
    border-radius: 15px;
    gap: 10px;
  }

  .download-button {
    border-radius: 15px;
    background-color:#8557A7;
    height: 38px;
    width: 218px;
    border: none;
    margin: 0px;
  }

  .right-bar {
    background-color: #662D91;
    width: 100%;
    height: 65px;
    max-width: 810px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-direction: row;
    border-radius: 5px;
  }
  .left-part{
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-direction: row;
  }
  .return-button{
    height: 20px;
    width: 18px;
    margin-left: 19px;
  }

  .text {
    color: white;
    font-size: 20px;
    margin-left: 20px;
  }

  .resource-icon{
    height: 25px;
    width: 33px;
    margin-left: 10px;
  }
  .right-part{
    margin-right: 20px;
  }
  .resource-part{
    background-color: #FCF2FF;
    width: 100%;
    height: auto;
  }

  .resource-image{
    margin-top: 30px;
    height: 98.6vh;
    width: 39.5vw;
  }
  .custom-text{
    color: black;
    font-size: 15px;
    text-align: left;
    white-space: pre-line;
    margin-left: 27px;
    font-family: "SOURCEHANSANSSC-VF";
    margin-bottom: 20px;
    margin-top: 20px;
  }

  .divider {
    width: 37.5vw;
    background-color: #C7C7C7;
  }
  </style>
  