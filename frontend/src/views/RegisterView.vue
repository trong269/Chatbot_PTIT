<template>
  <form class="login__form" @submit.prevent="createAccount">
    <div class="form__heading">
      <Image :src="logo" alt="Image" height="100" />
      <h2>Chatbot PTIT</h2>
    </div>
    <InputText
      v-model="registrationInfo.username"
      placeholder="Tên đăng nhập"
      :autofocus="true"
      fluid
    />
    <Password
      v-model="registrationInfo.password"
      placeholder="Mật khẩu"
      fluid
      :feedback="false"
      toggle-mask
    />
    <InputText v-model="registrationInfo.full_name" placeholder="Họ tên" fluid />
    <InputText v-model="registrationInfo.email" placeholder="Email" type="email" fluid />
    <div class="form__actions">
      <Button type="submit" :disabled="submitting" fluid>Đăng ký</Button>
      <Divider class="form__action-divider" align="center"> Đã có tài khoản? </Divider>
      <RouterLink to="/login">
        <Button outlined fluid>Đăng nhập</Button>
      </RouterLink>
    </div>
  </form>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import logo from '../assets/logo.png'
import { RegistrationInfo } from '../models/user'
import { register } from '../services/auth-service'
import { useRouter } from 'vue-router'

const router = useRouter()
const submitting = ref(false)
const registrationInfo = ref<RegistrationInfo>({
  username: '',
  password: '',
  full_name: '',
  email: '',
})

const createAccount = async () => {
  submitting.value = true
  try {
    await register(registrationInfo.value)
    router.push('/login')
  } finally {
    submitting.value = false
  }
}
</script>

<style scoped>
.login__form {
  display: flex;
  flex-direction: column;
  gap: 20px;
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
</style>
