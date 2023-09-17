<template>
  <v-toolbar color="primary">
    <div class="ps-6">
      <v-img
        :src="require('@/assets/logo.png')"
        alt="logo"
        width="40"
        height="40px"
      />
    </div>
    <v-toolbar-title class="ps-2 float-start">
      <template #text>
        <div class="text-start">One-gO</div>
      </template></v-toolbar-title
    >

    <v-spacer></v-spacer>

    <template v-slot:extension>
      <v-tabs v-model="tab" align-tabs="title">
        <v-tab
          v-for="item in items"
          :key="item.name"
          :value="item.name"
          :to="item.path"
        >
          {{ item.name }}
        </v-tab>
      </v-tabs>
    </template>
  </v-toolbar>

  <v-window v-model="tab">
    <v-window-item v-for="item in items" :key="item" :value="item">
    </v-window-item>
  </v-window>
</template>

<script>
export default {
  name: "NavBar",
  data() {
    return {
      tab: null,
      items: [
        { name: "Simple Scan", path: "/" },
        { name: "Custom Scan", path: "/custom-scan" },
        { name: "Schedule", path: "/schedule" },
      ],
    };
  },
};
</script>

<style scoped></style>
