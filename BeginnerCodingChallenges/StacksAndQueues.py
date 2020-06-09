import sys


class Solution:
    # Write your code here
    queue_s = []
    stack_s = []
    # Stack function
    def pushCharacter(self, ele):
        # Add ele from S to the beginning of the stack
        self.stack_s.insert(0,ele)
    # Queue function
    def enqueueCharacter(self, ele):
        # Add ele from S to the end of the queue
        self.queue_s.append(ele)
    # Removing ele from stack
    def popCharacter(self):
        return self.stack_s.pop(0)
    # Removing ele from queue
    def dequeueCharacter(self):
        return self.queue_s.pop(0)

# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")