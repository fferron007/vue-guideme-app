<template>
    <div>
      <div v-for="(options, key) in filters" :key="key">
        <label :for="key">{{ key }}</label>
        <select :id="key" @change="(e) => updateFilter(key, e.target.value)">
          <option value="">Select {{ key }}</option>
          <option v-for="option in options" :key="option" :value="option">
            {{ option }}
          </option>
        </select>
      </div>
    </div>
  </template>

<script>
export default {
  props: ['filters'],
  emits: ['updateFilters'],
  data() {
    return {
      selectedFilters: {},
    };
  },
  methods: {
    updateFilter(key, value) {
      this.selectedFilters[key] = value;
      this.$emit('updateFilters', { ...this.selectedFilters });
    },
  },
};
</script>