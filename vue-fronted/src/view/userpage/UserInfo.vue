<template>
  <el-row class="user-info-root">
    <user-header></user-header>
    <el-col :lg="{ span: 16, offset: 4 }" class="container">
      <div class="container-header">
        <img src="https://placekitten.com/800/600" alt="background" class="header-image" />
      </div>
      <el-row class="container-body">
        <el-col :span="6" class="container-body-nav">
          <div class="user-profile-nav">
            <div class="user-profile-avatar">
              <img :src=userInfo.userAvatar alt="avatar" />
              <span>{{ userInfo.userNickName }}</span>
            </div>
            <div class="user-profile-setting" :class="{ active: activeOption === 'option1' }" @click="toggleActive1()">
              <svg width="36" height="41" viewBox="0 0 36 41" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path
                  d="M0 0V41H36V20.5H15.4286V0H0ZM20.5714 0V15.375H36L20.5714 0ZM5.14286 10.25H10.2857V15.375H5.14286V10.25ZM5.14286 20.5H10.2857V25.625H5.14286V20.5ZM5.14286 30.75H25.7143V35.875H5.14286V30.75Z"
                  fill="#662D91" />
              </svg>
              <span>资料设置</span>
            </div>
            <div class="user-profile-setting" :class="{ active: activeOption === 'option2' }" @click="toggleActive2()">
              <svg width="36" height="36" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path
                  d="M24.75 0C18.54 0 13.5 5.04 13.5 11.25C13.5 11.97 13.5 12.69 13.635 13.365L0 27V36H13.5V27H22.5V22.5L22.635 22.365C23.31 22.5 24.03 22.5 24.75 22.5C30.96 22.5 36 17.46 36 11.25C36 5.04 30.96 0 24.75 0ZM27 4.5C29.475 4.5 31.5 6.525 31.5 9C31.5 11.475 29.475 13.5 27 13.5C24.525 13.5 22.5 11.475 22.5 9C22.5 6.525 24.525 4.5 27 4.5Z"
                  fill="#662D91" />
              </svg>
              <span>安全设置</span>
            </div>
            <div class="user-profile-setting" :class="{ active: activeOption === 'option3' }" @click="toggleActive3()">
              <svg width="36" height="36" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M0 0V4.5L18 13.5L36 4.5V0H0ZM0 9V27H36V9L18 18L0 9Z" fill="#662D91" />
              </svg>
              <span>发布设置</span>
            </div>
          </div>
        </el-col>

        <el-col :span="16" class="container-body-content">
          <div class="user-profile-body" v-if="activeOption === 'option1'">
            <span>资料设置</span>
            <div class="user-profile-body-line">
              <div style="background-color: #662d91; width: 20%; height: 8px"></div>
            </div>
            <el-row class="user-profile-body-item">
              <el-col :span="4">
                <span>头像</span>
              </el-col>
              <el-col :span="16">
                <img :src=userInfo.userAvatar alt="avatar" />
              </el-col>
              <el-col :span="4">
                <!-- <el-upload
                  :action="uploadURL"
                  :headers="userHeader"
                  :before-upload="beforeUploadFile"
                  :data="uploadData"
                  accept=".png, .jpg">
                  <button>修改</button>
                </el-upload> -->
                <button @click="changeAvatar()">修改</button>
              </el-col>
            </el-row>
            <el-row class="user-profile-body-item">
              <el-col :span="4">
                <span>昵称</span>
              </el-col>
              <el-col :span="16">
                <div v-if = "changeNickName === false" class="user-profile-body-content">{{userInfo.userNickName}}</div>
                <el-input v-if = "changeNickName === true" v-model="userInfo.userNickName"/>
              </el-col>
              <el-col :span="4">
                <button v-if="changeNickName === false" @click="clickNickName">修改</button>
                <button v-if="changeNickName === true" @click="changeUserInfo(0)">提交</button>
              </el-col>
            </el-row>
            <el-row class="user-profile-body-item">
              <el-col :span="4">
                <span>个人简介</span>
              </el-col>
              <el-col :span="16">
                <div v-if="changeSignature === false" class="user-profile-body-content">{{userInfo.userSignature}}</div>
                <el-input v-if="changeSignature === true" v-model="userInfo.userSignature"/>
              </el-col>
              <el-col :span="4">
                <button v-if="changeSignature === false" @click="clickSignature">修改</button>
                <button v-if="changeSignature === true" @click="changeUserInfo(1)">提交</button>
              </el-col>
            </el-row>
            <el-row class="user-profile-body-item">
              <el-col :span="4">
                <span>性别</span>
              </el-col>
              <el-col :span="16">
                <div v-if="changeGender === false" class="user-profile-body-content">{{userInfo.userGender}}</div>
                <!-- <el-input v-if="changeGender === true" v-model="userInfo.userGender"/> -->
                <el-select v-if="changeGender === true" v-model="userInfo.userGender" class="gender-select">
                  <el-option
                    v-for="item in genderOptions"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value"
                  />
                </el-select>
              </el-col>
              <el-col :span="4">
                <button v-if="changeGender === false" @click="clickGender">修改</button>
                <button v-if="changeGender === true" @click="changeUserInfo(2)">提交</button>
              </el-col>
            </el-row>
            <el-row class="user-profile-body-item">
              <el-col :span="4">
                <span>邮箱</span>
              </el-col>
              <el-col :span="16">
                <div class="user-profile-body-content">{{userInfo.userEmail}}</div>
              </el-col>
            </el-row>
          </div>
          <div class="user-profile-body" v-if="activeOption === 'option2'">
            <span style="">安全设置</span>
            <div class="user-profile-body-line">
              <div style="background-color: #662d91; width: 20%; height: 8px"></div>
            </div>
            <el-row class="user-profile-body-item">
              <el-col :span="4">
                <span>密码</span>
              </el-col>
              <el-col :span="16">
                <div>********</div>
              </el-col>
              <el-col :span="4">
                <button @click="dialogVisible = true">修改</button>
              </el-col>
            </el-row>
          </div>
          <div class="user-profile-body" v-if="activeOption === 'option3'">
            <span>发布设置</span>
            <div class="user-profile-body-line">
              <div style="background-color: #662d91; width: 20%; height: 8px"></div>
            </div>
          </div>
        </el-col>
      </el-row>
    </el-col>
    <el-dialog v-model="dialogVisible" title="修改密码" width="30%" :before-close="handleClose">
      <!-- <span>This is a message</span> -->
      <el-form :model="pwdForm" label-width="120px" ref="pwdForm" :rules="rules" class="pwdForm">
        <el-form-item label="原密码" prop="oldPwd">
          <el-input v-model="pwdForm.oldPwd" type="password"/>
        </el-form-item>
        <el-form-item label="新密码" prop="newPwd">
          <el-input v-model="pwdForm.newPwd" type="password"/>
        </el-form-item>
        <el-form-item label="确认新密码" prop="confirmPwd">
          <el-input v-model="pwdForm.confirmPwd" type="password"/>
        </el-form-item>
      </el-form>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="cancelForm('pwdForm')">取消修改</el-button>
          <el-button type="primary" @click="submitForm('pwdForm')">保存设置</el-button>
        </span>
      </template>
    </el-dialog>
    <!-- 剪裁组件弹窗 -->
    <el-dialog
        title="头像上传"
        v-model="cropperModel"
        width="950px"
       >
     <cropper-image
         :Name="cropperName"
         @uploadImgSuccess = "handleUploadSuccess"
         ref="child">
     </cropper-image>
    </el-dialog>
  </el-row>
</template>

<script>
import UserHeader from "../../components/UserHeader.vue";
import CropperImage from "../../components/CropperImage.vue";
import { alertBox } from "@/utils/alertBox.js";

export default {
  name: "UserInfo",
  components: {
    UserHeader,
    CropperImage,
},
  data() {
    var validateOldPass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('原密码不能为空'));
      } else {
        callback();
      }
    };
    var validateNewPass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入新密码'));
      } else {
        var box = /^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,20}$/;
        if (box.test(value)) {
          if (this.pwdForm.confirmPwd !== '') {
            this.$refs.pwdForm.validateField('confirmPwd');
          }
          callback();
        } else {
          callback(new Error('密码必须在6~20位之间，且包含数字和字母'));
        }
      }
    };
    var validateConfirmPass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'));
      } else if (value !== this.pwdForm.newPwd) {
        callback(new Error('两次输入密码不一致!'));
      } else {
        callback();
      }
    };
    return {
      activeOption: "option1",
      dialogVisible: false,
      userInfo: {
        userGender: "男",
        userEmail: "761769323@qq.com",
        userNickName: "叫我 zizi 就好了",
        userAvatar: "http://123.56.45.70/user_avatar/8c9d9dbcc7ab402f8d7f096afd9b2547.jpg",
        userSignature:"我是大傻逼冀泽华"
      },
      uploadURL:"/api/user/upload_file",
      userHeader:{
        token:localStorage.getItem('token'),
      },
      uploadData:{},
      changeNickName:false,
      changeGender:false,
      changeSignature:false,
      genderOptions:[
        {
          value:"男",
          label:"男"
        },
        {
          value:"女",
          label:"女"
        },
        {
          value:"无",
          label:"无"
        }
      ],
      pwdForm:{
        oldPwd:"",
        newPwd:"",
        confirmPwd:""
      },
      rules: {
        oldPwd: [
          { validator: validateOldPass, trigger: 'blur' }
        ],
        newPwd: [
          { validator: validateNewPass, trigger: 'blur' }
        ],
        confirmPwd: [
          { validator: validateConfirmPass, trigger: 'blur' }
        ]
      },
      //裁切图片参数
      cropperModel:false,
      cropperName:'',
    };
  },
  methods: {
    toggleActive1() {
      this.activeOption = "option1";
    },
    toggleActive2() {
      this.activeOption = "option2";
    },
    toggleActive3() {
      this.activeOption = "option3";
    },
    beforeUploadFile(file) {
      console.log(file);
      this.uploadData['file_name'] = file.name;
    },
    changeAvatar() {
      console.log("进入修改头像");
      this.cropperName = 'test';
      this.cropperModel = true;
    },
    handleUploadSuccess(data) {
      console.log("上传成功");
      console.log(data);
      this.cropperModel = false;
    },
    changeUserInfo(type) {
      console.log("修改用户个人信息");
      console.log(this.userInfo);
      var Data = JSON.parse(JSON.stringify(this.userInfo));
      var that = this;
      this.$api.user.changeUserInfo(Data)
        .then(function (response) {
          if(response.data.msg === "success") {
            alertBox("用户信息修改成功！", "success", that);
            if (type === 0) {
              that.changeNickName = false;
            }
            if (type === 1) {
              that.changeSignature = false;
            }
            if (type === 2) {
              that.changeGender = false;
            }
          } else {
            alertBox("用户信息修改失败！", "error", that);
          }
        })
        .catch(function (error) {
          alertBox("连接异常，请检查网络或稍后再试。", "error", that);
        });
    },
    clickSignature() {
      this.changeSignature = true;
    },
    clickGender() {
      this.changeGender = true;
    },
    clickNickName() {
      this.changeNickName = true;
    },
    cancelForm(formName) {
      this.$refs[formName].resetFields();
      this.dialogVisible = false;
    },
    submitForm(formName) {
      var that = this;
      this.$refs[formName].validate((valid) => {
        if (valid) {
          that.$api.user.changeUserPwd(that.pwdForm)
            .then(function (response) {
              if(response.data.msg === "success") {
                if(response.data.data['statusCode'] === 0) {
                  alertBox("用户密码修改成功！", "success", that);
                  that.$refs[formName].resetFields();
                  that.dialogVisible = false;
                }
                if(response.data.data['statusCode'] === 1) {
                  alertBox("用户不存在！", "error", that);
                }
                if(response.data.data['statusCode'] === 2) {
                  alertBox("原密码错误！", "error", that);
                }
              } else {
                console.log('修改密码错误!!');
              }
            })
            .catch(function (error) {
              alertBox("连接异常，请检查网络或稍后再试。", "error", that);
            });
        } else {
          console.log('error submit!!!');
          return false;
        }
      });
    }
  },
  created() {
    var that = this;
    this.$api.user.getUserInfo()
      .then(function (response) {
        if (response.data.msg === "success") {
          if(response.data.data != ""){
            var statusCode = response.data.data.statusCode;
            if(statusCode == 1) {
              alertBox("获取用户信息失败，错误码：1", "error", that);
            } else {
              that.userInfo.userNickName = response.data.data.nickname;
              that.userInfo.userSignature = response.data.data.signature;
              if(response.data.data.gender === 'female'){
                that.userInfo.userGender = '女';
              } else if(response.data.data.gender === 'male'){
                that.userInfo.userGender = '男';
              } else {
                that.userInfo.userGender = '无';
              }
              that.userInfo.userEmail = response.data.data.email;
              that.userInfo.userAvatar = response.data.data.avatar;
              if(that.userInfo.userAvatar == ""){
                that.userInfo.userAvatar = "http://123.56.45.70/user_avatar/8c9d9dbcc7ab402f8d7f096afd9b2547.jpg"
              }
            }
          }
        } else {
          alertBox("获取用户信息失败", "error", that);
        }
      })
      .catch(function (error) {
          alertBox("连接异常，请检查网络或稍后再试。", "error", that);
      });
  }
};
</script>

<style scoped>
.user-info-root {
  background-color: #fcf2ff;
  min-width: 1200px;
  font-size: 16px;
  /* height: auto; */
  /* overflow-x: scroll; */
}

.container {
  background-color: #ffffff;
  height: auto;
  min-height: 90vh;
  /* width: 100px; */
}

.header-image {
  height: 121px;
  width: 100%;
  object-fit: cover;
}

.container-body-nav {
  /* background-color: red; */
  height: auto;
  /* margin: 22px 0 0 22px; */
  margin-top: 22px;
  margin-left: 1.25vw;
  margin-right: 1.25vw;
}

.container-body-content {
  /* background-color: green; */
  height: auto;
  margin-top: 22px;
  margin-right: 1.3vw;
  /* margin: 22px 22px 0 20px; */
}

.user-profile-nav {
  width: 100%;
  height: 432px;
  background-color: #fcf2ff;
  border-radius: 5px;
  float: left;
  /* display: inline-block; */
}

.user-profile-avatar {
  width: 100%;
  height: 132px;
  display: flex;
}

.user-profile-avatar>img {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  margin: 27px 18px 25px 35px;
}

.user-profile-avatar>span {
  margin: 52px 35px 0 0;
  white-space: nowrap;
  /* 禁止换行 */
  overflow: hidden;
  /* 控制文本溢出隐藏 */
  text-overflow: ellipsis;
  /* 使用省略号截断文本 */
}

.user-profile-setting {
  display: flex;
  cursor: pointer;
  justify-content: space-around;
  align-items: center;
  height: 100px;
}

.user-profile-setting.active {
  background-color: #c2abd3;
}

/* .user-profile-setting svg {
  margin: 30px 0 29px 49px;
}

.user-profile-setting span {
  margin-top: 38px;
  margin-left: 65px;
} */

.user-profile-body {
  width: 100%;
  height: 780px;
  /* margin: 22px 29px 0 23px; */
  background-color: #fcf2ff;
  border-radius: 5px;
  float: right;
  /* display: inline-block; */
}

.user-profile-body>span {
  line-height: 30.26px;
  width: 100px;
  height: 30px;
  margin-left: 30px;
  margin-top: 27px;
  margin-bottom: 27px;
  font-size: 25px;
  display: block;
}

.user-profile-body-item {
  display: flex;
  align-items: center;
  margin: 10px 0;
  height: 100px;
}

.user-profile-body-item img {
  width: 68px;
  height: 68px;
  border-radius: 50%;
  float: left;
}

.user-profile-body-item button {
  width: 50px;
  height: 22px;
  background-color: #fcf2ff;
  border: none;
  cursor: pointer;
}

/* .user-profile-body-item div {
  float: left;
} */
.user-profile-body-content {
  float: left;
}

.gender-select {
  width: 100%;
}

.pwdForm {
  padding-right: 55px;
}
</style>
