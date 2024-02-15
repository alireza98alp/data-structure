from stack import Stack
word = input()
s = Stack(len(word))
for char in word:
    s.Push(char)
for _ in range(len(s)):
    print(s.pop(), end="")
