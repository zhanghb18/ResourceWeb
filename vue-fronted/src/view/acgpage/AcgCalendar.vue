<template>
  <div class="calendar">
    <div class="top-bar">
      <div class="Calendar_logo">
        <div class="Calendar_L">
          <img src="../../assets/acgpage/CalendarLogo.png" alt="logo" />
        </div>
          <p>追番周历</p>
      </div>
      <div class="Search_All">
        <p>查看全部 ></p>
      </div>
    </div>
    <div class="calendar-body">
      <div class="weekdays">
        <p>一</p>
        <p>二</p>
        <p>三</p>
        <p>四</p>
        <p>五</p>
        <p>六</p>
        <p>日</p>
      </div>
      <img src="../../assets/acgpage/Line.png" alt="line" />
      <div class="content">
        <div class="col1">
        </div>
        <div class="col2">
        </div>
        <div class="col3">
        </div>
        <div class="col4">
        </div>
        <div class="col5">
        </div>
        <div class="col6">
        </div>
        <div class="col7">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      list: [
        {
          img_src: "https://www.themoviedb.org/t/p/original/6hbd2zP73s9pm8ndy1xwEv7Ehem.jpg",
          weekdate:'1',
        },
        {
          img_src: "https://www.themoviedb.org/t/p/original/6hbd2zP73s9pm8ndy1xwEv7Ehem.jpg",
          weekdate:'1',
        },
        {
          img_src: "https://www.themoviedb.org/t/p/original/6hbd2zP73s9pm8ndy1xwEv7Ehem.jpg",
          weekdate:'1',
        },
        {
          img_src: "https://www.themoviedb.org/t/p/original/6hbd2zP73s9pm8ndy1xwEv7Ehem.jpg",
          weekdate:'1',
        },
      ],
    };
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
    background-color: #4D226D;
  }
  .top-bar {
    height: 55px;
    display: flex;
    justify-content: space-between;
  }
  .Calendar_logo {
  /* logo样式 */
  display: flex;
  align-items: flex-start;
  margin-left: 25px; 
  padding-top:15px;
  }
  .Calendar_logo p {
  /* logo文字样式 */
  font-size: 22px;
  margin: 0px 0px 0px 15px;
  font-family: 'Inter';
  color: white;
  }
  .Search_All{
    width: 90px;
    height: 30px;
    margin: 13px 16px 0px 0px;
    background: #8557A7;
    border-radius: 15px;
  }

  .Search_All p {
  /*查看全部文字样式*/
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 13.67px;
  line-height: 17px;
  margin: 0px;
  padding-top: 7px;
  color: white;
  }
  .calendar-body{
    position: relative;
    height: 345px;
    background-color: #8557A7;
    border-radius: 0px 0px 15px 15px;
  }
  .weekdays {
    display: flex;
    justify-content: space-between;
    margin: 0 46px 0 46px;
    font-size: 20px;
    color: white;
  }
  .weekdays p {
    font-family: 'Alibaba PuHuiTi';
    font-style: normal;
    font-weight: 900;
    font-size: 41px;
    line-height: 56px;
    margin: 0;
    padding-top: 11px;
    padding-bottom:10px;
  }
  .week-image {
    position: absolute;
    top: 100px;
    left: 0;
    right: 0;
    margin: auto;
    width: 42px;
    height: 42px;
    border-radius:100px;
  }
  .content{
    display: flex;
    justify-content: space-between;
    margin: 0 43px 0 43px;
  }
</style>

