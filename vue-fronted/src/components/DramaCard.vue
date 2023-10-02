<template>
  <div>
    <div class="card">
      <img
        class="image"
        :src="msg.imgSrc"
      />
      <div class="drama_name">{{ msg.name }}</div>
      <div class="drama_data">{{ msg.browseNum }} 浏览  {{ msg.collectNum }} 收藏</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "DramaCard",
  props: ['msg'],
  data() {
  },
};
</script>

<style lang="less" scoped>

.card {
  width: 230px;
  height: 315px;
  border-radius: 5px;
  box-shadow: 0 5px 5px 0 rgba(0, 0, 0, 0.2);
}

.image {
  width: 230px;
  height: 230px;
  border-radius: 5px;
}

.image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.drama_name {
  height: 30px;
  text-align: left;
  font-size: 17px;
  padding-left: 15px;
  margin-top: 10px;
}

.drama_data {
  height: 15%;
  text-align: left;
  font-size: 14px;
  color: #818181;
  padding-left: 15px;
  margin-top: 5px;
}
</style>
