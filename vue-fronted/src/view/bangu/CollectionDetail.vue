<template>
  <!-- 收藏夹详情页面 -->
  <div>
    <el-row class="user-center-root">
      <user-header></user-header>
      <el-col :lg="{ span: 16, offset: 4 }" class="container">
        <el-row>
          <el-col :span="8">
            <DramaCard :msg="collectionMsg" class="collection-card"></DramaCard>
          </el-col>
          <el-col :span="16" class="sheet-col">
            <el-row :msg=sheet v-for="(sheet, index) in collectionSheets" class="sheet-row">
              <span>
                {{ index + 1 }}.
              </span>
              <div>
                <img :src="sheet.imgSrc" alt="" class="cover-img">
              </div>
              <span>
                {{ sheet.title }}
              </span>
            </el-row>
          </el-col>
        </el-row>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import UserHeader from "../../components/UserHeader.vue";
import DramaCard from "../../components/DramaCard.vue";

export default {
  name: "UserCenter",
  components: {
    UserHeader,
    DramaCard,
  },
  data() {
    return {
      collectionMsg: {
        title: "收藏夹1",
        imgSrc: "http://123.56.45.70/images/1.jpg",
        description: "这是收藏夹1的描述",
        dramaNum: 10,
        collectNum: 100,
      },
      collectionSheets: [
        {title : "剧名1", imgSrc : "http://123.56.45.70/images/1.jpg"},
        {title : "剧名2", imgSrc : "http://123.56.45.70/images/1.jpg"},
        {title : "剧名3", imgSrc : "http://123.56.45.70/images/1.jpg"},
      ],
    };
  },
  methods: {
    
  },
  created() {
    // TODO: 请求收藏夹信息
  },
};
</script>

<style lang="less" scoped>
.user-center-root {
  background-color: #fcf2ff;
  min-width: 1200px;
  font-size: 16px;
}

.container {
  background-color: #fff;
  width: 62.5%;
  height: auto;
  min-height: 90vh;
  min-width: 900px;
}

.collection-card {
  margin-top: 15%;
  margin-left: 15%;
}

.sheet-row {
  height: 100px;
  border-bottom: 1px solid #e9e9f3;
  display: flex;
  align-items: center;
  margin-top: 30px;
  font-size: 20px;
}

.sheet-col {
  margin-top: 1%;
  padding-left: 5%;
}

.cover-img {
  width: 150px;
  height: 80px;
  margin-left: 20px;
  margin-right: 20px;
  object-fit: cover;
}
</style>
