from django.db import models
from django.forms import CharField

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre

class Bodega(models.Model):
    nombre = models.CharField(max_length=30)
    año = models.DateField()
    direccion = models.CharField(max_length=40)
    estado = models.CharField(max_length=40)
    pais = models.CharField(max_length=30)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.nombre

class Vino(models.Model):
    nombre = models.CharField(max_length=30)
    año = models.DateField()
    pais = models.CharField(max_length=40)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria)
    portada = models.ImageField(upload_to='portadas')
    sitioweb = models.URLField()

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
   
    def __str__(self):
        return {self.precio}

    


    
