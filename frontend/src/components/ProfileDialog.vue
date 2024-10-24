<template>
  <Dialog
    header="Thông tin cá nhân"
    v-model:visible="visible"
    modal
    dismissable-mask
    style="width: 400px"
  >
    <ConfirmDialog></ConfirmDialog>
    <form class="profile_form">
      <div>
        <div class="form_item__label">Họ tên</div>
        <InputText v-model="user.full_name" placeholder="Họ tên" :autofocus="true" fluid />
      </div>
      <div>
        <div class="form_item__label">Email</div>
        <InputText v-model="user.email" type="email" placeholder="Email" fluid />
      </div>
      <div>
        <div class="form_item__label">Mật khẩu</div>
        <Password
          v-model="user.password"
          placeholder="Mật khẩu mới"
          :feedback="false"
          toggle-mask
          fluid
        />
      </div>
      <div class="form__actions">
        <Button type="button" label="Hủy" severity="secondary" @click="visible = false"></Button>
        <Button
          type="button"
          label="Xóa tài khoản"
          severity="secondary"
          @click="handleDeleteAccount"
        ></Button>
        <Button label="Lưu" @click="updateProfile"></Button>
      </div>
    </form>
  </Dialog>
</template>

<script setup lang="ts">
import ConfirmDialog from 'primevue/confirmdialog'
import Dialog from 'primevue/dialog'
import { useConfirm } from 'primevue/useconfirm'
import { useRouter } from 'vue-router'
import { deleteAccount } from '../services/auth-service'
import { ref, watch } from 'vue'
import { UpdatedUser } from '../models/user'
import { getUserInfo, updateUserInfo } from '../services/user-service'

const visible = defineModel()
const confirm = useConfirm()
const router = useRouter()
const user = ref<UpdatedUser>({
  full_name: '',
  email: '',
  password: '',
})

const updateProfile = async () => {
  await updateUserInfo(user.value)
  visible.value = false
}

const handleDeleteAccount = () => {
  confirm.require({
    message: 'Bạn có chắc chắn muốn xóa tài khoản?',
    header: 'Xác nhận',
    rejectProps: {
      label: 'Hủy',
      severity: 'secondary',
      outlined: true,
    },
    acceptProps: {
      label: 'Xóa',
    },
    accept: async () => {
      await deleteAccount()
      router.push('/login')
    },
  })
}


watch(visible, async (value) => {
  if (value) {
    user.value = await getUserInfo()
  }
})
</script>

<style lang="scss" scoped>
.profile_form {
  display: flex;
  flex-direction: column;
  gap: 15px;

  .form_item__label {
    margin-bottom: 5px;
  }

  .form__actions {
    margin-top: 20px;
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: flex-end;
  }
}
</style>
