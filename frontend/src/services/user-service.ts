import axios from 'axios'
import { UpdatedUser, User } from '../models/user'

export const getUserInfo = async (): Promise<User> => {
  return (await axios.get('/users')).data
}

export const updateUserInfo = async (info: UpdatedUser): Promise<User> => {
  return (await axios.put('/users', info)).data
}
