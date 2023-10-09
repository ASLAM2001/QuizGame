import random

# Define a list of questions, each represented as a dictionary
questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['London', 'Berlin', 'Paris', 'Madrid'],
        'correct_answer': 'Paris'
    },
    {
        'question': 'Which planet is known as the Red Planet?',
        'options': ['Mars', 'Venus', 'Jupiter', 'Saturn'],
        'correct_answer': 'Mars'
    },
    {
        'question': 'What is the largest mammal in the world?',
        'options': ['Elephant', 'Giraffe', 'Blue Whale', 'Hippopotamus'],
        'correct_answer': 'Blue Whale'
    }
]

# Function to display a question and its options
def display_question(question_obj):
    print(question_obj['question'])
    for i, option in enumerate(question_obj['options'], start=1):
        print(f"{i}. {option}")

# Function to check if the user's answer is correct
def check_answer(question_obj, user_answer):
    return question_obj['correct_answer'] == question_obj['options'][user_answer - 1]

# Shuffle the order of questions
random.shuffle(questions)

# Initialize the score
score = 0

# Iterate through each question
for question in questions:
    display_question(question)
    user_choice = int(input("Enter the number of your answer: "))

    if 1 <= user_choice <= len(question['options']):
        if check_answer(question, user_choice):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {question['correct_answer']}\n")
    else:
        print("Invalid choice. Skipping to the next question.\n")

# Display the final score
print(f"Quiz completed! Your score: {score}/{len(questions)}")
