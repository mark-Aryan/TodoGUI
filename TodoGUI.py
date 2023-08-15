import functions
import PySimpleGUI as sg
import time


"""
List theme using this:-
"""
# theme_name_list = sg.theme_list()
# print(theme_name_list)

sg.theme("Material1")

clock = sg.Text(key="clock")
add_input = sg.InputText(tooltip="Enter Todo Here", key="todo")
add_button = sg.Button(image_source="add.png", tooltip="Add Todo", key="Add")
list_box = sg.Listbox(values=functions.get_todos(),
                      key="todos",
                      enable_events=True,
                      size=(40, 10))
edit_btn = sg.Button("Edit", size=10)
complete_btn = sg.Button("Complete", size=10)
exit_btn = sg.CloseButton("Exit", size=15)
window = sg.Window("My Todo App",
                   layout=[[clock],[add_input, add_button],
                           [list_box, edit_btn,complete_btn],
                           [exit_btn]],
                   font=("Roboto", 16))
while True:
    event, value = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d,%Y %I:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = value["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:

                todo_to_edit = value["todos"][0]
                new_todo = value["todo"]

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup_error("Please select an item first.", font=('Roboto',16), title="Error")

        case "Complete":
            try:
                todo_to_complete = value["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value='')
            except IndexError:
                sg.popup('Select any item first!', font=('Roboto',16), title="Error")
        case "todos":
            window["todo"].update(value=value["todos"][0])
        case sg.WIN_CLOSED:
            break

window.close()
