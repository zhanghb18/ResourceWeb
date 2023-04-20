<template>
  <div class="search_container" ref="sbar">
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
        <div class="panel_title_row">
          <span class="panel_title">搜索历史</span>
          <button class="clear_history">清空</button>
        </div>
        <div class="panel_content_row">
          <button v-for="item in history_items" class="panel_elem">
            {{ item }}
          </button>
        </div>

        <div class="panel_title_row">
          <span class="panel_title">热门搜索</span>
        </div>
        <div class="panel_content_row">
          <button v-for="item in hot_items" class="panel_elem">
            {{ item }}
          </button>
        </div>
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
      history_items: [
        "阿萨德哈我发",
        "达瓦开放时间啊哈",
        "阿苏来得及看呢嘎",
      ],
      hot_items: [
        "阿萨德哈我发",
        "达瓦开放时间啊哈",
        "阿苏来得及看呢嘎",
        "到无法进步嘎嘎",
        "到无法进步嘎嘎",
        "阿双方饭卡个巨大啊",
        "达和公司领导附近发掘",
        "达瓦开放时间啊哈",
        "阿苏来得及看呢嘎",
        "到无法进步嘎嘎",
        "阿双方饭卡个巨大啊",
        "达和公司领导附近发掘",
      ],
    };
  },
  methods: {
    clickOutside(e) {
      let flag = this.$refs.sbar.contains(e.target);
      console.log(this.$refs.searchBar);
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
  height: 52px;
  margin-top: 37px;
  margin-bottom: 58.5px;
  position: relative;
  overflow-y: visible;
  z-index: 4;
}

.search_box {
  width: 574px;
  padding: 0px 0px;
  height: 52px;
  background-color: #fff;
  border-radius: 15px;
  border: none;
}

.search_box_focus {
  height: 237px;
}

.search_input {
  width: 500px;
  height: 36px;
  margin: 8px 9px;
  padding: 0px 10px;
  border-radius: 6px;
  box-sizing: border-box;
  border: none;
  box-shadow: none;
  font-size: 18px;
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
  width: 56px;
  background-color: transparent;
  border: none;
  cursor: pointer;
  vertical-align: middle;
}

.search_button img {
  height: 28px;
}

.serch_panel {
  height: 185px;
}

.panel_title_row {
  height: 20px;
  margin: 5px 14px;
}

.panel_title {
  float: left;
  font-style: normal;
  font-size: 13px;
  margin: 0 1px;
}

.clear_history {
  float: right;
  font-style: normal;
  font-size: 10px;
  color: rgba(0, 0, 0, 0.3);
  background-color: transparent;
  border: none;
  cursor: pointer;
}

.panel_content_row {
  margin: 2px 14px 3px 14px;
  max-height: 56px;
  text-align: left;
  overflow-y: hidden;
}

.panel_elem {
  height: 20px;
  font-size: 10px;
  border-radius: 5px;
  border: #efefef;
  margin: 4px 6px 4px 0px;
  cursor: pointer;
}
</style>
