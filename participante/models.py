from django.db import models

# Create your models here.

class Formulario(models.Model):

    participante = models.ForeignKey(
        Participante,
        on_delete=models.DO_NOTHING)

    posto_cadastramento = models.ForeignKey(
        PostoCadastramento,
        on_delete=models.DO_NOTHING)

    numero_cartao = models.BigIntegerField()

    lote = models.IntegerField()

    sublote = models.IntegerField()

    data_recebimento_cartao = models.DateTimeField(
        blank=True, null=True)

    data_inclusao = models.DateTimeField()

    data_alteracao = models.DateTimeField(
        blank=True, null=True)

    observacao = models.TextField(
        blank=True, null=True)

    data_cartao_inicializado = models.DateTimeField(
        blank=True, null=True)

    nisrlfamilia = models.CharField(
        max_length=15, blank=True, null=True)

    nisrlfamiliadtref = models.DateTimeField(
        blank=True, null=True)

    nisrlfamiliadtatual = models.DateTimeField(
        blank=True, null=True)





