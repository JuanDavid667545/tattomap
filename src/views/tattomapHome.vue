<template>
  <div class="tattoo-map-home">
    <nav>
      <ul>
        <li :class="{ active: seleccion === 'tatuadores' }" @click="seleccionar('tatuadores')">TATUADORES</li>
        <li :class="{ active: seleccion === 'tatuajes' }" @click="seleccionar('tatuajes')">TATUAJES</li>
        <li :class="{ active: seleccion === '¿TATÚAS?' }" @click="seleccionar('¿TATÚAS?')">¿TATÚAS?</li>
      </ul>
    </nav>
    <main>
      <h1>¿Quieres un tatuaje?</h1>
      <p>TE FACILITAMOS ENCONTRANDOLO, CON QUIÉN Y DONDE</p>
      <button @click="comenzarBusqueda">EMPEZAR</button>
    </main>
  </div>
</template>

<script>
export default {
  name: 'tattomapHome',
  data() {
    return {
      seleccion: ''
    };
  },
  methods: {
    seleccionar(opcion) {
      console.log('Opción seleccionada:', opcion);
      this.seleccion = opcion;
      if (opcion === '¿TATÚAS?') {
        this.$router.push('/registro');
      } else {
        console.log(`Seleccionaste: ${opcion}`);
      }
    },
    comenzarBusqueda() {
      console.log('Iniciando la búsqueda de tatuajes desde la página de inicio');
    }
  }
};
</script>

<style scoped>
.tattoo-map-home {
  background-color: #000;
  color: #fff;
  font-family: Arial, sans-serif;
  height: 100vh;
  padding: 20px;
}

nav ul {
  list-style-type: none;
  display: flex;
  justify-content: flex-start;
  padding: 0;
  margin-bottom: 50px; /* Aumenta la separación entre el menú y el contenido */
}

nav ul li {
  margin-right: 20px;
  cursor: pointer;
  padding: 10px;
  transition: background-color 0.3s ease;
}

nav ul li.active {
  background-color: #555;
  border-radius: 5px;
}

main {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: calc(60vh - 40px); /* Deja espacio para el menú */
  text-align: center;
}

h1 {
  font-size: 68px;
  margin-bottom: 20px;
}

p {
  font-size: 20px;
  margin-bottom: 20px;
}

button {
  background-color: #333;
  color: #fff;
  border: none;
  padding: 10px 20px;
  font-size: 18px;
  cursor: pointer;
  margin-top: 20px;
}

button:hover {
  background-color: #555;
}
</style>
