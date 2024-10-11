<template>
  <Card class="auth-ctn">
    <template #content>
      <RouterView />
    </template>
  </Card>
</template>

<style scoped>
.auth-ctn {
  max-width: 400px;
  margin: 0 auto;
  margin-top: 100px;
  padding: 15px;
  border-radius: 20px;
  box-shadow: none;
}
</style>
