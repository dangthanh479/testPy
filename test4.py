"""
4. Write a program to produce Fibonacci series in Python
5. Dãy số Fibonacci được định nghĩa như sau: 
F0 = 0, F1 = 1, F2 = 1, Fn = F(n-1) + F(n-2) với n >= 2. 
Ví dụ: 0, 1, 1, 2, 3, 5, 8, ... """

a = 0
b = 1
n = int(input())
for i in range (2,n):
    c = a + b 
    a = b 
    b = c
print(str(c))



