from django.shortcuts import render
from .models import *
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'index.html')

def dados(request):
    if request.method == 'POST':
        res = Despesas().saveDespesa(request.POST)
        messages.success(request, res)
    context = {
        'nomev': NomeViagem().getNomesAtivos(),
        'tipos': Tipos().getTipos(),
        'cidade': Cidades().getCidade(),
        'pagamento': Pagamentos().getPagamentos(),
        'despesas': Despesas().getDespesas()
    }
    return render(request, 'dados.html', context)

def carros(request):
    if request.method == 'POST':
        res = Carros().salveCarros(request.POST)
        messages.success(request, res)
    context = {
        'carro': Carros().getCarros()
    }
    return render(request, 'carro.html', context)
    

def cidades(request):
    if request.method == 'POST':
        res = Cidades().salveCidade(request.POST)
        messages.success(request, res)
    context = {
        'cidade': Cidades().getCidade()
    }
    return render(request, 'cidade.html', context)

def nomeViagem(request):
    if request.method == 'POST':
        res = NomeViagem().saveNomeViagem(request.POST)
        messages.success(request, res)
    context = {
        'carro': Carros().getCarros(),
        'user': Usuario().getUsers(),
        'nomeviagem': NomeViagem().getNomeViagem()
    }
    return render(request, 'nome-viagem.html', context)

def pagamentos(request):
    if request.method == 'POST':
        res = Pagamentos().savePagamentos(request.POST)
        messages.success(request, res)
    context = {
        'pagamento': Pagamentos().getPagamentos()
    }
    return render(request, 'pagamento.html', context)

def tipos(request):
    if request.method == 'POST':
        res = Tipos().saveTipos(request)
        messages.success(request, res)
    context = {
        'tipo': Tipos().getTipos()
    }
    return render(request, 'tipo.html', context)

def usuarios(request):
    if request.method == 'POST':
        res = Usuario().saveUsuarios(request.POST)
        messages.success(request, res)
    context = {
        'usuario': Usuario().getUsers()
    }
    return render(request, 'usuario.html', context)