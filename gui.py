import functions
import PySimpleGUI as sg
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(),key='todos', enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")

window=sg.Window('My To-Do App',
                 layout=[[label],[input_box,add_button],[list_box,edit_button]],
                 font=('Helvetica', 18))
while True:
    event,values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values['todo']+"\n")
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
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
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break
window.close()