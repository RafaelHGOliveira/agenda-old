from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    
class Contato(models.Model):
    nome = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    categoria = models.ForeignKey(Categoria)