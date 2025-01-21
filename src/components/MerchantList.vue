<template>
    <div>
      <h2>Merchants</h2>
      <ul>
        <li v-for="merchant in merchants" :key="merchant.id">{{ merchant.name }}</li>
      </ul>
    </div>
  </template>

<script>
export default {
  props: ['merchants'],
};
</script>