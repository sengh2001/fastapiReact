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
import ForMembers from '../views/ForMembers.vue'

const routes = [
  { path: '/', component: Welcomess },
  { path: '/Home', component: Home },
  { path: '/Contact', component: Contact },
  { path: '/Projects', component: Projects },
  { path: '/About', component: About },
  { path: '/Resume', component: Resume },
  { path: '/Members', component: Member },
  { path: '/ForMembers', component: ForMembers },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  const publicPages = ['/', '/Home', '/Projects', '/Contact', '/About', '/Members', '/Resume']
  const authRequired = !publicPages.includes(to.path)
  const token = localStorage.getItem('token')

  if (authRequired && !token) {
    return next('/Members')  // Redirect to login
  }

  next()
})


export default router
