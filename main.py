import database
while True:
    print('''1- Cadastrar um cliente
2- Deletar um cliente
3- Ler lista de cliente
4- Alterar um cliente
0- Sair''')
    opcao = int(input("Selecione uma operacao: "))

    if opcao == 1:
        database.database.insert()
    elif opcao == 2:
        database.database.delete()
    elif opcao == 3:
        database.database.read()
    elif opcao == 4:
        database.database.update()
    elif opcao == 0:
        break
    else:
        print("Opção inválida. Selecione novamente.")