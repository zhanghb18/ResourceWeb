import { createRouter, createWebHashHistory } from "vue-router";
import Home from "../view/home/Home.vue"
import UserCenter from "../view/userpage/UserCenter.vue"
import UserInfo from "../view/userpage/UserInfo.vue"

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
}]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
})

export default router