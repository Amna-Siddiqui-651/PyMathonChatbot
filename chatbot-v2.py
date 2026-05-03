import math

responses = {
    "hi": "Hi, I'm Lexi. What can I help you?",
    "hy": "Hy, I'm Lexi. What can I help you?",
    "hye": "Hye, I'm Lexi. What can I help you?",
    "hello": "Hello, I'm Lexi. How can I help you?",
    "how are you": "I'm good, what about you?",
    "what is value of pi": "Value of pi is 3.142",
    "thank you": "My pleasure!",
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

    elif user in ["sqrt", "square root", "calculate the squre root of numbers", "calculate the sqrt", "calculate the sqrt of numbers","calculate the sqrt of number"]:
        num = int(input("Enter number: "))
        print(f"Chatbot: {math.sqrt(num)}")

    elif user in ["add", "addition", "i want addition", "help me in addition", "i want add numbers"]:
        numbers = []
        while True:
            num = input("Chatbot: Enter number (or = to finish): ").strip()
            if num == '=':
                break
            try:
                numbers.append(float(num))
            except:
                print("Chatbot: Invalid input try again!")
        if numbers:
            result = sum(numbers)
            print(f"Chatbot: Result of all additon is:{result}")
        else:
            print("Chatbot : No number entered!")
        

    elif user in ["sub","subb", "subtraction", "i want subbtraction", "help me in subbtraction", "i want sub numbers"]:
        numbers = []
        while True:
            num = input("Enter number here (or = to finish): ").strip()
            if num == "=":
                break
            try:
                numbers.append(float(num))
            except:
                print("Chatbot: Invalid inpput try again")
        if numbers:
           result = numbers[0]
           for n in numbers[1:]:
            result -= n
           print(f"Chatbot: Result is {result}")
        else:
            print("Chatbot: No number entered!")

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