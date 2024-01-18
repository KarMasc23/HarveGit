import mysql.connector

# essa parte vai criar a conexao
conn = mysql.connector.connect(
    user = 'root',
    password = 'root',
    host = '127.0.0.1',
    database = 'meu',
    port = '3307'
)
# teste de conexão
# if conn.is_connected():
#     print("Conectamos")

#essa parte vai criar o codigo
print("Este e um jogo pedra papel e tesoura")
print("Insira seu nome")
nome_jogador = input()

while True:
    print("Insira a sua jogada")
    jogador = input()

    computador = 'PEDRA'

    if jogador == computador:
        resultado = 'EMPATE'
    elif jogador == 'PAPEL':
        resultado = 'VITORIA'
    else:
        resultado = 'DERROTA'

    print(resultado)

# essa parte vai criar o cursor (criar uma query de inserção do mysql)
    cursor = conn.cursor()
    query = f"""
        INSERT INTO contagem_jogos 
            (nome_player, jogada_player, jogada_computador, resultado)
        VALUES
            ('{nome_jogador}', '{jogador}', '{computador}', '{resultado[0]}')
    """
    #aqui ele vai conectar e executar essa query
    cursor.execute(query)
    conn.commit()
    cursor.close()

    print("Deseja continuar jogando? S/N")
    continuar = input()
    if continuar == 'N':
        break
