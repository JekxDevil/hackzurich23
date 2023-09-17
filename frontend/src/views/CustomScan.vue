<template>
  <div>
    <div class="d-flex flex-column justify-content-center align-items-center">
      <div class="d-flex flex-column align-center">
        <v-img :src="require('@/assets/spider.png')" alt="hi" width="160" height="160"/>
        <h1 class="my-8">One-gO</h1>
        <p class="">
          Please specify the Directory you would like to scan
        </p>

        <div class="d-flex flex-column align-center mt-8">
          <v-text-field
            v-model="directory"
            label="Directory"
            outlined
            dense
            class="w-100"
          />

        </div>

      </div>
      <div class="d-flex flex-column align-center mt-8">
        <ScanButton />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CustomScan"
};
</script>

<style scoped>

</style>