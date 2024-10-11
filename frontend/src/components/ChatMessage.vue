<template>
  <ChatAnswer v-if="data.type === 'answer'" :content="data.content" />
  <ChatQuestion v-else :content="data.content" />
</template>

<script setup lang="ts">
import { Message } from '../models/chat'
import ChatAnswer from './ChatAnswer.vue'

defineProps<{
  data: Message
}>()
</script>
