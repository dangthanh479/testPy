
x = input()
digit = 0
letters = 0
for i in x:
    if i.isalpha():
        letters += 1
    elif i.isnumeric():
        digit += 1
print("Số chữ cái là:" + str(letters))
print("Số chữ số là:" + str(digit))        
