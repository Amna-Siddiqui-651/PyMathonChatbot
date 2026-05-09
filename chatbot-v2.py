import math

responses = {
    "hi": "Hi, I'm Lexi. What can I help you?",
    "hy": "Hy, I'm Lexi. What can I help you?",
    "hye": "Hye, I'm Lexi. What can I help you?",
    "hello": "Hello, I'm Lexi. How can I help you?",
    "how are you": "I'm good, what about you?",
    "i'm good, what about you":"I",
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

    elif user in ["help","menu"]:
        print("----AVAILABLE COMMAND----" )
        print("1. Square root")
        print("2. Addition" )
        print("3. Subtraction" )
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

    elif user in ["sqrt", "1", "1.", "square root", "calculate the square root of numbers", "calculate the sqrt", "calculate the sqrt of numbers","calculate the square root of number"]:
        num = int(input("Enter number: "))
        result = math.sqrt(num)
        history.append(result)
        print(f"Chatbot: {result}")

    elif user.startswith(("add", "sum", "plus")):
        parts = user.split()
        numbers = []
        try:
            for num in parts[1:]:
                numbers.append(float(num))
                result = sum(numbers)
            print(f"Chatbot: Result is {result}")
            history.append(result)
        except:
            print("Chatbot: Invalid Input! please enter numbers only")

    elif user in ["add", "2", "2.", "addition", "i want addition", "help me in addition", "i want add numbers"]:
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
            history.append(result)
            print(f"Chatbot: Result of all additon is:{result}")
        else:
            print("Chatbot : No number entered!")

    elif user.startswith(("sub", "minus", "subtract it")):
        parts = user.split()
        numbers = []
        try:
            for num in parts[1:]:
                numbers.append(float(num))
                result = numbers[0]
                for i in numbers[1:]:
                    result -= i
            print(f"Chatbot: Result is {result}")
            history.append(result)
        except:
            print("Chatbot: Invalid input! Please enter numbers only")
        
    elif user in ["sub","subb", "3","3.", "subtraction", "i want subtraction", "help me in subtraction", "i want sub numbers"]:
        numbers = []
        while True:
            num = input("Chatbot: Enter number here (or = to finish): ").strip()
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
           history.append(result) 
        
           print(f"Chatbot: Result is {result}")
        else:
            print("Chatbot: No number entered!")

    elif user.startswith(("multiply", "mul", "multiply it")):
        parts = user.split()
        numbers = []
        try:
            for num in parts[1:]:
                numbers.append(float(num))
                result = numbers[0]
                for i in numbers:
                    result *= i
            print(f"Chatbot: Result is {result}")
            history.append(result)
        except:
            print("Chatbot: Invalid input! Please enter numbers only")

    elif user in ["mul","4","4.", "multiplication", "i want multiplication", "help me in multiplication", "i want mul numbers"]:
        numbers = []
        while True:
            num = input("Chatbot: Enter number here (or = for finished): ")
            if num == "=":
                break
            try:
                numbers.append(float(num))
            except:
                print("Chatbot: Invalid input try again")
        if numbers:
            result = numbers[0]
            for n in numbers[1:]:
                result *= n
            history.append(result)
            print(f"Chatbot: Result is {result}")
        else:
            print("Chatbot: No numbr entered")

    elif user in ["div", "5","5.", "division", "i want division", "help me in division", "i want divide numbers", "divide"]:
        num1 = int(input("Enter number1: "))
        num2 = int(input("Enter number2: "))

        if num2 == 0:
            print("Chatbot: Cannot divide by zero")
        else:
            result = num1 // num2
            history.append(result)
            print(f"Chatbot: {result}")
            

    elif user in ["//","6","6.", "floor division"]:
        num1 = int(input("Enter number1: "))
        num2 = int(input("Enter number2: "))
        if num2 == 0:
            print("Can't divide zero")
        else:
            result = num1 // num2
            history.append(result)
            print(f"Chatbot: {result}")

    elif user in ["power", "i waant to calculate power", "7", "7."]:
        num1 = int(input("Enter base: "))
        num2 = int(input("Enter power: "))
        result = num1 % num2
        history.append(result)
        print(f"Chatbot: {result}")
        

    elif user in ["%","8", "8.", "mod", "modulus"]:
        num1 = int(input("Enter number1: "))
        num2 = int(input("Enter number2: "))
        result = num1 % num2
        history.append(result)
        print(f"Chatbot: {result}")

    elif user in ["even/odd", "check even or odd", "9", "9."]:
        num = int(input("Enter number: "))
        if num % 2 == 0:
            print(f"Chatbot: Even")
        else:
            print("Chatbot: Odd")

    elif user in ["fact", "factorial", "calculate factorial", "10", "10."]:
        num = int(input("Enter number: "))
        fact = 1
        for i in range(1, num + 1):
            fact *= i
            history.append(fact)
        print(f"Chatbot: {fact}")

    elif user in ["percentage","i want to calculate percentage", "11", "11.", "percent"]:
        num1 = int(input("Enter Obtained marks here: "))
        num2 = int(input("Enter Total marks here: "))
        result = num1 * 100 / num2
        history.append(result)
        print(f"Chatbot: The percentage of {num1} and {num2} is {result}")

    elif user in ["table", "i want times tables", "i want tables", "help me in tables", "12", "12."]:
        num = int(input("Enter number here: "))
        start = int(input("Enter Starting number here: "))
        end = int(input("Enter Ending number here: "))
        print(f"Chatbot: ---Table of {num}---")
        for i in range(start, end+1):
            result = num*i
            history.append(result)
            print(f"{num} * {i} = {result}")
        print("------------------------")

    elif user in ["history", "let me check history", "13", "13."]:
        if history:
            print("----Calculation History----")
            for item in history:
                print(item)
        else:
            print("No history found")

    else:
        print("Chatbot: I didn't understand. Try another command.")