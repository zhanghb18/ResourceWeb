import { createRouter, createWebHashHistory } from "vue-router";
import Home from "../view/home/Home.vue"
import UserCenter from "../view/userpage/UserCenter.vue"
import UserInfo from "../view/userpage/UserInfo.vue"
import BanguDetail from "../view/bangu/BanguDetail.vue"

<<<<<<< HEAD
const routes = [{
  path: "/",
  name: "home",
  component: Home
},
{
  path: "/usercenter",
  name: "usercenter",
  component: UserCenter
},
{
  path: "/userinfo",
  name: "userinfo",
  component: UserInfo
},
{
  path: "/bangudetail",
  name: "bangudetail",
  component: BanguDetail
}]
=======
const routes = [
  {
    path: "/",
    name: "home",
    component: Home
  },
  {
    path: "/usercenter",
    name: "usercenter",
    component: UserCenter
  },
  {
    path: "/userinfo",
    name: "userinfo",
    component: UserInfo
  }
]
>>>>>>> develop

const router = createRouter({
  history: createWebHashHistory(),
  routes,
})

export default router