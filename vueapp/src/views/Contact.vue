<template>
  <div class="isolate bg-white px-6 py-24 sm:py-32 lg:px-8">
    <div class="absolute inset-x-0 -top-40 -z-10 transform-gpu overflow-hidden blur-3xl sm:-top-80" aria-hidden="true">
      <div class="relative left-1/2 -z-10 aspect-1155/678 w-[144.5rem] max-w-none -translate-x-1/2 rotate-[30deg] bg-gradient-to-tr from-[#ff80b5] to-[#9089fc] opacity-30 sm:left-[calc(50%-40rem)] sm:w-[288.75rem]" style="clip-path: polygon(74.1% 44.1%, 100% 61.6%, 97.5% 26.9%, 85.5% 0.1%, 80.7% 2%, 72.5% 32.5%, 60.2% 62.4%, 52.4% 68.1%, 47.5% 58.3%, 45.2% 34.5%, 27.5% 76.7%, 0.1% 64.9%, 17.9% 100%, 27.6% 76.8%, 76.1% 97.7%, 74.1% 44.1%)" />
    </div>

    <div class="mx-auto max-w-2xl text-center">
      <h2 class="text-4xl font-semibold tracking-tight text-balance text-gray-900 sm:text-5xl">Contact Me</h2>
      <p class="mt-2 text-lg/8 text-gray-600">Hey! Let’s collaborate — I’d love to hear from you.</p>
    </div>

    <form @submit.prevent="submitForm" class="mx-auto mt-16 max-w-xl sm:mt-20">
      <div class="grid grid-cols-1 gap-x-8 gap-y-6 sm:grid-cols-2">
        <div class="sm:col-span-2">
          <label for="name" class="block text-sm font-semibold text-gray-900">Name</label>
          <div class="mt-2.5">
            <input v-model="form.name" type="text" name="name" id="name" autocomplete="name"
              class="block w-full rounded-md bg-white px-3.5 py-2 text-base text-gray-900 shadow-sm outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600"
              placeholder="Your name" required />
          </div>
        </div>

        <div class="sm:col-span-2">
          <label for="email" class="block text-sm font-semibold text-gray-900">Email</label>
          <div class="mt-2.5">
            <input v-model="form.email" type="email" name="email" id="email" autocomplete="email"
              class="block w-full rounded-md bg-white px-3.5 py-2 text-base text-gray-900 shadow-sm outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600"
              placeholder="you@example.com" required />
          </div>
        </div>

        <div class="sm:col-span-2">
          <label for="message" class="block text-sm font-semibold text-gray-900">Message</label>
          <div class="mt-2.5">
            <textarea v-model="form.message" name="message" id="message" rows="4"
              class="block w-full rounded-md bg-white px-3.5 py-2 text-base text-gray-900 shadow-sm outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600"
              placeholder="Write your message here..." required />
          </div>
        </div>
      </div>

      <div class="mt-10">
        <button type="submit"
          class="block w-full rounded-md bg-indigo-600 px-3.5 py-2.5 text-center text-sm font-semibold text-white shadow-md hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">
          Send Message
        </button>
      </div>

      <div v-if="responseMsg" class="mt-6 text-center text-green-600 font-medium">
        {{ responseMsg }}
      </div>
    </form>
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
    responseMsg.value = res.data.message || 'Message sent successfully!'
    form.value = { name: '', email: '', message: '' }
  } catch (err) {
    responseMsg.value = 'Something went wrong. Please try again.'
  }
}
</script>
