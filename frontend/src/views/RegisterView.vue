<template>
  <form class="login__form">
    <div class="form__heading">
      <Image
        src="https://slinkid.ptit.edu.vn/auth/resources/p64ct/login/ptit/dist/img/logo.png"
        alt="Image"
        height="100"
      />
      <h2>Chatbot PTIT</h2>
    </div>
    <InputText placeholder="Tên đăng nhập" :autofocus="true" fluid />
    <Password placeholder="Mật khẩu" fluid :feedback="false" toggle-mask />
    <Password placeholder="Nhập lại mật khẩu" fluid :feedback="false" toggle-mask />
    <div class="form__actions">
      <Button fluid>Đăng ký</Button>
      <Divider class="form__action-divider" align="center"> Đã có tài khoản? </Divider>
      <RouterLink to="/login">
        <Button outlined fluid>Đăng nhập</Button>
      </RouterLink>
    </div>
  </form>
</template>

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
