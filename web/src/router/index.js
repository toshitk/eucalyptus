import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/Login.vue'

const routes = [
  {
    path: '/',
    name: 'login',
    component: LoginView
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
