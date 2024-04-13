import os
def Menu():
    clientes={}
    while True:
        os.system('cls')
        print('='*30)
        print('Gerenciamento de Clintes'.center(30))
        print('='*30)
        print(
            '''
            [1]-Listar Clientes
            [2]-Cadastrando Cliente
            [3]-Editando Cliente
            [4]-Excluindo Cliente
            [5]-Break
            '''
        )
        print('='*30)

        opcao = input('Selecione a sua opcao: ')
        print('='*30)

        match opcao:
            case '1':
                Listar_Clientes(clientes)
            case '2':
                Cadastrar_Clientes(clientes)
            case '3':
                Editando_Cliente(clientes)
            case '4':
                Excluindo_Cliente(clientes)
            case '5':
                break
        
        input('Aperte Enter para continuar')

def Listar_Clientes(clientes):

    for cliente in clientes:
        print(cliente)

def Cadastrar_Clientes(clientes):

    nome = input('Digite o nome: ')
    cpf = input('Digite o CPF:')
    telefone = input('Digite o telefone')
    endereco = input('Digite o endereco')

    cliente = {
        'nome': nome,
        'telefone': telefone,
        'endereco': endereco
    }

    clientes[cpf]= cliente

def Editando_Cliente(clientes):

    cpf = input('Digite o CPF do cliente que deseja editar')

    if cpf in clientes:
        nome = input('Digite o nome: ')
        telefone = input('Digite o telefone')
        endereco = input('Digite o endereco')

        cliente = {
          'nome': nome,
          'telefone': telefone,
          'endereco': endereco
        }

        clientes[cpf]= cliente
    else:
        print('Nao existe esse cliente')

def Excluindo_Cliente(clientes):

    cpf = input('Digite o CPF do cliente que deseja apagar')

    if cpf in clientes:
        valor_removido = clientes.pop(cpf)
    
    else:
        print('Nao existe esse cliente')

