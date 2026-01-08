#draft 1

print("Welcome to the Quiz!!")
name = input("What is your name? ")
print(f"\nHello, {name}. The quiz will contain 5 multiple choice questions where your answer must be either A, B, or C. Lets Begin!\n")

questions = ("What German became the recent England football manager?", "What sauce is traditionally served with Turkey?", "What vehicle is used by Santa and ran using Christmas Spirit?", "The bestselling book 'Glucose Revolution' is subtitled 'the Life-changing Power of Balancing Your Blood' what?", "Meerkat Movies is a promotion by what comparison website?")
answers = ("A. Thomas Tuchel. B. Thomas Frank. C. Thomas Muller.", "A. Mint. B. Gravy. C. Cranberry.", "A. Car. B. Sleigh. C. Bicycle.", "A. Pressure. B. Alcohol Content. C. Sugar.", "A. Compare the Market. B. Confused. C. Money Supermarket.")
correct_answers = ("A", "C", "B", "C", "A")
score = 0
i = 0

while i < 5:
    print(questions[i])
    print(answers[i])
    choice = input("Answer: ").upper()
    if choice == correct_answers[i]:
        print("Correct!")
        score = score + 1
    else:
        print("Incorrect!")
    i = i + 1

print(f"{name} your score is: {score}! Well done!")
