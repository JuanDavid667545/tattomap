<!-- components/TattooMapHome.vue -->
<template>
<div class="tattoo-map-home">
    <!-- Navegación -->
<nav class="nav-container">
<div class="nav-content">
    <ul>
      <li 
         v-for="item in menuItems" 
          :key="item.name"
          :class="{ active: seleccion === item.route }"
          @click="handleNavigation(item)"
          class="nav-item"
          >
            {{ item.name }}
      </li>
    </ul>
</div>
</nav>

<!-- Carrusel con transiciones -->
<div class="carrusel">
      <transition-group name="fade">
        <img 
          v-for="(imagen, index) in imagenes" 
          :key="imagen"
          v-show="indiceActual === index"
          :src="require(`@/assets/${imagen}`)" 
          :alt="`Imagen carrusel ${index + 1}`"
          class="carrusel-imagen"
        >
</transition-group>
<!-- Overlay gradiente -->
      <div class="carrusel-overlay"></div>
    </div>

<!-- Contenido principal -->
<main class="main-content">
<div class="content-wrapper">
      <h1 class="animate-title">¿Quieres un tatuaje?</h1>
      <p class="animate-text">TE FACILITAMOS ENCONTRANDOLO, CON QUIÉN Y DONDE</p>
          <button 
          @click="comenzarBusqueda"
          class="main-button">
          EMPEZAR
        </button>

</div>
      
<!-- Elementos decorativos -->
      <div class="decorative-circle circle-1"></div>
      <div class="decorative-circle circle-2"></div>
    </main>
  </div>
</template>

<script>





export default {

  name: 'TattomapHome',
  data() {
    return {
      seleccion: '',
      imagenes: [
        'carrusel1.jpg',
        'carrusel2.jpg'
      ],
      indiceActual: 0,
      intervalId: null,
      menuItems: [
        { name: 'TATUADORES', route: 'tatuadores' },
        { name: 'TATUAJES', route: 'tatuajes' },
        { name: '¿TATÚAS?', route: 'tatuas' },
        { name: 'CONTÁCTENOS', route: 'contactenos' },
        { name: 'REGISTRARSE', route: 'registro' }
      ]
    };
  },


  mounted() {
    // Agregar clase al body solo cuando este componente está montado
    document.body.classList.add('tattoo-home-page');
    this.iniciarCarrusel();
    this.iniciarAnimaciones();
  },


  beforeUnmount() {
    // Remover clase del body cuando el componente se desmonta
    document.body.classList.remove('tattoo-home-page');
    this.detenerCarrusel();
  },


  methods: {
    handleNavigation(item) {
      this.seleccion = item.route;
      if (item.route === 'tatuas') {
        this.$router.push('/registro');
      } else if (item.route === 'registro') {
        this.$router.push('/registro-usuario');
      } else if (item.route === 'contactenos') {
        this.$router.push('/Contactenos');
      } else {
        console.log(`Navegando a: ${item.route}`);
      }
    },

    comenzarBusqueda() {
      console.log('Iniciando la búsqueda de tatuajes desde la página de inicio');
    },


    iniciarCarrusel() {
      this.intervalId = setInterval(() => {
        this.indiceActual = (this.indiceActual + 1) % this.imagenes.length;
      }, 5000);
    },


    detenerCarrusel() {
      if (this.intervalId) {
        clearInterval(this.intervalId);
      }
    },

    
    iniciarAnimaciones() {
      // Las animaciones se manejan con CSS
    }
  }
};
</script>


<style>
@import '../styles/home.css';
</style>



