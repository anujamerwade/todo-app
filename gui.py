import functions
import FreeSimpleGUI as sg

label = sg.Text("Add a to-do")
input_box = sg.InputText(tooltip="Enter a to-do", key="todo")   # key for the dictionary generated in "values" below
add_btn = sg.Button("Add")

window = sg.Window("My to-do app",
                   layout=[[label], [input_box, add_btn]])

while True:
    event, values = window.read()
    print(event)
    print(values)
    if event == "Add":
        todos = functions.get_todos()
        new_todo = values["todo"] + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)
    if event == sg.WIN_CLOSED:
        break

window.close()
