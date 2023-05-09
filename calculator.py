import random

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def get_friendly_insult(result):
    if result == 0:
        insults = ["0. Like the number of friends that you have.",
                   "0. Just like your contribution to society."]
    elif result < 0:
        insults = ["{:.2f}. Like the sum of your bank account.",
                   "{:.2f}. The amount of money you owe to your friends."]
    else:
        insults = ["{:.2f}. The number of times you've been rejected by your crush.",
                   "{:.2f}. The number of times you've watched your favorite show because you have nothing else to do."]
    return random.choice(insults).format(result)

def get_goodbye_insult():
    goodbye_insults = [
        "Never forget you're someone's reason to smile (because you're a joke!).",
        "You're living proof that even a broken clock is right twice a day.",
        "If laughter is the best medicine, your face must be curing the world!"
    ]
    return random.choice(goodbye_insults)

print("Welcome to the Funny Calculator!")
print("Let's do some calculations while having a little fun.")
print()
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = None
        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)

        print(get_friendly_insult(result))

        while True:
            another_operation = input("Would you like to do another operation? (yes/no): ").lower()
            if another_operation == 'yes':
                print("Select operation:")
                print("1. Add")
                print("2. Subtract")
                print("3. Multiply")
                print("4. Divide")
                break
            elif another_operation == 'no':
                print("Goodbye!")
                print(get_goodbye_insult())
                exit()
            else:
                print("Invalid input. Please try again.")
    else:
        print("Invalid input. Please try again.")