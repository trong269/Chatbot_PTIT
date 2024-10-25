import axios from 'axios'
import { Answer, Conversation } from '../models/chat'

export const sendQuestion = async (conversationId: number, content: string): Promise<Answer> => {
  return (await axios.post(`/conversations/${conversationId}/messages`, { content })).data
}

export const startConversation = async (title: string): Promise<Conversation> => {
  return (await axios.post('/conversations', null, { params: { title } })).data
}

export const getAllConversations = async (): Promise<Conversation[]> => {
  return (await axios.get('/conversations')).data
}

export const getConversation = async (id: number): Promise<Conversation> => {
  const all = await getAllConversations()
  const conversation = all.find((c) => c.conversation_id === id)
  if (!conversation) throw new Error('Conversation not found')
  return conversation
}

export const endConversation = async (id: number): Promise<void> => {
  await axios.put(`/conversations/${id}/end`)
}

export const deleteConversation = async (id: number): Promise<void> => {
  await axios.delete(`/conversations/${id}`)
}
