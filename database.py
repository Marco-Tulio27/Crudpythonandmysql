import mysql.connector
# faz a conexão com o banco de dados
cnx = mysql.connector.connect(user='root', password='',
host='localhost',
database='crud')
# cria um cursor para executar comandos SQL
class database():
    def insert():
        try:    # insere um novo registro na tabela cliente
            cursor = cnx.cursor()
            nome = input('Digite seu nome: ')
            idade = int(input('Digite sua idade: '))
            profissao = input('Digite sua profissão: ')

            # protege contra injeção de SQL
            sql = "INSERT INTO CLIENTE (nome, idade, profissao) VALUES (%s, %s, %s)"
            val = (nome, idade, profissao)
            cursor.execute(sql, val)
            cnx.commit()
            cursor.close()
            cnx.close()
        except Exception as e:
                print(f'Erro ao cadastrar o cliente: {e}')        
            # fecha a conexão com o banco de dados
    def delete():
        try:
            cursor = cnx.cursor()
            nome = input('Para deletar um cliente, Digite seu nome: ')
            # protege contra injeção de SQL
            sql = "DELETE FROM CLIENTE WHERE nome = %s"
            val = (nome,)
            cursor.execute(sql, val)
            cnx.commit()
            cursor.close()
        except Exception as e:
                print(f'Erro ao deletar o cliente: {e}')
    def read():
        cursor = cnx.cursor()
        sql = "SELECT * FROM cliente"
        cursor.execute(sql)
        result = cursor.fetchall()
        cnx.close()
        for row in result:
            print(row)
    
    def update():
        cursor = cnx.cursor()
        print('''O que deseja editar?
            1- Nome
            2- Profissão
            3- Idade''')
        opcao = int(input('Digite a opção que deseja alterar: '))
        if opcao == 1:
            try:
                nome = input('Para editar um cliente, digite seu nome atual: ')
                novonome = input('Digite o novo nome: ')
                id = int(input('Agora digite o ID do cliente que você deseja editar: '))
                sql = f"UPDATE CLIENTE SET nome='{novonome}' WHERE nome='{nome}' AND id={id}"
                cursor.execute(sql)
                cnx.commit()
                cnx.close()
            except Exception as e:
                print(f'Erro ao editar o cliente: {e}')
        if opcao == 2:
            try:
                profissao = input('Para editar um cliente, digite sua profissão atual: ')
                novaprofissao = input('Digite o nova Profissão: ')
                id = int(input('Agora digite o ID do cliente que você deseja editar: '))
                sql = f"UPDATE CLIENTE SET profissao='{novaprofissao}' WHERE profissao='{profissao}' AND id={id}"
                cursor.execute(sql)
                cnx.commit()
                cnx.close()
            except Exception as e:
                print(f'Erro ao editar o cliente: {e}')
        if opcao == 3:
            try:
                idade = input('Para editar um cliente, digite sua idade atual: ')
                novaidade = input('Digite o nova idade: ')
                id = int(input('Agora digite o ID do cliente que você deseja editar: '))
                sql = f"UPDATE CLIENTE SET nome='{novaidade}' WHERE nome='{idade}' AND id={id}"
                cursor.execute(sql)
                cnx.commit()
                cnx.close()
            except Exception as e:
                print(f'Erro ao editar o cliente: {e}')

        #id=int(input('Agora digite o id do cliente que '))
        # insere um novo registro na tabela cliente
        #sql = "UPDATE CLIENTE SET nome='kaio1' where(nome='kaio')"
        #cursor.execute(sql)
        #cursor.execute("SELECT * FROM cliente")
        #result=cursor.fetchall()
        # confirma as alterações na transação
        #cnx.commit()
        #cnx.close()
        #database.update()
        
        