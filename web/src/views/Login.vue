<template>
  <div class="login-button">
    <button @click="login">Login</button>
  </div>
  <div class="token-button">
    <button @click="doSomethingWithToken">getToken</button>
  </div>
</template>

<style>
.login-button {
  display: flex;
  align-items: center;
  justify-content: center;
}
.token-button {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>

<script>
import { useAuth0 } from '@auth0/auth0-vue';

export default {
  setup() {
    const { loginWithRedirect, getAccessTokenSilently } = useAuth0();

    return {
      login: () => {
        loginWithRedirect();
      },
      doSomethingWithToken: async () => {
        const token = await getAccessTokenSilently();
        console.log(token)
      }
    };
  }
};
</script>