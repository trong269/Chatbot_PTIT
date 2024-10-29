<template>
  <ChatAnswer v-if="data.sender === 'bot'" :content="data.content" />
  <ChatQuestion v-else :content="data.content" />
</template>

<script setup lang="ts">
import { SimpleMessage } from '../models/chat'
import ChatAnswer from './ChatAnswer.vue'

defineProps<{
  data: SimpleMessage
}>()
</script>
