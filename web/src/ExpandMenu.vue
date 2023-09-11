<template>
  <!-- <v-card> -->
    <v-layout>
      <v-navigation-drawer class="header-margin" expand-on-hover rail :model-value="drawer" @update:model-value="$emit('update:drawer', $event)">
        <v-list>
          <v-list-item prepend-avatar="https://randomuser.me/api/portraits/women/85.jpg" title="Sandra Adams"
            subtitle="sandra_a88@gmailcom"></v-list-item>
        </v-list>

        <v-divider></v-divider>

        <v-list density="compact" nav>
          <v-list-item prepend-icon="mdi-folder" title="My Files" value="myfiles"></v-list-item>
          <v-list-item prepend-icon="mdi-account-multiple" title="Shared with me" value="shared"></v-list-item>
          <v-list-item prepend-icon="mdi-star" title="Starred" value="starred"></v-list-item>
        </v-list>
      </v-navigation-drawer>

      <v-main></v-main>
    </v-layout>
  <!-- </v-card> -->
</template>

<script lang="ts">
export default {
  props: {
    drawer: {
      type: Boolean,
      required: true
    },
  },
};
</script>

<style>
.header-margin {
  margin-top: 64px;
}
</style>
