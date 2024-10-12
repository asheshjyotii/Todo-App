'''
Todo:
switch statement
add 
show
edit
exit
'''

todos = []

service = True

while service:
    userInput = input('''Available Options:
    add -> to add a todo
    show -> to show todo list
    edit -> to edit any particular todo
    exit -> to show the todo list & exit the app
    complete -> to complete a todo\n
-> ''')
    userInput = userInput.strip(" ")
    match userInput:
        case 'add':
            userInput = input("Enter the todo: ")
            todo = userInput.capitalize()
            todos.append(todo)
            print(f"Added '{todo}' to the list...")
        case 'show':
            print("The todo List:")
            for index,x in enumerate(todos):
                print(f"{index+1}.{x}")
        case 'edit':
            for index,x in enumerate(todos):
                print(f"Enter {index+1} to change {x}")

            userInput = int(input("-> "))
            if userInput <=0 or userInput > len(todos):
                print("Invalid choice.")
                continue

            newTodo = input("Enter the new todo: ")
            todos [userInput-1] = newTodo

            print("The new todo list:")
            for x in todos:
                print(x)
        case 'complete':
            for index,x in enumerate(todos):
                print(f"Enter {index+1} to mark '{x}' as complete")

            userInput = int(input("-> "))
            todos.pop(userInput-1)
            print("The updated list:")
            for x in todos:
                print(x)
        case 'exit':
            for x in todos:
                print(x)
            break
