from time import sleep
import pandas as pd


def menu():
    print("\n\n#####################\n")
    print("Welcome to the Quiz!!")
    name = input("\nWhat is your name? ")
    print(f"\nHello, {name}. The quiz will contain 5 multiple choice questions.")
    print("Your answer must be either 1, 2, or 3. Lets Begin!")
    sleep(3)
    data(name)


def data(name):
    df = pd.read_csv("data.csv")
    quiz(name, df)


def quiz(name, df):
    score = 0
    i = 0
    while i < 5:
        print("\n\n#####################\n")
        print(f"Question {i + 1}.\n")
        print(df.iloc[i]["Questions"])
        sleep(1)
        print(df.iloc[i]["Answers"])
        choice = input("\nAnswer: ")
        sleep(0.5)
        choice = int_range(choice)
        score = is_correct(choice, df.iloc[i]["Correct Answers"], score)
        i = i + 1
        sleep(2)
    print (f"\n\n{name} your final score is: {score}/5! Well done!")


def int_range(choice):
    try:
        choice = int(choice)
        if 0 < choice < 4:
            return int(choice)
        else:
            return choice
    except ValueError:
        return choice


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