from django.db import models

# -----------------------------------------------------------
# 1. Modelo Usuario
# -----------------------------------------------------------
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    correo = models.EmailField(unique=True, verbose_name="Correo")
    contraseña = models.CharField(max_length=128, verbose_name="Contraseña")
    fecha_de_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")

    def _str_(self):
        return self.nombre


# -----------------------------------------------------------
# 2. Modelo TatuadorUser
#   
# -----------------------------------------------------------
class TatuadorUser(models.Model):
    id_tatuador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    especialidad = models.CharField(max_length=100, verbose_name="Especialidad")
    experiencia = models.IntegerField(verbose_name="Años de Experiencia")
    redes_sociales = models.TextField(blank=True, null=True, verbose_name="Redes Sociales")
    portafolio = models.TextField(blank=True, null=True, verbose_name="Portafolio")
    direccion = models.CharField(max_length=150, blank=True, null=True, verbose_name="Dirección")
    horario = models.CharField(max_length=100, blank=True, null=True, verbose_name="Horario")

    def _str_(self):
        return f"Tatuador: {self.nombre}"


# -----------------------------------------------------------
# 3. Modelo Reseña
# -----------------------------------------------------------
class Reseña(models.Model):
    id_reseña = models.AutoField(primary_key=True)
    # Relación con Usuario (quien escribe la reseña)
    id_usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name="reseñas_creadas",
        verbose_name="Usuario"
    )
    # Relación con TatuadorUser (a quién va dirigida la reseña)
    id_tatuador = models.ForeignKey(
        TatuadorUser,
        on_delete=models.CASCADE,
        related_name="reseñas_recibidas",
        verbose_name="Tatuador"
    )
    calificacion = models.IntegerField(verbose_name="Calificación")
    comentario = models.TextField(verbose_name="Comentario")
    # Puedes agregar un campo de fecha si lo deseas
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    def _str_(self):
        return f"Reseña de {self.id_usuario.nombre} a {self.id_tatuador.nombre}"


# -----------------------------------------------------------
# 4. Modelo Categoria
# -----------------------------------------------------------
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")

    def _str_(self):
        return self.nombre


# -----------------------------------------------------------
# 5. Modelo Tatuaje
# -----------------------------------------------------------
class Tatuaje(models.Model):
    id_tatuaje = models.AutoField(primary_key=True)
    # Relación con TatuadorUser
    id_tatuador = models.ForeignKey(
        TatuadorUser,
        on_delete=models.CASCADE,
        related_name="tatuajes",
        verbose_name="Tatuador"
    )
    # Relación con Categoria ()
    id_categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        related_name="tatuajes",
        blank=True,
        null=True,
        verbose_name="Categoría"
    )
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Tatuaje")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")

    def _str_(self):
        return self.nombre
  

