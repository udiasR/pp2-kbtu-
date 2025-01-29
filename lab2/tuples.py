thistuple = ("apple", "banana", "cherry")
print(thistuple)


# Access Tuple Items
# Print the second item in the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])


# Change Tuple Values
# Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


# Loop Through a Tuple
# Iterate through the items and print the values:
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


# Join Two Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)