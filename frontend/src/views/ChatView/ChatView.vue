<template>
  <div class="page_ctn">
    <div class="left">
      <ChatSidebar :conversations="conversations" @delete-conversation="fetchConversations" />
    </div>
    <div class="right">
      <NewConversationView v-if="!conversationId" @created="fetchConversations" />
      <ConversationView v-else />
    </div>
    <ChatHeader />
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import ChatHeader from '../../components/ChatHeader.vue'
import ChatSidebar from '../../components/ChatSidebar.vue'
import { Conversation } from '../../models/chat'
import { getAllConversations } from '../../services/chat-service'
import ConversationView from './ConversationView.vue'
import NewConversationView from './NewConversationView.vue'

const route = useRoute()
const conversationId = computed(() => Number(route.params.id))
const conversations = ref<Conversation[]>([])

const fetchConversations = async () => {
  conversations.value = await getAllConversations()
}

onMounted(fetchConversations)
</script>

<style lang="scss" scoped>
.page_ctn {
  display: flex;
  flex-direction: row;
  align-items: stretch;
  height: 100vh;
  position: relative;

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
    gap: 30px;
    padding: 30px 0px;
  }
}
</style>
