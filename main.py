'''
Todo:
Change the saving to a text file
'''
todos =[]

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
            todos.append(todo+"\n")
            with open('todosData.txt','w') as f:
                f.writelines(todos)
            print(f"Added '{todo}' to the list...")
        case 'show':
            print("The todo List:")
            with open('todosData.txt','r') as f:
                show_todos = f.readlines()
            
            for index,x in enumerate(show_todos):
                print(f"{index+1}.{x.rstrip("\n")}")
        case 'edit':
            with open('todosData.txt','r') as f:
                show_todos = f.readlines()
            for index,x in enumerate(show_todos):
                print(f"Enter {index+1} to change {x.rstrip("\n")}")

            userInput = int(input("-> "))
            if userInput <=0 or userInput > len(todos):
                print("Invalid choice.")
                continue

            newTodo = input("Enter the new todo: ").capitalize()
            todos [userInput-1] = newTodo+"\n"
            with open('todosData.txt','w') as f:
                f.writelines(todos)
            print("The new todo list:")
            with open('todosData.txt','r') as f:
                show_todos = f.readlines()
            for index,x in enumerate(show_todos):
                print(f"{index+1}. {x.rstrip("\n")}")
        case 'complete':
            with open('todosData.txt','r') as f:
                show_todos = f.readlines()
            for index,x in enumerate(show_todos):
                print(f"Enter {index+1} to mark '{x.rstrip("\n")}' as complete")

            userInput = int(input("-> "))
            show_todos.pop(userInput-1)
            with open('todosData.txt','w') as f:
                f.writelines(show_todos)
            print("The updated list:")
            with open('todosData.txt','r') as f:
                show_todos = f.readlines()
            for index,x in enumerate(show_todos):
                print(f"{index+1}.{x.rstrip("\n")}")
        case 'exit':
            print("Incomplete todos:")
            with open('todosData.txt','r') as f:
                show_todos = f.readlines()
            for index,x in enumerate(show_todos):
                print(f"{index+1}. {x.rstrip("\n")}")
            break
