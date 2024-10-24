import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import AuthLayout from '../layouts/AuthLayout.vue'
import ChatView from '../views/ChatView/ChatView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    redirect: '/chat',
  },
  {
    path: '/chat/:id?',
    component: ChatView,
    beforeEnter: (_, __, next) => {
      const token = localStorage.getItem('token')
      if (!token) next('/login')
      else next()
    },
  },
  {
    path: '/',
    component: AuthLayout,
    children: [
      { path: '/login', component: LoginView },
      { path: '/register', component: RegisterView },
    ],
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
