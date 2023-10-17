<template>
  <div class="card" @click="jumpToPage()">
    <img class="image" :src="msg.imgSrc" />
    <div class="drama_name">{{ msg.title }}</div>
    <div class="drama_data">
      {{ msg.comments }} 评论 {{ msg.collects }} 收藏
    </div>
  </div>
</template>

<script>
export default {
  name: "DramaCard",
  props: ["msg"],
  data() {},
  methods: {
    jumpToPage() {
      this.$router.push({
        path: "/bangudetail/" + this.msg.title
      });
    }
  }
};
</script>

<style lang="less" scoped>
.card {
  display: inline-block;
  width: 22%;
  min-width: 225px;
  height: 315px;
  border-radius: 5px;
  box-shadow: 0 5px 5px 0 rgba(0, 0, 0, 0.2);
  cursor: pointer;
}

.image {
  width: 100%;
  height: 73%;
  border-radius: 5px;
}

.image img {
  object-fit: cover;
}

.drama_name {
  height: 30px;
  text-align: left;
  font-size: 17px;
  padding-left: 15px;
  margin-top: 10px;
}

.drama_name:hover {
  color: #662D91;
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
