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
          <v-form v-model="validForm" @submit.prevent="submit" class="w-100">
            <v-text-field
              v-model="dir"
              label="Directory"
              variant="outlined"
              :rules="[validateDirectory]"
            ></v-text-field>
            <div class="d-flex flex-column align-center">
              <ScanButton />
            </div>
          </v-form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ScanButton from "@/components/ScanButton.vue";

export default {
  name: "CustomScan",
  components: { ScanButton },
  data() {
    return {
      dir: null,
      validForm: true,
    };
  },
  methods: {
    validateDirectory(value) {
      console.log(value);
      return true;
    },
    submit() {
      if (!this.validForm) return;
      alert("Submitted");
    },
  },
};
</script>

<style scoped></style>
