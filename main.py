l = len('Bem vindo a Empresa do Ronald Gabriel Costa Silva')

def cadastrar_funcionario(id): #Funcao para cadastrar funcionario
    print('MENU CADASTRAR FUNCIONARIO'.center(l, '-'))
    print(f'Id do funcionário: {id}')
    nome = (input('Digite o nome do funcionario: '))
    setor = (input('Digite o setor do funcionario: '))
    salario = (input('Digite o salário do funcionário: '))
    cadastroFuncionario = {'id': id, 'nome':nome, 'setor':setor, 'salario':salario }
    return cadastroFuncionario

def consultar_funcionario(): #Funcao para consultar todos os funcionario, por id e por setor
   while True: 
    print('MENU CONSULTAR FUNCIONARIO'.center(l, '-'))
    print('Escolha a opção desejada: ')
    print('1 - Consultar todos os funcionários')
    print('2 - Consultar funcionário por id')
    print('3 - Consultar funcionário(s) por setor')
    print('4 - Retornar ao menu principal')
    consult = (int(input('>>'))) 
    if consult == 1 :
        for i in range(len(lista_funcionarios)):
            print(f'ID: {lista_funcionarios[i]["id"]} \nNome: {lista_funcionarios[i]["nome"]} \nSetor: {lista_funcionarios[i]["setor"]} \nSalário: {lista_funcionarios[i]["salario"]}')
            print()
    elif consult == 2:
        id = int(input('Digite o id do funcionario: '))
        for i in range (len(lista_funcionarios)):
            if id == lista_funcionarios[i]['id']:
                print(f'ID: {lista_funcionarios[i]["id"]} \nNome: {lista_funcionarios[i]["nome"]} \nSetor: {lista_funcionarios[i]["setor"]} \nSalário: {lista_funcionarios[i]["salario"]}')
                print()
    elif consult == 3:
        setor = input('Informe o setor do funcionário: ')
        for i in range(len(lista_funcionarios)):
            if setor == lista_funcionarios [i] ['setor']:
                print(f'ID: {lista_funcionarios [i]['id']} \nNome: {lista_funcionarios[i]['nome']} \nSetor: {lista_funcionarios[i]['setor']} \nSalário: {lista_funcionarios[i]['salario']}')
                print()
    elif consult == 4 :
            break
    else:
        if consult not in [1, 2, 3, 4]:
            print('Opção inváida')
            print()
            continue

def remover_funcionario(): #Funcao para remover funcionario por id
    print('MENU REMOVER FUNCIONÁRIO'.center(l, '-'))
    remov = int(input(('1 - Digite o id do funcionário a ser removido: ')))
    for i in range (len(lista_funcionarios)):
        if remov == lista_funcionarios[i]['id']:
            del lista_funcionarios[i]
            print(f'Funcionário com id {remov} removido com sucesso!')
            break
        else:
            print(f'Funcionário com id {remov} não encontrado.')
            continue

lista_funcionarios = [] #Lista para armazenar os funcionarios(dicionarios)
id_global =  5209902 #Id global

#Programa principal
while True:
  print() 
  print('Bem vindo a Empresa do Ronald Gabriel Costa Silva')
  print('-' * l )
  print('MENU PRINCIPAL'.center(l, '-'))
  print('Escolha a opção desejada:')
  print('1 - Cadastrar Funcionário')
  print('2 - Consultar Funcionário(s)')
  print('3 - Remover Funcionário')
  print('4 - Sair')
  op = (int(input('>>')))
  print()

  if op == 1:
   cadastrarFuncionario = cadastrar_funcionario(id_global)
   print()
   lista_funcionarios.append(cadastrarFuncionario.copy())
   id_global += 1
   continue
  elif op == 2:
    consultarFuncionario = consultar_funcionario()
    print()
    continue
  elif op == 3:
    removerFuncionario = remover_funcionario()
    print()
    continue
  elif op == 4:
     break
  elif op not in [1, 2, 3, 4]:
     print('Opção inválida')
     print()
     continue        
  
