<template>
    <div class="registro-container">
      <div class="registro-form">
        <h2>Registro de Usuario</h2>
        <form @submit.prevent="registrarUsuario">
          <div class="form-group">
            <label for="nombre">Nombre</label>
            <input 
              type="text" 
              id="nombre" 
              v-model="usuario.nombre" 
              required
              placeholder="Ingresa tu nombre"
            >
          </div>
          
          <div class="form-group">
            <label for="email">Correo Electrónico</label>
            <input 
              type="email" 
              id="email" 
              v-model="usuario.email" 
              required
              placeholder="Ingresa tu correo"
            >
          </div>
          
          <div class="form-group">
            <label for="password">Contraseña</label>
            <input 
              type="password" 
              id="password" 
              v-model="usuario.password" 
              required
              placeholder="Ingresa tu contraseña"
            >
          </div>
          
          <button type="submit" class="submit-btn">Registrarse</button>
          <button @click="volver" type="button" class="volver-btn">Volver</button>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'RegistroUsuario',
    data() {
      return {
        usuario: {
          nombre: '',
          email: '',
          password: ''
        }
      }
    },
    methods: {
      registrarUsuario() {
        console.log('Datos del usuario:', this.usuario);
        // Aquí puedes agregar la lógica para enviar los datos al backend
      },
      volver() {
        this.$router.push('/'); // Redirige a la página de inicio o a donde desees
      }
    }
  }
  </script>
  
  <style scoped>
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
  
  input {
    width: 100%;
    padding: 10px;
    border: 1px solid #333;
    border-radius: 5px;
    background-color: #333;
    color: #fff;
    font-size: 16px;
  }
  
  input:focus {
    outline: none;
    border-color: #555;
  }
  
  .submit-btn,
  .volver-btn {
    width: 100%;
    padding: 12px;
    background-color: #333;
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
  }
  
  .volver-btn {
    background-color: #333;
    margin-top: 10px; /* Espacio entre los botones */
  }
  </style>
  