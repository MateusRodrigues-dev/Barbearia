from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    barbeiro = models.CharField(max_length=100, blank=True)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return self.nome


