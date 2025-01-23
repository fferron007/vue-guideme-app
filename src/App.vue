<template>
  <div id="app" style="display: flex; flex-direction: column; height: 100vh">
    <!-- Filters on top in one line -->
    <div style="display: flex; padding: 1rem; gap: 1rem; background-color: #f8f8f8;">
      <Filters :filters="filters" @updateFilters="updateFilters" />
    </div>
    <!-- Main content: Merchant list on the left and map on the right -->
    <div style="display: flex; flex: 1;">
      <div style="width: 30%; padding: 1rem; overflow-y: auto;">
        <MerchantList :merchants="merchants" />
      </div>
      <div style="width: 70%; height: 100%;">
        <Map :merchants="merchants" />
      </div>
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
      axios.get('http://127.0.0.1:81/api/filters').then((response) => {
        this.filters = response.data;
      });
    },
    fetchMerchants() {
      axios
        .get('http://127.0.0.1:81/api/merchants', { params: this.selectedFilters })
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
