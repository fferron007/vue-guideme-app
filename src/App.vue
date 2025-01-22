<template>
  <div id="app" style="display: flex; height: 100vh">
    <div style="width: 30%; padding: 1rem">
      <Filters :filters="filters" @updateFilters="updateFilters" />
      <MerchantList :merchants="merchants" />
    </div>
    <div style="width: 70%">
      <Map :merchants="merchants" />
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Filters from './components/Filters.vue';
import MerchantList from './components/MerchantList.vue';
import Map from './components/Map.vue';

export default {
  components: { Filters, MerchantList, Map },
  data() {
    return {
      filters: {},
      merchants: [],
      selectedFilters: {},
    };
  },
  methods: {
    fetchFilters() {
      axios.get('http://127.0.0.1:81/api/filters/').then((response) => {
        this.filters = response.data;
      });
    },
    fetchMerchants() {
      axios
        .get('http://127.0.0.1:81/api/merchants/', { params: this.selectedFilters })
        .then((response) => {
          this.merchants = response.data;
        });
    },
    updateFilters(filters) {
      this.selectedFilters = filters;
      this.fetchMerchants();
    },
  },
  mounted() {
    this.fetchFilters();
    this.fetchMerchants();
  },
};
</script>

<style>
</style>
