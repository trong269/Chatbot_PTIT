<template>
  <div class="page_ctn">
    <div class="left">
      <ChatSidebar :conversations="conversations" :active="selected" @update="fetchAll" />
    </div>
    <div class="right">
      <NewConversationView v-if="!selected" @created="fetchAll" />
      <ConversationView v-else :conversation="selected" />
    </div>
    <ChatHeader />
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import ChatHeader from '../../components/ChatHeader.vue'
import ChatSidebar from '../../components/ChatSidebar.vue'
import { Conversation } from '../../models/chat'
import { getAllConversations, getConversation } from '../../services/chat-service'
import ConversationView from './ConversationView.vue'
import NewConversationView from './NewConversationView.vue'

const route = useRoute()
const conversations = ref<Conversation[]>([])
const selected = ref<Conversation>()

const fetchAll = async () => {
  conversations.value = await getAllConversations()
  console.log(conversations)
  fetchConv()
}

const fetchConv = async () => {
  selected.value = route.params.id ? await getConversation(Number(route.params.id)) : undefined
}

onMounted(fetchAll)
watch(() => route.params.id, fetchConv)
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
