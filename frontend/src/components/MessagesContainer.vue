<template>
  <div ref="container" class="messages_ctn">
    <ChatMessage v-for="msg in messages" :key="msg.content" :data="msg" />
    <ChatAnswer v-if="composing" composing />
  </div>
</template>

<script setup lang="ts">
import { onUpdated, ref, watch } from 'vue'
import { SimpleMessage } from '../models/chat'
import ChatAnswer from './ChatAnswer.vue'
import ChatMessage from './ChatMessage.vue'

const { composing } = defineProps<{
  messages: SimpleMessage[]
  composing: boolean
}>()
const container = ref<HTMLDivElement>()

onUpdated(() => container.value?.scrollTo(0, container.value.scrollHeight))
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
.messages_ctn {
  background-image: url('/src/assets/logo-trans.png');
  background-repeat: no-repeat;
  background-position: center;
}
</style>
