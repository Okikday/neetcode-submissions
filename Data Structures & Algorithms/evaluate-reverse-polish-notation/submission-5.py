class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        calc = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b
        }

        stack = list()
        for t in tokens:
            if t in calc:
                b, a = stack.pop(), stack.pop()
                stack.append(int(calc[t](a, b)))
            else:
                stack.append(int(t))
        
        return int(stack.pop())