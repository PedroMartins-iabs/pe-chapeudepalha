from django.db import models


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
