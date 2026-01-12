#draft 1

print("Welcome to the Quiz!!")
name = input("What is your name? ")
print(f"\nHello, {name}. The quiz will contain 5 multiple choice questions where your answer must be either A, B, or C. Lets Begin!\n")

questions = ("What German became the recent England football manager?", "What sauce is traditionally served with Turkey?", "What vehicle is used by Santa and ran using Christmas Spirit?", "The bestselling book 'Glucose Revolution' is subtitled 'the Life-changing Power of Balancing Your Blood' what?", "Meerkat Movies is a promotion by what comparison website?")
answers = ("1. Thomas Tuchel. 2. Thomas Frank. 3. Thomas Muller.", "1. Mint. 2. Gravy. 3. Cranberry.", "1. Car. 2. Sleigh. 3. Bicycle.", "1. Pressure. 2. Alcohol Content. 3. Sugar.", "1. Compare the Market. 2. Confused. 3. Money Supermarket.")
correct_answers = (1, 3, 2, 3, 1)
score = 0
i = 0

while i < 5:
    print(f"Question {i+1}. \n{questions[i]}")
    print(answers[i])
    choice = int(input("Answer: "))
    if choice == int(choice):
        if 0 < choice < 4:
            if choice == correct_answers[i]:
                print("Correct!")
                score = score + 1
            else:
                print(f"Incorrect! the correct answer is {correct_answers[i]}")
                #print("answer not correct")
        else:
            print(f"Incorrect! the correct answer is {correct_answers[i]}")
            #print("not in range")
    else:
        print(f"Incorrect! the correct answer is {correct_answers[i]}")
        #print("not defined as int")

    i = i + 1

print(f"{name} your score is: {score}! Well done!")
