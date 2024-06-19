import functions
import FreeSimpleGUI as sg

label = sg.Text("Add a to-do")
input_box = sg.InputText(tooltip="Enter a to-do")
add_btn = sg.Button("Add")

window = sg.Window("My to-do app", layout=[[label], [input_box, add_btn]])
window.read()
window.close()
