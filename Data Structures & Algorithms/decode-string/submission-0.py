class Solution:
    def decodeString(self, s):
        stack = []
        num = 0
        current = ""

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '[':
                stack.append((current, num))
                current = ""
                num = 0
            elif char == ']':
                prev, repeat = stack.pop()
                current = prev + current * repeat
            else:
                current += char

        return current