from django.contrib import admin
from .models import Usuario, TatuadorUser, Reseña, Categoria, Tatuaje

# Register your models here.


admin.site.register(Usuario)
admin.site.register(TatuadorUser)
admin.site.register(Reseña)
admin.site.register(Categoria)
admin.site.register(Tatuaje)

