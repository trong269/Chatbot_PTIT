<!-- src/components/Login.vue -->
<template>
    <div>
      <h2>Login</h2>
      <form @submit.prevent="login">
        <input v-model="username" placeholder="Username" required />
        <input type="password" v-model="password" placeholder="Password" required />
        <button type="submit">Login</button>
      </form>
      <router-link to="/register">Register</router-link>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  import axios from 'axios';
  import { useStore } from 'vuex';
  import { useRouter } from 'vue-router';
  
  export default {
    setup() {
      const username = ref('');
      const password = ref('');
      const store = useStore();
      const router = useRouter();
  
      const login = async () => {
        try {
          const response = await axios.post('http://localhost:8000/api/login', {
            username: username.value,
            password: password.value,
          });
          store.commit('setUser', response.data.user);
          store.commit('setToken', response.data.token);
          router.push('/chat');
        } catch (error) {
          console.error(error);
        }
      };
  
      return {
        username,
        password,
        login,
      };
    },
  };
  </script>
  