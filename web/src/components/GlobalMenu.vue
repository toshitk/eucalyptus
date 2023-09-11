<template>
  <div>
    <!-- <v-toolbar dark prominent image="https://cdn.vuetifyjs.com/images/backgrounds/vbanner.jpg"> -->
    <v-toolbar>
      <v-app-bar-nav-icon @click="$emit('toggle-drawer')"></v-app-bar-nav-icon>

      <v-toolbar-title>Global Menu</v-toolbar-title>

      <v-spacer></v-spacer>
    </v-toolbar>
  </div>
</template>
