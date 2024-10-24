export type Sender = 'user' | 'bot'

export interface Message {
  sender: Sender
  content?: string
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
