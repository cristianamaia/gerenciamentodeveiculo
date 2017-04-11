from django.shortcuts import render

# Create your views here.
from app_veiculo.models import Veiculo


def index(request):

    consulta_no_banco = Veiculo.objects.all()

    return render(request, 'index.html',{'consulta_no_banco': consulta_no_banco})