<template>
  <div class="tab-content">
    <el-table :data="list" :show-header="false" stripe style="width: 100%">
      <!-- <el-table-column type="expand" width="20px">
        <template v-slot="scope" @change="handleChange">
          <DramaInfoPreview :title="scope.row.title"></DramaInfoPreview>
        </template>
      </el-table-column> -->
      <el-table-column prop="title" label="title" width="500px">
        <template v-slot="scope">
          <span>{{ scope.row.title }} {{ scope.row.episodes }}</span>
          <span v-if="scope.row.resolution === '4K'">
            <img src="@/assets/DramaList/4K.png" alt="4K" class="el-table-item" />
          </span>
          <span v-if="scope.row.resolution === '1080p'">
            <img src="@/assets/DramaList/1080p.png" alt="1080p" class="el-table-item" />
          </span>
          <span v-if="scope.row.type === 'bt'">
            <img src="@/assets/DramaList/bt.png" alt="bt" class="el-table-item" />
          </span>
          <span v-if="scope.row.type === 'magnet'">
            <img src="@/assets/DramaList/magnet.png" alt="magnet" class="el-table-item" />
          </span>
          <span v-if="scope.row.subtitles === 'chs'">
            <img src="@/assets/DramaList/chs.png" alt="chs" class="el-table-item" />
          </span>
          <span v-if="scope.row.subtitles === 'cht'">
            <img src="@/assets/DramaList/cht.png" alt="cht" class="el-table-item" />
          </span>
          <span v-if="scope.row.subtitles === 'all'">
            <img src="@/assets/DramaList/chs.png" alt="chs" class="el-table-item" />
            <img src="@/assets/DramaList/cht.png" alt="cht" class="el-table-item" />
          </span>
        </template>
      </el-table-column>
      <el-table-column prop="organization" label="organization" width="calc(100% - 500px)">
        <template v-slot="scope">
          <img src="@/assets/DramaList/up.png" alt="up" class="el-table-item" style="padding-right: 5px" />
          <span>{{ scope.row.organization }}</span>
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
          resolution: "4K",
          type: "magnet",
          subtitles: "chs",
          organization: "梦幻之境翻译组",
        },
        {
          title: "德凯奥特曼",
          episodes: "12",
          resolution: "1080p",
          type: "bt",
          subtitles: "chs",
          organization: "紫色幻想翻译组",
        },
        {
          title: "电锯人",
          episodes: "8",
          resolution: "1080p",
          type: "bt",
          subtitles: "all",
          organization: "四季花语汉化团队",
        },
        {
          title: "死神·千年血战篇",
          episodes: "12",
          resolution: "1080p",
          type: "magnet",
          subtitles: "chs",
          organization: "星辰翼汉化组",
        },
        {
          title: "孤独摇滚",
          episodes: "12",
          resolution: "4K",
          type: "magnet",
          subtitles: "chs",
          organization: "天使之羽汉化组",
        },
        {
          title: "真·进化之实 踏上胜利的人生",
          episodes: "1",
          resolution: "1080p",
          type: "bt",
          subtitles: "chs",
          organization: "碧海蓝天汉化社",
        },
      ],
    };
  },
};
</script>

<style lang="less" scoped>
.tab-content {
  width: 100%;
  /* height: 200px; */
  /* background-color: #6b778c; */
}

/deep/ .el-table__body {
  font-size: 13px;
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

// 尝试加展开项
/deep/ .cell {
  
  padding: 0 5px;
}

/deep/ .el-table__expand-icon {
  width: 20px;
  margin-right: 0;
}
</style>
