from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre =models.CharField(max_length=50)
    nacionalidad =models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)

class Libro(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    nombre  =models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)
    