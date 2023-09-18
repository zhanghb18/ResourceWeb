  <template>
    <el-row class="bangu-detail-root">
      <user-header></user-header>
      <el-col :lg="{ span: 16, offset: 4 }" class="container">
        <el-row class="container-head">
          <img :src="imgURL" class="background-img" :style="{'opacity': bgOpacity}">
          <el-col :span="7" class="left-col">
            <img :src="imgURL" class="bangu-image">
          </el-col>
          <el-col :span="15" class="right-col">
            <p class="bangu-name">{{ banguName }}</p>
            <p class="bangu-info">{{ "放送日期：" + turnOverTime }}</p>
            <p class="bangu-info">{{ "放送起始：" + startTime }}</p>
            <p class="bangu-info">{{ '总集数：' + totalNum }}</p>
            <p class="brief-info">
              简介：{{ displayInfo }}
              <span v-if="!moreInfoFlag && briefInfo.length > 150" class="more" @click="toggleMore">[更多]</span>
              <span v-if="moreInfoFlag" class="more" @click="toggleMore">[隐藏]</span>
            </p>
            <div class="taginfo">
              <p v-for="(tag, index) in tagInfo" :key="index" class="tag">{{ tag }}</p>
            </div>
          </el-col>
        </el-row>
        <el-row class="container-body">
          <el-col :span="7" class="left-col">
            <div class="view-mode">
              <div class="button-group">
                <el-button class="diver-view" :class="{'active-button': viewMode === 'diver'}" @click="changeViewMode('diver')">
                  <img src="../../assets/BanGu/DiverView.png" alt="button-image" class="diver-mode-image">分集查看
                </el-button>
                <div v-if="viewMode === 'diver'" class="grid-buttons">
                  <el-button v-for="i in displayGridButtons()" :key="i" class="grid-button">{{ i }}</el-button>
                </div>
                <div v-if="viewMode === 'diver'" class="page-buttons">
                  <div class="arrow prev" @click="changePage(currentPage - 1)">
                    <i class="el-icon-arrow-left"></i>
                  </div>
                  <div class="page-input">
                    <input v-model.number="inputPage" @keydown.enter="jumpToPage" @blur="jumpToPage" class="page-input-box" type="number">
                    <span class="total-pages">/ {{ totalPages }}</span>
                  </div>
                  <div class="arrow next" @click="changePage(currentPage + 1)">
                    <i class="el-icon-arrow-right"></i>
                  </div>
                </div>
                <el-button class="chinese-view" :class="{'active-button': viewMode === 'chinese'}" @click="changeViewMode('chinese')">
                  <img src="../../assets/BanGu/ChineseView.png" alt="button-image" class="chinese-mode-image">汉化查看
                </el-button>
              </div>
            </div>
          </el-col>
          <el-col :span="15" class="right-col">
            <div class="search_input_rect"></div>
            <div style="display: flex">
              <input type="text" class="search_input"/>
              <button class="search_button">
                <img src="../../assets/acgpage/SearchLogo.png" />
              </button>
            </div>
            <bangu-list-table></bangu-list-table>
          </el-col>
        </el-row>
      </el-col>
    </el-row>
  </template>

  <script>
  import UserHeader from "../../components/UserHeader.vue";
  import BanguListTable from "./BanguListTable.vue";

  export default {
    components: {
      UserHeader,
      BanguListTable,
    },
    data() {
      return {
        bgOpacity: 0.15,
        imgURL: 'https://s3-alpha-sig.figma.com/img/c0ef/6f30/db825b75e4a7ed38777131fded749f57?Expires=1687737600&Signature=AjcP1ZaOqnIDNEIAM72zk~bX0FXD8ViYPARIc6MZ1twNgNHwjzweeid6TwVxc8GqEXsdMpHRSFKSOWwYd3Lr~DulVkGx870TZESRemLuftYWU3tv9Lp-rdmEXxNYvZgTNehiIuvKd7grRHa1NDTnRH65~Bx7xVvztTvnpQO8Of1SVdu6Xwv6oan5K1iuv6mwIf3AK5xlXd08etkpVD2dNrBXGpI6LQczFFuY3JS7kwGHiU3gyz3w167hNdmhVG77eb0gRrJ8zfpoDwrLaNn6zi2RYPOZftkGdMmq0CNNfCIwyj5sbSRYZdEJAigkDa3CxCfSKA~dnCt3txGcH~zcsA__&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4',
        banguName: "久保同学不放过我",
        turnOverTime: "星期二",
        startTime: "2023年1月23日",
        totalNum: 12,
        currentNum: 10,
        briefInfo: "懒坑小子张后斌，他是一个大sb，脑子不好爱睡觉，同时还是大虚比，哈哈哈哈哈哈，嘻嘻嘻嘻嘻嘻，你能把我怎么样，我是你爹你是屁，懒坑小子张后斌，他是一个大sb，脑子不好爱睡觉，同时还是大虚比，哈哈哈哈哈哈，嘻嘻嘻嘻嘻嘻，你能把我怎么样，我是你爹你是屁，懒坑小子张后斌，他是一个大sb，脑子不好爱睡觉，同时还是大虚比，哈哈哈哈哈哈，嘻嘻嘻嘻嘻嘻，你能把我怎么样，我是你爹你是屁，懒坑小子张后斌，他是一个大sb，脑子不好爱睡觉，同时还是大虚比，哈哈哈哈哈哈，嘻嘻嘻嘻嘻嘻，你能把我怎么样，我是你爹你是屁",
        moreInfoFlag: false,
        tagInfo: ['# 老张是狗', '# 如来', '# 老张真是狗？','# 贺启爬坏','# 贺启爬没jj','# 矛头','# 毛字','# 呃呃','#啦啦啦'],
        viewMode: 'diver',
        currentPage: 1, // 当前页数，默认为1
        pageSize: 12, // 每页的按钮数量
        inputPage: 1, // 用户输入的页码
      };
    },
    computed: {
      displayInfo() {
        return this.moreInfoFlag ? this.briefInfo : this.briefInfo.substring(0, 150) + "...";
      },
      totalPages() {
        return Math.ceil(this.totalNum / this.pageSize);
      },
    },
    methods: {
      toggleMore() {
        this.moreInfoFlag = !this.moreInfoFlag;
      },
      changeViewMode(mode) {
        this.viewMode = mode;
      },
      displayGridButtons() {
        const startIndex = (this.currentPage - 1) * this.pageSize;
        const endIndex = Math.min(startIndex + this.pageSize, this.totalNum);
        return Array.from({ length: endIndex - startIndex }, (_, i) => startIndex + i + 1);
      },
      changePage(page) {
        if (page >= 1 && page <= this.totalPages) {
          this.currentPage = page;
          this.inputPage = page;
        }
      },
      jumpToPage() {
        const page = parseInt(this.inputPage);
        if (page >= 1 && page <= this.totalPages) {
          this.currentPage = page;
          this.inputPage = page;
        } else if (page < 1) {
          this.currentPage = 1;
          this.inputPage = 1;
        } else if (page > this.totalPages) {
          this.currentPage = this.totalPages;
          this.inputPage = this.totalPages;
        }
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

  .view-mode{
    position: relative;
    height: auto;
    width: auto;
    display: flex;
    justify-content: center;
  }
  .button-group {
    position: relative;
    width: 200px;
    background-color: #F4ECF6;
    padding: 10px;
    border-radius: 15px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 10px;
  }
  .diver-view{
    width: 180px;
    height: 54px;
    border-radius: 15px;
    background-color: #C2ABD3;
    font-size: 20px;
    color: white;
  }
  .chinese-view{
    width: 180px;
    height: 54px;
    margin: 0px;
    border-radius: 15px;
    background-color: #C2ABD3;
    font-size: 20px;
    color: white;
  }

  .active-button {
    background-color: #662D91;
  }

  .diver-mode-image{
    width: 25px;
    height: 22px;
    margin-right: 10px;
  }

  .chinese-mode-image{
    width: 25px;
    height: 22px;
    margin-right: 10px;
  }
  .grid-buttons {
    margin-top: 2px;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 5px;
  }
  .grid-button {
    width: 54px;
    height: 27px;
    border-radius: 15px;
    margin: 0px;
  }
  .grid-button:focus,
  .grid-button:active {
    background-color: #662D91;
    color: white;
    border-color: #662D91;
    box-shadow:0 0 0 0.5px rgba(102, 51, 153, 0.5);
  }
  .grid-button:hover {
    background-color: #C2ABD3;
    color: white;
    border-color: #C2ABD3;
    box-shadow:0 0 0 0.5px rgba(102, 51, 153, 0.5);
  }
  .page-buttons {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 2px;
    gap: 5px;
  }

  .arrow {
    width: 15px;
    height: 15px;
    border-radius: 50px;
    background-color: #8557A7; /* 紫色 */
    cursor: pointer;
    transition: background-color 0.3s ease;
  }

  .arrow:hover {
    background-color: #662D91; /* 鼠标悬停时的紫色 */
  }
  .arrow.prev::before {
    content: "";
    position: absolute;
    top: 72.4%;
    left: 63px;
    transform: translateY(-50%);
    width: 0;
    height: 0;
    border-top: 4px solid transparent;
    border-right: 4px solid #fff;
    border-bottom: 4px solid transparent;
  }

  .arrow.next::after {
    content: "";
    position: absolute;
    top: 72.4%;
    right: 63px;
    transform: translateY(-50%);
    width: 0;
    height: 0;
    border-top: 4px solid transparent;
    border-left: 4px solid #fff;
    border-bottom: 4px solid transparent;
  }
  .page-input {
    display: flex;
    align-items: center;
    gap: 5px;
  }

  .page-input-box {
    width: 40px;
    height: 20px;
    text-align: center;
    font-size: 10px;
    border-radius: 5px;
    outline: none;
    border: none;
  }

  .page-input-box::-webkit-outer-spin-button,
  .page-input-box::-webkit-inner-spin-button {
    -webkit-appearance: none;
    margin: 0;
  }
  .total-pages {
    font-size: 12px;
  }

  .search_input_rect{
    height: 60px;
    width: 100%;
    max-width: 810px;
    background-color: #C2ABD3;
    border-radius: 15px;
  }
  .search_input {
    /* 搜索框样式 */
    box-sizing: border-box;
    height: 35px;
    width: 720px;
    border-radius: 15px;
    border: none;
    box-shadow: none;
    padding: 5px 29px;
    font-size: 18px;
    outline-color: none;
    margin-top: -45px;
    margin-left: 23px;
    margin-bottom: 15px;
    display: flex;
    align-items: center;
  }

  .search_input:focus {
    /* 搜索框聚焦样式 */
    outline: 0px;
  }

  .search_button {
    /* 搜索按钮样式 */
    background-color: transparent;
    border: none;
    cursor: pointer;
    margin-top: -46px;
    margin-bottom: 15px;
    margin-left: 5px;
  }

  .search_button img {
    /* 搜索按钮图片样式 */
    height: 26px;
  }
  </style>
  