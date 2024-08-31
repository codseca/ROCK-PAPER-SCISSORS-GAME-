
class Calculator:
    
    def add(self, a, b):
        return a + b

   
    def subtract(self, a, b):
        return a - b

   
    def multiply(self, a, b):
        return a * b

   
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return ("Cannot divide bb zero.")

while True:
    


    print("MENU \n1.ADDITION (+) \n2.SUBTRACTION (-) \n3.MULTIPLICATION (*) \n4.DIVISION (/)")
    c=input("ENTER YOUR CHOICE ")

    if c=='+' :
        calculator = Calculator()

        x=int(input("ENTER A NUMBER"))
        y=int(input("ENTER A NUMBER"))
        result = calculator.add(x, y)
        print(f"{x} + {y} =", result)
    elif c=='-' :
        calculator = Calculator()
        x=int(input("ENTER A NUMBER"))
        y=int(input("ENTER A NUMBER"))
        result = calculator.subtract(x, y)
        print(f"{x} - {y} =", result)
    elif c=='*':
        calculator = Calculator()
        x=int(input("ENTER A NUMBER"))
        y=int(input("ENTER A NUMBER"))
        result = calculator.multiply(x, y)
        print(f"{x} * {y} =", result)
    elif c=='/' :
        calculator = Calculator()
        x=int(input("ENTER A NUMBER"))
        y=int(input("ENTER A NUMBER"))
        result = calculator.divide(x, y)
        print(f"{x} / {y} =", result)
        
    else:
       print("INVALID CHOICE ")
       break
       
