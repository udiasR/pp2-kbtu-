import shutil        # file operations such as copying, moving, and deleting files.

def copy_file(source_path, destination_path):
    shutil.copy(source_path, destination_path)