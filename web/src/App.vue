<template>
  <div id="app">
    <GlobalMenu />
    <!-- <ExpandMenu /> -->
  </div>
</template>

<script lang="ts">
import ExpandMenu from "./ExpandMenu.vue";
import GlobalMenu from "./GlobalMenu.vue";

export default {
  components: {
    ExpandMenu,
    GlobalMenu
  }
}
</script>
