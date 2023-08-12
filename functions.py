def get_todos(filepath="files/todos.txt"):
    """
    It will return the file you want to list out.
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local
# print(help(get_todos))

def write_todos(todos_args, filepath="files/todos.txt"):
    """
    It will write in the file you want to append the list
    :param todos_args: list of files
    :param filepath: path of that file
    :return: None: return none because it will update the file
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_args)
