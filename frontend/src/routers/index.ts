import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import LoginView from '../views/LoginView.vue'
import AuthLayout from '../layouts/AuthLayout.vue'
import RegisterView from '../views/RegisterView.vue'
import ChatView from '../views/ChatView.vue'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    redirect: '/chat',
  },
  {
    path: '/chat',
    component: ChatView,
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
