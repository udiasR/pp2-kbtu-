import re


with open('row.txt', 'r') as file:
    content = file.read()

one = re.findall("ab*", content)
print(one)

two = re.findall("ab{2,3}", content)
print(two)

three = re.findall("[a-z]_", content)
print(three)

four = re.findall("[A-Z]{1}[a-z]*", content)
print(four)

five = re.findall("a.*b", content)
print(five)

six = re.sub("[.,\s]", ":", content)
print(six)

seven = re.sub(r'_([a-z])', lambda match: match.group(1).upper(), content)
print(seven) 

eight = re.findall(r'[A-Z][a-z]*', content)
print(eight)  

nine = re.sub(r'([a-z])([A-Z])', r'\1 \2', content)
print(nine) 

ten = re.sub(r'([a-z])([A-Z])', r'\1_\2', content).lower()
print(ten)  
