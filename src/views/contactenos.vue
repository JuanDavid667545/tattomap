<template>
    <div class="contacto-container">
      <div class="contacto-content">
        <!-- Sección de información de contacto -->
        <div class="info-contacto">
          <h2>Contacto</h2>
          <div class="contact-info">
            <div class="info-item">
              <i class="fas fa-envelope"></i>
              <span>Daviderazomalagon@gmail.com</span>
            </div>
            
            <div class="ontact-info">
              <i class="info-item"></i>
              <span>leobaquero456@gmail.com</span>
            </div>
            
            <div class="info-item">
              <i class="fas fa-phone"></i>
              <div class="phone-numbers">
                <span>(+57) 312 3820362</span>
                <span>(+57) 310 7547938</span>
              </div>
            </div>
          </div>
          
          <div class="redes-sociales">
            <a href="#" class="social-icon">
              <i class="fab fa-facebook-f"></i>
            </a>
            <a href="#" class="social-icon">
              <i class="fab fa-twitter"></i>
            </a>
            <a href="#" class="social-icon">
              <i class="fab fa-linkedin-in"></i>
            </a>
          </div>
        </div>
  
        <!-- Formulario de contacto -->
        <div class="formulario-contacto">
          <form @submit.prevent="enviarMensaje">
            <div class="form-group">
              <input 
                type="text" 
                v-model="contacto.nombre" 
                placeholder="Nombre"
                required
              >
            </div>
            
            <div class="form-group">
              <input 
                type="email" 
                v-model="contacto.email" 
                placeholder="Correo electrónico"
                required
              >
            </div>
            
            <div class="form-group">
              <input 
                type="text" 
                v-model="contacto.asunto" 
                placeholder="Asunto"
                required
              >
            </div>
            
            <div class="form-group">
              <textarea 
                v-model="contacto.mensaje" 
                placeholder="Mensaje"
                rows="5"
                required
              ></textarea>
            </div>
            
            <div class="botones">
              <button type="submit" class="enviar-btn">Enviar</button>
              <button type="button" class="volver-btn" @click="volver">Volver</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </template>
  
  
  <script>
  export default {
    name: 'ContactoForm',
    data() {
      return {
        contacto: {
          nombre: '',
          email: '',
          asunto: '',
          mensaje: ''
        }
      }
    },
    methods: {
      contactenos() {
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
  .contacto-container {
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 40px;
    background-color: #000;
  }
  
  .contacto-content {
    display: flex;
    width: 100%;
    max-width: 1200px;
    background-color: #1a1a1a;
    border-radius: 10px;
    overflow: hidden;
  }
  
  .info-contacto {
    flex: 1;
    padding: 40px;
    color: #fff;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .info-contacto h2 {
    color: #00e676;
    margin-bottom: 30px;
    font-size: 28px;
    text-align: center;
  }
  
  .contact-info {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 25px;
    margin-bottom: 20px;
  }
  
  .info-item {
    display: flex;
    align-items: center;
    gap: 15px;
  }
  
  .info-item i {
    color: #00e676;
    width: 20px;
    margin-top: 3px;
    font-size: 18px;
  }
  
  .info-item span {
    font-size: 16px;
    line-height: 1.5;
    color: #ffffff;
  }
  
  .phone-numbers {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }
  
  .redes-sociales {
    display: flex;
    gap: 15px;
    justify-content: flex-end; /* Mover los círculos a la derecha */
    margin-top: 20px;
    transform: translateX(20px);
  }
  
  .social-icon {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background-color: #00e676;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #fff;
    text-decoration: none;
    transition: background-color 0.3s ease;
  }
  
  .social-icon:hover {
    background-color: #00c853;
  }
  
  .formulario-contacto {
    flex: 2;
    padding: 40px;
    background-color: #1a1a1a;
  }
  
  .form-group {
    margin-bottom: 20px;
  }
  
  input, textarea {
    width: 100%;
    padding: 12px;
    border: 1px solid #333;
    border-radius: 5px;
    font-size: 16px;
    background-color: #222;
    color: #fff;
  }
  
  input::placeholder, textarea::placeholder {
    color: #888;
  }
  
  textarea {
    resize: vertical;
    min-height: 120px;
  }
  
  input:focus, textarea:focus {
    outline: none;
    border-color: #00e676;
  }
  
  .botones {
    display: flex;
    gap: 10px;
    justify-content: flex-end; /* Alinear los botones a la derecha */
  }
  
  .enviar-btn, .volver-btn {
    background-color: #00e676;
    color: #fff;
    border: none;
    padding: 12px 30px;
    border-radius: 5px;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .enviar-btn:hover, .volver-btn:hover {
    background-color: #00c853;
  }
  
  @media (max-width: 768px) {
    .contacto-content {
      flex-direction: column;
    }
    
    .info-contacto, .formulario-contacto {
      width: 100%;
    }
  
    .info-item {
      font-size: 14px;
    }
  
    .info-contacto {
      padding: 30px;
    }
  
    .formulario-contacto {
      padding: 30px;
    }
  }
  </style>
  