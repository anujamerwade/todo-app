import functions
import FreeSimpleGUI as sg

label = sg.Text("Add a to-do")
input_box = sg.InputText(tooltip="Enter a to-do", key="todo")   # key for the dictionary generated in "values" below
add_btn = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True,
                      size=(45, 10))
edit_btn = sg.Button("Edit")

window = sg.Window("My to-do app",
                   layout=[[label], [input_box, add_btn], [list_box, edit_btn]])

while True:
    event, values = window.read()
    print(event)
    print(values)
    if event == "Add":
        todos = functions.get_todos()
        new_todo = values["todo"] + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)
        window["todos"].update(values=todos)
    if event == "Edit":
        todo_to_edit = values["todos"][0]
        new_todo = values["todo"]
        todos = functions.get_todos()
        index = todos.index(todo_to_edit)
        todos[index] = new_todo
        functions.write_todos(todos)

        window["todos"].update(values=todos)
    if event == "todos":
        window["todo"].update(value=values["todos"][0])
    if event == sg.WIN_CLOSED:
        break

window.close()
