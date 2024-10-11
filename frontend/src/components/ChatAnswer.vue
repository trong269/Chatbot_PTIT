<template>
  <div class="chat__ans">
    <div class="chat__ans_avatar">
      <Avatar label="P" shape="circle" />
    </div>
    <WaitingDots v-if="!content" />
    <p v-if="content" class="chat__ans_content">{{ content }}</p>
  </div>
</template>

<style lang="scss" scoped>
.chat__ans {
  align-self: flex-start;
  background: transparent;
  display: flex;
  gap: 20px;

  .chat__ans_avatar {
    position: relative;
    top: -10px;

    .p-avatar {
      background-color: var(--p-primary-color);
      width: 46px;
      height: 46px;
      color: var(--p-primary-contrast-color);
    }
  }

  .chat__ans_content {
    margin: 0;
  }
}
</style>

<script setup lang="ts">
import WaitingDots from './WaitingDots.vue'

defineProps<{
  content?: string
}>()
</script>
