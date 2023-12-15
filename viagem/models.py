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
            if id == '':
                self.placa = plac
                self.modelo = model
                self.save()
            else:
                car = Carros.objects.get(id=id)
                car.placa = plac
                car.modelo = model
                car.save()
            return f'Carros {plac}, {acao} com sucesso !!'
        except:
            return 'Dados NÃO salvos!!!'
    
class Cidades(models.Model):
    nome = models.CharField(name='nome', unique=True ,max_length=100)
    estado = models.CharField(name='estado', max_length=2)

    def salveCidade(self, post: dict) -> str:
        acao = 'salvo'
        id = post['id']
        nome: str = post['nome']
        estado: str = post['estado']
        nome = nome.title().strip()
        estado = estado.title().strip()
        try:
            if id == '':
                self.nome = nome
                self.estado = estado
                self.save()
            else:
                cid = Cidades.objects.get(id=id)
                cid.nome = nome
                cid.estado = estado
                cid.save()
            return f'Cidade {nome}, {acao} com sucesso!!'
        except:
            return 'Dados NÃO salvos!!!'

class Pagamentos(models.Model):
    forma = models.CharField(name='forma', unique=True, max_length=50)

    def savePagamentos(self, post: dict) -> str:
        acao = 'salvo'
        id = post['id']
        frm = post['tipo']
        frm = frm.strip().title()
        try:
            if id == '':
                self.forma = frm
                self.save()
            else:
                pag = Pagamentos.objects.get(id=id)
                pag.forma = frm
                pag.save()
            return f'Forma de pagamento {frm}, {acao} com sucesso!!!'
        except:
            return 'Dados NÂO salvos!!'

class Tipos(models.Model):
    tipo = models.CharField(name='tipo', max_length=50, unique=True)

    def saveTipos(self, request) -> str:
        acao = 'salvo'
        id = request.POST.get('id')
        tp = request.POST.get('tipo')
        tp = tp.strip().title()
        try:
            if id == '':
                self.tipo = tp
                self.save()
            else:
                tipoid = Tipos.objects.get(id=id)
                tipoid.tipo = tp
                tipoid.save()
                acao = 'alterado'
            return f'Tipos de despesa {tp}, {acao} com sucesso!!'
        except:
             return 'Dados NÂO salvos!!'

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
        print(nome)
        print(post)
        try:
            if id == '':
                self.usuario = nome
                self.login = login
                self.email = email
                self.senha = senha
                self.save()
            else:
                user = Usuario.objects.get(id=id)
                user.usuario = nome
                user.login = login
                user.email = email
                user.senha = senha
                acao = 'alterado'
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
        print(post)
        acao = 'salvo'
        id = post['id']
        nome = post['nome']
        nome = nome.strip().title()
        datainicio = post['datai']
        datafim = post['dataf']
        car = post['carro']
        car = Carros.objects.get(id=car)
        print(car)
        usuario = Usuario.objects.get(id=post['user'])
        try:
            atv = post['atv']
        except KeyError:
            atv = 0
        try:
            if id == '':
                self.nome = nome
                self.datainicio = datainicio
                self.datafinal = datafim
                self.idcarro = car
                self.usuario = usuario
                self.atividade = atv
                self.save()
            else:
                nomev = NomeViagem.objects.get(id=id)
                nomev.nome = nome
                nomev.datainicio = datainicio
                nomev.datafinal = datafim
                nomev.idcarro = car
                nomev.usuario = usuario
                nomev.atividade = atv
                nomev.save()
                acao = 'alterado'
            return f'Viagem {nome}, {acao} salvo com sucesso!!'
        except:
            return 'Dados NÂO salvos!!'
        
    def getNomeViagem(self):
        try:
            return NomeViagem.objects.all()
        except:
            return list()


class Despesas(models.Model):
    nomeviagem = models.ForeignKey(NomeViagem, name='idnomeviagem', on_delete=models.CASCADE)
    data = models.DateField(name='data')
    tipo = models.ForeignKey(Tipos, name='idtipo', on_delete=models.CASCADE)
    qnt = models.DecimalField(name='qnt',decimal_places=2, max_digits=10)
    valor = models.DecimalField(name='valor', decimal_places=2, max_digits=10)
    nota = models.IntegerField(name='nota')
    kminicial = models.IntegerField(name='kminicial')
    kmfinal = models.IntegerField(name='kmfinal')
    kmrodado = models.IntegerField(name='kmrodado')
    media = models.DecimalField(name='media', decimal_places=2, max_digits=10)
    cidade = models.ForeignKey(Cidades, name='idcidade', on_delete=models.CASCADE)
    pagamento = models.ForeignKey(Pagamentos, name='idpagamento', on_delete=models.CASCADE)



