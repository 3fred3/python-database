from mysql.connector import connect

conexao = connect(  # função com parâmetros nomeados
    host='localhost',
    port=3306,
    user='root',
    password='12345678'
)

# print(conexao)
