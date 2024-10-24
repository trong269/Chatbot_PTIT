<template>
  <RouterView />
  <Toast />
</template>

<script setup lang="ts">
import axios, { AxiosError } from 'axios'
import Toast from 'primevue/toast'
import { useToast } from 'primevue/usetoast'

const toast = useToast()

axios.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error instanceof AxiosError) {
      toast.add({
        severity: 'error',
        summary: 'Error',
        detail: error.response?.data.detail || error.message,
        life: 3000,
      })
    }
    return Promise.reject(error)
  }
)
</script>
