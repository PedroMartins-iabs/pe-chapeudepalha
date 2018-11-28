from django.db import models

class Status(models.Model):
    tipo = models.CharField(max_length=100)
    chave  = models.CharField(max_length=100)
    texto  = models.CharField(max_length=200)
    parent = models.IntegerField(default=0)
    ordem = models.IntegerField(default=0)
    label_code= models.IntegerField(default=0)

class Uf(models.Model):
    sigla = models.CharField(max_length=50)
    nome = models.CharField(max_length=100)

    # status = models.CharField(max_length=1)


class Cidade(models.Model):
    uf = models.ForeignKey(Uf, models.DO_NOTHING)
    nomecidade = models.CharField(max_length=250)
    zona = models.CharField(max_length=18, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)

    # etapa = models.IntegerField(blank=True, null=True)
    # status = models.CharField(max_length=1)


class Localidade(models.Model):
    cidade = models.ForeignKey(Cidade, models.DO_NOTHING)
    nomelocalidade = models.CharField(max_length=100)

    # status = models.CharField(max_length=1)


class Bairro(models.Model):
    localidade = models.ForeignKey(Localidade, models.DO_NOTHING)
    nome = models.CharField(max_length=100)
    dataalteracao = models.DateTimeField()

    # status = models.CharField(max_length=1)
    # sincronizado = models.BooleanField(blank=True, null=True)
    # idusuarioalteracao = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='fk_idusuarioalteracao')

class ProgramaChapeu(models.Model):

    nome = models.CharField(max_length=100)
    anoinicio = models.CharField(max_length=5)
    status = models.ForeignKey(Status, models.DO_NOTHING)

class ProgramaChapeuAnual(models.Model):

    programa_chapeu = models.ForeignKey(ProgramaChapeu,on_delete=models.DO_NOTHING)
    ano_referencia = models.CharField(max_length=5)
    data_inicio_programa = models.DateTimeField()
    data_fim_programa = models.DateTimeField()
    #usuario_alteracao = models.ForeignKey(
    #    Usuario, models.DO_NOTHING)
    data_alteracao = models.DateTimeField()
    status = models.ForeignKey(Status,on_delete=models.DO_NOTHING)

    ##Campos rejeitados##
    #urlformulariocadastro = models.CharField(max_length=500, blank=True, null=True)
    #validacaoativa = models.TextField(blank=True, null=True)

class PostoCadastramento(models.Model):

    nome = models.CharField(
        max_length=100, blank=True, null=True)

    cidade = models.ForeignKey(
        Cidade,on_delete=models.DO_NOTHING)

    #responsavel = models.ForeignKey(
    #    Usuario,on_delete=models.DO_NOTHING, blank=True, null=True)

    status = models.ForeignKey(Status,on_delete=models.DO_NOTHING)

    programa_anual = models.ForeignKey(ProgramaChapeuAnual,on_delete=models.DO_NOTHING, blank=True, null=True)
