<template>
  <div class="container">
    <Image :src="logo" alt="Logo" height="150" />
    <form class="input_area" @submit.prevent="start">
      <InputText v-model="title" placeholder="Nhập tiêu đề" class="inp" />
      <Button type="submit" :disabled="submitting"> Bắt đầu </Button>
    </form>
  </div>
</template>

<script setup lang="ts">
import Button from 'primevue/button'
import Image from 'primevue/image'
import InputText from 'primevue/inputtext'
import { ref } from 'vue'
import logo from '../../assets/logo.png'
import { useRouter } from 'vue-router'
import { startConversation } from '../../services/chat-service'

const emit = defineEmits<{
  (e: 'created'): void
}>()
const router = useRouter()
const title = ref('')
const submitting = ref(false)

const start = async () => {
  submitting.value = true
  try {
    const conversation = await startConversation(title.value)
    emit('created')
    router.push(`/chat/${conversation.conversation_id}`)
  } finally {
    submitting.value = false
  }
}
</script>

<style lang="scss" scoped>
.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 80%;
  gap: 30px;

  .input_area {
    display: flex;
    gap: 15px;

    .inp {
      flex-grow: 1;
      padding: 10px 20px;
      width: 350px;
    }
  }
}
</style>
