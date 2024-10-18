<template>
  <div class="Registro">
    <h1>Registro</h1>
    <p>¡Rellena nuestro formulario!</p>

    <form @submit.prevent="enviarFormulario">

      <div class="campo">
        <label for="nombre">Nombre</label>
        <input type="text" id="nombre" v-model="nombre" placeholder="Añade tu nombre">
      </div>

      <div class="campo">
        <label for="telefono">Teléfono</label>
        <div class="telefono-input">
          <input type="text" value="+57" disabled>
          <input type="tel" id="telefono" v-model="telefono" placeholder="Número de teléfono">
        </div>
      </div>

      <div class="campo">
        <label for="email">Email</label>
        <input type="email" id="email" v-model="email" placeholder="Añade tu email">
      </div>

      <div class="campo">
        <label for="Contraseña">Contraseña</label>
        <input type="text" id="contraseña" v-model="Contraseña" placeholder="Ingresa tu contraseña">
      </div>

      <div class="campo">
        <label for="instagram">Perfil de Instagram</label>
        <input type="text" id="instagram" v-model="instagram" placeholder="Añade tu perfil">
      </div>

      <div class="campo">
        <label for="ciudad">Ciudad</label>
        <select id="ciudad" v-model="ciudad">
          <option value="" disabled selected>Selecciona tu ciudad</option>
          <option v-for="ciudad in ciudades" :key="ciudad" :value="ciudad">{{ ciudad }}</option>
        </select>
      </div>

      <button type="submit">ENVIAR</button>
    </form>

    <!-- Botón Volver -->
    <button class="boton-volver" @click="volverAlInicio">Volver</button>
  </div>
</template>

<script>
export default {
  name: 'tattoRegister',
  data() {
    return {
      nombre: '',
      telefono: '',
      email: '',
      instagram: '',
      ciudad: '',
      ciudades: ['Villavicencio'] // Añade más ciudades según necesites
    };
  },
  methods: {
    enviarFormulario() {
      // Aquí puedes añadir la lógica para enviar el formulario
      console.log('Formulario enviado', {
        nombre: this.nombre,
        telefono: this.telefono,
        email: this.email,
        instagram: this.instagram,
        ciudad: this.ciudad
      });
      // Implementa la lógica de envío real aquí
    },
    volverAlInicio() {
      this.$router.push('/'); // Redirección a la página de inicio
    }
  }
}
</script>

<style scoped>
.Registro {
  background-color: #000;
  color: #fff;
  font-family: Arial, sans-serif;
  padding: 20px;
  max-width: 400px;
  margin: 50px auto; /* Centra el componente verticalmente */
  text-align: center; /* Centra el contenido */
}

h1 {
  font-size: 24px;
  margin-bottom: 10px;
}

p {
  font-size: 14px;
  margin-bottom: 20px;
}

.campo {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input[type="text"],
input[type="tel"],
input[type="email"],
select {
  width: 100%;
  padding: 8px;
  background-color: #333;
  border: none;
  color: #fff;
}

.telefono-input {
  display: flex;
}

.telefono-input input[type="text"] {
  width: 50px;
  margin-right: 5px;
}

.telefono-input input[type="tel"] {
  flex-grow: 1;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #0056b3;
  color: #fff;
  border: none;
  cursor: pointer;
  margin-top: 10px; /* Añadir espacio entre botones */
}

button:hover {
  background-color: #003d82;
}

.boton-volver {
  background-color: #777; /* Color diferente para el botón Volver */
}

.boton-volver:hover {
  background-color: #555;
}
</style>
