from time import sleep
import pandas as pd


def menu():
    print("\n\n#####################\n")
    print("Welcome to the Quiz!!")
    name = input("\nWhat is your name? ")
    print(f"\nHello, {name}. The quiz will contain 5 multiple choice questions.")
    print("Your answer must be either 1, 2, or 3. Lets Begin!\n")
    sleep(3)
    data(name)


def data(name):
    df = pd.read_csv("data.csv")
    quiz(name, df)


def quiz(name, df):
    score = 0
    i = 0
    while i < 5:
        question(df, i)
        sleep(0.5)
        choice = choice_range(df, i)
        score = is_correct(choice, df.iloc[i]["Correct Answers"], score)
        i = i + 1
        sleep(1.5)
    print (f"\n\n{name} your final score is: {score}/5! Well done!")


def question(df, i):
    print("\n#####################\n")
    print(f"Question {i + 1}.\n")
    print(df.iloc[i]["Questions"])
    sleep(1)
    print("\n", df.iloc[i]["Answers"])


def choice_range(df, i):
    while True:
        choice = input("\nAnswer: ")
        try:
            choice = int(choice)
            if 0 < choice < 4:
                return int(choice)
            else:
                print("Enter a number between 1 and 3. Please try again.")
                sleep(1)
                question(df, i)
        except ValueError:
            print("Incorrect value entered, please try again.")
            sleep(1)
            question(df, i)


def is_correct(choice, correct_answers, score):
    if choice == correct_answers:
        print("\nCorrect!")
        score = score + 1
        return score
    else:
        print(f"\nIncorrect! the correct answer is {correct_answers}")
        return score


if __name__ == "__main__":
    menu()