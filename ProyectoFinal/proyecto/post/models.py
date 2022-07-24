from django.db import models

# Create your models here.
class Posts (models.Model):
    titulo = models.CharField(max_length=80)
    subtitulo = models.CharField(max_length=120)

    def __str__(self):
        return f"Titulo: {self.titulo} - subtitulo: {self.subtitulo}"