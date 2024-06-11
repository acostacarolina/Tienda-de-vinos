from django.contrib import admin
from tiendavinos.models import Categoria, Bodega, Vino, Producto


class ProductoAdmin(admin.ModelAdmin):
    ordering = ("precio",)



class CategoriaAdmin(admin.ModelAdmin):
    ordering = ("nombre",)

class BodegaAdmin(admin.ModelAdmin):
    list_display = ("nombre","pais","email")
    ordering = ("nombre",)
    search_fields = ("nombre","email")
    list_filter = ("año",)


class VinoAdmin(admin.ModelAdmin):
    list_display = ("nombre","pais")
    ordering = ("nombre",)
    search_fields = ("categorias","bodega")
    list_filter = ("año",)
    filter_horizontal = ("categorias",)


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Bodega, BodegaAdmin)
admin.site.register(Vino, VinoAdmin)