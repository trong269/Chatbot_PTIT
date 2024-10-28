<template>
  <li class="conversation" :class="{ active }">
    <RouterLink :to="'/chat/' + conversation.conversation_id" class="label">
      <span>{{
        conversation.title.length > 20
          ? conversation.title.substring(0, 20) + '...'
          : conversation.title
      }}</span>
    </RouterLink>
    <div class="more">
      <i class="pi pi-ellipsis-h" @click="toggle"></i>
      <Menu ref="menu" :model="items" :popup="true"></Menu>
    </div>
  </li>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'
import { Conversation } from '../../models/chat'
import { deleteConversation, endConversation } from '../../services/chat-service'

const emit = defineEmits<{
  (e: 'deleted'): void
  (e: 'ended'): void
}>()
const props = defineProps<{
  conversation: Conversation
  active: boolean
}>()

const menu = ref()
const ITEM_END = {
  label: 'Kết thúc',
  icon: 'pi pi-times',
  command: async () => {
    await endConversation(props.conversation.conversation_id)
    emit('ended')
  },
}
const ITEM_DELETE = {
  label: 'Xóa',
  icon: 'pi pi-trash',
  command: async () => {
    await deleteConversation(props.conversation.conversation_id)
    emit('deleted')
  },
}
const items = computed(() => props.conversation.end_time ? [ITEM_DELETE] : [ITEM_END, ITEM_DELETE])

const toggle = (event: any) => {
  menu.value.toggle(event)
}
</script>

<style lang="scss" scoped>
.conversation {
  cursor: pointer;
  display: flex;
  align-items: center;
  border-radius: var(--p-inputtext-border-radius);
  min-width: 250px;
  font-size: 0.95rem;
  &:hover {
    background-color: var(--p-surface-200);
  }
  &.active {
    background-color: var(--p-surface-200);
    font-weight: bold;
  }

  .label {
    padding: 8px 18px;
    flex-grow: 1;
  }

  .more {
    display: none;
    margin-right: 18px;
  }
  &:hover .more {
    display: block;
  }
}
</style>
