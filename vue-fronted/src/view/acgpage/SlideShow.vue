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
        "https://www.themoviedb.org/t/p/original/6hbd2zP73s9pm8ndy1xwEv7Ehem.jpg",
        "https://www.themoviedb.org/t/p/original/rwNSHACnL14YJfG7u2AFrF63qYe.jpg",
        "https://www.themoviedb.org/t/p/original/rCnuLUcIqGjDzAkx0YHNcTR0O4y.jpg",
        "https://www.themoviedb.org/t/p/original/iXXbG5IJeScJ2kCLiX9vxnUxFkk.jpg",
      ],
    }
  }
  }
</script>

<style lang='less' scoped>
/* 轮播图容器 */
.el-carousel {
  position: relative;
  width: 700px;
  height: 400px;
  margin: 0 auto;
  margin-top: 37px;
  border-radius: 15px;
  z-index: 2;
}
/deep/.el-carousel__container {
  height: 400px !important;
}
/* 阴影 */
.slideshow__shadow {
  position:absolute;
  top:85%;
  left:0;
  width:100%;
  height:15%;
  background: linear-gradient(to top, rgba(0,0,0,0.8), rgba(0,0,0,0));
  border-radius:0px 0px 15px 15px;
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

/deep/.el-carousel__button { 
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
