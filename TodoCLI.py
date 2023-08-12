from functions import *
# from functions import get_todos, write_todos
# ''' function.get_todos() '''
# import functions
import time

print("It's " + time.strftime("%b, %d/%m/%Y, %I:%M:%S"))
while True:
    user_action = input("Choose add, show,  edit, complete, or exit: ")
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = user_action[4:]    # List Slicing

        todos = get_todos()

        todos.append(todo + "\n")

        write_todos(todos)

        '''This is another way  to doing this. 
        ---- write_todos(filepath="files/todos.txt", todos_args=todos)
        If your are using the arguments to assign the items then it will work properly.
        otherwise if will return an error. 
        '''

    elif 'show' in user_action:
        todos = get_todos()

        for index, item in enumerate(todos):
            row = f'{index + 1 }. {item}'
            print(row.strip())

    elif 'edit' in user_action:
        try:
            number = int(user_action[5:])
            new_todo = input("Enter New Todo: ") + "\n"

            todos = get_todos()

            todos[number-1] = new_todo

            write_todos(todos)
            print("Updated!")
        except ValueError:
            print("Incorrect Value... Do as follows \n 1,2,3,...")
            continue
    elif 'complete' in user_action:
        try:
            number = int(user_action[9:])

            todos = get_todos()

            c_todo = todos.pop(number-1)

            write_todos(todos)

            print(f'{c_todo} --- Done!')
        except IndexError:
            print("Item is not in the list... \n use 'show' command to check ")
            continue

    elif 'exit' in user_action:
        print("Exiting...")
        break

    else:
        print('Enter from given options!...')
print('Bye!')
