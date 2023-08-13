import functions
import PySimpleGUI as sg
import time

lable = sg.Text(time.strftime("%b  %d/%m/%Y"))
add_input = sg.InputText(tooltip="Enter Todo Here", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(),
                      key="todos",
                      enable_events=True,
                      size=(40, 10))
edit_btn = sg.Button("Edit")
complete_btn = sg.Button("Complete")
exit_btn = sg.CloseButton("Exit")
window = sg.Window("My Todo App",
                   layout=[[lable],[add_input, add_button],
                           [list_box, edit_btn,complete_btn],
                           [exit_btn]],
                   font=("Roboto", 16))
while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = value["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            todo_to_edit = value["todos"][0]
            new_todo = value["todo"]

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "Complete":
            todo_to_complete = value["todos"][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value='')
        case "todos":
            window["todo"].update(value=value["todos"][0])
        case sg.WIN_CLOSED:
            break

window.close()