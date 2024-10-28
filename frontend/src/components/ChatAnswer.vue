<template>
  <div class="chat__ans">
    <div class="chat__ans_avatar">
      <Avatar label="P" shape="circle" />
    </div>
    <WaitingDots v-if="composing" />
    <p v-else" class="chat__ans_content" v-html="processedContent"></p>
  </div>
</template>

<script setup lang="ts">
import { marked } from 'marked'
import WaitingDots from './WaitingDots.vue'
import { computed } from 'vue'

const { content } = defineProps<{
  content?: string
  composing?: boolean
}>()
const processedContent = computed(() => {
  const renderer = new marked.Renderer();
  renderer.link = function( {href, text}: {href: string, text: string} ) {
    console.log(href)
    return '<a target="_blank" href="'+ href +'">' + text + '</a>';
  }
  return content && marked(content.replace(/\\n/g, '<br>'), {renderer})
})
</script>

<style lang="scss">
.chat__ans {
  align-self: flex-start;
  background: transparent;
  display: flex;
  gap: 20px;
  z-index: 1;

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

    a {
      text-decoration: underline;
    }

    p,
    ul {
      margin-top: 0;
    }
  }
}
</style>
