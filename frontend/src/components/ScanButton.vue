<template>
  <v-btn size="large" rounded type="submit" @click="startScan"
    >Start Scan</v-btn
  >
</template>

<script>
export default {
  name: "ScanButton",
  props: {
    directory: {
      type: String,
      required: false,
      default: "/",
    },
  },
  methods: {
    startScan() {
      console.log(this.directory);
    },
  },
};
</script>

<style scoped></style>
