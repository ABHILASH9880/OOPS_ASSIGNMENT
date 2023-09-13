#IMPLEMENT A CALCULATOR CLASS

class Calculator:
    def _init_(self):
        pass

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero")
        
    
calc = Calculator()
print(calc.add(10,94))       
print(calc.subtract(94,10)) 
print(calc.multiply(10,94)) 
print(calc.divide(10,94))   