<template>
  <div class="search_container" ref="searchBar">
    <div :class="{ search_box: true, search_box_focus: isInputFocused }">
      <div>
        <input
          type="text"
          class="search_input"
          placeholder="搜索关键词:"
          @focus="this.isInputFocused = true"
        />
        <button class="search_button">
          <img src="../assets/acgpage/SearchLogo.png" />
        </button>
      </div>
      <div class="serch_panel" v-show="isInputFocused">
        <h2>历史记录</h2>
        <h2>当前热门</h2>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SearchBar",
  data() {
    return {
      isInputFocused: false,
    };
  },
  methods: {
    clickOutside(e) {
      let flag = this.$refs.searchBar.contains(e.target);
      if (!flag) {
        this.isInputFocused = false;
      }
    },
  },
  mounted() {
    document.addEventListener("click", this.clickOutside);
  },
};
</script>

<style scoped>
.search_container {
  height: 51px;
  margin-top: 37px;
  margin-bottom: 58.5px;
  position: relative;
  overflow-y: visible;
  z-index: 4;
}

.search_box {
  width: 600px;
  padding: 2px 2px;
  height: 51px;
  background-color: #fff;
  border-radius: 20px;
  border: none;
}

.search_box_focus {
  height: 201px;
}

.search_input {
  display: inline-block;
  box-sizing: border-box;
  width: 559px;
  height: 51px;
  padding: 0px 20px;
  border-radius: 20px;
  border: none;
  box-shadow: none;
  font-size: 18px;
  outline-color: none;
  align-items: center;
}

.search_input:hover {
  background-color: #e0e0e0;
}

.search_input:focus {
  outline: 0px;
  background-color: #e0e0e0;
}

.search_input::placeholder {
  color: #999;
  font-size: 18px;
  padding-left: 0px;
}

.search_button {
  display: inline-block;
  background-color: transparent;
  border: none;
  cursor: pointer;
  vertical-align: middle;
}

.search_button img {
  height: 26px;
}

.serch_panel {
  height: 150px;
  font-size: 10px;
}
</style>
