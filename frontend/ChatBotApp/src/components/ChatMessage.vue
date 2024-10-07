<!-- src/components/ChatMessage.vue -->
<template>
    <div :class="['message', message.sender === currentUser ? 'sent' : 'received']">
      <strong>{{ message.sender }}</strong>: {{ message.content }}
    </div>
  </template>
  
  <script>
  export default {
    props: {
      message: {
        type: Object,
        required: true,
      },
    },
    computed: {
      currentUser() {
        return this.$store.state.user.username;
      },
    },
  };
  </script>
  
  <style>
  .message {
    margin: 5px 0;
  }
  .sent {
    color: blue;
  }
  .received {
    color: green;
  }
  </style>
  