import tkinter as tk
import mysql.connector

class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer
    
    def display_question(self):
        question_label.config(text=self.question + '\n\n' + '\n'.join(self.options), fg="black")

class Game:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.current_question = 0
    
    def check_answer(self, user_answer):
        question = self.questions[self.current_question]
        if question.answer == user_answer:
            self.score += 1
            self.show_message("Resposta correta!")
        else:
            self.show_message("Resposta incorreta!")
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.display_question()
        else:
            self.end_game()
    
    def display_question(self):
        question = self.questions[self.current_question]
        question.display_question()
    
    def end_game(self):
        self.show_message(f"Sua pontuação final: {self.score}/{len(self.questions)}")
        self.store_score()
        root.quit()
        
    def show_message(self, message):
        message_label.config(text=message)
    
    def store_score(self):
        connection = mysql.connector.connect(
            host="seu_host",
            user="seu_usuario",
            password="sua_senha",
            database="seu_banco_de_dados"
        )
        cursor = connection.cursor()

        nome_usuario = "exemplo_usuario"
        pontuacao_final = self.score

        query = "UPDATE Usuarios SET Pontuacao = %s WHERE usuario = %s"
        cursor.execute(query, (pontuacao_final, nome_usuario))

        connection.commit()
        connection.close()

# Criar perguntas
question1 = Question("Qual é a capital da França?", ["a) Paris", "b) Londres", "c) Berlim", "d) Roma"], 1)
question2 = Question("Quem pintou a Mona Lisa?", ["a) Van Gogh", "b) Picasso", "c) Leonardo da Vinci", "d) Michelangelo"], 3)
question3 = Question("Quanto é 2 + 2?", ["a) 2", "b) 3", "c) 4", "d) 5"], 3)

# Criar jogo
game = Game([question1, question2, question3])

# Configurar a interface gráfica
root = tk.Tk()
root.title("Show do Milhão")
root.geometry("600x400")
root.configure(bg="#FDFEFE")

question_label = tk.Label(root, wraplength=500, font=("Arial", 14), fg="#2C3E50", bg="#FDFEFE")
question_label.pack(pady=20)

colors = ["#1ABC9C", "#3498DB", "#9B59B6", "#F1C40F"]
for i in range(4):
    button = tk.Button(root, text=f"Opção {i+1}", width=20, font=("Arial", 12), bg=colors[i], fg="white", bd=0,
                       command=lambda i=i: game.check_answer(i+1))
    button.pack(pady=5)

message_label = tk.Label(root, font=("Arial", 12), fg="black", bg="#FDFEFE")
message_label.pack(pady=10)

# Iniciar o jogo
game.display_question()

# Iniciar a interface gráfica
root.mainloop()

