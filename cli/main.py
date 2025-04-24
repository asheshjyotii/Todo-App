
from pathlib import Path 
'''
Todo:
Change the saving-> to a text file
'''
todos =[]

service = True

txt_file_location = Path("todos_data.txt")

def copy_prev_data(file_location=txt_file_location):
    try:
        with open (txt_file_location, 'r') as f:
            return f.readlines()
        return True
    except Exception as e:
        return False
def add_new_data(todos, file_location=txt_file_location):
    
    try:
        with open (txt_file_location, 'w') as f:
            f.writelines(todos)
        return True
    except Exception as e:
        return False
        

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
            prev_data = copy_prev_data()
            
            userInput = input("Enter the todo: ")
            todo = userInput.capitalize()
            todos.append(todo+"\n")
            success = add_new_data(todos)
            if success:
                print(f"Added '{todo}' to the list...")
            else: 
                print("There was some issue white writing into file....")
                continue
        case 'show':
            print("The todo List:")
            show_todos = copy_prev_data()
            if show_todos:
                for index,x in enumerate(show_todos):
                    print(f"{index+1}.{x.rstrip("\n")}")
            else:
                print("Some problem occured while reading the file")
                continue
            
        case 'edit':
            show_todos = copy_prev_data()
            if show_todos:
                for index,x in enumerate(show_todos):
                    print(f"Enter {index+1} to change {x.rstrip("\n")}")
            else:
                print("Some problem occured while reading the file")
                continue
            

            userInput = int(input("-> "))
            print(userInput)
            if userInput <=0 or userInput > len(show_todos):
                print("Invalid choice.")
                continue

            newTodo = input("Enter the new todo: ").capitalize()
            todos = show_todos
            todos [userInput-1] = newTodo+"\n"
            success = add_new_data(todos)
            if success:
                print("The new todo list:")
            else: 
                print("There was some issue white writing into file....")
                continue
            
            show_todos = copy_prev_data()
            if show_todos:
                for index,x in enumerate(show_todos):
                    print(f"{index+1}. {x.rstrip("\n")}")
            else:
                print("Some problem occured while reading the file")
                continue
            
        case 'complete':
            show_todos = copy_prev_data()
            if show_todos:
                for index,x in enumerate(show_todos):
                    print(f"Enter {index+1} to mark '{x.rstrip("\n")}' as complete")
            else:
                print("Some problem occured while reading the file")
                continue
            

            userInput = int(input("-> "))
            show_todos.pop(userInput-1)
            todos = show_todos
            success = add_new_data(todos)
            if success:
                print("The updated list:")
            else: 
                print("There was some issue white writing into file....")
                continue
            
            show_todos = copy_prev_data()
            if show_todos:
                for index,x in enumerate(show_todos):
                    print(f"{index+1}.{x.rstrip("\n")}")
            else:
                print("Some problem occured while reading the file")
                continue
            
        case 'exit':
            print("Incomplete todos:")
            show_todos = copy_prev_data()
            if show_todos:
                for index,x in enumerate(show_todos):
                    print(f"{index+1}. {x.rstrip("\n")}")
                break
            else:
                print("Some problem occured while reading the file")
                continue
            
            
