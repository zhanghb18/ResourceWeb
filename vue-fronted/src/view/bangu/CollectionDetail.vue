<template>
  <div>
    <el-row class="user-center-root">
      <user-header></user-header>
      <el-col :lg="{ span: 16, offset: 4 }" class="container">
        
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
      collectionSheet: [

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
</style>
