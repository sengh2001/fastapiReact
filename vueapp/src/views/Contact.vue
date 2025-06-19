<template>
  <div class="container py-5" style="max-width: 600px;">
    <h2 class="mb-4 text-center">Hey ! , Let's Collaborate...</h2>
    <h4 class="mb-4 text-center">Contact Me</h4>
    <form @submit.prevent="submitForm">
      <div class="form-floating mb-3">
        <input v-model="form.name" type="text" class="form-control" id="name" placeholder="Your Name" required />
        <label for="name">Name</label>
      </div>
      <div class="form-floating mb-3">
        <input v-model="form.email" type="email" class="form-control" id="email" placeholder="name@example.com" required />
        <label for="email">Email</label>
      </div>
      <div class="form-floating mb-3">
        <textarea v-model="form.message" class="form-control" placeholder="Your message here..." id="message" style="height: 120px;" required></textarea>
        <label for="message">Message</label>
      </div>
      <div class="d-grid">
        <button class="btn btn-dark" type="submit">Send</button>
      </div>
    </form>
    <div v-if="responseMsg" class="alert alert-success mt-4 text-center">{{ responseMsg }}</div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import api from '@/lib/axios'

const form = ref({
  name: '',
  email: '',
  message: ''
})

const responseMsg = ref('')

const submitForm = async () => {
  try {
    const res = await api.post('/contact', form.value)
    responseMsg.value = res.data.message
    form.value = { name: '', email: '', message: '' }
  } catch (err) {
    responseMsg.value = 'Something went wrong.'
  }
}
</script>
