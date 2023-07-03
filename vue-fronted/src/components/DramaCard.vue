<template>
  <div style="display: inline-block;">
    <el-card :body-style="{ padding: '0px' }" class="card">
      <img
        class="image"
        :src="msg.imgSrc"
      />
      <div class="drama_name">{{ msg.name }}</div>
      <div class="drama_data">{{ msg.browseNum }}浏览 {{ msg.collectNum }}收藏</div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: "DramaCard",
  props: ['msg'],
  data() {
    return {
      image:
        "https://www.themoviedb.org/t/p/original/mvolqXssikgLeUomc59cB2RkH1k.jpg",
    };
  },
};
</script>

<style lang="less" scoped>
.card {
  width: 216px;
  height: 289px;
  margin: 0 38px 28px 0;
}

.image {
  width: 215px;
  height: 215px;
}

.drama_name {
  text-align: left;
}

.drama_data {
  text-align: left;
}
</style>
