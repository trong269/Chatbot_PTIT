import { Answer } from '../models/chat'

export const sendQuestion = async (content: string): Promise<Answer> => {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve({ type: 'answer', content: `I am a bot. Your question is ${content}` })
    }, 1000)
  })
}
