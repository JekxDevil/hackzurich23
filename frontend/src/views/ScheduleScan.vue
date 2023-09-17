<template>
  <div class="">
    <div class="w-100 d-flex flex-row justify-space-between align-center">
      <h1 class="">Scheduled jobs</h1>
      <v-btn class="" color="primary">
        New Job
        <NewScheduleScan @job-created="fetchJobs" />
      </v-btn>
    </div>
    <v-data-table
      :headers="headers"
      :items="jobs"
      :loading="loading"
      class="mt-6"
    >
      <template v-slot:item.actions="{ item }">
        <v-btn icon @click="deleteJob(item)" color="red" variant="text">
          <v-icon>mdi-delete</v-icon>
        </v-btn>
      </template>
    </v-data-table>
  </div>
</template>

<script>
import NewScheduleScan from "@/components/NewScheduleScan";

export default {
  name: "ScheduleScan",
  components: {
    NewScheduleScan,
  },
  data() {
    return {
      jobs: [],
      loading: false,
    };
  },
  async mounted() {
    await this.fetchJobs();
  },
  computed: {
    headers() {
      return [
        { title: "Name", key: "name", align: "start" },
        { title: "Cron", key: "cron", align: "start" },
        { title: "Actions", key: "actions", align: "start", width: "100px" },
      ];
    },
  },
  methods: {
    async fetchJobs() {
      this.loading = true;
      this.jobs = await window.jobs?.get();
      this.loading = false;
    },
    async deleteJob(job) {
      this.loading = true;
      await window.jobs.delete(job);
      this.jobs = await window.jobs.get();
      this.loading = false;
    },
  },
};
</script>

<style scoped>
:deep(.v-data-table__td) {
  text-align: start !important;
}
</style>
