import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(todo+"\n")

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for i, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{i+1}-{item}")
    elif user_action.startswith("edit"):
        try:

            num = int(user_action[5:])
            num = num - 1

            todos = functions.get_todos()

            new_todo = input("enter new todo: ")
            todos[num] = new_todo + "\n"

            functions.write_todos(todos)
        except ValueError:
            print("your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:

            num = int(user_action[8:])
            num = num - 1

            todos = functions.get_todos()

            todos.pop(num)

            functions.write_todos(todos)
        except IndexError:
            print("Item does not exist")
            continue
    elif user_action.startswith("exit"):
        break

    else:
        print("invalid input")


