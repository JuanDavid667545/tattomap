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

<style scoped>



/* css */

/**contenetor */
.registro-container {
  background-color: #000;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
}

.registro-form {
  background-color: #1a1a1a;
  padding: 40px;
  border-radius: 10px;
  width: 100%;
  max-width: 400px;
}

h2 {
  color: #fff;
  text-align: center;
  font-family: "Inter", sans-serif;
  margin-bottom: 30px;
  font-size: 24px;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  color: #fff;
  margin-bottom: 8px;
  font-size: 16px;
}

input,
select {
  width: 100%;
  padding: 10px;
  border: 1px solid #333;
  border-radius: 5px;
  background-color: #333;
  color: #fff;
  font-size: 16px;
}

input:focus,
select:focus {
  outline: none;
  border-color: #00e676;
}

.telefono-input {
  display: flex;
}

.telefono-input input[type="text"] {
  width: 60px;
  margin-right: 5px;
}

.submit-btn,
.volver-btn {
  width: 100%;
  padding: 12px;
  background-color: #00c853;
  color: #fff;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  margin-bottom: 15px;
}

.submit-btn:hover,
.volver-btn:hover {
  background-color: #555;
  box-shadow:
      0px 0px 10px #33ff5850,
      0px 0px 40px #33ff5850,
      0px 0px 60px #33ff5850;
}

.volver-btn {
  margin-top: 10px;
}
</style>
