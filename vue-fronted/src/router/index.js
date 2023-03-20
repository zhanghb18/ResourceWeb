import { createRouter, createWebHashHistory } from "vue-router";
import Home from "../view/home/Home.vue"
import MainPage from "../view/home/MainPage.vue"
import LoginForm from "../view/LoginForm.vue"

const routes = [{
    path: "/",
    name: "home",
    component: MainPage
}]

const router = createRouter({
    history: createWebHashHistory(),
    routes,
})

export default router