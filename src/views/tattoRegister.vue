<template>


<div class="registro-container">
<div class="registro-form">
    <h2>Registro de Tatuador</h2>

<!--formulario-->

<form @submit.prevent="registrarTatuador">
    <div class="form-group">
          <label for="nombre">Nombre</label>
          <input
            type="text"
            id="nombre"
            v-model="tatuador.nombre"
            required
            placeholder="Ingresa tu nombre"
          />
    </div>


    <div class="form-group">
          <label for="telefono">Teléfono</label>
          <div class="telefono-input">
            <input type="text" value="+57" disabled />
            <input
              type="tel"
              id="telefono"
              v-model="tatuador.telefono"
              placeholder="Número de teléfono (opcional)"
            />
          </div>
    </div>


    <div class="form-group">
          <label for="email">Correo Electrónico</label>
          <input
            type="email"
            id="email"
            v-model="tatuador.email"
            required
            placeholder="Ingresa tu correo"
          />
    </div>


    <div class="form-group">
          <label for="instgram">Instgram</label>
          <div class="instagram-input">
            <input
              type="instagram"
              id="instagramuser"
              v-model="tatuador.instagram"
              required
              placeholder="Usuario de intagram"
            />
          </div>
    </div>


    <div class="form-group">
          <label for="password">Contraseña</label>
          <input
            type="password"
            id="password"
            v-model="tatuador.password"
            required
            placeholder="Ingresa tu contraseña"
          />
    </div>


    <div class="form-group">
          <label for="ciudad">Ciudad</label>
          <select id="ciudad" v-model="tatuador.ciudad" required>
            <option value="" disabled selected>Selecciona tu ciudad</option>
            <option v-for="ciudad in ciudades" :key="ciudad" :value="ciudad">
              {{ ciudad }}
            </option>
          </select>
    </div>

<!-- BOTONES-->

        <button type="submit" class="submit-btn">Registrarse</button>
        <button @click="volver" type="button" class="volver-btn">Volver</button>
      </form>
    </div>
  </div>
</template>

<script>


export default {
  name: "RegistroTatuador",
  data() {
    return {
      tatuador: {
        nombre: "",
        telefono: "",
        email: "",
        password: "",
        ciudad: "",
      },
      ciudades: ["Villavicencio"], // Agrega más ciudades según sea necesario
    };
  },
  methods: {
    registrarTatuador() {
      console.log("Datos del tatuador:", this.tatuador);
    },
    volver() {
      this.$router.push("/");
    },
  },
};
</script>

<style>
@import '../styles/tattoregister.css';

</style>



