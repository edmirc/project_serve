from collections.abc import Iterable
from django.db import models


class Carros(models.Model):
    placa = models.CharField(name='placa', unique=True, max_length=7)
    modelo = models.CharField(name='modelo', max_length=150)

    def salveCarros(self, post: dict) -> str:
        acao = 'salvo'
        id = post['id']
        plac: str = post['placa']
        model: str = post['modelo']
        plac = plac.upper()
        model = model.strip().title()
        try:
            if id != '':
                car = Carros.objects.get(id=id)
                acao = 'alterado'
            else:
                car = Carros()
            car.placa = plac
            car.modelo = model
            car.save()
            return f'Carros {plac}, {acao} com sucesso !!'
        except:
            return 'Dados NÃO salvos!!!'
    
    def getCarros(self):
        try:
            return Carros.objects.all()
        except:
            return list()
    
class Cidades(models.Model):
    nome = models.CharField(name='nome', unique=True ,max_length=100)
    estado = models.CharField(name='estado', max_length=2)

    def salveCidade(self, post: dict) -> str:
        acao = 'salvo'
        id = post['id']
        nome: str = post['nome']
        estado: str = post['estado']
        nome = nome.title().strip()
        estado = estado.upper().strip()
        try:
            if id != '':
                cid = Cidades.objects.get(id=id)
                acao = 'alterado'
            else:
                cid = Cidades()
            cid.nome = nome
            cid.estado = estado
            cid.save()
            return f'Cidade {nome}, {acao} com sucesso!!'
        except:
            return 'Dados NÃO salvos!!!'
        
    def getCidade(self):
        try:
            return Cidades.objects.all()
        except:
            return list()

class Pagamentos(models.Model):
    forma = models.CharField(name='forma', unique=True, max_length=50)

    def savePagamentos(self, post: dict) -> str:
        acao = 'salvo'
        id = post['id']
        frm = post['tipo']
        frm = frm.strip().title()
        try:
            if id != '':
                pag = Pagamentos.objects.get(id=id)
                acao = 'alterado'
            else:
                pag = Pagamentos()
            pag.forma = frm
            pag.save()
            return f'Forma de pagamento {frm}, {acao} com sucesso!!!'
        except:
            return 'Dados NÂO salvos!!'
    
    def getPagamentos(self):
        try:
            return Pagamentos.objects.all().order_by('id')
        except:
            return list()

class Tipos(models.Model):
    tipo = models.CharField(name='tipo', max_length=50, unique=True)

    def saveTipos(self, request) -> str:
        acao = 'salvo'
        id = request.POST.get('id')
        tp = request.POST.get('tipo')
        tp = tp.strip().title()
        try:
            if id != '':
                tipoid = Tipos.objects.get(id=id)
                acao = 'alterado'
            else:
                tipoid = Tipos()
            tipoid.tipo = tp
            tipoid.save()
                
            return f'Tipos de despesa {tp}, {acao} com sucesso!!'
        except:
             return 'Dados NÂO salvos!!'
        
    def getTipos(self):
        try:
            return Tipos.objects.all()
        except:
            return list()

class Usuario(models.Model):
    nome = models.CharField(name='usuario', max_length=150)
    login = models.CharField(name= 'login', max_length=20)
    senha = models.CharField(name='senha', max_length=15)
    email = models.CharField(name='email', max_length=100)

    def saveUsuarios(self, post: dict) -> str:
        acao = 'salvo'
        id = post['id']
        nome = post['nome'].title().strip()
        login = post['user'].strip().lower()
        email = post['email'].strip().lower()
        senha = post['senha']
        try:
            if id != '':
                user = Usuario.objects.get(id=id)
                acao = 'alterado'
            else:
                user = Usuario()
            user.usuario = nome
            user.login = login
            user.email = email
            user.senha = senha
            user.save()
            return f'Usuário {login}, {acao} com sucesso!!'
        except:
            return 'Dados NÃO salvo!!!'
    

    def getUsers(self):
        try:
            return Usuario.objects.all()
        except:
            return list()
        
class NomeViagem(models.Model):
    nome = models.CharField(name='nome', max_length=100)
    datainicio = models.DateField(name='datainicio')
    datafinal = models.DateField(name='datafinal')
    carro = models.ForeignKey(Carros, on_delete=models.CASCADE, name='idcarro')
    usuario = models.ForeignKey(Usuario, name='usuario', on_delete=models.CASCADE)
    atividade = models.BooleanField(name='atividade')

    def saveNomeViagem(self, post: dict) -> str:
        acao = 'salvo'
        id = post['id']
        nome = post['nome']
        nome = nome.strip().title()
        datainicio = post['datai']
        datafim = post['dataf']
        car = post['carro']
        car = Carros.objects.get(id=car)
        usuario = Usuario.objects.get(id=post['user'])
        try:
            atv = post['atv']
        except KeyError:
            atv = 0
        try:
            if id != '':
                nomev = NomeViagem.objects.get(id=id)
                acao = 'alterado'
            else:
                nomev = NomeViagem()
            nomev.nome = nome
            nomev.datainicio = datainicio
            nomev.datafinal = datafim
            nomev.idcarro = car
            nomev.usuario = usuario
            nomev.atividade = atv
            nomev.save()
            return f'Viagem {nome}, {acao} salvo com sucesso!!'
        except:
            return 'Dados NÂO salvos!!'
        
    def getNomeViagem(self):
        try:
            return NomeViagem.objects.all()
        except:
            return list()
        
    def getNomesAtivos(self):
        try:
            return NomeViagem.objects.filter(atividade=True)
        except:
            return list()


class Despesas(models.Model):
    nomeviagem = models.ForeignKey(NomeViagem, name='idnomeviagem', on_delete=models.CASCADE)
    data = models.DateField(name='data')
    tipo = models.ForeignKey(Tipos, name='idtipo', on_delete=models.CASCADE)
    qnt = models.DecimalField(name='qnt',decimal_places=2, max_digits=10)
    valor = models.DecimalField(name='valor', decimal_places=2, max_digits=10)
    nota = models.IntegerField(name='nota', unique=True)
    kminicial = models.IntegerField(name='kminicial')
    kmfinal = models.IntegerField(name='kmfinal')
    kmrodado = models.IntegerField(name='kmrodado')
    media = models.DecimalField(name='media', decimal_places=2, max_digits=10)
    cidade = models.ForeignKey(Cidades, name='idcidade', on_delete=models.CASCADE)
    pagamento = models.ForeignKey(Pagamentos, name='idpagamento', on_delete=models.CASCADE)

    def saveDespesa(self, post: dict):
        acao = 'salvo'
        id  = post['id']
        viagem = NomeViagem.objects.get(id=post['nome-viagem'])
        data = post['data']
        tipo = Tipos.objects.get(id=post['tipo'])
        qnt = post['qnt']
        valor = post['valor']
        nota = post['nota']
        kmi = post['kmi']
        kmf = post['kmf']
        kmr = post['kmr']
        consumo = post['consumo']
        cidade = Cidades.objects.get(id=post['cidade'])
        pg = Pagamentos.objects.get(id=post['pg'])
        try:
            if id != '':
                dados = Despesas.objects.get(id = id)
                acao = 'Alterado'
            else:
                dados = Despesas()
            dados.idnomeviagem = viagem
            dados.data = data
            dados.idtipo = tipo
            dados.qnt = qnt
            dados.valor = valor
            dados.nota = nota
            dados.kminicial = kmi
            dados.kmfinal = kmf
            dados.kmrodado = kmr
            dados.media = consumo
            dados.idcidade = cidade
            dados.idpagamento = pg
            dados.save()
            return f'Despesa {tipo.tipo}, {acao} com sucesso!!!'
        except:
            return 'Dados NÂO salvos!!!'
    
    def getDespesas(self):
        try:
            return Despesas.objects.all()
        except:
            return list()
