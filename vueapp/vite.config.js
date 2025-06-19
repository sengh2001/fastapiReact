import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path' // ⬅️ Required to resolve absolute path

export default defineConfig({
  plugins: [vue()],
  server: {
    fs: {
      allow: ['..']
    }
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'), // ⬅️ This enables `@/` imports
      '~bootstrap-icons': '/node_modules/bootstrap-icons'
    }
  }
})
