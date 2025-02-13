import { createRouter, createWebHistory } from 'vue-router'; 
import tattoRegister from '@/views/tattoRegister.vue';
import tattomapHome from '@/views/tattomapHome.vue';
import RegistroUsuario from '@/views/RegistroUsuario.vue';
import contactenos from '@/views/PaginaContactenos.vue';
import RepositorioTatu from '@/views/RepositorioTatu.vue';
// Definición correcta de rutas
const routes = [
  {
    path: '/',
    name: 'Home',
    component: tattomapHome,
    meta: { hideSidebar: true }
    
  },
  {
    path: '/registro',
    name: 'Registro',
    component: tattoRegister,
  },
  {
    path: '/registro-usuario',
    name: 'RegistroUsuario',
    component: RegistroUsuario
  },
  {
    path: '/Contactenos',
    name: 'contactenos',
    component: contactenos
  },

  {
    path: '/RepositorioTatu',
    name: 'repositorioTatu',
    component: RepositorioTatu
  }



 


];


// Crear el enrutador
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL || '/'), // Usa process.env.BASE_URL para Vue CLI
  routes,
});

export default router;
