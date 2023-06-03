#Name - Kavya Sri Garikipati
#UTA id: 1001953373
#April 5th ,2023
#Mac OS

#Extra Credit : 2
########################################################################################################################################################

# Additional operator is ^ (for exponential) and % for modulo division

# importing os
import os
#Stack Class --- used to store and parse Reverse Polish Notation
class Stack:
    def __init__(equation):
        equation.values = []

    def push(equation, values): #user defined stack method for inserting an element into the stack
        equation.values.append(values)

    def pop(equation): #user defined stack method to remove the topmost element from the stock
        return equation.values.pop()


# Converts algebraic expression to postfix expression
class PostFixStack:
    def __init__(equation, size):
        equation.output = []
        equation.values = []
        equation.top = -1
        equation.size = size
        equation.precedence = {'+': 1, '-': 1, '/': 2, '*': 2, '^': 3, '%': 2} #precedence is declared

    def is_empty(equation):
        return True if equation.top == -1 else False

    def push(equation, values): #user defined stack method for inserting an element into the stack
        equation.top += 1
        equation.values.append(values)

    def pop(equation): #user defined stack method to remove the topmost element from the stock
        if not equation.is_empty():
            equation.top = equation.top - 1
            return equation.values.pop()
        else:
            return "#"

    def peek(equation):
        return equation.values[-1]

    def is_operand(equation, index):
        return index.isdigit() #returns true if characters are digits

   #Check if the operator's precedence is less than the top of the stack.
    def not_greater_than(equation, s):
        try:
            p = equation.precedence[s]
            q = equation.precedence[equation.peek()]
            return True if p <= q else False
        except KeyError:
            return False
        
# This is used to convert the given algebraic expression to postfix notation
    def infix_to_postfix(equation, expression):
      # here we are using for loop over the given algebraic expression
        for s in expression:
             # This is for the case when character is an operand
            if equation.is_operand(s):
                equation.output.append(s)
 
  # If the character is an '(', push it to stack
            elif s == '(':
                equation.push(s)
        # we should pop ')' and iterate till '(' is found, if the character is an ')'
            elif s == ')':
                while ((not equation.is_empty()) and
                       equation.peek() != '('):
                    p = equation.pop()
                    equation.output.append(p)
                if not equation.is_empty() and equation.peek() != '(':
                    return -1
                else:
                    equation.pop()

           # Here an operator is confronted
            else:
                while not equation.is_empty() and equation.not_greater_than(s):
                    equation.output.append(equation.pop())
                equation.push(s)

       # Pop all the available operators from the stack
        while not equation.is_empty():
            equation.output.append(equation.pop())

        print("RPN: " + "".join(equation.output))
        return equation.output

# BASIC CALCULATOR which returns output when two operands and a operator is PROVIDED
def calc(operator, operand_First, operand_Second):
    if operator == "+":
        return operand_First + operand_Second #returns addition
    elif operator == "-":
        return operand_First - operand_Second #returns subtraction
    elif operator == "*":
        return operand_First * operand_Second #returns multiplication
    elif operator == "/":
        return operand_First / operand_Second #returns division
    # Here , exponentiation operator is added for ec2, it powers first operand by second operand
    elif operator == "^":
        return operand_First ** operand_Second
    # Here , modulo operator is added for ec2, it gives modulo operation of first operand and second operand
    elif operator == "%":
        return operand_First % operand_Second


def postfix_evaluator(Expression):
    operators = ["+", "-", "*", "/", "^", "%"]
    operand_stack = Stack()
    expression_stack = PostFixStack(len(Expression))
    index_list = expression_stack.infix_to_postfix(Expression)

    for index in index_list:
        # checks if an index is an operand or an operator!
        if index in operators:
            operand_Second = operand_stack.pop()
            operand_First = operand_stack.pop()
            RESULT = calc(index, operand_First, operand_Second)
            operand_stack.push(RESULT)
        # This is the case when Index is an operand
        else:
            operand_stack.push(float(index))

    return operand_stack.pop()


# to run the script,click the green button in the gutter.
if __name__ == '__main__':
    Python_file_path = os.path.dirname(os.path.abspath(__file__))
    RPN_inputFile_location_path = os.path.join(Python_file_path, "input_RPN_ec2.txt")
    with open(RPN_inputFile_location_path, "r") as file_in:
        lines = []
        for line in file_in:
            print("Output: " + str(postfix_evaluator(line.strip('\n'))))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
