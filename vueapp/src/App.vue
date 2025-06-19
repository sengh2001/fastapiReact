<template>
  <div class="flex flex-col min-h-screen">
    <!-- Navbar -->
    <nav class="fixed top-0 left-0 right-0 bg-[#0a0a0f]/80 backdrop-blur border-b border-cyan-100/10 shadow z-50">
      <div class="container mx-auto px-4 flex items-center justify-between h-16">
        <router-link class="text-white font-bold text-lg tracking-widest neon-text" to="/Home">
          <span class="flicker-slow">ਅਰਸ਼ਦੀਪ</span>
          <span class="flicker-fast">ਸਿੰਘ</span>
        </router-link>
        <button @click="isOpen = !isOpen" class="md:hidden text-cyan-400 focus:outline-none">
          ☰
        </button>
        <div :class="['md:flex space-x-6', isOpen ? 'block' : 'hidden']" class="hidden md:block">
          <router-link class="text-white nav-link neon-hover" to="/Home">Home</router-link>
          <router-link class="text-white nav-link neon-hover" to="/About">About</router-link>
          <router-link class="text-white nav-link neon-hover" to="/Projects">Projects</router-link>
          <router-link class="text-white nav-link neon-hover" to="/Contact">Contact</router-link>
          <router-link class="text-white nav-link neon-hover" to="/Resume">Resume</router-link>
          <router-link class="text-white nav-link neon-hover" to="/Members">Login / Signup</router-link>
        </div>
      </div>
    </nav>

    <!-- Main content -->
    <main class="flex-grow mt-16 px-4 pt-3">
      <router-view />
    </main>

    <!-- Footer -->
    <footer class="bg-gray-100 text-center text-sm py-4 mt-auto">
      <div class="flex flex-col items-center gap-2">
        <p class="text-gray-500">&copy; 2025 Arshdeep Singh. All rights reserved.</p>
        <div class="flex gap-4 text-xl text-gray-700">
          <a href="https://github.com/sengh2001" target="_blank"><i class="bi bi-github"></i></a>
          <a href="https://www.linkedin.com/in/arshdeep-singh-bhankhar/" target="_blank"><i class="bi bi-linkedin"></i></a>
          <a href="https://twitter.com/arshdeep" target="_blank"><i class="bi bi-twitter-x"></i></a>
          <a href="mailto:arsh.thapar24@gmail.com"><i class="bi bi-envelope-fill"></i></a>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref } from 'vue';
const isOpen = ref(false);
</script>

<style scoped>
/* Keep your neon animation styles here */
.flicker-slow {
  animation: flicker 3s linear infinite;
}
.flicker-fast {
  animation: flicker 1s linear infinite;
}

@keyframes flicker {
  0%, 19.999%, 22%, 62.999%, 64%, 64.999%, 70%, 100% {
    opacity: 1;
    text-shadow:
      0 0 5px #fff,
      0 0 10px #fff,
      0 0 20px #0ff,
      0 0 40px #0ff;
  }
  20%, 21.999%, 63%, 63.999%, 65%, 69.999% {
    opacity: 0.5;
    text-shadow: none;
  }
}
</style>
