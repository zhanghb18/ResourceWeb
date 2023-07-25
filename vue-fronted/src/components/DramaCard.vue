<template>
  <div class='drama_card_root'>
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
.drama_card_root {
  width: 25%;
  display: inline-block;
}

.card {
  height: 213px;
  margin: 0 38px 28px 0;
  border-radius: 5px;
  box-shadow: 0 5px 5px 0 rgba(0, 0, 0, 0.2);
}

.image {
  width: 100%;
  height: 75%;
  border-radius: 5px;
}

.image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.drama_name {
  height: 10%;
  text-align: left;
  font-size: 15px;
  padding-left: 15px;
}

.drama_data {
  height: 15%;
  text-align: left;
  font-size: 8px;
  color: #818181;
  padding-left: 15px;
  margin-top: 5px;
}
</style>
