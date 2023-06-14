<template>
  <el-tabs type="card" class="demo-tabs">
    <el-tab-pane>
      <template #label>
        <div class="custom-tabs-label">
          <img src="@/assets/DramaList/hot.png" alt="Hot" class="icon-header" />
          <span>热门番剧</span>
        </div>
      </template>
      <drama-list-table></drama-list-table>
    </el-tab-pane>
    <el-tab-pane>
      <template #label>
        <div class="custom-tabs-label">
          <img src="@/assets/DramaList/favor.png" alt="Favor" class="icon-header" />
          <span>我的收藏</span>
        </div>
      </template>
    </el-tab-pane>
    <el-tab-pane>
      <template #label>
        <div class="custom-tabs-label">
          <img src="@/assets/DramaList/history.png" alt="History" class="icon-header" />
          <span>历史记录</span>
        </div>
      </template>
    </el-tab-pane>
  </el-tabs>
</template>

<script>
import DramaListTable from "./DramaListTable.vue";

export default {
  name: "DramaList",
  components: {
    DramaListTable,
  },
};
</script>

<!-- 不要写 scoped，否则修改不了 ElementUI 的样式 -->
<style lang="less" scoped>
:root {
  --tabs-header-height: 30px;
  --el-border-radius-base: 10px;
  // --el-tabs-header-height: 0px;
}

.demo-tabs {
  font-size: 16px !important;
  margin-top: 39px;
  margin-bottom: 195px;
  width: 1520px;
  height: 250px;
  /* 边框不是很好看 */
  /* border-radius: 2px; */
  position: relative;
}

/deep/ .el-tabs__header {
  height: 48px;
  margin-bottom: 0;
}

/deep/ .el-tabs__nav-wrap {
  height: inherit;
}

/deep/ .el-tabs__nav-scroll {
  height: inherit;
}

/deep/ .el-tabs__nav {
  background-color: #A4A5C3;
  height: inherit;
  // width: 322px;
  border-radius: 12px 12px 0 0 !important;
}

/deep/ .el-tabs__item {
  height: inherit;
  padding: 0 10px 0 10px !important;
  border: none !important;
  color: #030303;
}

/deep/ .custom-tabs-label {
  height: inherit !important;
  display: flex;
  align-items: center;
}

/deep/ .custom-tabs-label span {
  height: inherit !important;
  // vertical-align: middle;
  line-height: 48px;
  margin-left: 4px;
  // transform: translateY(-4px);
}

.icon-header {
  width: 16px;
  height: 16px;
  vertical-align: middle;
  transform: translateY(-1px);
}

/deep/ .is-active {
  background-color: #EAE9Ef;
  border-radius: 10px 10px 0 0;
}

/deep/ .is-active img {
  /* 这里还是要修改一下 */
  filter: brightness(110%) hue-rotate(80deg);
}

/deep/ .el-tabs__content {
  height: 250px;
  padding: 0 0;
}

/deep/ .el-table__body {
  height: 250px !important;
}
</style>
