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
    async startScan() {

      await window.scan.start(this.directory);
    },
  },
};
</script>

<style scoped></style>
