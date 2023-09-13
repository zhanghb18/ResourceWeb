<template>
  <div class="tab-content">
    <el-table 
      :data="list" 
      :show-header="false" 
      stripe 
      style="width: 100%" 
      height="250"
    >
      <!-- <el-table-column type="expand" width="20px">
        <template v-slot="scope" @change="handleChange">
          <DramaInfoPreview :title="scope.row.title"></DramaInfoPreview>
        </template>
      </el-table-column> -->
      <el-table-column prop="title" label="title" width="342px">
        <template v-slot="scope">
          <router-link :to="`/bangudetail?name=${scope.row.title}`" class="nav-link">
            <span>{{ scope.row.title }} {{ scope.row.episodes }}</span>
          </router-link>
        </template>
      </el-table-column>
      <el-table-column prop="icons" label="icons" width="896px">
        <template v-slot="scope">
          <span v-if="scope.row.UHD">
            <img src="../assets/DramaList/UHD.png" alt="4K" class="el-table-item" />
          </span>
          <span v-if="scope.row.HD">
            <img src="../assets/DramaList/HD.png" alt="1080p" class="el-table-item" />
          </span>
          <span v-if="scope.row.inlineSub">
            <img src="../assets/DramaList/inlineSub.png" alt="内嵌字幕" class="el-table-item" />
          </span>
          <span v-if="scope.row.externalSub">
            <img src="../assets/DramaList/externalSub.png" alt="外挂字幕" class="el-table-item" />
          </span>
          <span v-if="scope.row.chs">
            <img src="../assets/DramaList/chs.png" alt="简中字幕" class="el-table-item" />
          </span>
          <span v-if="scope.row.cht">
            <img src="../assets/DramaList/cht.png" alt="繁中字幕" class="el-table-item" />
          </span>
        </template>
      </el-table-column>
      <el-table-column prop="date" label="date" width="167px">
        <template v-slot="scope">
          <span>{{ scope.row.latestDate }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="organization" label="organization" width="114px">
        <template v-slot="scope">
          <img src="@/assets/DramaList/follow.png" alt="up" class="el-table-item" style="padding-right: 5px" />
          <img src="@/assets/DramaList/star.png" alt="up" class="el-table-item" style="padding-right: 5px" />
          <img src="@/assets/DramaList/more.png" alt="up" class="el-table-item" style="padding-right: 5px" />
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
// import DramaInfoPreview from "./DramaInfoPreview.vue"

export default {
  name: "DramaListTable",
  // components: {
  //   DramaInfoPreview,
  // },
  data() {
    return {
      list: [
        {
          title: "间谍过家家",
          episodes: "24",
          UHD: true,
          HD: false,
          inlineSub: true,
          externalSub: false,
          chs: true,
          cht: false,
          latestDate: "2022-10-23",
          collects: 278,
          comments: 19,
        },
        {
          title: "德凯奥特曼",
          episodes: "12",
          UHD: false,
          HD: true,
          inlineSub: true,
          externalSub: false,
          chs: true,
          cht: false,
          latestDate: "2022-10-23",
          collects: 278,
          comments: 19,
        },       
        {
          title: "德凯奥特曼",
          episodes: "12",
          UHD: false,
          HD: true,
          inlineSub: true,
          externalSub: false,
          chs: true,
          cht: false,
          latestDate: "2022-10-23",
          collects: 278,
          comments: 19,
        },
        {
          title: "德凯奥特曼",
          episodes: "12",
          UHD: false,
          HD: true,
          inlineSub: true,
          externalSub: false,
          chs: true,
          cht: false,
          latestDate: "2022-10-23",
          collects: 278,
          comments: 19,
        },
        {
          title: "德凯奥特曼",
          episodes: "12",
          UHD: false,
          HD: true,
          inlineSub: true,
          externalSub: false,
          chs: true,
          cht: false,
          latestDate: "2022-10-23",
          collects: 278,
          comments: 19,
        },
        {
          title: "德凯奥特曼",
          episodes: "12",
          UHD: false,
          HD: true,
          inlineSub: true,
          externalSub: false,
          chs: true,
          cht: false,
          latestDate: "2022-10-23",
          collects: 278,
          comments: 19,
        },
        {
          title: "德凯奥特曼",
          episodes: "12",
          UHD: false,
          HD: true,
          inlineSub: true,
          externalSub: false,
          chs: true,
          cht: false,
          latestDate: "2022-10-23",
          collects: 278,
          comments: 19,
        },
        {
          title: "德凯奥特曼",
          episodes: "12",
          UHD: false,
          HD: true,
          inlineSub: true,
          externalSub: false,
          chs: true,
          cht: false,
          latestDate: "2022-10-23",
          collects: 278,
          comments: 19,
        },
      ],
    };
  },
};
</script>

<style lang="less" scoped>
.tab-content {
  width: 100%;
}

/deep/ .el-table__body {
  font-size: 15px;
  font-weight: normal;
}

/deep/ .el-table__body td {
  padding: 0;
  height: 30px;
  background-color: #e9e9f3;
  cursor: pointer;
}

/deep/ .el-table-item {
  width: 20px;
  padding-left: 5px;
  vertical-align: middle;
  transform: translateY(-1.5px);
}

.nav-link {
  text-decoration: none;
  color: inherit;
}

// 尝试加展开项
// /deep/ .cell {

//   padding: 0 5px;
// }

// /deep/ .el-table__expand-icon {
//   width: 20px;
//   margin-right: 0;
// }
</style>
