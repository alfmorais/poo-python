def show_task(todo_list: list):
    print("-" * 50)
    print("Tarefas: ")

    if not todo_list:
        print(todo_list)
    else:
        for index, task in enumerate(todo_list):
            print(f"{index}: {task}")

    print("-" * 50)
    print()


def do_undo(todo_list: list, redo_list: list):
    if not todo_list:
        print("-" * 50)
        print("Nada para desfazer.")
        print("-" * 50)
        return

    last_todo = todo_list.pop()
    redo_list.append(last_todo)


def do_redo(todo_list: list, redo_list: list):
    if not redo_list:
        print("-" * 50)
        print("Nada para refazer.")
        print("-" * 50)
        return

    last_redo = redo_list.pop()
    todo_list.append(last_redo)


def do_add(todo: str, todo_list: list):
    todo_list.append(todo)


if __name__ == "__main__":
    todo_list = []
    redo_list = []

    while True:
        todo = input("Digite uma tarefa ou undo, redo, ls: ")

        if todo.lower() == "ls":
            show_task(todo_list=todo_list)
            continue

        elif todo.lower() == "undo":
            do_undo(todo_list=todo_list, redo_list=redo_list)
            continue

        elif todo.lower() == "redo":
            do_redo(todo_list=todo_list, redo_list=redo_list)
            continue

        do_add(todo=todo, todo_list=todo_list)
