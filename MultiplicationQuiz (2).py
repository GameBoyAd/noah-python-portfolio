#Noah Dong
#Multiplication Quiz


#Init

import random
import time

#Function



#Main
total_correct = 0
start_time = time.time()
questionyouwant = int(input("How many question do you want to do?"))

for i in range(questionyouwant):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    result = num1 * num2

    print(f"Question {i + 1}")
    user_answer = int(input(f"What is the product of {num1} and {num2}? "))
    if user_answer == result:
        print("Correct!")
        total_correct += 1
    else:
        print("Incorrect. The correct answer is", result)

print("Your total score is", total_correct, "out of 5")

end_time = time.time()
elapsed_time = end_time - start_time

print("It took you", elapsed_time, "seconds")
