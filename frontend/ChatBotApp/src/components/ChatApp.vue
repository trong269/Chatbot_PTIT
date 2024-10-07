<!-- src/components/ChatApp.vue -->
<template>
    <div>
      <h1>Chatbot PTIT</h1>
      <div class="chat-window">
        <div class="messages">
          <ChatMessage
            v-for="msg in currentConversation.messages"
            :key="msg.id"
            :message="msg"
          />
        </div>
        <ChatInput @sendMessage="sendMessage" />
      </div>
    </div>
  </template>
  
  <script>
  import { ref, computed, onMounted } from 'vue';
  import { useStore } from 'vuex';
  import { useWebSocket } from '../composables/useWebSocket';
  import ChatMessage from './ChatMessage.vue';
  import ChatInput from './ChatInput.vue';
  
  export default {
    components: {
      ChatMessage,
      ChatInput,
    },
    setup() {
      const store = useStore();
      const { sendMessageToWebSocket, connectWebSocket, receiveMessageFromWebSocket } = useWebSocket();
      const currentConversation = computed(() => store.state.currentConversation);
  
      const sendMessage = (content) => {
        const message = {
          id: Date.now(),
          content,
          sender: store.state.user.username,
        };
  
        // Gửi tin nhắn đến WebSocket
        sendMessageToWebSocket(message);
        
        // Cập nhật cuộc trò chuyện
        store.commit('setCurrentConversation', {
          ...currentConversation.value,
          messages: [...currentConversation.value.messages, message],
        });
      };
  
      onMounted(() => {
        connectWebSocket('ws://localhost:8000/ws/chat'); // URL WebSocket của server FastAPI
  
        // Nhận tin nhắn từ WebSocket
        receiveMessageFromWebSocket((message) => {
          // Cập nhật cuộc trò chuyện khi nhận được tin nhắn
          store.commit('setCurrentConversation', {
            ...currentConversation.value,
            messages: [...currentConversation.value.messages, message],
          });
        });
      });
  
      return {
        currentConversation,
        sendMessage,
      };
    },
  };
  </script>
  
  <style>
  .chat-window {
    border: 1px solid #ccc;
    padding: 10px;
    height: 400px;
    overflow-y: scroll;
  }
  .messages {
    margin-bottom: 10px;
  }
  </style>
  