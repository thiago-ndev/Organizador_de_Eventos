from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Evento(models.Model):
    criador = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    data_inicio = models.DateTimeField()
    data_termino = models.DateTimeField()
    carga_horaria = models.IntegerField()
    logo = models.ImageField(upload_to="logos")

    #paleta de cores
    cor_principal = models.CharField(max_length=7)
    cor_secundaria = models.CharField(max_length=7)
    cor_fundo = models.CharField(max_length=7)

    def __str__(self) -> str:
        return self.nome
