import random




#----------------------------
def new_game():
    guesses = []
    question_num = 0
    points = 0

    for key in questions:
        print("/-----------------------/")
        print(key)
        for index in answers[question_num]:
            print(index)
        guess = input("Enter (A, B, C or D): ")
        guess = guess.upper()
        guesses.append(guess)

        points = points + check_answer(questions.get(key), guess)

        question_num += 1
    display_score(points, questions)
    play_again()


#----------------------------
def check_answer(correctAnswer, guess):
    if correctAnswer == guess:
        print("You are CORRECT!\n")
        return 1
    else:
        print("Not correct!\nThe correct anwer is "+correctAnswer,"\n")
        return 0
#----------------------------
def display_score(points, questions):
    print("/-----------------------/")
    score = int((points/len(questions))*100)
    print("YOUR SCORE IS: "+str(score)+"%!")
#----------------------------
def play_again():
    print("\n")
    response = (input("Do you want to play again? (yes/no): ").upper())
    if response == "YES":
        print("\n")
        new_game()
    else:
        print("Bye! Have a good day!")

questions = {
    "Who ate the chocolate?: ": "A",
    "What year is it now?: ": "B",
    "Where is Kazakhstan?: ": "C",
    "What is a rohlik?: ": "D"
}

answers = [["A. Akzhol", "B. Elon Musk", "C. Donald Trump", "D. Arthur Morgan"],
           ["A. 1999", "B. 2024", "C. 1386", "D. 2023"],
           ["A. Central Asia", "B. Europe", "C. Mars", "D. America"],
           ["A. a gun", "B. a toy", "C. Czech president", "D. pecivo"]]

new_game()