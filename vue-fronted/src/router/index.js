import { createRouter, createWebHashHistory } from "vue-router";
import Home from "../view/home/Home.vue"
import UserCenter from "../view/userpage/UserCenter.vue"
import UserInfo from "../view/userpage/UserInfo.vue"
import BanguDetail from "../view/bangu/BanguDetail.vue"
import ResourceDetail from "../view/bangu/ResourceDetail.vue"

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
  path: "/bangudetail/:banguName",
  name: "bangudetail",
  component: BanguDetail
},
{
  path: "/resourcedetail",
  name: "resourcedetail",
  component: ResourceDetail
}
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
})

export default router