from django.db import models

# Create your models here.
class Tipodeveiculo (models.Model):
    tipo = models.CharField('Tipo de veiculo', max_length=20, help_text='Ex. Carro ou Moto')

    def __str__(self):
        return "{}". format(self.tipo)

    class Meta:
        ordering= ('tipo',)
        verbose_name='Tipo de Veiculo'
        verbose_name_plural= 'Tipo De Veiculos'


class Marcadoveiculo(models.Model):
    marca = models.CharField('MarcaDoVeiculo',max_length=20,help_text='Ex. Nissan, Honda''Fiat')

    def __str__(self):
        return "{}". format(self.marca)

    class Meta:
        ordering= ('marca',)
        verbose_name='Marca de Veiculo'
        verbose_name_plural= 'Marca De Veiculos'


class Veiculo(models.Model):
    tipo= models.ForeignKey(Tipodeveiculo)
    marca= models.ForeignKey(Marcadoveiculo)

    modelo= models.CharField('Modelo', max_length=50)
    placa = models.CharField('Placa', max_length=8)
    cor = models.CharField('Cor', max_length=10)

    def __str__(self):
        return "{}".format(self.placa, self.modelo)

    class Meta:
        ordering = ('tipo','marca','modelo')
        verbose_name = 'Veiculo'
        verbose_name_plural = 'Veiculos'