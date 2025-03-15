import re


with open('row.txt', 'r') as file:
    content = file.read()

one = re.findall("ab*", content)               #Finds occurrences of "a" followed by zero or more "b" characters (b*)
print(one)

two = re.findall("ab{2,3}", content)           #Finds "a" followed by 2 or 3 "b" characters (b{2,3})
print(two)

three = re.findall("[a-z]_", content)          #Finds a lowercase letter (a-z) followed by _
print(three)

four = re.findall("[A-Z]{1}[a-z]*", content)    #Finds words that start with an uppercase letter followed by lowercase letters.
print(four)

five = re.findall("a.*b", content)        #Finds everything between a and b, including all characters in between
print(five)

six = re.sub("[.,\s]", ":", content)      
#Replaces all:
"." (dots),
"," (commas),
"\s" (spaces, tabs, newlines)
with a colon (:).#
print(six)

seven = re.sub(r'_([a-z])', lambda match: match.group(1).upper(), content)
#Finding _ followed by a lowercase letter.
Removing _ and converting the letter to uppercase.#
print(seven) 

eight = re.findall(r'[A-Z][a-z]*', content)     #Finds words that start with an uppercase letter and continue with lowercase letters
print(eight)  

nine = re.sub(r'([a-z])([A-Z])', r'\1 \2', content)
print(nine) 

ten = re.sub(r'([a-z])([A-Z])', r'\1_\2', content).lower()
print(ten)  
