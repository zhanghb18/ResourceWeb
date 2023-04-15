<template>
  <div class="search_holder">
    <div class="search_box">
      <div style="display: flex" class="search_bar">
        <input
          type="text"
          class="search_input"
          placeholder="搜索关键词:"
          @focus="inputFocused"
        />
        <button class="search_button">
          <img src="../assets/acgpage/SearchLogo.png" />
        </button>
      </div>
      <div class="serch_panel"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SearchBar",
  data() {
    return {};
  },
  methods: {
    inputFocused() {
      console.log("inputFocused");
    },
  },
};
</script>

<style scoped>
.search_holder {
  /* 搜索框容器样式 */
  width: 600px;
  /* height: 51px; */
}

.search_box {
  width: 600px;
  margin-top: 37px;
  margin-bottom: 58.5px;
  /* height: 200px; */
  overflow-y: visible;
  /* background-color: #fff; */
  border-radius: 20px;
  border: none;
}
.search_input {
  /* 搜索框样式 */
  box-sizing: border-box;
  width: 600px;
  height: 51px;
  margin-bottom: 58.5px;
  border-radius: 20px;
  border: none;
  box-shadow: none;
  padding: 5px 29px;
  font-size: 18px;
  outline-color: none;
  display: flex;
  align-items: center;
}

.search_input:focus {
  /* 搜索框聚焦样式 */
  border-color: #409eff;
  box-shadow: inset 0 -3em 3em #f2f2f2, 0.3em 0.3em 1em rgba(155, 155, 155, 0.3);
  outline: 0px;
}

.search_input::placeholder {
  /* 搜索框占位符样式 */
  color: #999;
  font-size: 18px;
  padding-left: 0px;
}
.search_button {
  /* 搜索按钮样式 */
  background-color: transparent;
  border: none;
  cursor: pointer;
  /* margin-top: 37px; */
  margin-bottom: 58.5px;
  margin-left: -48px;
}

.search_button img {
  /* 搜索按钮图片样式 */
  height: 26px;
}

.serch_panel {
  /* height: 100px;
  overflow-y: visible;
  background-color: #fff; */
}
</style>
