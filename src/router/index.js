import { createRouter, createWebHistory } from 'vue-router'; 
import tattoRegister from '@/components/tattoRegister.vue';
import tattomapHome from '@/views/tattomapHome.vue';

// Definición correcta de rutas
const routes = [
  {
    path: '/',
    name: 'Home',
    component: tattomapHome,
  },
  {
    path: '/registro',
    name: 'Registro',
    component: tattoRegister,
  },
];

// Crear el enrutador
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL || '/'), // Usa process.env.BASE_URL para Vue CLI
  routes,
});

export default router;
