<template>
  <div class="circle" @mouseover="iconMouseOver()" @mouseout="iconMouseOut()">
    <div ref="circle" class="icon_circle">
      <img :src="imgSrc" />
    </div>
    <transition name="tooltip-transition">
      <div class="tooltip" v-show="isOnIcon">{{ text }}</div>
    </transition>
  </div>
</template>

<script>
export default {
  name: "IconCircle",
  data() {
    return {
      isOnIcon: false,
    };
  },
  props: {
    imgSrc: String,
    text: String,
  },
  methods: {
    iconMouseOver() {
      this.isOnIcon = true;
      // 动画
      this.$refs.circle.style.transform = "scale(1.2) translateX(-10px)";
      this.$refs.circle.style.transition = "transform 0.3s";
    },
    iconMouseOut() {
      this.isOnIcon = false;
      // 动画
      this.$refs.circle.style.transform = "scale(1) translateX(0)";
    },
  },
};
</script>

<style scoped>
.circle {
  position: relative;
  width: 90px;
  height: 50px;
}
.icon_circle {
  width: 43.5px;
  height: 43.5px;
  border-radius: 50%;
  background-color: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  z-index: 2;
}

.icon_circle img {
  width: 60%;
  height: 60%;
  object-fit: contain;
}

.tooltip {
  display: inline;
  position: absolute;
  top: 15%;
  left: 25%;
  width: 60px;
  border-radius: 50px;
  padding: 5px;
  background-color: #794b9c;
  color: #fff;
  z-index: -2;
}

.tooltip-transition-enter-active,
.tooltip-transition-leave-active {
  transition: all 0.3s;
}

.tooltip-transition-enter-from,
.tooltip-transition-leave-to {
  left: 32%;
  scale: 1;
}

.tooltip-transition-enter-from,
.tooltip-transition-leave-to {
  left: 0%;
  scale: 0.6;
}
</style>
