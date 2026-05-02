import math

responses = {
    "hi": "Hi, I'm Lexi. What can I help you?",
    "hello": "Hello, I'm Lexi. How can I help you?",
    "how are you": "I'm good, what about you?",
    "what is value of pi": "Value of pi is 3.142",
    "thank you": "My pleasure",
    "bye": "Bye, see you soon!",
    "by": "Bye, see you soon!"
}

while True:
    user = input("You: ").lower()

    if user in ["by", "bye"]:
        print(f"Chatbot: {responses[user]}")
        break

    elif user in responses:
        print(f"Chatbot: {responses[user]}")

    elif user in ["sqrt", "square root"]:
        num = int(input("Enter number: "))
        print(f"Chatbot: {math.sqrt(num)}")

    elif user in ["add", "addition"]:
        num1 = int(input("Enter number1: "))
        num2 = int(input("Enter number2: "))
        print(f"Chatbot: {num1 + num2}")

    elif user in ["sub", "subtraction"]:
        num1 = int(input("Enter number1: "))
        num2 = int(input("Enter number2: "))
        print(f"Chatbot: {num1 - num2}")

    elif user in ["mul", "multiplication"]:
        num1 = int(input("Enter number1: "))
        num2 = int(input("Enter number2: "))
        print(f"Chatbot: {num1 * num2}")

    elif user in ["div", "division"]:
        num1 = int(input("Enter number1: "))
        num2 = int(input("Enter number2: "))

        if num2 == 0:
            print("Chatbot: Cannot divide by zero")
        else:
            print(f"Chatbot: {num1 / num2}")

    elif user in ["//", "floor division"]:
        num1 = int(input("Enter number1: "))
        num2 = int(input("Enter number2: "))
        print(f"Chatbot: {num1 // num2}")

    elif user == "power":
        num1 = int(input("Enter base: "))
        num2 = int(input("Enter power: "))
        print(f"Chatbot: {num1 ** num2}")

    elif user in ["%", "mod", "modulus"]:
        num1 = int(input("Enter number1: "))
        num2 = int(input("Enter number2: "))
        print(f"Chatbot: {num1 % num2}")

    elif user == "even/odd":
        num = int(input("Enter number: "))
        if num % 2 == 0:
            print("Chatbot: Even")
        else:
            print("Chatbot: Odd")

    elif user in ["fact", "factorial"]:
        num = int(input("Enter number: "))
        fact = 1
        for i in range(1, num + 1):
            fact *= i
        print(f"Chatbot: {fact}")

    else:
        print("Chatbot: I didn't understand. Try another command.")