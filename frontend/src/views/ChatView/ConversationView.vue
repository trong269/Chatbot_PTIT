<template>
  <MessagesContainer :messages="messages" :composing="composing" />
  <form
    class="input_area"
    :class="{ disabled: !conversation || conversation?.end_time }"
    @submit.prevent="doSendQuestion"
  >
    <InputText v-model="question" placeholder="Nhập câu hỏi" class="inp" />
    <Button
      type="submit"
      icon="pi pi-send"
      class="btn_send"
      :disabled="composing || !conversation || !question.trim()"
    ></Button>
  </form>
</template>

<script setup lang="ts">
import { computed, ref, watch } from 'vue'
import MessagesContainer from '../../components/MessagesContainer.vue'
import { Conversation, SimpleMessage } from '../../models/chat'
import { sendQuestion } from '../../services/chat-service'

const { conversation } = defineProps<{ conversation: Conversation }>()
const messages = computed<SimpleMessage[]>(() => conversation.messages.sort((a, b) => a.message_id - b.message_id) || [])
const question = ref('')
const composing = ref(false)

const doSendQuestion = async () => {
  if (!conversation || composing.value || !question.value?.trim()) return
  try {
    const content = question.value?.trim()
    messages.value.push({ content, sender: 'user' })
    question.value = ''
    composing.value = true
    const answer = await sendQuestion(conversation.conversation_id, content)
    if (answer.conversation_id == conversation.conversation_id) {
      messages.value.push(answer)
    }
  } finally {
    composing.value = false
  }
}

watch(
  () => conversation,
  () => (composing.value = false)
)
</script>

<style lang="scss" scoped>
.input_area {
  display: flex;
  gap: 20px;
  margin-top: 10px;
  margin: 0 30px;
  width: 80%;
  max-width: var(--app-chat-max-width);
  align-self: center;

  &.disabled {
    visibility: hidden;
  }

  .inp {
    flex-grow: 1;
    padding: 10px 20px;
  }
}
</style>
