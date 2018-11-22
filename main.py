import sys
import datetime
from datetime import timedelta

class carro():
    def __init__(self, marca, modelo,ano,diaria,status,idv):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.diaria = diaria
        self.status = status
        self.idv = idv

class aluguel():
    def __init__(self, nomeloc, prazo, idv, dias):
        self.nomeloc = nomeloc
        self.prazo = prazo
        self.idv = idv
        self.dias = dias

class reserva():
    def __init__(self, nomeloc, prazo, idv, dias):
        self.nomeloc = nomeloc
        self.prazo = prazo
        self.idv = idv
        self.dias = dias


print('Bem vindo\n')
cont = 1
agora = datetime.datetime.now()
cad = 0
alu = 0
atr = 0
idveiculo = 1
reservas = []
alugueis = []
carros = []
while cont == 1:
    print('Data atual: %d/%d/%d\nQuantidade de veículos cadastrados: %d\n'
          'Quantidade de veículos alugados: %d\nQuantidade de atrasos: %d\n\n' % (agora.day, agora.month, agora.year, cad,alu, atr))

    op = input('a. Consultar veículos\nb. Adicionar veículos\n'
               'c. Alugar/reservar veículos\nd. Devolver/liberar veículos\n'
               'e. Excluir veículos\nf. Avançar data atual\ng. Sair\n')

    if op == 'a':
        for carro in carros:
            print ('Id:%d Modelo:%s Status:%s\n' % (carro.idv,carro.modelo,carro.status))

        opa = input('Deseja mais detalhes de algum carro?\n s.Sim \nn.Não\n')
        if opa == 's':
            ida = int(input('Digite o id do carro:\n'))
            ida = ida - 1
            print('Id:%d Modelo:%s Marca:%s Ano:%s Diaria:%f Status:%s' % (carros[ida].idv, carros[ida].modelo,
                                                                           carros[ida].marca, carros[ida].ano,
                                                                           carros[ida].diaria, carros[ida].status))
        print('\n\n\n')
    if op == 'b':
        marca = input('Marca:\n')
        modelo = input('Modelo:\n')
        ano = int(input('Ano:\n'))
        diaria = float(input('Diária:\n'))
        status = 'Disponível'
        carros.append(carro(marca, modelo, ano, diaria, status, idveiculo))
        idveiculo += 1
        cad += 1
    if op == 'c':
        opc = input('Deseja alugar ou reservar?\na.alugar\nr.reservar\n')
        if opc == 'a':
            nomeloc = input('Nome do locatário:')
            idv = int(input('Id do veículo:'))
            if carros[idv-1].status != 'Disponível':
                print('Carro indisponível')
            else:
                prazo = int(input('Prazo de locação:'))
                while prazo > 30:
                    print('Prazo muito grande')
                    prazo = int(input('Prazo de locação:'))
                dias = prazo
                prazo = agora + timedelta(days=prazo)
                alugueis.append(aluguel(nomeloc, agora, idv, dias))
                carros[idv - 1].status = 'Alugado'
                alu += 1
        if opc == 'r':
            nomeloc = input('Nome do locatário:')
            idv = int(input('Id do veículo:'))
            if carros[idv - 1].status != 'Disponível':
                print('Carro indisponível')
            else:
                prazo = int(input('Prazo de locação:'))
                while prazo > 30:
                    print('Prazo muito grande')
                    prazo = int(input('Prazo de locação:'))
                dias = prazo
                prazo = agora + timedelta(days=prazo)
                reservas.append(aluguel(nomeloc, agora, idv, dias))
                carros[idv - 1].status = 'Reservado'

    if op == 'd':
        idv = int(input('Id do veículo:'))
        if carros[idv-1].status != 'Disponível':
            if carros[idv-1].status == 'Alugado':
                diff = agora - carros[idv-1].prazo
                result = int(diff.days) * carros[idv-1].diaria
                print('Preço a ser pago: R$ %f' & result)
            carros[idv - 1].status = 'Disponível'
        else:
            print('Devolução indisponível')

    if op == 'e':
        idv = int(input('Id do veículo:'))
        if carros[idv-1].status != 'Disponível':
            print('Remoção indisponível')
        else:
            carros.remove(idv-1)
            print('Carro removido')
            cad -= 1

    if op == 'f':
        agora = agora + timedelta(days=1)
        for carro in carros:
            for aluguel in alugueis:
                if aluguel.idv == carro.idv:
                    if aluguel.prazo + timedelta(days=aluguel.dias) == agora:
                        if carro.status == "Alugado":
                            carro.status = "Atrasado"
                            alu -= 1
                            atr += 1
    if op == 'g':
        exit()