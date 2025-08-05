import random

number = random.randint(1, 100)
guess = 0
while guess != number:
    guess = int(input("ทายเลข (1-100): "))
    if guess < number:
        print("มากกว่านี้")
    elif guess > number:
        print("น้อยกว่านี้")
print("ถูกต้อง!")