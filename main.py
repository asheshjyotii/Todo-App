'''
Todo:
create list object
infinite take user input
prit user input in first letter capitals
add the user input into the list
'''
service = True
todos =[]
todo = input("Enter First Todo:\n")
todo = todo.capitalize()
print('The entered todo is:',todo)
todos.append(todo)  
while service:
    todo = input("Enter next Todo or 'exit' to Exit:\n")
    if todo == 'exit':
        service = False
    else:
        todo = todo.capitalize()
        print('The entered todo is:',todo)
        todos.append(todo)
print("The todos are:")
for x in todos:
    print(x)
