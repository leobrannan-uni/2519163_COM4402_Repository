#from time import sleep


def menu():
    print("\n\n#####################\n")
    print("Welcome to the Quiz!!")
    name = input("\nWhat is your name? ")
    print(f"\nHello, {name}. The quiz will contain 5 multiple choice questions where your answer must be either A, B, or C. Lets Begin!")
    #sleep(3)
    data(name)

def quiz(questions, answers, correct_answers, name):
    score = 0
    i = 0
    while i < 5:
        print("\n\n#####################\n")
        print(f"Question {i + 1}. \n{questions[i]}\n")
        print(answers[i])
        choice = input("\nAnswer: ")
        check_answer(choice, correct_answers, i, score)
        i = i + 1

    print (f"\n\n{name} your final score is: {score}/5! Well done!")

def check_answer(choice, correct_answers, i, score):
        while True:
            choice = is_int(choice, correct_answers, i)
            in_range(choice, correct_answers, i)
            score = is_correct(choice, correct_answers, score, i)
            break

def is_int(choice, correct_answers, i):
    try:
        return int(choice)
    except ValueError:
        print(f"\nIncorrect! the correct answer is {correct_answers[i]}")
        return False

def in_range(choice, correct_answers, i):
    if 0 < choice < 4:
        return True
    else:
        print(f"\nIncorrect! the correct answer is {correct_answers[i]}")
        return False

def is_correct(choice, correct_answers, score, i):
    if choice == correct_answers[i]:
        #sleep(0.5)
        print("\nCorrect!")
        score = score + 1
        #sleep(2)
        return True
    else:
        #sleep(0.5)
        print(f"\nIncorrect! the correct answer is {correct_answers[i]}")
        # print
        #sleep(2)
        return False


def data(name):
    questions = ("What German became the recent England football manager?", "What sauce is traditionally served with Turkey?", "What vehicle is used by Santa and ran using Christmas Spirit?", "The bestselling book 'Glucose Revolution' is subtitled 'the Life-changing Power of Balancing Your Blood' what?", "Meerkat Movies is a promotion by what comparison website?")
    answers = ("1. Thomas Tuchel. 2. Thomas Frank. 3. Thomas Muller.", "1. Mint. 2. Gravy. 3. Cranberry.", "1. Car. 2. Sleigh. 3. Bicycle.", "1. Pressure. 2. Alcohol Content. 3. Sugar.", "1. Compare the Market. 2. Confused. 3. Money Supermarket.")
    correct_answers = (1, 3, 2, 3, 1)
    quiz(questions, answers, correct_answers, name)






if __name__ == "__main__":
    menu()
