import os

def test_path_details(path):
    if os.path.exists(path):
        print("Path exists.")
        print("Directory:", os.path.dirname(path))   
        #Extracts the directory portion of the given path.
        #It removes the last part (filename or last folder) and returns the remaining directory path.
        print("Filename:", os.path.basename(path))   #last one
    else:
        print("Path does not exist.")

test_path_details(r"/home/hp/Documents/pp2-kbtu-/lab7")