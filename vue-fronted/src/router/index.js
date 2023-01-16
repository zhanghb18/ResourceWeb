import { createRouter, createWebHashHistory } from "vue-router";
import Home from "../view/home/Home.vue"
import Login from "../view/Login.vue";

const routes = [{
        path: "/",
        name: "home",
        component: Home
    },
    {
        path: "/login",
        name: "login",
        component: Login
    },
]

const router = createRouter({
    history: createWebHashHistory(),
    routes,
})

export default router