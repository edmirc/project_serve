from django.shortcuts import render
from .models import *
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'index.html')

def dados(request):
    return render(request, 'dados.html')

def carros(request):
    return render(request, 'carro.html')

def cidades(request):
    if request.method == 'POST':
        res = Cidades().salveCidade(request.POST)
        messages.success(request, res)
    context = {
        'cidade': Cidades.objects.all()
    }
    return render(request, 'cidade.html', context)

def nomeViagem(request):
    return render(request, 'nome-viagem.html')

def pagamentos(request):
    return render(request, 'pagamento.html')

def tipos(request):
    return render(request, 'tipo.html')