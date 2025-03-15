import math
import time
#1
list = [1,2,3,4,5]
result = math.prod(list)
print(result)
# -----------------------------------

#2
string = "My name is Dias"
upper = 0
lower = 0
for x in string:
    if x.isupper():
        upper+=1
    else:
        lower+=1
print(upper)
print(lower)
#-------------------------------------


#3
str = input()
reversedStr = "".join(reversed(str))
if reversedStr == str:
    print("Yes")
else:
    print("No")

#--------------------------------------
#4
num = int(input())
def squareRoot(num):
    time.sleep(5000/1000)
    print(math.sqrt(num))
squareRoot(num)

#-----------------------------------------
#5
tuple = ("dsd","sdfsdf",232,43)
print(all(tuple))