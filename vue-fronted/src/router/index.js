import { createRouter, createWebHashHistory } from "vue-router";
import Home from "../view/home/Home.vue"
import AcgPage from "../view/acgpage/AcgPage.vue"
import LoginForm from "../view/LoginForm.vue"

const routes = [{
    path: "/",
    name: "home",
    component: Home
},
{
    path: "/acgpage",
    name: "acgpage",
    component: AcgPage
}]

const router = createRouter({
    history: createWebHashHistory(),
    routes,
})

export default router