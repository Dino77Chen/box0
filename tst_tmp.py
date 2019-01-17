import os


def is_file_in_use(file_path):
    if not os.path.isfile(file_path):
        raise("Given file {} does not exist.")
    try:
        with open(file_path, 'w') as f:
            return False
    except IOError:
        return True


print(is_file_in_use("abc.txt"))
