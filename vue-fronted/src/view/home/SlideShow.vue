<template>
  <div class="slideshow__container" @mouseover="stopTimer" @mouseleave="startTimer" style="margin-top: 50px;border-radius:10px;position:relative;">
    <div style="position:absolute;top:85%;left:0;width:100%;height:15%;background: linear-gradient(to top, rgba(0,0,0,0.8), rgba(0,0,0,0));z-index:1;"></div>      
    <transition :name="transitionName">
            <img :key="currentImage" :src="currentImage" alt="slideshow image" class="slideshow__image" style="width:100%;height:100%;object-fit:contain;z-index: -2;"/>
          </transition>
        <div class="slideshow__arrow slideshow__arrow--left" @click="prevImage">
          <i class="fas fa-chevron-left"></i>
        </div>
        <div class="slideshow__arrow slideshow__arrow--right" @click="nextImage">
          <i class="fas fa-chevron-right"></i>
        </div>
        <div class="slideshow__dots" style="z-index:2">
          <span
            v-for="(image, index) in images"
            :key="index"
            :class="{ 'slideshow__dot--active': index === currentIndex }"
            class="slideshow__dot"
            @click="changeImage(index)"
            :style="{transform: index === currentIndex ? 'scale(1.2)' : 'scale(1)'}"
          ></span>
        </div>
      </div>
</template>

<script>
export default {
data() {
  return {
    images: [
      require("../assets/资源1.jpg"),
      require("../assets/资源2.jpg"),
      require("../assets/资源3.jpg"),
      require("../assets/资源4.jpg"),
    ],
    currentIndex: 0,
    timer: null,
    transitionName: ''
  };
},
computed: {
  currentImage() {
    return this.images[this.currentIndex];
  },
},
mounted() {
  this.startTimer();
},
methods: {
  startTimer() {
    this.timer = setInterval(() => {
      this.nextImage();
    }, 3000);
  },
  stopTimer() {
    clearInterval(this.timer);
  },
  nextImage() {
    this.transitionName = 'slide-right'
    setTimeout(() => {
      this.currentIndex = (this.currentIndex + 1) % this.images.length;
      this.transitionName = 'slide-left'
    }, 500)
  },
  prevImage() {
    this.transitionName = 'slide-left'
    setTimeout(() => {
      this.currentIndex =
        (this.currentIndex - 1 + this.images.length) % this.images.length;
      this.transitionName = 'slide-right'
    }, 500)
  },
  changeImage(index) {
    if (index === this.currentIndex) return
    this.transitionName = 'fade'
    setTimeout(() => {
      this.currentIndex = index;
    }, 500)
  },
},
};
</script>

<style scoped>
.slideshow__container {
position: relative;
width: 500px;
height: 300px;
margin: 0 auto;
overflow: hidden;
z-index: 2;
display:flex;
flex-direction:row;
}

.slideshow__image {
width: 100%;
height: 100%;
object-fit: cover;
display: inline-block;
}

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

.slideshow__dots {
position: absolute;
bottom: 20px;
left: 50%;
transform: translateX(-50%);
display: flex;
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
