// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'

// Import views
import Welcomess from '../views/Welcome.vue'
import akash from '../views/akash.vue'
import mom from '../views/mom.vue'    
import father from '../views/father.vue'
import Arsh from '../views/Arsh.vue'

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
