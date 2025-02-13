// src/mixin.js
export default {
    mounted() {
      document.body.classList.add('no-scroll');
    },
    beforeUnmount() {
      document.body.classList.remove('no-scroll');
    },
  };