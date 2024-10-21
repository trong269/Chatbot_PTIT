<template>
  <div class="messsages_wrapper">
    <div class="messages_ctn">
      <ChatMessage v-for="msg in messages" :key="msg.content" :data="msg" />
      <ChatMessage v-if="composing" :data="{ type: 'answer' }" />
    </div>
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
.messsages_wrapper {
  flex-grow: 1;
  overflow-y: auto;
  padding: 20px;
}
.messages_ctn {
  display: flex;
  flex-direction: column;
  gap: 20px;
  max-width: var(--app-chat-max-width);
  margin: 0 auto;
}
</style>
