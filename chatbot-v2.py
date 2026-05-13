import math

responses = {
    "hi": "Hi, I'm Lexi. What can I help you?",
    "hy": "Hy, I'm Lexi. What can I help you?",
    "hye": "Hye, I'm Lexi. What can I help you?",
    "hello": "Hello, I'm Lexi. How can I help you?",
    "how are you": "I'm good, what about you?",
    "i'm good, what about you": "I'm great too!",
    "what is value of pi": "Value of pi is 3.142",
    "thank you": "My pleasure!",
    "bye": "Bye, see you soon!",
    "by": "Bye, see you soon!"
}

history = []

while True:
    user = input("You: ").lower()

    if user in ["by", "bye"]:
        print(f"Chatbot: {responses[user]}")
        break

    elif user in responses:
        print(f"Chatbot: {responses[user]}")

    elif user in ["help", "menu"]:
        print("----AVAILABLE COMMAND----")
        print("1. Square root")
        print("2. Addition")
        print("3. Subtraction")
        print("4. Multiplication")
        print("5. Division")
        print("6. Floor Division")
        print("7. Power")
        print("8. Modulus")
        print("9. Even/Odd")
        print("10. Factorial")
        print("11. Percentage")
        print("12. Table")
        print("13. History")
        print("14. Clear History")

    # Square Root
    elif user in [
        "sqrt", "1", "1.", "square root",
        "calculate the square root of numbers",
        "calculate the sqrt",
        "calculate the sqrt of numbers",
        "calculate the square root of number"
    ]:
        num = float(input("Enter number: "))
        result = math.sqrt(num)
        history.append(f"Square Root of {num} = {result}")
        print(f"Chatbot: {result}")

    # Addition direct
    elif user.startswith(("add ", "sum ", "plus ")):
        parts = user.split()
        numbers = []

        try:
            for num in parts[1:]:
                numbers.append(float(num))

            result = sum(numbers)

            print(f"Chatbot: Result is {result}")

            hist = f"Addition: {numbers} = {result}"
            history.append(hist)

        except:
            print("Chatbot: Invalid Input! Please enter numbers only")

    # Addition manual
    elif user in [
        "add", "2", "2.", "addition",
        "i want addition",
        "help me in addition",
        "i want add numbers"
    ]:
        numbers = []

        while True:
            num = input("Chatbot: Enter number (or = to finish): ").strip()

            if num == "=":
                break

            try:
                numbers.append(float(num))

            except:
                print("Chatbot: Invalid input try again!")

        if numbers:
            result = sum(numbers)

            hist = f"Addition: {numbers} = {result}"
            history.append(hist)

            print(f"Chatbot: Result of all addition is: {result}")

        else:
            print("Chatbot: No number entered!")

    # Subtraction direct
    elif user.startswith(("sub ", "minus ", "subtract ")):
        parts = user.split()
        numbers = []

        try:
            for num in parts[1:]:
                numbers.append(float(num))

            result = numbers[0]

            for i in numbers[1:]:
                result -= i

            print(f"Chatbot: Result is {result}")

            history.append(f"Subtraction: {numbers} = {result}")

        except:
            print("Chatbot: Invalid input! Please enter numbers only")

    # Subtraction manual
    elif user in [
        "sub", "subb", "3", "3.",
        "subtraction",
        "i want subtraction",
        "help me in subtraction",
        "i want sub numbers"
    ]:
        numbers = []

        while True:
            num = input("Chatbot: Enter number here (or = to finish): ").strip()

            if num == "=":
                break

            try:
                numbers.append(float(num))

            except:
                print("Chatbot: Invalid input try again")

        if numbers:
            result = numbers[0]

            for n in numbers[1:]:
                result -= n

            history.append(f"Subtraction: {numbers} = {result}")

            print(f"Chatbot: Result is {result}")

        else:
            print("Chatbot: No number entered!")

    # Multiplication direct
    elif user.startswith(("multiply ", "mul ")):
        parts = user.split()
        numbers = []

        try:
            for num in parts[1:]:
                numbers.append(float(num))

            result = 1

            for i in numbers:
                result *= i

            print(f"Chatbot: Result is {result}")

            history.append(f"Multiplication: {numbers} = {result}")

        except:
            print("Chatbot: Invalid input! Please enter numbers only")

    # Multiplication manual
    elif user in [
        "mul", "4", "4.",
        "multiplication",
        "i want multiplication",
        "help me in multiplication",
        "i want mul numbers"
    ]:
        numbers = []

        while True:
            num = input("Chatbot: Enter number here (or = for finish): ")

            if num == "=":
                break

            try:
                numbers.append(float(num))

            except:
                print("Chatbot: Invalid input try again")

        if numbers:
            result = 1

            for n in numbers:
                result *= n

            history.append(f"Multiplication: {numbers} = {result}")

            print(f"Chatbot: Result is {result}")

        else:
            print("Chatbot: No number entered")

    # Division
    elif user in [
        "div", "5", "5.",
        "division",
        "i want division",
        "help me in division",
        "i want divide numbers",
        "divide"
    ]:
        num1 = float(input("Enter number1: "))
        num2 = float(input("Enter number2: "))

        if num2 == 0:
            print("Chatbot: Cannot divide by zero")

        else:
            result = num1 / num2

            history.append(f"Division: {num1} / {num2} = {result}")

            print(f"Chatbot: {result}")

    # Floor Division
    elif user in ["//", "6", "6.", "floor division"]:
        num1 = int(input("Enter number1: "))
        num2 = int(input("Enter number2: "))

        if num2 == 0:
            print("Chatbot: Can't divide by zero")

        else:
            result = num1 // num2

            history.append(f"Floor Division: {num1} // {num2} = {result}")

            print(f"Chatbot: {result}")

    # Power
    elif user in [
        "power",
        "i want to calculate power",
        "7",
        "7."
    ]:
        num1 = float(input("Enter base: "))
        num2 = float(input("Enter power: "))

        result = num1 ** num2

        history.append(f"Power: {num1}^{num2} = {result}")

        print(f"Chatbot: {result}")

    # Modulus
    elif user in ["%", "8", "8.", "mod", "modulus"]:
        num1 = int(input("Enter number1: "))
        num2 = int(input("Enter number2: "))

        result = num1 % num2

        history.append(f"Modulus: {num1} % {num2} = {result}")

        print(f"Chatbot: {result}")

    # Even/Odd
    elif user in ["even/odd", "check even or odd", "9", "9."]:
        num = int(input("Enter number: "))

        if num % 2 == 0:
            print("Chatbot: Even")

        else:
            print("Chatbot: Odd")

    # Factorial
    elif user in [
        "fact",
        "factorial",
        "calculate factorial",
        "10",
        "10."
    ]:
        num = int(input("Enter number: "))

        fact = 1

        for i in range(1, num + 1):
            fact *= i

        history.append(f"Factorial of {num} = {fact}")

        print(f"Chatbot: {fact}")

    # Percentage
    elif user in [
        "percentage",
        "i want to calculate percentage",
        "11",
        "11.",
        "percent"
    ]:
        num1 = float(input("Enter Obtained marks here: "))
        num2 = float(input("Enter Total marks here: "))

        result = (num1 * 100) / num2

        history.append(f"Percentage: {result}%")

        print(f"Chatbot: The percentage is {result}%")

    # Table
    elif user in [
        "table",
        "i want times tables",
        "i want tables",
        "help me in tables",
        "12",
        "12."
    ]:
        num = int(input("Enter number here: "))
        start = int(input("Enter Starting number here: "))
        end = int(input("Enter Ending number here: "))

        print(f"Chatbot: ---Table of {num}---")

        for i in range(start, end + 1):
            result = num * i

            history.append(f"{num} x {i} = {result}")

            print(f"{num} * {i} = {result}")

        print("------------------------")

    # History
    elif user in ["history", "let me check history", "13", "13."]:
        if history:
            print("----Calculation History----")

            for item in history:
                print(item)

        else:
            print("No history found")

    # Clear History
    elif user in ["clear", "clear history", "14", "14."]:
        history.clear()

        print("Chatbot: History cleared!")

    else:
        print("Chatbot: I didn't understand. Try another command.")