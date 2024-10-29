<template>
  <Card class="sidebar">
    <template #content>
      <ul class="conversation_list">
        <RouterLink to="/chat" class="new">
          <span>Hội thoại mới</span>
          <i class="pi pi-comment"></i>
        </RouterLink>
        <Divider style="margin-block: 5px" />
        <ConversationItem
          v-for="conversation in conversations"
          :key="conversation.conversation_id"
          :conversation="conversation"
          :active="conversation.conversation_id === active?.conversation_id"
          @deleted="handleDelete(conversation)"
          @ended="handleEnd(conversation)"
        />
      </ul>
    </template>
  </Card>
</template>

<script setup lang="ts">
import Card from 'primevue/card'
import Divider from 'primevue/divider'
import { useRouter } from 'vue-router'
import { Conversation } from '../models/chat'
import ConversationItem from './Sidebar/ConversationItem.vue'

const emit = defineEmits<{
  (e: 'update'): void
}>()
const router = useRouter()
const { conversations, active } = defineProps<{
  conversations: Conversation[]
  active?: Conversation
}>()

const handleDelete = (conversation: Conversation) => {
  emit('update')
  if (conversation.conversation_id === active?.conversation_id) {
    router.replace('/chat')
  }
}

const handleEnd = (_: Conversation) => {
  emit('update')
}
</script>

<style lang="scss" scoped>
.sidebar {
  --p-card-body-padding: 15px;

  .conversation_list {
    list-style-type: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 5px;
    font-size: 0.95rem;

    .new {
      padding: 8px 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-radius: var(--p-inputtext-border-radius);
      min-width: 250px;
      cursor: pointer;
      &:hover {
        background-color: var(--p-surface-200);
      }
    }
  }
}
</style>
