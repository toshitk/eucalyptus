<template>
  <div id="app">
    <!-- <GlobalMenu @toggle-drawer="toggleDrawer" /> -->
    <!-- <ExpandMenu :drawer="drawer" @update:drawer="drawer = $event" /> -->
    <router-view/>
    <!-- <Login /> -->
    <!-- <LineChart /> -->
  </div>
</template>

<script lang="ts">
import ExpandMenu from "./components/ExpandMenu.vue";
import GlobalMenu from "./components/GlobalMenu.vue";
import LineChart from "./components/LineChart.vue";
import Login from "./views/Login.vue";

export default {
  components: {
    ExpandMenu,
    GlobalMenu,
    LineChart,
    Login,
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
