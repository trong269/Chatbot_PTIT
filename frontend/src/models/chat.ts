export type MessageType = 'answer' | 'question'

export interface Message {
  type: MessageType
  content?: string
}

export interface Answer extends Message {
  type: 'answer'
}
