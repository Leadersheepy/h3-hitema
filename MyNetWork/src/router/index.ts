import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import CreationView from '@/views/CreationView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/identification',
      name: 'identification',
      component: LoginView
    },
    {
      path: '/creation',
      name: 'creation',
      component: CreationView
    }
  ]
})

export default router
