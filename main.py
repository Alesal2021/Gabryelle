import random
import string
random.seed(100)
nova_lista = {}
inscricao = []

while True:
  try:
    print('**********Menu Contêiner***********')
    print('1 - Nova inscrição de clientes')
    print('2 - Visualizar inscrição')
    print('0 - Encerrar')
    opcao = int(input('Opção escolhida:'))
    if opcao == 1:

        cliente = input('Digite o nome do cliente:')
        conteiner = int(input('Digite o numero do conteiner:'))
        tipo = int(input('Digite o Tipo: 20 / 40:'))
        status = input('Digite o Status: Cheio / Vazio:')
        categoria = input('Importação / Exportação')

        nova_lista['cliente'] = cliente
        nova_lista['conteiner numero'] = random.randint(100,400,)
        nova_lista['Tipo: 20 / 40'] = tipo
        nova_lista['status'] = status
        nova_lista['categoria'] = categoria
        inscricao.append(nova_lista.copy())
        print(inscricao)



    elif opcao == 2:
        print('---lista de Inscritos---')
        for e in inscricao:
            for i, j in e.items():
                print('{}={}'.format(i, j,))
            print('------------------')

    elif opcao != 0:
        print('Erro: digite uma opção válida!”.')

    elif opcao == 0:
        print('Programa encerrado')
        break
  except ValueError:
        print('Operação invalida')
