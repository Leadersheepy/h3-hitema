<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import NavBar from './components/NavBar.vue';
</script>

<template>
  <header>
    <div id="app">
      <NavBar />
    </div>
  </header>

  <RouterView />
</template>
