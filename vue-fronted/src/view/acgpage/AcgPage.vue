<template>
  <div class="background">
    <div class="container">
      <div class="container-top">
        <slide-show></slide-show>
        <acg-calendar></acg-calendar>
      </div>
      <div class="container-table">
        <drama-list></drama-list>
      </div>
    </div>
  </div>
</template>

<script>
import SlideShow from "./SlideShow.vue"
import AcgCalendar from "./AcgCalendar.vue"
import DramaList from "../../components/DramaList.vue"

export default {
  components: {
    SlideShow,
    DramaList,
    AcgCalendar,
  }
};
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  height: 100%;
}

.background {
  width: 100%;
  height: auto;
  background-color: #f2f2f2;
  z-index: -4;
}

.container-top {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: row;
}
</style>
