from django.db import models
from django.contrib.auth.models import User
from core.models import Cidade,Bairro

class DadosBancarios(models.Model):

    agenciabancaria = models.CharField(max_length=50, blank=True, null=True)
    numerocontabancaria = models.CharField(max_length=50, blank=True, null=True)

    operacaobancaria = models.CharField(max_length=50, blank=True, null=True)

class Usuario(models.Model):

    bairro = models.ForeignKey(Bairro, models.DO_NOTHING, blank=True, null=True)
    cidade = models.ForeignKey(Cidade, models.DO_NOTHING, blank=True, null=True)
    dados_bancarios = models.ForeignKey(DadosBancarios, models.DO_NOTHING, blank=True, null=True)
    django_user = models.ForeignKey(User,models.DO_NOTHING, unique=True)

    dataalteracao = models.DateTimeField()
    usuario_alteracao = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(max_length=1)

    nomemae = models.CharField(max_length=200, blank=True, null=True)
    logradouro = models.CharField(max_length=200, blank=True, null=True)

    #Dados de Endereço
    numero = models.CharField(max_length=50, blank=True, null=True)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    fone = models.CharField(max_length=30, blank=True, null=True)

    ##Campos descartados
    #login = models.CharField(unique=True, max_length=50)
    #senha = models.CharField(max_length=200)
    #email = models.CharField(max_length=150)
    #cpf = models.CharField(max_length=11, blank=True, null=True) -->CPF será o login
    #nome = models.CharField(max_length=300)
    #dataultimoacesso = models.DateTimeField(blank=True, null=True)
    #quantidadeacessos = models.IntegerField(blank=True, null=True)
    #fk_idperfil = models.ForeignKey(Tblperfil, models.DO_NOTHING, db_column='fk_idperfil')
    #sincronizado = models.BooleanField(blank=True, null=True)
