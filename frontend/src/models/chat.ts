export type Sender = 'user' | 'bot'

export interface SimpleMessage {
  sender: Sender
  content: string
}

export interface Message {
  message_id: number
  sender: Sender
  content: string
  conversation_id: number
}

export interface Answer extends Message {
  sender: 'bot'
}

export interface Conversation {
  conversation_id: number
  title: string
  messages: Message[]
  end_time?: string
}
