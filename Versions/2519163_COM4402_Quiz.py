from time import sleep # this is used to give delays inbetween information
import pandas as pd # this is used for collecting data for the quiz using an external csv file

""" Function menu is used to introduce the user to the quiz, 
    asking for a name and explaining the structure. """
def menu():
    print("\n\n#####################\n")
    print("Welcome to the Quiz!!")
    name = input("\nWhat is your name? ")
    print(f"\nHello, {name}. The quiz will contain 5 multiple choice questions.")
    print("Your answer must be either 1, 2, or 3. Lets Begin!\n")
    sleep(3)
    data(name)

""" Function data is then ran, gathering the data from the csv file so questions, 
    answers and correct answers can be taken from the dataframe and into the program.
    This is expressed in the standard variable choice df. """
def data(name):
    df = pd.read_csv("data.csv")
    quiz(name, df)

""" Function quiz is the centre point of this program, having many different functions called 
    inside of it, with the program ending in this function. First of all, it creates the variables
    'i' and 'score', which are essential to the program. 'i' is the counter of which iteration 
    the user is on, used for things like gathering the correct data from the csv file and 
    outputting the correct question number before questions are asked. 'score' is used to keep a tally
    of how many correct answers the user has had out of the 5 answers given. A while loop is added, 
    capturing the functions inside this loop that iterates per question. The variable 'name' has 
    been passed through so that when the user gets their score it is more personalised. """
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

""" The first function called in quiz, question is simply used to print out the question and
    the multiple choice answers, with the help of the iloc function. This function allows specific
    data to be accessed using indexes, which is extremely helpful for this program. Using the variable
    'i', the correct question, answer and correct answer can be collected and used for the program. """
def question(df, i):
    print("\n#####################\n")
    print(f"Question {i + 1}.\n")
    print(df.iloc[i]["Questions"])
    sleep(1)
    print("\n", df.iloc[i]["Answers"])

""" Function choice_range then gets the user to input their answer and verifies if it is in the 
    correct range or not. the function will try to convert the string into an integer, and 
    if it can check if the input is in the range. if it is not in the range or not an integer,
    a unique error message will show, and the user can try again. """
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

""" Function is_correct takes the users correct input and verifies if it is the correct answer. 
    If it is not an error message will appear, and move on to the next question. """
def is_correct(choice, correct_answers, score):
    if choice == correct_answers:
        print("\nCorrect!")
        score = score + 1
        return score
    else:
        print(f"\nIncorrect! the correct answer is {correct_answers}")
        return score

""" This is the first thing that the code runs, as it is the only code outside a function.
    Used as standard practice, this if statement enables the first function to be called, 
    and the quiz to begin. """
if __name__ == "__main__":
    menu()