<template>
  <div class="text-center mt-5">
    <h1>Welcome, {{ userName }} 🎉</h1>
    <p class="text-secondary">This is a members-only area.</p>
    <button class="btn btn-danger mt-4" @click="logout">Logout</button>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const userName = ref('Guest')
const router = useRouter()

onMounted(() => {
  const userData = localStorage.getItem('user')
  if (userData) {
    try {
      const parsed = JSON.parse(userData)
      userName.value = parsed.name || 'Member'
    } catch {
      userName.value = 'Member'
    }
  }
})

const logout = () => {
  localStorage.removeItem('token')
  localStorage.removeItem('user')
  router.push('/Members')
}
</script>
