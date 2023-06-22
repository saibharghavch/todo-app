import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open('todos.txt','w') as file:
        pass

sg.theme("Black")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button(size=10, image_source="add.png",
                       tooltip="Add Todo", key="Add")
list_box = sg.Listbox(values=functions.get_todos(),key='todos', enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")
complete_button=sg.Button("Complete")
exit_button = sg.Button("Exit")

window=sg.Window('My To-Do App',
                 layout=[[clock],
                         [label],
                         [input_box,add_button],
                         [list_box,edit_button, complete_button],
                         [exit_button]],
                 font=('Helvetica', 18))
while True:
    # For getting the time displayed and changed every second we do this line of code so that after every 200 milliseconds
    # the clock will update itself
    event,values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values['todo']+"\n")
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                # By clicking on the buttons there is a dictionary which is created with events and values
                # To get the to-do which needed to be edited
                todo_to_edit = values['todos'][0]
                # We write the to-do which needs to be inplace of the to-do select
                new_todo = values['todo']
                todos = functions.get_todos()
                # Get the index and then override it
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                # Once the update is done on the backend we need to update it on the GUI so we use update function
                # window is like the parent object which contains all the layouts
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Complete':
            try:
                todo_to_complete=values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
window.close()