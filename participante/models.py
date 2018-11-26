from django.db import models

from core.choices import(
    GRAU_ESCOLARIDADE,TURNO_ATIVIDADE_ESCOLAR,RACA,
    TIPOS_DEFICIENCIA,SEXO,SITUACAO)

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

    cartao_inicializado = models.BooleanFieldField(
        blank=True, null=True)

    data_cartao_inicializado = models.DateTimeField(
        blank=True, null=True)

    nis_rl_familia = models.CharField(
        max_length=15, blank=True, null=True)

    nis_rl_familia_dt_ref = models.DateTimeField(
        blank=True, null=True)

    nis_rl_familia_dt_atual = models.DateTimeField(
        blank=True, null=True)

    tempo_cadastro = models.BigIntegerField(
        blank=True, null=True)

    status_participante = models.ForeignKey(
        Status, models.DO_NOTHING)

    statusrecebimentocartao = models.ForeignKey(
        Status, models.DO_NOTHING,related_name='formularios_situacao_cartao')

    usuario_inclusao = models.ForeignKey(
        Usuario, models.DO_NOTHING,related_name='formulario_inclusao')

    usuario_alteracao = models.ForeignKey(
        Usuario, models.DO_NOTHING, related_name='formulatio_alteracao', blank=True, null=True)

    usuario_entregacartao = models.ForeignKey(
        Usuario, models.DO_NOTHING, related_name='formulario_entrega_cartao', blank=True, null=True)

    status_rlmds = models.ForeignKey(
        Status, models.DO_NOTHING,related_name='formulario_rlmds')

    status_rlmdsdup = models.ForeignKey(
        Status, models.DO_NOTHING, related_name='formulario_rlmdsdup')

    status = models.ForeignKey(
        Status, models.DO_NOTHING, related_name='formulario_status')

    ##Campos descartados##

    #fk_idprogramachapeuanual = models.ForeignKey('Tblprogramachapeuanual', models.DO_NOTHING, db_column='fk_idprogramachapeuanual')
    #fk_idselamento = models.CharField(max_length=50, blank=True, null=True)
    #naoencontradocaixaposfolha = models.IntegerField(blank=True, null=True)
    #idformulariocana14 = models.BigIntegerField(blank=True, null=True)
    #auditado = models.BooleanField(blank=True, null=True)
    #sincronizado = models.BooleanField(blank=True, null=True)

class Indicado(models.Model):

    formulario = models.ForeignKey(
        Formulario,on_delete=models.DO_NOTHING)

    cpf = models.CharField(
        max_length=11, blank=True, null=True)

    datanascimento = models.DateTimeField(
        blank=True, null=True)

    sexo = models.CharField(
        choices=SEXO,max_length=1, blank=True, null=True)

    nomeindicado = models.CharField(
        max_length=200)

    grauparentesco = models.IntegerField(
        blank=True, null=True)

    alfabetizado = models.BooleanField()

    grauescolaridade = models.IntegerField(
        choices=GRAU_ESCOLARIDADE,default=1
    )

    telefone = models.CharField(
        max_length=50, blank=True, null=True)a

    celular = models.CharField(
        max_length=15, blank=True, null=True)

    logradouro = models.CharField(
        max_length=150, blank=True, null=True)

    numero = models.CharField(
        max_length=50, blank=True, null=True)

    complemento = models.CharField(
        max_length=50, blank=True, null=True)

    bairro = models.ForeignKey(
        Bairro, on_delete=models.DO_NOTHING)

    cep = models.CharField(
        max_length=10, blank=True, null=True)

    apresentoucopiacpf = models.BooleanField(
        blank=True, null=True)

    apresentoucopiaendereco = models.BooleanField(
        blank=True, null=True)

    estaestudando = models.BooleanField(
        blank=True, null=True)

    turnoatividadeescolar = models.IntegerField(
        choices=TURNO_ATIVIDADE_ESCOLAR,blank=True, null=True)

    raca = models.IntegerField(
        choices=RACA,blank=True, null=True)

    portadordedeficiencia = models.IntegerField(
        choices=TIPOS_DEFICIENCIA,blank=True, null=True)

    dataalteracao = models.DateTimeField()

    UsuarioAlteracao = models.ForeignKey('Usuario', models.DO_NOTHING)

    enderecomesmoparticipante = models.BooleanField(
        blank=True, null=True)

    datacomprovanteresidencia = models.DateTimeField(
        blank=True, null=True)

    status = models.ForeignKey(
        Status, models.DO_NOTHING, related_name='indicado_status')

    ##Campos descartados##
    #area = models.IntegerField(blank=True, null=True)
    #sincronizado = models.BooleanField(blank=True, null=True)





