import Aura from '@primevue/themes/aura'
import PrimeVue, { PrimeVueConfiguration } from 'primevue/config'
import { createApp } from 'vue'
import App from './App.vue'
import router from './routers'
import 'primeicons/primeicons.css'
import './style.css'
import { definePreset } from '@primevue/themes'
import axios from 'axios'
import ConfirmationService from 'primevue/confirmationservice'
import ToastService from 'primevue/toastservice'

const MyPreset = definePreset(Aura, {
  semantic: {
    primary: {
      50: '{red.50}',
      100: '{red.100}',
      200: '{red.200}',
      300: '{red.300}',
      400: '{red.400}',
      500: '{red.500}',
      600: '{red.600}',
      700: '{red.700}',
      800: '{red.800}',
      900: '{red.900}',
      950: '{red.950}',
    },
    formField: {
      borderRadius: '10px',
    },
    colorScheme: {
      light: {
        formField: {
          placeholderColor: '{gray.400}',
          focusBorderColor: '{surface.400}',
        },
      },
    },
  },
})

axios.defaults.baseURL = 'http://localhost:8000'
axios.interceptors.request.use((config) => {
  const token = localStorage.getItem('token')
  if (token) {
    if (new Date(Number(localStorage.getItem('expiration')) || '') < new Date()) {
      localStorage.removeItem('token')
      localStorage.removeItem('expiration')
      window.location.href = '/login'
    }
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

createApp(App)
  .use(router)
  .use(PrimeVue, {
    theme: {
      preset: MyPreset,
      options: {
        darkModeSelector: '.dark-mode',
      },
    },
  } as PrimeVueConfiguration)
  .use(ConfirmationService)
  .use(ToastService)
  .mount('#app')
