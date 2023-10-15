from replit import clear
from art import logo

#Calculator

#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

operators_dic = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,  
}
def calculator():
  print(logo)
  
  num1 = float(input("What's the first number? "))
  
  for operators in operators_dic:
    print(operators)
  operator_symbol = input("Pick an operation from the line above: ")
  
  num2 = float(input("What's the second number? "))
  
  solution = operators_dic[operator_symbol]
  first_answer = solution(num1, num2)
  
  print(f"{num1} {operator_symbol} {num2} = {first_answer}")
  restart = True
  while restart:
    operator_symbol = input("Pick another operation: ")
    num3 = float(input("What's the next number?: "))
    solution = operators_dic[operator_symbol]
    second_answer = solution(first_answer, num3)
    print(f"{first_answer} {operator_symbol} {num3} = {second_answer}")
    loop_ans = input(f"Type 'y' to continue calculating with {second_answer}, or type 'n' to start a new calculator: ")
    if loop_ans == "n":
      restart = False
      clear()
      calculator()

calculator()
    
      
    
    
      
      
  












