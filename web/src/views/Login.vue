<template>
  <div class="login-button">
    <button @click="login">Login</button>
  </div>
</template>

<style>
.login-button {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>

<script>
export default {
  name: 'Login',
  methods: {
    // Log the user in
    login() {
      // console.log(this.$auth)
      // console.log(this.$auth.loginWithRedirect)
      this.$auth.loginWithRedirect();
    },
    // Log the user out
    logout() {
      this.$auth.logout({
        returnTo: window.location.origin
      });
    }
  }
}
</script>