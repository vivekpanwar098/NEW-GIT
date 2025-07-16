# Simple Quiz App in Python

def run_quiz(questions):
    score = 0
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Enter your answer (A/B/C/D): ").strip().upper()
        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}")
    print("\n🎯 Quiz Completed!")
    print(f"Your Score: {score} out of {len(questions)}")


# Define your questions here
quiz_questions = [
    {
        "question": "1. What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "2. Who developed Python?",
        "options": ["A. Dennis Ritchie", "B. James Gosling", "C. Guido van Rossum", "D. Bjarne Stroustrup"],
        "answer": "C"
    },
    {
        "question": "3. Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. def", "C. define", "D. func"],
        "answer": "B"
    },
    {
        "question": "4. What is the output of: 3 * 1 ** 3?",
        "options": ["A. 3", "B. 9", "C. 1", "D. 0"],
        "answer": "A"
    }
]

# Run the quiz
run_quiz(quiz_questions)
