while True:
    user_action = input('Type add, show, edit, complete, or exit: ')
    if 'add' in user_action:
        content = user_action[4:]
        with open('todos.txt','r') as file:
            todos=file.readlines()
        with open('todos.txt','w') as file:
            todos.append(content)
            file.writelines(todos)
    elif 'show' in user_action:
        with open('todos.txt','r') as file:
            todos=file.readlines()
        for index,item in enumerate(todos):
            item=item.strip('\n')
            print(f"{index+1} - {item}")
    elif 'edit' in user_action:
        number = int(user_action[5:])
        print(number)
        number = number-1
        with open('todos.txt','r') as file:
            todos = file.readlines()

        new_todo=input('Enter new todo: ')
        todos[number]=new_todo+'\n'
        with open('todos.txt','w') as file:
            file.writelines(todos)
    elif 'complete' in user_action:
        number = int(user_action[9])
        with open('todos.txt','r') as file:
            todos=file.readlines()
        index = number-1
        todo_to_remove=todos[index].strip('\n')
        todos.pop(index)

        with open('todos.txt','w') as file:
            file.writelines(todos)

        message=f"Todo {todo_to_remove} was removed from the list."
        print(message)
    elif 'exit' in user_action:
        break
    else:
        print('Command is not valid!')
print("Bye!")