<template>
  <div class="page_ctn">
    <div class="left">
      <Menu
        :model="items"
        :pt="{
          root: {
            style: {
              border: 'none',
              borderRadius: '20px',
              padding: '20px',
              '--p-menu-item-padding': '13px 22px',
            },
          },
          list: {
            style: {
              gap: '10px',
            },
          },
        }"
      ></Menu>
    </div>
    <div class="right">
      <MessagesContainer :messages="messages" :composing="composing" />
      <form class="input_area" @submit.prevent="doSendQuestion">
        <InputText v-model="question" placeholder="Nhập câu hỏi" class="inp" />
        <Button type="submit" icon="pi pi-send" class="btn_send" :disabled="composing"></Button>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import MessagesContainer from '../components/MessagesContainer.vue'
import { Message } from '../models/chat'
import { sendQuestion } from '../services/chat-service'

const items = [
  {
    label: 'Tin nhắn',
    icon: 'pi pi-inbox',
    to: '/chat',
  },
  {
    label: 'Cài đặt',
    icon: 'pi pi-cog',
    to: '/settings',
  },
]

const question = ref('')
const messages = ref<Message[]>([])
const composing = ref(false)

const doSendQuestion = async () => {
  if (composing.value || !question.value?.trim()) return
  try {
    const content = question.value?.trim()
    messages.value.push({ content, type: 'question' })
    question.value = ''
    composing.value = true
    const answer = await sendQuestion(content)
    messages.value.push(answer)
  } finally {
    composing.value = false
  }
}
</script>

<style lang="scss" scoped>
.page_ctn {
  display: flex;
  flex-direction: row;
  align-items: stretch;
  height: 100vh;

  .left {
    display: flex;
    height: 100%;
    margin-left: 20px;
    padding: 30px 0px;
  }

  .right {
    flex-grow: 1;
    height: 100%;
    display: flex;
    flex-direction: column;
    gap: 20px;
    padding: 30px 0px;

    .input_area {
      display: flex;
      gap: 15px;
      margin-top: 10px;
      margin: 0 30px;
      width: 100%;
      max-width: var(--app-chat-max-width);
      align-self: center;
      padding: 0 20px;

      .inp {
        flex-grow: 1;
        padding: 10px 20px;
        border-radius: 40px;
      }

      .btn_send {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        padding: 0;
      }
    }
  }
}
</style>
