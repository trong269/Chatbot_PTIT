<template>
  <form class="login__form">
    <div class="form__heading">
      <Image :src="logo" alt="Image" height="100" />
      <h2>Chatbot PTIT</h2>
    </div>
    <InputText v-model="username" placeholder="Tên đăng nhập" :autofocus="true" fluid />
    <Password v-model="password" placeholder="Mật khẩu" fluid :feedback="false" toggle-mask />
    <div>
      <label class="remember">
        <Checkbox v-model="remember" binary />
        Ghi nhớ tài khoản
      </label>
    </div>
    <div class="form__actions">
      <Button type="submit" fluid @click="doLogin" :disabled="submitting">Đăng nhập</Button>
      <Divider class="form__action-divider" align="center"> Chưa có tài khoản? </Divider>
      <RouterLink to="/register">
        <Button outlined fluid>Đăng ký</Button>
      </RouterLink>
    </div>
  </form>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { login } from '../services/auth-service'
import logo from '../assets/logo.png'

const router = useRouter()
const username = ref('')
const password = ref('')
const remember = ref(true)
const submitting = ref(false)

const doLogin = async () => {
  try {
    submitting.value = true
    const result = await login({ username: username.value, password: password.value })
    localStorage.setItem('token', result.access_token)
    localStorage.setItem('expiration', '' + new Date().getTime() + 20*60*1000) // 20 phut
    router.push('/chat')
  } catch (error) {
    console.error(error)
  } finally {
    submitting.value = false
  }
}
</script>

<style scoped>
.login__form {
  display: flex;
  flex-direction: column;
  gap: 25px;
}
.form__heading {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.form__heading h2 {
  margin: 15px 0 0 0;
}
.form__action-divider {
  margin-block: 15px;
}
.remember {
  display: flex;
  align-items: center;
  gap: 10px;
}
</style>
