# Python quiz game

questions = ("How many continents are there?: ",
             "What is the capital of India?: ",
             "How heavy is an adult elephant?: ",
             "What is the smallest country in the world?: ",
             "What is the longest river in the world?: ")

options = (("A. 5","B. 6","C. 7","D. 8"),
           ("A. Budapest","B. London","C. Paris","D. New Delhi "),
           ("A. 1000 Kg","B. 1200 Kg","C. 1400 kg","D. Above 1600 kg"),
           ("A. Malta","B. Maldives ","C. Tuvalu","D. Vatican City"),
           ("A. Congo","B. Yangtze","C. Amazon ","D. Nile"))

answers = ("C", "D", "D", "D", "D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input("Enter A, B, C or D: ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer.")
    question_num += 1
print("----------------------------------")
print("             RESULTS              ")
print("----------------------------------")

print("Answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")

score = int(score / len(questions) * 100)
print()
print(f"Your score is: {score}%")