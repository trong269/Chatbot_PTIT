import axios from 'axios'
import { AuthResult, Credentials } from '../models/auth'
import { RegistrationInfo, User } from '../models/user'

export const login = async (credentials: Credentials): Promise<AuthResult> => {
  return (await axios.postForm<AuthResult>('/login', credentials)).data
}

export const register = async (info: RegistrationInfo): Promise<User> => {
  return (await axios.post('/users', info)).data
}

export const deleteAccount = async (): Promise<void> => {
  await axios.delete('/users/me')
}
