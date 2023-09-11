<template>
  <div id="app">
    <GlobalMenu @toggle-drawer="toggleDrawer" />
    <ExpandMenu :drawer="drawer" @update:drawer="drawer = $event" />
  </div>
</template>

<script lang="ts">
import ExpandMenu from "./ExpandMenu.vue";
import GlobalMenu from "./GlobalMenu.vue";

export default {
  components: {
    ExpandMenu,
    GlobalMenu
  },
  data() {
    return {
      drawer: true,
    };
  },
  methods: {
    toggleDrawer() {
      this.drawer = !this.drawer;
    }
  }
}
</script>
