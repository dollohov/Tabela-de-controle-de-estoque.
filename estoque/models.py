# estoque/models.py

from django.db import models # type: ignore

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    valor_lote = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome
