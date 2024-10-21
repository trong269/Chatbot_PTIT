export const login = async (username: string, password: string) => {
  return new Promise((resolve) => {
    console.log(username, password)
    setTimeout(() => resolve(''), 1000)
  })
}
