from django.db import models
from django.contrib.auth.models import User

class Atleta(models.Model):
    FAIXA_BRANCA = 'branca'
    FAIXA_AZUL = 'azul'
    FAIXA_ROXA = 'roxa'
    FAIXA_MARROM = 'marrom'
    FAIXA_PRETA = 'preta'
    FEMININO = 'feminino'
    MASCULINO = 'masculino'
    GRADUACAO = [
       (FAIXA_BRANCA, 'Faixa Branca'),
       (FAIXA_AZUL, 'Faixa Azul'),
       (FAIXA_ROXA, 'Faixa Roxa'),
       (FAIXA_MARROM, 'Faixa Marrom'),
       (FAIXA_PRETA, 'Faixa Preta'),
    ]
    GENERO = [
       (FEMININO, 'Feminino'),
       (MASCULINO, 'Masculino'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    equipe = models.CharField(max_length=200)
    idade = models.IntegerField(default=0)
    graduacao = models.CharField(max_length=200, choices=GRADUACAO) 
    peso = models.IntegerField(default=0)
    genero = models.CharField(max_length=200, choices=GENERO)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return (self.nome + " - " + self.equipe)
