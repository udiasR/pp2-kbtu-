import string

def generate_26_files():
    for letter in string.ascii_uppercase:                        #Iterates over each uppercase letter from 'A' to 'Z'.
        with open(f"{letter}.txt", 'w') as file:
            pass                                        #pass is used because we don’t need to write anything inside the files.


generate_26_files()