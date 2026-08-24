class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Edit 1: Added a dictionary to match brackets
        mapping = {")": "(", "}": "{", "]": "["}

        for value in s:
            if value in "({[":
                stack.append(value)
            
            elif value in ')}]':
                # Edit 2: Check if stack is empty, and compare using the dictionary
                if not stack or stack.pop() != mapping[value]:
                    return False

        # Edit 3: Return True only if the stack is completely empty at the end
        return len(stack) == 0