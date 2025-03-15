import os

def list_dir_files(path):
    items = os.listdir(path) #os.listdir(path) returns a list of all items (files and directories) in the specified path
    dirs = [item for item in items if os.path.isdir(os.path.join(path, item))]   #os.listdir() only returns names, so we need os.path.join() to get the full path.
    files = [item for item in items if os.path.isfile(os.path.join(path, item))]

    print("Directories:", dirs)
    print("Files:", files)
    print("All items:", items)


list_dir_files("./")