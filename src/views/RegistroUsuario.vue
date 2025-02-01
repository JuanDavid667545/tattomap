<template>
  <div class="registro-container">
  <div class="registro-form">
  <h2>Registro de Usuario</h2>

<!--FORMULARIO-->

<form @submit.prevent="registrarUsuario">
    <div class="form-group">
      <label for="nombre">Nombre</label>
          <input
            type="text"
            id="nombre"
            v-model="usuario.nombre"
            required
            placeholder="Ingresa tu nombre"
          />
    </div>

    <div class="form-group">
      <label for="email">Correo Electrónico</label>
          <input
            type="email"
            id="email"
            v-model="usuario.email"
            required
            placeholder="Ingresa tu correo"
          />
    </div>

    <div class="form-group">
      <label for="password">Contraseña</label>
          <div class="input-wrapper">
            <input
              type="Password"
              id="password"
              v-model="usuario.password"
              required
              placeholder="Ingresa tu contraseña"
            />

          </div>
    </div>


<!-- BOTONES -->

        <button type="submit" class="submit-btn">Registrarse</button>
        <button @click="volver" type="button" class="volver-btn">Volver</button>


      </form>
    </div>
  </div>
</template>

<script>





export default {
  name: "RegistroUsuario",
  data() {
    return {
      usuario: {
        nombre: "",
        email: "",
        password: "",
      },
      showPassword: false
    };
  },
  methods: {
    registrarUsuario() {
      console.log("Datos del usuario:", this.usuario);
    },
    volver() {
      this.$router.push("/");
    },
    togglePasswordVisibility() {
      this.showPassword = !this.showPassword
    }
  },
};
</script>

<style>
@import '../styles/registrouser.css';
</style>

