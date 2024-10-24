<template>
  <div class="chat__question">
    <p class="chat__question_content">{{ content }}</p>
  </div>
</template>

<style scoped>
.chat__question {
  align-self: flex-end;
  background-color: var(--p-gray-300);
  padding: 8px 18px;
  border-radius: var(--p-inputtext-border-radius);
}
.chat__question_content {
  margin: 0;
}
</style>

<script setup lang="ts">
defineProps<{
  content: string
}>()
</script>
