<!-- src/App.vue -->
<template>
  <div>
    <!-- Add a simple navbar -->
    <nav class="p-4 bg-indigo-600 text-white flex gap-4">
      <router-link to="/">Home</router-link>
      <router-link to="/todo">Todo</router-link>
      <router-link to="/arsh">Arsh</router-link>
      <router-link to="/akash">Akash</router-link>
      <router-link to="/mom">Mom</router-link>
      <router-link to="/father">Dad</router-link>
    </nav>

    <!-- This is where pages load -->
    <router-view />
  </div>
</template>

<script setup>
// No need to import anything here
</script>
