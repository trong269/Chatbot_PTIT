export interface RegistrationInfo {
  username: string
  password: string
  email: string
  full_name: string
}

export interface User {
  user_id: number
  username: string
  email: string
  full_name: string
}

export interface UpdatedUser {
  email: string
  full_name: string
  password?: string
}
