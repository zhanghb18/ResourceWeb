import { createRouter, createWebHashHistory } from "vue-router";
import Home from "../view/home/Home.vue"
import UserCenter from "../view/userpage/UserCenter.vue"

const routes = [{
    path: "/",
    name: "home",
    component: Home
},
{
    path: "/userpage",
    name: "userpage",
    component: UserCenter
}]

const router = createRouter({
    history: createWebHashHistory(),
    routes,
})

export default router