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

window = sg.Window("My Todo App",
                   layout=[[lable],[add_input, add_button], [list_box, edit_btn]],
                   font=("Roboto", 16))
while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = value["todo"]
            todos.append(new_todo + "\n")
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
        case "todos":
            window["todo"].update(value=value["todos"][0])
        case sg.WIN_CLOSED:
            break

window.close()