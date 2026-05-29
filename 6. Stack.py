# Stack and its applications
# 1. Reverse (done)
# 2. Parentheses checking (done)
# 3. Postfix evaluation (done)
# 4. Infix to Postfix (done)
# 5. Infix to Prefix (done)
# 6. Prefix evaluation (done)
# 9. Undo/Redo (Done)


# --> stack Code :-
class stack:
    def __init__(self):
        self.s = []

    def length(self):
        return len(self.s)

    def push(self, val):
        return self.s.insert(0, val)

    def peek(self):
        if len(self.s) == 0:
            raise Exception("Stack is empty")
        return self.s[0]

    def pop(self):
        if len(self.s) == 0:
            raise Exception("Stack is empty")
        return self.s.pop(0)

    def is_empty(self):
        return len(self.s) == 0


s = stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
print(s.peek())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())

# Stack applications :-
# --> Reversing a string
stk1 = stack()
s = input("Enter the string: ")

for ch in s:
    stk1.push(ch)

print(" ".join(stk1.s))

# --> Checking for balanced parentheses
stk2 = stack()
exp = input("Enter the expression: ")

flag = True

for ch in exp:
    if ch in "({[":
        stk2.push(ch)
    elif ch in ")}]":
        if stk2.length() == 0:
            flag = False
            break
            
        top = stk2.peek()
        
        if (
            (ch == ")" and top == "(")
            or (ch == "}" and top == "{")
            or (ch == "]" and top == "[")
        ):
            stk2.pop()
        else:
            flag = False
            break

if stk2.length() != 0:
    flag = False
    
if flag:
    print("Balanced")
else:
    print("Not Balanced")


# --> Evaluating postfix expression
def Evaluate_postfix(expression):
    stack = []
    
    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            if len(stack) < 2:
                return "Invalid Expression"          
                b = stack.pop()
                a = stack.pop()
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "//":
                    if b == 0:
                        return "Error: Zero Division Error"
                    stack.append(a // b)
                    else:
                        return "Invalid Operator"
            if len(stack) != 1:
                return "Invalid Expression"
    return stack[0]


exp = input("Enter Expression (Space -  Separated): ")
result = Evaluate_postfix(exp)
print("Result: ", result)


# Infix to postfix :
def precendence(op):
    if op == "+" or "-":
        return 1
    elif op == "*" or "/":
        return 2
    elif op == "^":
        return 3
    return 0


def Infix_to_Prefix(expression):
    stack = []
    output = ""

    expression = expression.replace(" ", "")

    for ch in expression:
        if ch.isalnum():
            output += ch

        elif ch == "(":
            stack.append(ch)

        elif ch == ")":
            while stack and stack[-1] != "(":
                output += stack.pop()
            stack.pop()

        else:
            while stack and precendence(stack[-1]) >= precendence(ch):
                output += stack.pop()
            stack.append(ch)

    while stack:
        output += stack.pop()

    return output


exp = input("Enter Expression: ")
result = Infix_to_Prefix(exp)
print("Result: ", result)


# Infix to Prefix :
def priority(op):
    if op == "+" or "-":
        return 1
    elif op == "*" or "/":
        return 2
    return 0

def Infix_to_Prefix(expression):
    stack = []
    output = ""

    expression = expression[::-1]

    for ch in expression:
        if ch == ")":
            stack.append(ch)
        elif ch == "(":
            while stack and stack[-1] != ")":
                output += stack.pop()
            stack.pop()
        elif ch.isalnum():
            output += ch
        else:
            while stack and priority(stack[-1]) > priority(ch):
                output += stack.pop()
            stack.append(ch)

    while stack:
        output += stack.pop()
        
    return output[::-1]


exp = input("Enter Expression: ")
result = Infix_to_Prefix(exp)
print("Result: ", result)


# Prefix evaluation :
def Prefix_evaluation(expression):
    stack = []

    for ch in reversed(expression.split()):
        if ch.isdigit():
            stack.append(int(ch))
        else:
            a = stack.pop()
            b = stack.pop()

            if ch == "+":
                stack.append(a + b)
            elif ch == "-":
                stack.append(a - b)
            elif ch == "*":
                stack.append(a * b)
            elif ch == "/":
                stack.append(a // b)

    return stack[0]

exp = input("Enter Expression: ")
result = Prefix_evaluation(exp)
print("Result: ", result)


# Undo/Redo using stack :
undo = []
redo = []

while True:
    print("1.Add")
    print("2.Undo")
    print("3.Redo")
    print("4.Show")
    print("5.Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        text = input("Enter Text: ")
        undo.append(text)
        redo.clear()
    elif ch == 2:
        if undo:
            items = undo.pop()
            redo.append(items)
            print("Undo: ", items)
        else:
            print("Nothing to undo")
    elif ch == 3:
        if redo:
            items = redo.pop()
            undo.append(items)
            print("Redo: ", items)
        else:
            print("Nothing to Redo")
    elif ch == 4:
        print("Current Data: ", undo)
    elif ch == 5:
        break
    else:
        print("Invalid Choice")
    else:
        print("Invalid Choice")


