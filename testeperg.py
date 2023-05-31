import mysql.connector

# Conecta ao banco de dados
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ritdiw-jomjiw-8jIxbe",
    database="Registro_usuario"
)
# Cria o cursor


# Função para exibir uma pergunta e verificar a resposta
def exibir_pergunta(id_pergunta):
    # Recupera a pergunta do banco de dados
    cursor = conexao.cursor()
    cursor.execute("SELECT Pergunta, Resposta FROM Perguntas WHERE ID = %s", (id_pergunta,))
    pergunta, resposta_correta = cursor.fetchone()
    cursor.close()

    # Exibe a pergunta para o usuário
    print("Pergunta:", pergunta)
    resposta_usuario = input("Resposta: ")

    # Verifica se a resposta está correta
    if resposta_usuario.lower() == resposta_correta.lower():
        print("Resposta correta!")
        # Atualiza a pontuação do usuário no banco de dados
        cursor = conexao.cursor()
        cursor.execute("UPDATE Pontuacao SET Pontos = Pontos + 1 WHERE Usuario = %s", (nome_usuario,))
        conexao.commit()
        cursor.close()
    else:
        print("Resposta incorreta!")

# Obtém o nome do usuário
nome_usuario = input("Digite seu nome: ")

# Define a quantidade de perguntas a serem feitas
quantidade_perguntas = 3

# Loop para exibir as perguntas e obter as respostas
for i in range(1, quantidade_perguntas + 1):
    print("\nPergunta", i)
    exibir_pergunta(i)

# Fecha a conexão com o banco de dados
conexao.close()
