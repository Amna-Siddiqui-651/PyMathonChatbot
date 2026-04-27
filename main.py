import math

responses = {"hi": "Hi, I'm Lexi, What can I help you?", 
             "hello":"Hello, I'm Lexi, How can I help you?", 
             "how are you":"I'm good, what about you", 
             "what is value of pi":"Value of pi is 3.142",
             "thank you": "My Pleasure",
             "bye":"Bye, see you soon!",
             "by":"Bye, see you soon!"}

while True:
    user = input("You: ").lower()

    if user == 'by' or "bye": 
        print(f"Chatbot: {responses[user]}")
        break

    elif user in responses:
        print(f"Chatbot: {responses[user]}")
    
    elif user == "sqrt" or "square root":
        num = int(input("Enter number here: "))
        result = math.sqrt(num)
        print(f"The square root of {num} is {result}")

    elif user == "add" or 'addition':
        num2 = int(input("Enter number2 here: "))
        result = num1 + num2
        print(f"Chatbot: The result of {num1} + {num2} is {result}")

    elif user == "sub" or "subbtraction":
        num1 = int(input("Enter number1 here: "))
        num2 = int(input("Enter number2 here: "))
        result = num1 - num2
        print(f"Chatbot: The result of {num1} - {num2} is {result}")

    elif user == "mul" or 'multiplication':
        num1 = int(input("Enter number1 here: "))
        num2 = int(input("Enter number2 here: "))
        result = num1 * num2
        print(f"Chatbot: The result of {num1} * {num2} is {result}")

    elif user == "div" or "divison":
        num1 = int(input("Enter number1 here: "))
        num2 = int(input("Enter number2 here: "))
            
        if num2 == 0:
            print("Chatbot: Number2 shouldn't be zero in division")

        else:
            result = num1 / num2
            print(f"Chatbot: The result of {num1} / {num2} is {result}")
            

    elif user in ["whole divion", "floor div", "floor division", "//", "int div", "int division"] :
        num1 = int(input("Enter number1 here: "))
        num2 = int(input("Enter number2 here: "))

        if num2 == 0:
            print("Chatbot: Number2 shouldn't be zero in division")

        else:
            result = num1 // num2
            print(f"Chatbot: The result of {num1} // {num2} is {result}")

    elif user == "power":
        num1 = int(input("Enter base number here: "))
        num2 = int(input("Enter power number here: "))
        result = num1 ** num2
        print(f"Chatbot: The result of {num1}^{num2} is {result}")

    elif user == "%" or "mod" or "modulus":
        num1 = int(input("Enter number1 here: "))
        num2 = int(input("Enter number2 here: "))
        result = num1 % num2
        print(f"Chatbot: The result of {num1} % {num2} is {result}")

    elif user == "percentage":
        num1 = int(input("Enter Obtained marks here: "))
        num2 = int(input("Enter Total marks here: "))
        result = num1 * 100 / num2
        print(f"Chatbot: The percentage of {num1} and {num2} is {result}")

    elif user == "table":
        num = int(input("Enter number here: "))
        start = int(input("Enter Starting number here: "))
        end = int(input("Enter Ending number here: "))
        for i in range(start, end+1):
            result = num*i
            print(f"Chatbot: ---Table of {num}---")
            print(f"{num} * {i} = {result}")
            print("------------------------")
    
    elif user == "even/odd":
        num = int(input("Enter number here: "))
        if num % 2 ==0:
            print(f"The {num} is even")
        else:
            print(f"The {num}is odd")

    elif user == "fact" or "factorial":
        num = int(input("Enter number here"))
        fact = 1
        for i in range(1,num+1):
            fact = fact * i
            print(f"Chatbot: The factorial of {num} is {fact}")

    else:
        print("I didn't understand, Please enter another commond")