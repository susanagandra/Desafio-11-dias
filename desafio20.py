import json

def load_questions(file_path):
    with open(file_path, 'r') as file:
        questions = json.load(file)
    return questions

def run_quiz(questions):
    score = 0

    for q_data in questions:
        question = q_data["question"]
        options = q_data["options"]
        correct_option = q_data["correct_option"]

        print(question)

        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        user_answer = int(input("Opção correcta: "))

        if user_answer == correct_option:
            print("Correto!\n")
            score += 1
        else:
            print(f"Resposta incorreta. A resposta correta é {correct_option}: {options[correct_option - 1]}\n")

    print(f"Pontuação final: {score}/{len(questions)}")

# Carregar perguntas do arquivo
questions_data = load_questions('data.json')

# Executar o quiz com as perguntas fornecidas
run_quiz(questions_data)
