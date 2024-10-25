<template>
  <div class="messages_ctn">
    <ChatMessage v-for="msg in messages" :key="msg.content" :data="msg" />
    <ChatMessage v-if="composing" :data="{ sender: 'bot' }" />
  </div>
</template>

<script setup lang="ts">
import { Message } from '../models/chat'
import ChatMessage from './ChatMessage.vue'

defineProps<{
  messages: Message[]
  composing: boolean
}>()
</script>

<style scoped>
.messages_ctn {
  flex-grow: 1;
  width: 80%;
  max-width: var(--app-chat-max-width);
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin: 0 auto;
  background: rgba(255, 255, 255, 0);
  border-radius: 20px;
  position: relative;
  padding: 30px;
}
.messages_ctn::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url('/src/assets/logo.png');
  background-repeat: no-repeat;
  background-position: center;
  opacity: 0.1;
}
</style>
