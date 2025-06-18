// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'

// Import views
import Welcomess from '../views/Resume.vue'
import akash from '../views/Home.vue'
import mom from '../views/Contact.vue'    
import father from '../views/Projects.vue'
import Arsh from '../views/About.vue'

const routes = [
  { path: '/', component: Welcomess },
  { path: '/arsh', component: Arsh },
  { path: '/akash', component: akash },
  { path: '/mom', component: mom },
  { path: '/father', component: father },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
