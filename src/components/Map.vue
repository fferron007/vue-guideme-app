<template>
  <div id="map" style="height: 100%; width: 100%"></div>
</template>

<script>
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';

export default {
  props: ['merchants'],
  mounted() {
    this.map = L.map('map').setView([0, 0], 2);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(this.map);
    this.updateMarkers();
  },
  watch: {
    merchants: 'updateMarkers',
  },
  methods: {
    updateMarkers() {
      if (!this.map) return;
      this.map.eachLayer((layer) => {
        if (layer instanceof L.Marker) {
          this.map.removeLayer(layer);
        }
      });
      this.merchants.forEach((merchant) => {
        L.marker([merchant.lat, merchant.lng]).addTo(this.map).bindPopup(merchant.name);
      });
    },
  },
};
</script>