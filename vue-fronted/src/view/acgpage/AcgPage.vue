<template>
  <div class="container">
    <Head></Head>
    <div style="display: flex; justify-content: center; align-items: center; flex-direction: row;">
      <SlideShow></SlideShow>
      <div class="calendar">
        <p>Calendar</p>
      </div>
    </div>
    <DramaList></DramaList>
  </div>
</template>

<script>
import SlideShow from "./SlideShow"
import Head from "./Head"
import DramaList from "@/components/DramaList.vue"

export default {
  components: {
    SlideShow,
    Head,
    DramaList,
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

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  padding: 20px;
  background-color: #f2f2f2;
}

.search {
  display: flex;
  align-items: center;
}

.search input {
  padding: 10px;
  border: none;
  border-radius: 5px;
  margin-right: 10px;
}

.search button {
  padding: 10px;
  border: none;
  border-radius: 5px;
  background-color: #4caf50;
  color: #fff;
  cursor: pointer;
}

.calendar {
  margin: 37px 0 0 120px;
  padding: 0px;
  width: 700px;
  height: 389px;
  border: 1px solid #ccc;
  border-radius: 10px;
  cursor: pointer;
}
</style>
