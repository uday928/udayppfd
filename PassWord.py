import string
import random

length=int(input("enter length:"))
selectionList=" "
print('''Enter:-
      1: Characters
      2: Punctuations
      3: Digits
      4: Exit''')

while True:
    Num=int(input("Enter option:"))
    if Num==1:
        selectionList+=string.ascii_letters #Characters
    elif Num==2:
        selectionList+=string.punctuation #punctuations
    elif Num==3:
        selectionList+=string.digits #digits
    elif Num==4:
        break
    else:
        print("make valid option")

Password=[]

for i in range(length):
    h=random.choice(selectionList)
    Password.append(h)

print("Generated password is:"+"".join(Password))