<!-- src/components/Register.vue -->
<template>
    <div>
      <h2>Register</h2>
      <form @submit.prevent="register">
        <input v-model="username" placeholder="Username" required />
        <input type="password" v-model="password" placeholder="Password" required />
        <button type="submit">Register</button>
      </form>
      <router-link to="/">Login</router-link>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  import axios from 'axios';
  import { useRouter } from 'vue-router';
  
  export default {
    setup() {
      const username = ref('');
      const password = ref('');
      const router = useRouter();
  
      const register = async () => {
        try {
          await axios.post('http://localhost:8000/api/register', {
            username: username.value,
            password: password.value,
          });
          router.push('/');
        } catch (error) {
          console.error(error);
        }
      };
  
      return {
        username,
        password,
        register,
      };
    },
  };
  </script>
  