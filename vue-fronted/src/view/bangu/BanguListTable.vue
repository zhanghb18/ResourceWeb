<template>
  <div style="font-size: 20px; text-align: start; font-weight: bold; padding: 10px 0px;">第 1 话</div>
  <div class="tab-content">
    <el-table :data="list" :show-header="false" stripe style="width: 100%" height="250" :row-style="{ height: '40px' }">
      <!-- <el-table-column type="expand" width="20px">
          <template v-slot="scope" @change="handleChange">
            <DramaInfoPreview :title="scope.row.title"></DramaInfoPreview>
          </template>
        </el-table-column> -->
      <el-table-column prop="organization" label="organization" width="225px">
        <template v-slot="scope">
          <span style="padding-right: 11px">
            <img src="@/assets/DramaList/up.png" alt="字幕组" class="el-table-item">
          </span>
          <span>{{ scope.row.organization }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="icons" label="icons" width="165px">
        <template v-slot="scope">
          <span v-if="scope.row.UHD">
            <img src="@/assets/DramaList/UHD.png" alt="4K" class="el-table-item" />
          </span>
          <span v-if="scope.row.HD">
            <img src="@/assets/DramaList/HD.png" alt="1080p" class="el-table-item" />
          </span>
          <span v-if="scope.row.inlineSub">
            <img src="@/assets/DramaList/inlineSub.png" alt="内嵌字幕" class="el-table-item" />
          </span>
          <span v-if="scope.row.externalSub">
            <img src="@/assets/DramaList/externalSub.png" alt="外挂字幕" class="el-table-item" />
          </span>
          <span v-if="scope.row.chs">
            <img src="@/assets/DramaList/chs.png" alt="简中字幕" class="el-table-item" />
          </span>
          <span v-if="scope.row.cht">
            <img src="@/assets/DramaList/cht.png" alt="繁中字幕" class="el-table-item" />
          </span>
        </template>
      </el-table-column>
      <el-table-column prop="size" label="size" width="95px">
        <template v-slot="scope">
          <span v-if="scope.row.size >= 1024">{{ (scope.row.size / 1024).toFixed(1) }} GB</span>
          <span v-else>{{ scope.row.size }} MB</span>
        </template>
      </el-table-column>
      <el-table-column prop="flow" label="flow" width="180px">
        <template v-slot="scope">
          <div
            style="display: table-cell; padding: 0 5px; vertical-align:bottom; background-color: #662d91; height: 40px; transform: translate(0, -8px); color: #FFF; border-radius: 0 0 10px 10px;">
            {{ scope.row.upflow }} ↑ {{ scope.row.downflow }} ↓
          </div>
          <!-- <span style="color: #FFF; z-index: 2">{{ scope.row.upflow }}</span> -->
        </template>
      </el-table-column>
      <el-table-column prop="organization" label="organization" width="120px">
        <template v-slot="scope">
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
  name: "BanguListTable",
  // components: {
  //   DramaInfoPreview,
  // },
  data() {
    return {
      list: [
        {
          organization: "随便起名汉化组",
          size: 1638.4,
          upflow: 2345,
          downflow: 1432,
          UHD: true,
          HD: false,
          inlineSub: true,
          externalSub: false,
          chs: true,
          cht: false,
        },
        {
          organization: "不知叫啥汉化组",
          size: 432,
          upflow: 23,
          downflow: 1411,
          UHD: false,
          HD: true,
          inlineSub: true,
          externalSub: false,
          chs: true,
          cht: false,
        },
        {
          organization: "某次元汉化组",
          size: 441,
          upflow: 23,
          downflow: 142,
          UHD: false,
          HD: true,
          inlineSub: true,
          externalSub: false,
          chs: true,
          cht: false,
        },
        {
          organization: "nekoneko 汉化组",
          size: 1638.4,
          upflow: 23,
          downflow: 14,
          UHD: false,
          HD: true,
          inlineSub: true,
          externalSub: false,
          chs: true,
          cht: false,
        },
        {
          organization: "peropero 汉化组",
          size: 417,
          upflow: 23,
          downflow: 14,
          UHD: false,
          HD: true,
          inlineSub: true,
          externalSub: false,
          chs: true,
          cht: false,
        },
        {
          organization: "naninani 汉化组",
          size: 420,
          upflow: 23,
          downflow: 14,
          UHD: false,
          HD: true,
          inlineSub: true,
          externalSub: false,
          chs: true,
          cht: false,
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

/deep/ .el-scrollbar__view {
  display: block !important;
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
  