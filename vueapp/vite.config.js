import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    fs: {
      // Allow serving files from node_modules
      allow: ['..'] // This allows accessing files one level up from project root
    }
  },
  resolve: {
    alias: {
      // Optional: Create an alias for easier imports
      '~bootstrap-icons': '/node_modules/bootstrap-icons'
    }
  }
})