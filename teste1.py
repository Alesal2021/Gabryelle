import random
from datetime import date
random.seed(100)

lista_movimento2 = {}
incricao_movimento2 = []
lista_movimento = {}
incriscao_movimento = []
nova_lista = {}
inscricao = []
def cadastro():
    cliente = input('Digite o nome do cliente:')
    conteiner = int(input('Digite o numero do conteiner:'))
    tipo = int(input('Digite o Tipo: 20 / 40:'))
    status = input('Digite o Status: Cheio / Vazio:')
    categoria = input('Importação / Exportação')

    nova_lista['cliente'] = cliente
    nova_lista['conteiner numero'] = random.randint(100, 400, )
    nova_lista['Tipo: 20 / 40'] = tipo
    nova_lista['status'] = status
    nova_lista['categoria'] = categoria
    inscricao.append(nova_lista.copy())
    print(inscricao)

def listamenu():
    print('---lista de Inscritos---')
    for e in inscricao:
        for i, j in e.items():
            print('{}={}'.format(i, j, ))
        print('------------------')
def embarque():
    nome_do_navio = input('Digite o nome do navio e pais de origem:')
    gate_out = input('Qual o portão de saida')
    scaner = input('Situação do scanner aprovado/reprovado')
    pesagem = float(input('Qual o peso do conteiner'))


    lista_movimento['nome_do_navio'] = nome_do_navio
    lista_movimento['gate_out'] = gate_out
    lista_movimento['scaner'] = scaner
    lista_movimento['pesagem'] = pesagem
    lista_movimento['data'] = date.today()
    incriscao_movimento.append(lista_movimento)
    print(incriscao_movimento)


def descarga():
    nome_do_navio = input('Digite o nome do navio e pais de origem:')
    gate_in = input('Qual o portão de entrada')
    scaner = input('Situação do scanner de descarga aprovado/reprovado')
    pesagem = float(input('Qual o peso do conteiner'))
    box = input('Digite o numero do box de armazenamento')
    hora = input('digite a hora de descarga')
    tipo = input('digite o tipo de produto')

    lista_movimento2['navio'] = nome_do_navio
    lista_movimento2['gate_in'] = gate_in
    lista_movimento2['Scanner'] = scaner
    lista_movimento2['Pesagem'] = scaner
    lista_movimento2['Box'] = box
    lista_movimento2['Hora'] = hora
    lista_movimento2['Tipo'] = tipo
    lista_movimento2['data'] = date.today()
    incricao_movimento2.append(lista_movimento2)
    print(incricao_movimento2)

def list_embarque():
    print('---lista de embarque---')
    for a in incriscao_movimento:
        for c, d in a.items():
            print('{}={}'.format(c, d, ))
        print('------------------')
def list_desembarque():
    print('---lista de Desembarque---')
    for h in incricao_movimento2:
        for f, g in h.items():
            print('{}={}'.format(f, g, ))
    print('------------------')



def movimentacao():
    while True:

            print('**********Tipo de  movimentacao***********')
            print('1 - Embarque')
            print('2 - Descarga')
            print('3- Verificar Embarque')
            print('4- Verificar Desembarque')
            print('0 - Encerrar')
            opcao1 = int(input('Opção escolhida:'))
            if opcao1 == 1:
                embarque()
            elif opcao1 == 2:
                descarga()
            elif opcao1 == 3:
                list_embarque()
            elif opcao1 == 4:
                list_desembarque()
            elif opcao == 0:
                print('**********Menu Contêiner***********')
                cadastro()

while True:
  try:
    print('**********Menu Contêiner***********')
    print('1 - Nova inscrição de clientes')
    print('2 - Visualizar inscrição')
    print('3- movimentação')
    print('0 - Encerrar')
    opcao = int(input('Opção escolhida:'))
    if opcao == 1:
        cadastro()
    elif opcao == 2:
        listamenu()
    elif opcao == 3:
        movimentacao()
    elif opcao != 0:
        print('Erro: digite uma opção válida!”.')
    elif opcao == 0:
        print('Programa encerrado')
        break
  except ValueError:
        print('Operação invalida')

