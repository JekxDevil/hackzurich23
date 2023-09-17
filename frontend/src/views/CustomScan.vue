<template>
  <div>
    <div class="d-flex flex-column justify-content-center align-items-center">
      <div class="d-flex flex-column align-center">
        <v-img
          :src="require('@/assets/spider.png')"
          alt="hi"
          width="160"
          height="160"
        />
        <h1 class="my-8">One-gO</h1>
        <p class="">Please specify the Directory you would like to scan</p>
        <div class="d-flex w-100 justify-center my-6">
          <v-col cols="12" sm="6" md="4">
            <v-text-field
              label="Directory"
              variant="outlined"
            ></v-text-field>
          </v-col>
        </div>
      </div>
      <div class="d-flex flex-column align-center">
        <ScanButton />
      </div>
    </div>
  </div>
</template>

<script>
import ScanButton from "@/components/ScanButton.vue";

export default {
  name: "CustomScan",
  components: { ScanButton }
};
</script>

<style scoped></style>
