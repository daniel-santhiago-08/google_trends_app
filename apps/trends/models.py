from django.db import models


class TrendsRising(models.Model):

    assunto = models.CharField(max_length=100)
    tendencia = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    periodo = models.CharField(max_length=50)
    palavra_chave = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)


    class Meta:
        managed = False
        db_table = 'receitas_trends_rising'