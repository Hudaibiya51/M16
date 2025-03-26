# Define the quiz questions, options, and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "answer": "D"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["A. Charles Dickens", "B. William Shakespeare", "C. J.K. Rowling", "D. Mark Twain"],
        "answer": "B"
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
        "answer": "B"
    }
]

def run_quiz():
    score = 0
    total_questions = len(questions)

    print("Welcome to the Quiz Program!")
    print("Answer the following questions:")

    for index, q in enumerate(questions):
        print(f"\nQuestion {index + 1}: {q['question']}")
        for option in q['options']:
            print(option)

        answer = input("Your answer (A/B/C/D): ").upper()

        if answer == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")

    print(f"\nYour final score is: {score}/{total_questions}")
    if score == total_questions:
        print("Excellent! You got all the answers right!")
    elif score > total_questions // 2:
        print("Good job! You did well.")
    else:
        print("Better luck next time!")

# Run the quiz
run_quiz()
