<template>
  <div class="container d-flex flex-column justify-content-center align-items-center vh-100 bg-light text-center rounded shadow-sm">
    <div class="p-4 bg-white rounded-4 shadow-lg" style="min-width: 350px;">
      <h2 class="mb-4 text-primary fw-semibold">Welcome to the Members Page</h2>

      <div id="g_id_onload"
           data-client_id="753616388428-uecnbrgu3kgqqgvosjh28kq9ao9bfnm7.apps.googleusercontent.com"
           data-context="signin"
           data-ux_mode="popup"
           data-callback="handleCredentialResponse"
           data-auto_prompt="false">
      </div>

      <div class="g_id_signin"
           data-type="standard"
           data-shape="pill"
           data-theme="outline"
           data-text="sign_in_with"
           data-size="large">
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'
import api from '@/lib/axios'  // Adjust if needed

const router = useRouter()

onMounted(() => {
  const script = document.createElement('script')
  script.src = 'https://accounts.google.com/gsi/client'
  script.async = true
  script.defer = true
  document.head.appendChild(script)

  window.handleCredentialResponse = async (response) => {
    try {
      const { data } = await api.post('/auth/google', { token: response.credential })

      // Save JWT
      localStorage.setItem('token', data.access_token)

      // ✅ Store the user info (e.g., name, email, etc.)
      localStorage.setItem('user', JSON.stringify(data.user))

      // 🔁 Redirect to /ForMembers
      router.push('/ForMembers')
    } catch (err) {
      console.error('Login error:', err)
      alert('Login failed.')
    }
  }
})
</script>