<template>
  <!-- 轮播图容器 -->
  <div class="slideshow__container" @mouseover="stopTimer" @mouseleave="startTimer">
    <!-- 用来增添位于图片下半部分的阴影效果，不需要进行修改 -->
    <div class="slideshow__shadow"></div>     
    <!-- 图片排成一行，只显示当前需要显示的那张 -->
    <div class="slideshow__image-container" v-for="(image, index) in images" :key="index" v-show="index === currentIndex">
      <img :src="image" alt="slideshow image" class="slideshow__image"/>
    </div>
    <!-- 左箭头 -->
    <div class="slideshow__arrow slideshow__arrow--left" @click="prevImage">
      <i class="fas fa-chevron-left"></i>
    </div>
    <!-- 右箭头 -->
    <div class="slideshow__arrow slideshow__arrow--right" @click="nextImage">
      <i class="fas fa-chevron-right"></i>
    </div>
    <!-- 圆点 -->
    <div class="slideshow__dots">
      <span
        v-for="(image, index) in images"
        :key="index"
        :class="{ 'slideshow__dot--active': index === currentIndex }"
        class="slideshow__dot"
        @click="changeImage(index)"
      ></span>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      // 图片数组
      images: [
        require("../assets/资源1.jpg"),
        require("../assets/资源2.jpg"),
        require("../assets/资源3.jpg"),
        require("../assets/资源4.jpg"),
      ],
      // 当前图片的下标
      currentIndex: 1,
      // 定时器
      timer: null,
      // 过渡效果名称
      transitionName: ''
    };
  },
  computed: {
    // 当前图片的路径
    currentImage() {
      return this.images[this.currentIndex];
    },
  },
  mounted() {
    // 组件挂载时启动定时器
    this.startTimer();
  },
  methods: {
    // 启动定时器
    startTimer() {
      this.timer = setInterval(() => {
        this.nextImage();
      }, 3000);
    },
    // 停止定时器
    stopTimer() {
      clearInterval(this.timer);
    },
    // 切换到下一张图片
    nextImage() {
      // 设置过渡效果
      this.transitionName = 'slide-right'
      // 延迟500ms执行
      setTimeout(() => {
        // 切换到下一张图片
        this.currentIndex = (this.currentIndex + 1) % this.images.length;
        // 设置过渡效果
        this.transitionName = 'slide-left'
      }, 500)
    },
    // 切换到上一张图片
    prevImage() {
      // 设置过渡效果
      this.transitionName = 'slide-left'
      // 延迟500ms执行
      setTimeout(() => {
        // 切换到上一张图片
        this.currentIndex =
          (this.currentIndex - 1 + this.images.length) % this.images.length;
        // 设置过渡效果
        this.transitionName = 'slide-right'
      }, 500)
    },
    // 切换到指定图片
    changeImage(index) {
      // 如果点击的是当前图片，则不执行任何操作
      if (index === this.currentIndex) return
      // 设置过渡效果
      this.transitionName = 'fade'
      // 延迟500ms执行
      setTimeout(() => {
        // 切换到指定图片
        this.currentIndex = index;
      }, 500)
    },
  },
};
</script>

<style scoped>
/* 轮播图容器 */
.slideshow__container {
  position: relative;
  width: 500px;
  height: 300px;
  margin: 0 auto;
  overflow: hidden;
  display:flex;
  flex-direction:row;
  margin-top: 50px;
  border-radius:10px;
}

.slideshow__image-container {
  width: 500px;
  height: 100%;
}

/* 阴影 */
.slideshow__shadow {
  position:absolute;
  top:85%;
  left:0;
  width:100%;
  height:15%;
  background: linear-gradient(to top, rgba(0,0,0,0.8), rgba(0,0,0,0));
  z-index:1;
}

/* 图片 */
.slideshow__image {
  width: 100%;
  height: 100%;
  object-fit: contain;
  display: inline-block;
  z-index: -2;
}

/* 箭头 */
.slideshow__arrow {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 50px;
  height: 50px;
  background-color: rgba(255, 255, 255, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 50%;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.slideshow__arrow:hover {
  background-color: rgba(255, 255, 255, 0.8);
}

.slideshow__arrow--left {
  left: 20px;
}

.slideshow__arrow--right {
  right: 20px;
}

/* 圆点 */
.slideshow__dots {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  z-index: 2;
}

.slideshow__dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background-color: rgba(255, 255, 255, 0.5);
  margin-right: 10px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.slideshow__dot:hover,
.slideshow__dot--active {
  background-color: rgba(255, 255, 255, 0.8);
}

/* 过渡效果 */
.slide-left-enter-active, .slide-right-leave-active {
  transition: transform 0.5s ease;
}

.slide-left-enter, .slide-right-leave-to {
  transform: translateX(-100%);
}

.slide-right-enter-active, .slide-left-leave-active {
  transition: transform 0.5s ease;
}

.slide-right-enter, .slide-left-leave-to {
  transform: translateX(100%);
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>
