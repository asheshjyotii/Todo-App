import os
current_dir = os.path.dirname(__file__)
FILE_PATH = os.path.abspath(os.path.join(current_dir, '..', 'data', 'todos.txt'))


def read_todos(file_path=FILE_PATH):
    """
    Read the text file of todolist data and return the todolist items in form of list.
    """
    with open(file_path, 'r') as file:
        data = file.readlines()
    return data

def write_todos(todos_args,file_path=FILE_PATH):
    """
        Write todos to the text file.
    """
    with open(file_path,'w') as file:
        file.writelines(todos_args)

