<template>
  <div class="background">
    <div class="container">
      <div style="display: flex; justify-content: center; align-items: center; flex-direction: row;">
        <SlideShow></SlideShow>
        <AcgCalendar></AcgCalendar>
      </div>
      <DramaList></DramaList>
    </div>
  </div>
</template>

<script>
import SlideShow from "./SlideShow"
import AcgCalendar from "./AcgCalendar"
import DramaList from "@/components/DramaList.vue"

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
.background{
  width: 100%; 
  height: auto;
  background-color: #f2f2f2;
  z-index: -4;
}
</style>
