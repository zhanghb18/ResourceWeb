<template>
  <el-carousel :interval="4000" trigger="click">
    <div class="slideshow__shadow"></div>
    <el-carousel-item v-for="(image, index) in images" :key="index">
      <img :src="image" alt="slideshow image" class="slideshow__image"/>
    </el-carousel-item>
  </el-carousel>
</template>

<script>
export default {
  data() {
    return {
      // 图片数组
      images: [
        require("../../assets/acgpage/资源1.jpg"),
        require("../../assets/acgpage/资源2.jpg"),
        require("../../assets/acgpage/资源3.jpg"),
        require("../../assets/acgpage/资源4.jpg"),
      ],
    }
  }
  }
</script>

<style scoped>
/* 轮播图容器 */
.el-carousel {
  position: relative;
  width: 600px;
  height: 389px;
  margin: 0 auto;
  margin-top: 37px;
  border-radius:10px;
  z-index: 2;
}
/deep/.el-carousel__container {
  height: 389px !important;
}
/* 阴影 */
.slideshow__shadow {
  position:absolute;
  top:85%;
  left:0;
  width:100%;
  height:15%;
  background: linear-gradient(to top, rgba(0,0,0,0.8), rgba(0,0,0,0));
  border-radius:10px;
  z-index: 1;
}

/* 图片 */
.slideshow__image {
  width: auto;
  height: 100%;
  object-fit: contain;
  display: inline-block;
  z-index: -2;
}

/deep/ .el-carousel__button { 
  position: relative;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background-color: rgba(255, 255, 255, 0.8);
  margin-right: 10px;
  z-index: 2;
  margin-top: -20px;
}
</style>
