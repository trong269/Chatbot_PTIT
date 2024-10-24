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
          :active="selectedConversation?.conversation_id === conversation.conversation_id"
          @deleted="$emit('deleteConversation')"
        />
      </ul>
    </template>
  </Card>
</template>

<script setup lang="ts">
import Card from 'primevue/card'
import Divider from 'primevue/divider'
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { Conversation } from '../models/chat'
import ConversationItem from './Sidebar/ConversationItem.vue'

defineEmits<{
  (e: 'deleteConversation'): void
}>()
const { conversations } = defineProps<{
  conversations: Conversation[]
}>()
const route = useRoute()
const selectedConversation = computed(() =>
  conversations.find((c) => c.conversation_id === Number(route.params.id))
)
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
