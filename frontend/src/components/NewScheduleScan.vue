<template>
  <v-dialog v-model="dialog" activator="parent" width="auto">
    <v-card width="400">
      <v-card-title>New Job</v-card-title>
      <v-card-text>
        <v-form @submit.prevent="createJob" v-model="validForm">
          <v-text-field
            v-model="form.name"
            label="Name"
            required
            outlined
            dense
            :rules="[(v) => !!v || 'Name is required']"
          ></v-text-field>
          <v-text-field
            v-model="form.cron"
            label="Cron"
            required
            outlined
            dense
            :rules="[(v) => !!v || 'Cron is required', validateCron]"
          ></v-text-field>
          <v-card-actions class="d-flex flex-column w-100">
            <v-btn
              type="submit"
              color="primary"
              class="w-100"
              :disabled="loading"
              variant="flat"
              :loading="loading"
            >
              Create
            </v-btn>
            <v-btn
              @click="dialog = false"
              color="primary"
              class="w-100 mt-4"
              :disabled="loading"
            >
              Cancel
            </v-btn>
          </v-card-actions>
        </v-form>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: "ScheduleScan",
  data() {
    return {
      dialog: false,
      form: {
        name: "",
        cron: "",
      },
      validForm: false,
      loading: false,
    };
  },
  methods: {
    async createJob() {
      if (!this.validForm) return;
      this.loading = true;
      await window.jobs?.create(this.form);
      // clear form
      this.loading = false;
      this.form = {
        name: "",
        cron: "",
      };
      this.$emit("job-created");
      this.dialog = false;
    },
    async validateCron(value) {
      return await window.jobs?.validateCron(value);
    },
  },
};
</script>

<style scoped></style>
