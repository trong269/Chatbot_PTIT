<template>
  <div class="profile">
    <Avatar
      icon="pi pi-user"
      size="large"
      shape="circle"
      style="margin-bottom: 10px; color: var(--p-inputtext-color)"
      @click="toggleMenu"
    />
    <Menu ref="menu" :model="items" :popup="true"></Menu>
  </div>
  <ProfileDialog v-model="profileDialog" />
</template>

<script lang="ts" setup>
import Avatar from 'primevue/avatar'
import Menu from 'primevue/menu'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import ProfileDialog from '../components/ProfileDialog.vue'

const router = useRouter()
const profileDialog = ref(false)
const items = ref([
  {
    label: 'Options',
    items: [
      {
        label: 'Cá nhân',
        icon: 'pi pi-user',
        command: () => {
          profileDialog.value = true
        },
      },
      {
        label: 'Đăng xuất',
        icon: 'pi pi-sign-out',
        command: () => {
          localStorage.removeItem('token')
          router.push('/login')
        },
      },
    ],
  },
])
const menu = ref()

const toggleMenu = (event: any) => {
  menu.value.toggle(event)
}
</script>

<style>
.profile {
  position: absolute;
  top: 20px;
  right: 20px;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}
</style>
