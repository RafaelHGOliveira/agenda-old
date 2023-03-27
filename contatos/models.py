from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome
    
class Contato(models.Model):
    nome = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=150, blank=True)
    telefone = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome