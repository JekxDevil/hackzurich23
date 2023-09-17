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
      default: null,
    },
  },
  methods: {
    async startScan() {
      const res = await window.scan.start(this.directory);
      console.log(res);
    },
  },
};
</script>

<style scoped></style>
