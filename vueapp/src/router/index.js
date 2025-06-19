// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'

// Import views
import Welcomess from '../views/Resume.vue'
import Home from '../views/Home.vue'
import Contact from '../views/Contact.vue'    
import Projects from '../views/Projects.vue'
import About from '../views/About.vue'
import Resume from '../views/Resume.vue'
import Member from '../views/MemberSL.vue'


const routes = [
  { path: '/', component: Welcomess },
  { path: '/Home', component: Home },
  { path: '/Contact', component: Contact },
  { path: '/Projects', component: Projects },
  { path: '/About', component: About },
  { path: '/Resume', component: Resume },
  { path: '/Members', component: Member },
  
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})


export default router
