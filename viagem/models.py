from django.db import models


class Carros(models.Model):
    placa = models.CharField(name='placa', unique=True, max_length=7)
    modelo = models.CharField(name='modelo', max_length=150)


class Cidades(models.Model):
    nome = models.CharField(name='nome', unique=True ,max_length=100)
    estado = models.CharField(name='estado', max_length=2)

    def salveCidade(self, post: dict) -> str:
        nome: str = post['nome']
        estado: str = post['estado']
        self.nome = nome.title().strip()
        self.estado = estado.title().strip()
        try:
            self.save()
            return 'Dados salvos com sucesso!!'
        except:
            return False

class Pagamentos(models.Model):
    forma = models.CharField(name='forma', unique=True, max_length=50)

class Tipos(models.Model):
    tipo = models.CharField(name='tipo', max_length=50, unique=True)

class Usuario(models.Model):
    nome = models.CharField(name='usuario', max_length=150)
    login = models.CharField(name= 'login', max_length=20)
    senha = models.CharField(name='senha', max_length=15)
    email = models.CharField(name='email', max_length=100)

class NomeViagem(models.Model):
    nome = models.CharField(name='nome', max_length=100)
    datainicio = models.DateField(name='datainicio')
    datafinal = models.DateField(name='datafinal')
    carro = models.ForeignKey(Carros, on_delete=models.CASCADE, name='idcarro')
    usuario = models.ForeignKey(Usuario, name='ususario', on_delete=models.CASCADE)
    atividade = models.BooleanField(name='atividade')

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



