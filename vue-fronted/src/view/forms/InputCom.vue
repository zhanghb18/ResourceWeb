<template>
  <div>
    <el-row class="input_row">
      <el-col :span="4">
        <span class="text">{{ text }}</span>
      </el-col>
      <el-col :span="17">
        <el-input
          :show-password="this.type == 'password'"
          v-model="value"
          :type="this.type"
          @input="this.$emit('input', $event)"
          @blur="this.$emit('blur')"
        />
      </el-col>
      <el-col v-if="!btnText == ''" :span="3" style="margin: auto">
        <el-button
          :type="'primary'"
          text
          large
          @click="this.$emit('clickBtn')"
          :disabled="btnDisable"
        >
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
    modelValue: String,
    message: String,
    type: {
      type: String,
      default: "account",
    },
    btnText: {
      type: String,
      default: "",
    },
    btnDisable: {
      type: Boolean,
      default: false,
    },
  },
  computed: {
    isForgetShow() {
      return this.type === "password";
    },
    value: {
      get() {
        return this.modelValue;
      },
      set(value) {
        this.$emit("update:modelValue", value);
      },
    },
  },
};
</script>

<style lang="less" scoped>
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
  width: 100%;
  height: 100%;
  border: none;
  padding: 0 0;
  font-size: 20px;
  outline-style: none;
  box-shadow: none;
}

.el-input {
  height: 100%;
  .el-input__wrapper {
    height: 100%;
  }
}

:deep(.el-input__wrapper) {
  box-shadow: 0 0 0 0px var(--el-input-border-color, var(--el-border-color)) inset;
  .el-input__inner {
    height: 100%;
    color: #000;
  }
  font-size: 20px;
  padding: 0 0;
  height: 100%;
}

/deep/ .el-button--primary {
  width: 80px;
  padding: 0 7px;
}
</style>
