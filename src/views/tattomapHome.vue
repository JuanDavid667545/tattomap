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
      
      <div class="botones-acciones">
        <button @click="irContacenos" class="contactenos-btn">Contáctenos</button>
        <button @click="irRegistro" class="registro-btn">Registrarse</button>
      </div>
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
    },
    irRegistro() {
      this.$router.push('/registro-usuario');
    },
    irContacenos() {
      this.$router.push('/Contactenos');
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
  position: relative;
}

nav ul {
  list-style-type: none;
  display: flex;
  justify-content: flex-start;
  padding: 0;
  margin-bottom: 50px;
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
  height: calc(60vh - 40px);
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
  margin-right: 10px;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #555;
}

button:focus {
  outline: none;
}

/* Estilos para los botones de acción */
.botones-acciones {
  display: flex;
  gap: 10px;
  margin-top: 20px;
  position: absolute;
  right: 20px; /* Posicionar en la parte derecha de la pantalla */
  top: 20px;
}

.contactenos-btn,
.registro-btn {
  background-color: transparent;
  color: #fff;
  border: none;
  font-size: 18px;
  cursor: pointer;
  padding: 10px 20px;
  transition: background-color 0.3s ease;
}

.contactenos-btn:hover,
.registro-btn:hover {
  background-color: #555;
}
</style>
