import random

def quiz():
    print("\nWelcome to the Quiz Game!")
    print("Answer the following questions by selecting the correct option.")
    
    # Create a list of dictionaries to store multiple choice questions, their correct answers, and possible incorrect answers
    questions = [
        {
            "question": "Who is the prime minister of India",
            "correct_answer": "Modi",
            "options": ["KCR", "Jagan", "Modi", "Rahul"]
        },
        {
            "question": "How many IPL titles has RCB won?",
            "correct_answer": "Zero",
            "options": ["One", "Two", "Three", "Zero"]
        },
        {
            "question": "Who is the director of RRR?",
            "correct_answer": "Rajamouli",
            "options": ["Rajamouli", "neel", "Hirani", "Sandeep"]
        }
    ]
    
    # Set up scoring variables
    correct_answers = 0
    incorrect_answers = 0
    
    # Randomly select the questions from the list
    random.shuffle(questions)
    
    # Iterate through each question in the list
    for question in questions:
        print("\n" + question["question"])
        
        # Randomly select the options for each question
        random.shuffle(question["options"])
        
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        
        # Prompt the user to choose the correct answer using input
        user_answer = input("Select the correct option: ")
        
        # Convert the user's answer to an integer and subtract 1 to get the index of the correct answer
        user_answer = int(user_answer) - 1
        
        if question["options"][user_answer] == question["correct_answer"]:
            correct_answers += 1
            print("Correct!")
        else:
            incorrect_answers += 1
            print("Incorrect.")
    
    # Print the final score
    print("\nFinal Score:")
    print(f"Correct Answers: {correct_answers}")
    print(f"Incorrect Answers: {incorrect_answers}")
    print(f"Percentage: {(correct_answers / len(questions)) * 100}%")

if __name__ == "__main__":
    while True:
        quiz()
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again != "yes":
            break