<template>
  <div>
    <div class="d-flex flex-column justify-content-center align-items-center">
      <div class="d-flex flex-column align-center">
        <v-img :src="require('@/assets/spider.png')" alt="hi" width="160" height="160"/>
        <h1 class="my-8">One-gO</h1>
        <p class="">
          Experience both safety and freedom in an instant with one-go
        </p>
      </div>
        <div class="d-flex flex-column align-center mt-8">
          <ScanButton />
        </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

import ScanButton from "@/components/ScanButton.vue";

export default {
  name: "HomeView",
  components: { ScanButton }
};
</script>
