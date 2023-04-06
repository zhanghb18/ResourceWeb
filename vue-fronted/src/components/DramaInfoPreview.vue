<template>
  <div class="body">
    <div class="body-info">
      <h1 class="body-info-header">{{ title }}</h1>
      <img :src="image" alt="预览图" class="body-info-poster">
      <div class="body-info-right">
        23123
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "DramaInfoPreview",
  props: {
    title: {
      // 太坑了啊
      type: String,
      required: true,
    }
  },
  data() {
    return {
      image: "https://www.themoviedb.org/t/p/original/mvolqXssikgLeUomc59cB2RkH1k.jpg",
    }
  },
}
</script>

<style lang="less" scoped>
// /deep/ .el-table__expanded-cell {
//   background-color: lightcoral;
// }
.body {
  width: 100%;
  height: 300px;
  display: flex;
  background-color: #e9e9f3;
  /* text-align: center; */
}

.body-info {
  width: 80%;
  margin: 0 50px;
  // background-color: aquamarine;
}

.body-info-header {
  margin: 10px 2px;
}

.body-info-poster {
  width: 160px;
  height: 240px;
  margin-right: 20px;
  float: left;
}
</style>