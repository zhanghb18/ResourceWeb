<template>
  <div class="calendar">
    <!-- 这里是上面的导航栏 -->
    <div class="top-bar">
      <!-- 导航栏里面的logo部分 -->
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
            <img :src="drama.img_src" alt="" v-if="drama.weekdate === index" class="content-col-img">
          </template>
          <img src="../../assets/acgpage/ZzzLogo.png" alt="" v-if="!list.some(drama => drama.weekdate === index)" class="Zzz-img">
        </div>
      </div>
      <!-- 添加竖条 -->
      <div style="position: absolute; left: 29.6%; top: 0; z-index: -1; width: 98px; height: 345px; background-color: #662D91;"></div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      list: [
        {
          img_src: "https://s3-alpha-sig.figma.com/img/03f2/f9d5/b2bf2f6ef260ebe2dab056ce57f4d994?Expires=1682899200&Signature=NoX1CKOFHdPjHdziFEXziRzCo3JfSbihbryCadKFceqehgjD1A~F4uucFSppS~B1i0kHWXjpJnmx4AlQkrkstwxWXmJ~vAAwBp0IrufFlIW4-9Nx-c3ZPfzBo2fuP~PL73lmDR4UbqxNDeADfD-T7fxfEVYGFQuX68eQyXT~tFL35uhaawAHRCy~geKlR9aDG-QfQGtuu3KWkPybD481uGY~PiAIm4r0icit2FZOVjswg6p1miCBcbnyRctIFDGd-zaGKs1iwIiiJnelz1kZ7IFhWhTTKxCu6TRdZg~OSvorGY5DpYyZCpct7IEkk8QfZn0Hyl~l~SlPtjDzdxj3-A__&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4",
          weekdate: 2,
        },
        {
          img_src: "https://s3-alpha-sig.figma.com/img/4458/ad01/4c440db89ec16e46687ab704b7d75863?Expires=1682899200&Signature=ROUKzbsZ9rhbyzP18ml7WHGmuH1EndUO-M2b7LsmcV~nUt89TPVMz11I7eSVgmrZYUx9f13J1U-pyodNEUHQ-qKv2~IGuh-jIEsVuFwI~RQliorvTbyihbzKhnS8flxJW5YbefyntgoBPCy2TwFmkRbPrK3VqgE85xoTF7S77fvFFWVcgFTed0LwiExvVtdX75Uj7y9Mle6npWa163dZ3Vx-fMYCZBKoxWMeWMDwIzZB9tnJiIlm-NMqi~-QwBAlsin2UB~Hn~qPF6iYY3MxmAQItiWvBRWDDGpnfSyHc-VBxrHgE14EaQBXbgrXD1LyClBtbEfPljKWke0PGXTI7A__&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4",
          weekdate: 2,
        },
        {
          img_src: "https://s3-alpha-sig.figma.com/img/7b27/2cb0/6ac782b82593fa8711f75e17b9a920ed?Expires=1682899200&Signature=VPee0G~iX20H~~l~3hnoVyr75U2Zsn-oc8Kvth-PHL5GyFkqsoVmDk~soAmrj0QmJjB9P45Jnlm7i9cQ9eS8UEWMDFRwaa4foSA-SWXEJE9lY7HshGMv3uFPozwasFvJQpPmbey7DqfD4d8yADYUmJFL-Kw4YfM6nLpWuDp~qAXnucH63jl152xvGML0Hx3vSNLf1rAjqrES-xlXEpRmk1D-NBdsiBnRoYW9gZfC4oZfuDh~n0dxofk8S32G68bLLbPWon5h19zrignyy8adJm4mh~ImZepmrbClb35TbhtVQZ4lAcPuEdgP0KiuneEgm8A0D-1GNhhrh6gy3Y6rIA__&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4",
          weekdate: 3,
        },
        {
          img_src: "https://s3-alpha-sig.figma.com/img/0f1d/bb39/e0d52c35665c4883881273524a9ceeb7?Expires=1682899200&Signature=pXNAcX2HH2JzZagxIs0GwszN9Qy54Qw~9KIqbBpsOztl4ElP89w57gsOvdResbohhMZv81cQNLZDVGlAa-tEfJxpy0IrrNcoztRGkwiTF25xJLBt2hFVJXthSVhiKEDiNwHvlz7~YJasqqP3tu2wAjTO8Qg7TQ~RmZQgz4in3a6FvbycOnrUBI52HE3wioeDpV4C1Eg3JVsHZSBLQUkU88BH2NueCF0KR2Fxp12RacCHCdrrX3JvB0FIylvmI8pXsxBz110OCqQfbKouJPA~joYs98gAYLBqS136vCBexGZWCP7wO3rB0w78tDT9~31gAwGMZ38ucuuZ45mqUJOmpA__&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4",
          weekdate: 3,
        },
        {
          img_src: "https://s3-alpha-sig.figma.com/img/e068/3206/9adb638c6bb6b9a3c32c7d95509bd1a1?Expires=1682899200&Signature=eROo1GjvI2HfvJ856CUniXqc5HAN2TNza7PULv7~Kgy3HXGEG803Wf-JhNlVnQZqOIXckDXjK1PluK6EwiMIx90ndSkuBxG12BIq-DokYrq~MCfUMxW1XtNC~ZeAC5bAhAUPo87LOM3fSUPGs0bBrP9AOzhw69PDV3MvNN-SvFfIOibUuDrTUenkEq1SjO7d2egRBSGIfN~iEEiik8j3x0aFEp8XkDy-PLX5FSlhSmaddVWX3BHM0kZ5veWIkvcmO8v-KIrhQ1GOb4AHJXh81WvyJjqv5ZiMSbutxi8xJtBE-X0zzG0CZ93E4txSsU71qHNxWeJz4SaUyHKAOO4NGA__&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4",
          weekdate: 3,
        },
        {
          img_src: "https://s3-alpha-sig.figma.com/img/dfb5/1296/f87dd9e723ec4b2a7e926451a624da43?Expires=1682899200&Signature=AgeVio-VT-MSww-wqVOxcqnQoWqYACmV6FAHZ2UPHVU~6uoP77bCNpWKrTEP8vRS67e8bEXQjXpmR8ACquDUcozRnVGonze3YhA0J1C9UHlvmCO1r1QOHN2xl6lmjQF-V6iWJkydFD2O1T6JsB3PYZEICgsZUV3IIm1LSq-KedcTYy7oyY57nHZHjJT4hpS8~YfgIoCZ2qEJdXIvtB1OhmPSLMg6DKaVhw~kfiXIxsT0jn4dCt0Ju02HJktnd80bkLAp4wwes9jmsP6zpvo49gYTYLxTafa-5IdwQLnpqkB475SoLfLpnpV~LmtJwou0a9tHoG~U4g0fkrhAsU5vkw__&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4",
          weekdate: 4,
        },
        {
          img_src: "https://s3-alpha-sig.figma.com/img/8b98/998e/3bf74b107028d704883155397d5f26b3?Expires=1682899200&Signature=QrYZuK0ZyplPvI5ubVSOIJfdbDeLrWM0G47sjP~l55H5UBd2x93Mqa2wYAx84p5Q0EJ08xRH8ivca9zYGi9IQAD2Cxfr3R7sPCpEpwcbzJEK9zkU7YrTDdz8y5mmEkiInqvUXq7bW4fIDcDN5E5carB4sgt44gt12fbhWGwvEbqYBtxmzQAv7PTL5I~zpTP93HcnGmXW-WmhoqD0rcD36uqHEsDplffPv0asOOZcfTCLOVoi-LYleITR4-iblHaFmCyWhjcbZHLtTs8U1XGaSmCWQtxPlSRG2Pss2apwfIviLKM8qdqcSvNX-XZyP5KbYt5m4U0sB2I-RGkGbBd-Jw__&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4",
          weekdate: 4,
        },
        {
          img_src: "https://s3-alpha-sig.figma.com/img/eb68/48c3/b7867231db0ea379dcd169d9d407a0b6?Expires=1682899200&Signature=mgIQ-wK5X8x5vy~HD~oAYW5EXcKSytCHIBFimaIZRoQx5BND8iap7U2WR2a4hbqsotXz9eR4eGLaVxwTjrUY0CCqwVawlTZwar5oXEhCaD789iX~DqEB6leTRVMRauuzkYvg4uACBUb0mj32Z8XTF12LGMuniiEIwe4aCvQZOKsPtZo2I0AI3QqiLixcT-ZHrQ9Xx37ms5B55mPCTvZJFhT2O6dAt-PPeVONlruiKGy-9uE7LEBMV2uUM7J5c332v1XwdR5E9564uH1Bus1HHbeltIAABNoWcmy6~9rXhvQo6TvQxgkvV40So4cFlKN0WX7lP0xGPqFA3TOPhtwwyg__&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4",
          weekdate: 5,
        },
        {
          img_src: "https://s3-alpha-sig.figma.com/img/c195/0786/c962105f3072197589a6b93eb81d91c8?Expires=1682899200&Signature=W9KTNCYnnMi3yYX3XlA4osmFbCbRMLwX93gAAxPQgEHfc0270cI9I44vNhUb51c2GjXLOWVMA1uTBGf5q0KDpyesCn0TCVUJ6~VNqLsQBtSA9tihXMh54JD856kFUlHIjZ9a47BuqiNYG74j~ARfRlrVFHzsZu6w2A235tZdTS6aKnpAD6k0O0JA7EkQIsjk903uFh8~YUJniZ9gPqx5nGyafu5xaXN7yxhUeIODvtlU~szlCD1gm2Y9w~eTfSYk3kTceZePV0ZbxRnUdinQ0tZr7ZPG4ASgClic3689aOqo~GvfWtRiwGmSgIvfKIvYrBZwVxlwkNpcbR8XuSuAhA__&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4",
          weekdate: 5,
        },
        {
          img_src: "https://s3-alpha-sig.figma.com/img/8312/d516/a35aabfe0d1ff86c8642aff82786b30e?Expires=1682899200&Signature=Y1LuKGWVWF6l0tDgqgOfLiDfTybeYNbemkFflmXqNY-5f5n494OSkT0jhWk-W0lJLAkimSkyORl9EjIBCXERURwyySvZUtBwRTe7Odl8i-avb8d3vJEZOG281SLcGs9ylWVA9NU6R6Ew8n8VPZEJyK79l8dLlp-pVrqiwkuZBlkCWTPofgqtyhd2IS7-RH8T1yZ3Utfg-Bn2oLTLgdvR4eBkipe1EwhHY5ZOFlmbyiAVShxlX930-U3ApqZVYlvQeTftLl0ouU2ttMtI1GXWCGYnDkXaVs6RWTJFwOkEHOUdENzLLzY85DKYbkLSNNV03FDA4Vu8Sd3sUkn9Ssaa-Q__&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4",
          weekdate: 5,
        },
        {
          img_src: "https://s3-alpha-sig.figma.com/img/9646/54c0/defadc403aceaa8b6faf1883a7cf43aa?Expires=1682899200&Signature=kLFtFWduEKaSOYT3ufQBocJ-ZGKESZYYCoWuCri9Ba~dYOmrKzce~TcwNluk0kmgc85Mv5uXFTlgLGMvUG6t4LEtjHLATExNbiZFg8gBKXOh81CvfStTwOJHfcPWGo4t1LEmf8TELMF~8i9ZJDhvrjaILMjqgNLyqfmK0czZiVo-DHLoITFTDiwhLFd32QxzNbpZMLTtaiUVVJGROVyO5rMQQUnU53M8OqvrdG8SWE1Ygf464OKfD2vPzJT8eV4vG10pPQlL23jmxdBW9KKxYyNRv3vduxfEjOXz~qh4SwXzjjYw28Q7ygdvVHosd47O7DO5suxKv9SRKSIH2vMmAw__&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4",
          weekdate: 5,
        },
        {
          img_src: "https://s3-alpha-sig.figma.com/img/04ab/7572/9ca5a932a94f1a860ae5e3cf0f7d16e0?Expires=1682899200&Signature=d-CiMX2Hjx-cGtchUaxEvuyDS4Hc9yfx6hLqwmBY-w6-ikMphtDlpcQShIUuQzNhLfqyEBKRFeEy7g0CbOMjEjuDlYwGR9Vgeh~eznPSCLh0Y9YojrbzKZd73M16q0KPQIxD3ww3r-9bA7qkf45WIiLvXA3wCbFtAzocy5wtJzEaF47IuPe2Ma~VUnY352fSaevUWh-AgAZNfiGGssqbuSc6h1RZnyHlf5H-6i-9FEkp2sl0jUklMrP9gGTxba~k4HWQcFYeDxRL9TgXMMyATE8rCreIbuhgmiFbdMVZ7L8X-e8dEKH90FdqoP0JyadpzMywjWbMIcM2FVbwTMWHVw__&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4",
          weekdate: 6,
        },
        {
          img_src: "https://s3-alpha-sig.figma.com/img/a16e/21de/05116c7e23b02b910bbbb0797e6a007c?Expires=1682899200&Signature=V3dPxcg5XOmUoba~6pB24UE-uz~JPBV2832a~q2UNr5Vju8yTTX4Ua3XcZDtzwSuvhhT9HCx5-rSWteaCIrZq2LibQAK5QUPSjTFw-0URhxs73k6nzJ6NGU5juzruOztIWsULtIUBRqHlIMXmUn1jF2FOdP0OOe8TxOladtdY9cQ4ZxEcWcu9a1de5O20l9SUIP6EZudNGhKEdfDfFPx~R0KyhAZzYsX43KXkONpusJ4XsHFMun1gnWNM3I~cMo9qY~XQla99oB1IPNzRtLKaIrPHal8Dn~FCuA-c1XplfR~I0LNR3bZ4NwjarmFnXRw6qSWq~FPxiNE9SaE8XBAAA__&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4",
          weekdate: 7,
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
  background-color: #4d226d;
  z-index: 1;
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
  padding-top: 15px;
}

.Calendar_logo p {
  /* logo文字样式 */
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
.Zzz-img{
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
</style>
