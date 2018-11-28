from django.db import models
from usuario.models import Usuario

from core.choices import *

from core.models import Cidade, Bairro, ProgramaChapeuAnual, Status, PostoCadastramento
from usuario.models import Usuario

class Participante(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    municipio = models.ForeignKey(Cidade, models.DO_NOTHING)

    #-------------------------------------------------#
    #---DOCUMENTAÇÃO APRESENTADA E RESPECTIVA CÓPIA---#
    # -------------------------------------------------#
    apresentounis = models.BooleanField(blank=True, null=True)
    apresentoucopiacpf = models.BooleanField(blank=True, null=True)
    apresentoucopiarg = models.BooleanField(blank=True, null=True)
    apresentoucopiacontratotrab = models.BooleanField(blank=True, null=True)
    apresentoucopiactps = models.BooleanField(blank=True, null=True)
    apresentoucopiaendereco = models.BooleanField(blank=True, null=True)
    apresentoucertificadocurso = models.BooleanField(blank=True, null=True)

    #---------------------------------#
    #---INFORMAÇÕES DO PARTICIPANTE---#
    # ---------------------------------#
    nis = models.CharField(max_length=15)
    nisatual = models.BigIntegerField(blank=True, null=True)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=20, blank=True, null=True)
    rg_orgao_exp = models.CharField(max_length=20, blank=True, null=True)
    rg_uf = models.CharField(max_length=2, blank=True, null=True)

    nomeparticipante = models.CharField(max_length=200)

    nomepai = models.CharField(max_length=500, blank=True, null=True)
    nomemae = models.CharField(max_length=500, blank=True, null=True)

    datanascimento = models.DateTimeField()
    sexo = models.CharField(max_length=1)
    estadocivil = models.IntegerField(blank=True, null=True)

    municipionaturalidade = models.CharField(max_length=150, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    tituloeleitor = models.CharField(max_length=20, blank=True, null=True)

    ctps = models.BigIntegerField(blank=True, null=True)
    ctps_serie = models.CharField(max_length=10, blank=True, null=True)
    ctps_uf = models.CharField(max_length=2, blank=True, null=True)
    tipodocumentoempregador = models.IntegerField(blank=True, null=True)
    cnpj_ultimo_empregador = models.CharField(max_length=20, blank=True, null=True)

    nomeempresa = models.CharField(max_length=100, blank=True, null=True)

    funcao = models.CharField(max_length=100, blank=True, null=True)
    dataentrada = models.DateTimeField(blank=True, null=True)
    datasaida = models.DateTimeField(blank=True, null=True)

    qdtfilhos0_6meses = models.IntegerField(blank=True, null=True)
    qdtfilhos7meses_3anos = models.IntegerField(blank=True, null=True)
    qdtfiilhos4_7anos = models.IntegerField(blank=True, null=True)
    qdtfilhos8_12anos = models.IntegerField(blank=True, null=True)
    qdtfilhos13_17anos = models.IntegerField(blank=True, null=True)
    qdtfilhos18_29anos = models.IntegerField(blank=True, null=True)
    existegestantenafamilia = models.BooleanField(blank=True, null=True)

    alfabetizado = models.BooleanField(blank=True, null=True)
    estaestudando = models.BooleanField(blank=True, null=True)
    turnoatividadeescolar = models.IntegerField(blank=True, null=True)
    grauescolaridade = models.IntegerField(blank=True, null=True)
    raca = models.IntegerField(blank=True, null=True)
    portadordedeficiencia = models.IntegerField(blank=True, null=True)

    #--------------#
    #---ENDEREÇO---#
    # --------------#
    logradouro = models.CharField(max_length=200, blank=True, null=True)
    numero = models.CharField(max_length=50, blank=True, null=True)

    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.ForeignKey(Bairro, models.DO_NOTHING)
    cep = models.CharField(max_length=10, blank=True, null=True)

    celular = models.CharField(max_length=15, blank=True, null=True)
    fone = models.CharField(max_length=15, blank=True, null=True)
    datacomprovanteresidencia = models.DateTimeField(blank=True, null=True)

    rendamensalfamilia = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    qdtpessoasnacasa = models.IntegerField(blank=True, null=True)
    qdtpessoacontribuemrenda = models.IntegerField(blank=True, null=True)

    beneficiarioisindicado = models.BooleanField(blank=True, null=True)

    datainclusao = models.DateTimeField(blank=True, null=True)
    dataalteracao = models.DateTimeField(blank=True, null=True)

    fk_idusuarioinclusao = models.ForeignKey('Usuario', models.DO_NOTHING, related_name='participante_inclusao', blank=True, null=True)
    fk_idusuarioalteracao = models.ForeignKey('Usuario', models.DO_NOTHING, related_name='participante_alteracao', blank=True, null=True)

    # ------------------------------------------ #
    # ---DADOS REFERENTE AO CADASTRO DA PESCA--- #
    # ------------------------------------------ #
    pescacarteirahabilicatacao = models.CharField(max_length=50, blank=True, null=True)
    pescadataexpedicao = models.DateTimeField(blank=True, null=True)
    pescacategoria = models.CharField(max_length=50, blank=True, null=True)
    pescadocumentocomprobatorio = models.SmallIntegerField(blank=True, null=True)
    pescaregistrogeral = models.CharField(max_length=50, blank=True, null=True)
    pescaregistroorgao = models.CharField(max_length=50, blank=True, null=True)
    pescadataregistro = models.DateTimeField(blank=True, null=True)
    pescadatavalidade = models.DateTimeField(blank=True, null=True)
    pescaprotocolorgp = models.CharField(max_length=50, blank=True, null=True)
    pescadatasolicitacao = models.DateTimeField(blank=True, null=True)
    pescacoloniaassociacaotipo = models.SmallIntegerField(blank=True, null=True)
    pescacoloniaassociacaonum = models.CharField(max_length=30, blank=True, null=True)
    apresentoucopiargp = models.BooleanField(blank=True, null=True)


    ########## fk_idlistagem = models.ForeignKey(Tbllistagemdesligados, models.DO_NOTHING, db_column='fk_idlistagem', blank=True, null=True)

    # ---------------------- #
    # ---DADOS ECONÔMICOS--- #
    # ---------------------- #
    recebesegurodesemprego = models.BooleanField(blank=True, null=True)
    recebeaposentadoria = models.BooleanField(blank=True, null=True)
    pensionista = models.BooleanField(blank=True, null=True)
    possuimei = models.BooleanField(blank=True, null=True)
    parentepossuimei = models.BooleanField(blank=True, null=True)


    # area = models.IntegerField(blank=True, null=True)
    # apresentoulistagemdesligado = models.BooleanField(blank=True, null=True)
    # preferenciadiasaulas = models.IntegerField(blank=True, null=True)
    # matricula = models.CharField(max_length=20, blank=True, null=True)
    # idparticipantecana14 = models.BigIntegerField(blank=True, null=True)
    # status = models.CharField(max_length=1)
    # flag = models.IntegerField(blank=True, null=True)
    # rgnovo = models.CharField(max_length=20, blank=True, null=True)
    # justificativacriterionaoatendido = models.TextField(blank=True, null=True)
    # programasgoverno = models.TextField(blank=True, null=True)
    # programasgovernooutro = models.TextField(blank=True, null=True)
    # fk_idpostosaude = models.ForeignKey('Tblpostosaude', models.DO_NOTHING, db_column='fk_idpostosaude', blank=True, null=True)
    # sincronizado = models.BooleanField(blank=True, null=True)
    # apresentoucertificadocursoindicado = models.BooleanField(blank=True, null=True)


class Formulario(models.Model):
    participante = models.ForeignKey(Participante,on_delete=models.DO_NOTHING)
    programa_chapeu_anual = models.ForeignKey(ProgramaChapeuAnual,on_delete=models.DO_NOTHING)
    posto_cadastramento = models.ForeignKey(PostoCadastramento,on_delete=models.DO_NOTHING)
    statusrecebimentocartao = models.ForeignKey(Status, models.DO_NOTHING, related_name='formularios_situacao_cartao')

    #usuario_inclusao = models.ForeignKey(Usuario, models.DO_NOTHING, related_name='formulario_inclusao')
    #usuario_alteracao = models.ForeignKey(Usuario, models.DO_NOTHING, related_name='formulatio_alteracao', blank=True, null=True)
    #usuario_entregacartao = models.ForeignKey(Usuario, models.DO_NOTHING, related_name='formulario_entrega_cartao', blank=True, null=True)

    status_rlmds = models.ForeignKey(Status, models.DO_NOTHING, related_name='formulario_rlmds')
    status_rlmdsdup = models.ForeignKey(Status, models.DO_NOTHING, related_name='formulario_rlmdsdup')

    ##Dados do cartão
    data_recebimento_cartao = models.DateTimeField(blank=True, null=True)
    numero_cartao = models.BigIntegerField()
    cartao_inicializado = models.BooleanField(blank=True, null=True)
    data_cartao_inicializado = models.DateTimeField(blank=True, null=True)
    #Dados NIS
    nis_rl_familia = models.CharField(max_length=15, blank=True, null=True)
    nis_rl_familia_dt_ref = models.DateTimeField(blank=True, null=True)
    nis_rl_familia_dt_atual = models.DateTimeField(blank=True, null=True)
    ##Dados formulario
    lote = models.IntegerField()
    sublote = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    data_alteracao = models.DateTimeField(blank=True, null=True)

    observacao = models.TextField(blank=True, null=True)
    tempo_cadastro = models.BigIntegerField(blank=True, null=True)
    status = models.ForeignKey(Status, models.DO_NOTHING)

    ##Campos descartados##

    #fk_idselamento = models.CharField(max_length=50, blank=True, null=True)
    #naoencontradocaixaposfolha = models.IntegerField(blank=True, null=True)
    #idformulariocana14 = models.BigIntegerField(blank=True, null=True)
    #auditado = models.BooleanField(blank=True, null=True)
    #sincronizado = models.BooleanField(blank=True, null=True)


class Indicado(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    formulario = models.ForeignKey(Formulario,on_delete=models.DO_NOTHING)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    datanascimento = models.DateTimeField(blank=True, null=True)
    sexo = models.CharField(choices=SEXO,max_length=1, blank=True, null=True)
    nomeindicado = models.CharField(max_length=200)
    grauparentesco = models.IntegerField(blank=True, null=True)
    alfabetizado = models.BooleanField()
    grauescolaridade = models.IntegerField(choices=GRAU_ESCOLARIDADE,default=1)
    telefone = models.CharField(max_length=50, blank=True, null=True)
    celular = models.CharField(max_length=15, blank=True, null=True)
    logradouro = models.CharField(max_length=150, blank=True, null=True)
    numero = models.CharField(max_length=50, blank=True, null=True)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.ForeignKey(Bairro, on_delete=models.DO_NOTHING)
    cep = models.CharField(max_length=10, blank=True, null=True)
    apresentoucopiacpf = models.BooleanField(blank=True, null=True)
    apresentoucopiaendereco = models.BooleanField(blank=True, null=True)
    estaestudando = models.BooleanField(blank=True, null=True)
    turnoatividadeescolar = models.IntegerField(choices=TURNO_ATIVIDADE_ESCOLAR,blank=True, null=True)
    raca = models.IntegerField(choices=RACA,blank=True, null=True)
    portadordedeficiencia = models.IntegerField(choices=TIPOS_DEFICIENCIA,blank=True, null=True)
    dataalteracao = models.DateTimeField()
    UsuarioAlteracao = models.ForeignKey(Usuario, models.DO_NOTHING, blank=True, null=True)
    enderecomesmoparticipante = models.BooleanField(blank=True, null=True)
    datacomprovanteresidencia = models.DateTimeField(blank=True, null=True)
    status = models.ForeignKey(Status, models.DO_NOTHING, related_name='indicado_status')

    ##Campos descartados##
    #area = models.IntegerField(blank=True, null=True)
    #sincronizado = models.BooleanField(blank=True, null=True)





