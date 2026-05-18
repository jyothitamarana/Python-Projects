def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
operations={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
from art import logo
def calculator():
    print(logo)
    num1=int(input("Enter the first number: "))
    for symbol in operations:
        print(symbol)
    should_continue=True
    while(should_continue):
        operation_symbol=input("Enter the operation: ")
        num2=int(input("Enter the next number: "))
        calculation_function=operations[operation_symbol]
        answer = calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'yes' to continue calculating with {answer} or Type 'no' to start a new calculation: ").lower() == "yes":
            num1=answer
        else:
            should_continue=False
            calculator()

calculator()


