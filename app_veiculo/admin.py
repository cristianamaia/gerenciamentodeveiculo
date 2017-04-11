from django.contrib import admin

# Register your models here.
from app_veiculo.models import Tipodeveiculo, Marcadoveiculo, Veiculo

admin.site.register(Tipodeveiculo)
admin.site.register(Marcadoveiculo)
admin.site.register(Veiculo)

