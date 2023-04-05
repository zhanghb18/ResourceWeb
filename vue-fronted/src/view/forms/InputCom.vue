<template>
  <div>
    <el-row class="input_row">
      <el-col :span="3">
        <span class="text">{{ text }}</span>
      </el-col>
      <el-col :span="18">
        <input
          :value="input"
          :type="this.type"
          @input="$emit('update:modelValue', $event.target.value)"
        />
      </el-col>
      <el-col v-if="!btnText == ''" :span="3" style="margin: auto">
        <el-button :type="'primary'" text large>
          {{ btnText }}
        </el-button>
      </el-col>
    </el-row>
    <div style="border: 1px solid #ccc"></div>
    <el-row class="message_row">
      <el-col :span="3"></el-col>
      <el-col :span="18" style="display: contents">
        <span class="message_text"> {{ message }} </span>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "InputCom",
  data() {
    return {};
  },
  props: {
    text: String,
    input: String,
    message: String,
    type: String,
    btnText: String,
  },
  computed: {
    isForgetShow() {
      return this.type === "password";
    },
  },
};
</script>

<style scoped>
.input_row {
  height: 50px;
}

.text {
  line-height: 50px;
  color: black;
  font-size: 20px;
  justify-content: center;
  display: flex;
}

.message_row {
  height: 31px;
}

.message_text {
  color: red;
  font-size: 14px;
  margin-left: 20px;
  line-height: 20px;
}

input {
  width: 90%;
  height: 100%;
  border: none;
  padding: 0px 20px;
  font-size: 20px;
  outline-style: none;
}
</style>
