<template>
  <div class="container">
    <Head></Head>
    <div style="display: flex; justify-content: center; align-items: center; flex-direction: row;">
      <SlideShow></SlideShow>
      <div class="calendar" style="margin-left: 20px;">
        <p>Calendar</p>
      </div>
    </div>
    <table style="margin-top: 50px;">
      <tr>
        <td>Table Data</td>
        <td>Table Data</td>
      </tr>
      <tr>
        <td>Table Data</td>
        <td>Table Data</td>
      </tr>
    </table>
  </div>
</template>

<script>
import SlideShow from "./SlideShow"
import Head from "./Head"

export default {
  components: {
    SlideShow,
    Head
  }
};
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
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
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  cursor: pointer;
}

</style>
