<template>
  <div class="app-container">
    <div class="gradient-background"></div>
    <ChatPopup />
  </div>
</template>

<script setup>
import ChatPopup from './components/ChatPopup.vue'
</script>

<style>
.app-container {
  height: 100vh;
  position: relative;
}

.gradient-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #ff69b4, #8a2be2);
  z-index: -1;
}
</style>

