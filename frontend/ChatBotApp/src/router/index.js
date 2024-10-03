// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import ChatApp from '../components/ChatApp.vue';
import Login from '../components/Login.vue';
import Register from '../components/Register.vue';

const routes = [
  { path: '/', component: Login },
  { path: '/register', component: Register },
  { path: '/chat', component: ChatApp },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
