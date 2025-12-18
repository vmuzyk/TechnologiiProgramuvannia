import operator

class RPNCalculator:
    def __init__(self):
        
        self.operators = {
            '^': (4, operator.pow),
            '*': (3, operator.mul),
            '/': (3, operator.truediv),
            '+': (2, operator.add),
            '-': (2, operator.sub)
        }
        
        self.precedence = {op: self.operators[op][0] for op in self.operators}
        self.associativity = {
            '^': 'right',  
            '*': 'left',
            '/': 'left',
            '+': 'left',
            '-': 'left'
        }

    def infix_to_rpn(self, expression):
        
        output = []
        stack = []
        
        i = 0
        while i < len(expression):
            token = expression[i]
            
            
            if token == ' ':
                i += 1
                continue
                
            
            if token.isdigit() or (token == '.' and i + 1 < len(expression) and expression[i+1].isdigit()):
                num = token
                while i + 1 < len(expression) and (expression[i+1].isdigit() or expression[i+1] == '.'):
                    i += 1
                    num += expression[i]
                output.append(num)
            
            
            elif token in self.operators:
                
                while (stack and stack[-1] != '(' and 
                       (self.precedence[stack[-1]] > self.precedence[token] or
                        (self.precedence[stack[-1]] == self.precedence[token] and 
                         self.associativity[token] == 'left'))):
                    output.append(stack.pop())
                stack.append(token)
            
            
            elif token == '(':
                stack.append(token)
            
            
            elif token == ')':
                
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                if not stack or stack[-1] != '(':
                    raise ValueError("Неузгоджені дужки")
                stack.pop()  
            
            i += 1
        
        
        while stack:
            if stack[-1] == '(':
                raise ValueError("Неузгоджені дужки")
            output.append(stack.pop())
        
        return ' '.join(output)

    def evaluate_rpn(self, rpn_expression):
        
        stack = []
        tokens = rpn_expression.split()
        
        for token in tokens:
            if token.replace('.', '').isdigit():  
                stack.append(float(token))
            elif token in self.operators:
                if len(stack) < 2:
                    raise ValueError("Недостатньо операндів для операції")
                b = stack.pop()
                a = stack.pop()
                
                
                try:
                    result = self.operators[token][1](a, b)
                    stack.append(result)
                except ZeroDivisionError:
                    raise ValueError("Ділення на нуль")
        
        if len(stack) != 1:
            raise ValueError("Неправильний вираз")
        
        return stack[0]

    def calculate(self, expression):
        
        try:
            
            rpn = self.infix_to_rpn(expression)
            print(f"Зворотний польський запис: {rpn}")
            
            
            result = self.evaluate_rpn(rpn)
            return result
        except Exception as e:
            return f"Помилка: {str(e)}"

def main():
    calculator = RPNCalculator()
    
    print("Калькулятор зворотного польського запису")
    print("Введіть математичний вираз (напр.: 3 + 4 * 2 / (1 - 5) ^ 2)")
    print("Для виходу введіть 'exit'")
    
    while True:
        expression = input("\nВведіть вираз: ").strip()
        
        if expression.lower() == 'exit':
            break
        
        if not expression:
            continue
        
        result = calculator.calculate(expression)
        print(f"Результат: {result}")

if __name__ == "__main__":
    main()