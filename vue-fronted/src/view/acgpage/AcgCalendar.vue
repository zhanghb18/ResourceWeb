<template>
  <div class="calendar">
    <!-- 这里是上面的导航栏 -->
    <div class="top-bar">
      <!-- 导航栏里面的 logo 部分 -->
      <div class="Calendar_logo">
        <div class="Calendar_L">
          <img src="../../assets/acgpage/CalendarLogo.png" alt="logo" />
        </div>
        <p>追番周历</p>
      </div>
      <!-- 按钮部分 -->
      <div class="Search_All">
        <p>查看全部 ></p>
      </div>
    </div>
    <!-- 主体部分 -->
    <div class="calendar-body">
      <!-- 上面的星期情况 -->
      <div class="weekdays">
        <p>一</p>
        <p>二</p>
        <p>三</p>
        <p>四</p>
        <p>五</p>
        <p><img src="../../assets/acgpage/XingLogo.png" alt="star" class="star-image-saturday">六</p>
        <p><img src="../../assets/acgpage/XingLogo.png" alt="star" class="star-image-sunday">日</p>
      </div>
      <!-- 那条线 -->
      <img src="../../assets/acgpage/Line.png" style="z-index: 5;" alt="line" />
      <!-- 图片的导入 -->
      <div class="content">
        <div v-for="index in 7" :key="index" class="content-col">
          <template v-for="drama in list" :key="drama.img_src">
            <el-popover placement="right-start" trigger="hover" popper-style="padding: 0" :show-arrow="false" :offset="13" :width="150">
              <template #reference>
                <img :src="drama.img_src" alt="" v-if="drama.weekdate === index" class="content-col-img">
              </template>
              <img :src="drama.img_hover_src" alt="" v-if="drama.weekdate === index" class="content-col-img-hover">
            </el-popover>
          </template>
          <img src="../../assets/acgpage/ZzzLogo.png" alt="" v-if="!list.some(drama => drama.weekdate === index)" class="Zzz-img">
        </div>
      </div>
      <!-- 添加竖条 -->
      <div class = "today_day" v-bind:style="{left:left_today[x] + '%'}"></div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      left_today: {
        1: 2.6,
        2: 15.8,
        3: 29.8,
        4: 43,
        5: 56.2,
        6: 69.6, 
        7: 83.4
      },
      x : null,
      list: [{
          img_src: "http://123.56.45.70/images/1-little.jpg",
          img_hover_src: "https://www.themoviedb.org/t/p/original/fJZLob1SkfUQ7PXry6I345dIuVn.jpg",
          weekdate: 2,
        },
      ],
    };
  },
  created() {
    // 在created生命周期方法中获取当前时间的星期几
    const today = new Date().getDay(); // 获取当前时间的星期几，0表示星期日，1表示星期一，以此类推
    if (today === 0) {
      this.x = 7; // 如果是星期日，则将x设置为7
    } else {
      this.x = today; // 否则直接将x设置为当前时间的星期几
    }
    var that = this;
    this.$api.resource.getAnimeCalendar()
      .then(function (response) {
        if (response.data.msg === "success") {
          if(response.data.data != ""){
            that.list = response.data.data.list;
          }
        } else {
          alertBox("获取追番列表失败", "error", that);
        }
        that.$forceUpdate();
      })
      .catch(function (error) {
          alertBox("连接异常，请检查网络或稍后再试。", "error", that);
      });
  },
};
</script>
<style>
/* Move all styles to the style section */
.calendar {
  /* Some styles here */
  margin: 37px 0 0 120px;
  padding: 0px;
  width: 700px;
  height: 400px;
  border-radius: 15px;
  cursor: pointer;
  background-color: #4d226d;
  z-index: 1;
}

.top-bar {
  height: 55px;
  display: flex;
  justify-content: space-between;
}

.Calendar_logo {
  /* logo 样式 */
  display: flex;
  align-items: flex-start;
  margin-left: 25px;
  padding-top: 15px;
}

.Calendar_logo p {
  /* logo 文字样式 */
  font-size: 22px;
  margin: 0px 0px 0px 15px;
  font-family: "Inter";
  color: white;
}

.Search_All {
  width: 90px;
  height: 30px;
  margin: 13px 16px 0px 0px;
  background: #8557a7;
  border-radius: 15px;
}

.Search_All p {
  /*查看全部文字样式*/
  font-family: "Inter";
  font-style: normal;
  font-weight: 400;
  font-size: 13.67px;
  line-height: 17px;
  margin: 0px;
  padding-top: 7px;
  color: white;
}

.calendar-body {
  position: relative;
  height: 345px;
  background-color: #8557a7;
  border-radius: 0px 0px 15px 15px;
  z-index: -2;
}

.weekdays {
  display: flex;
  justify-content: space-between;
  margin: 0 46px 0 46px;
  font-size: 20px;
  color: white;
  z-index: 1;
}

.weekdays p {
  font-family: "Alibaba PuHuiTi";
  font-style: normal;
  font-weight: 900;
  font-size: 41px;
  line-height: 56px;
  margin: 0;
  padding-top: 11px;
  padding-bottom: 10px;
  z-index: 1;
}

.week-image {
  position: absolute;
  top: 100px;
  left: 0;
  right: 0;
  margin: auto;
  width: 42px;
  height: 42px;
  border-radius: 100px;
  z-index: 1;
}

.content {
  display: flex;
  justify-content: space-between;
  margin: 0 43px 0 43px;
}

.imgicon {
  width: 42px;
  height: 42px;
  border-radius: 50%;
  display: block;
}

.content {
  display: flex;
}

.content-col {
  width: 55px;
}

.content-col-img {
  width: 42px;
  height: 42px;
  border-radius: 50%;
}

.content-col-img-hover {
  max-width: 100%;
  max-height: 250px;
  transform: scale(1.1);
  border-radius: 5px;
  margin-top: 6px;
}

.Zzz-img {
  width: 50px;
  height: 105px;
  padding-top: 90px;
  
}
.star-image-saturday{
  width: 25px;
  height: 25px;
  position: absolute; 
  left: 71.71%; 
  top: 2.3%;
  z-index: -1;
}
.star-image-sunday{
  width: 25px;
  height: 25px;
  position: absolute; 
  left: 85.73%; 
  top: 2.3%;
  z-index: -1;
}

.today_day{
  position: absolute; 
  left: 29.8%;
  top: 0; 
  z-index: -1; 
  width: 98px; 
  height: 345px; 
  background-color: #662D91;
}
</style>
