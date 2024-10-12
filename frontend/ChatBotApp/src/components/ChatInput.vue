<!-- src/components/ChatInput.vue -->
<template>
    <div>
      <input v-model="message" @keyup.enter="send" placeholder="Type your message..." />
      <button @click="send">Send</button>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  
  export default {
    setup(props, { emit }) {
      const message = ref('');
  
      const send = () => {
        if (message.value.trim()) {
          emit('sendMessage', message.value);
          message.value = '';
        }
      };
  
      return {
        message,
        send,
      };
    },
  };
  </script>
  
  <style>
  input {
    width: 80%;
    padding: 5px;
  }
  button {
    padding: 5px;
  }
  </style>
  