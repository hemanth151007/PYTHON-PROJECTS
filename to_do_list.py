import json

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def main():
    print("Welcome to the To-Do List!")
    tasks = load_tasks()

    while True:
        command = input("Command (add/view/remove/done/exit): ").lower()

        if command == "add":
            task = input("Add task: ").strip()
            if not task:
                print("Task cannot be empty")
                continue

            try:
                priority = int(input("Priority (1-3): "))
                if not 1 <= priority <= 3:
                    print("Invalid priority. Please enter a number between 1 and 3.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            tasks.append({"task": task, "done": False, "priority": priority})
            save_tasks(tasks)
            print("Task added")

    elif command == "view":
        if not tasks:
            print("No tasks")
        else:
            sorted_tasks = sorted(tasks, key=lambda x: (x["done"], x["priority"]))
            for i, t in enumerate(sorted_tasks, 1):
                status = "✓" if t["done"] else "✗"
                print(i, f"[{status}]", t["task"], f"(Priority: {t['priority']})")
    elif command == "remove":
        try:
            task_num = int(input("Task number: "))
        except ValueError:
            print("Invalid input")
            continue

        if 1 <= task_num <= len(tasks):
            sorted_indices = sorted(range(len(tasks)), key=lambda idx: (tasks[idx]["done"], tasks[idx]["priority"]))
            index = sorted_indices[task_num - 1]
            tasks.pop(index)
            save_tasks(tasks)
            print("Task removed")
        else:
            print("Invalid task number")
    elif command == "done":
        try:
            task_num = int(input("Task number: "))
        except ValueError:
            print("Invalid input")
            continue

        if 1 <= task_num <= len(tasks):
            sorted_indices = sorted(range(len(tasks)), key=lambda idx: (tasks[idx]["done"], tasks[idx]["priority"]))
            index = sorted_indices[task_num - 1]
            tasks[index]["done"] = not tasks[index]["done"]
            save_tasks(tasks)
            print("Task updated")
        else:
            print("Invalid task number")
    elif command == "exit":
        print("Goodbye!")
        break
    else:
        print("Invalid command")


if __name__ == "__main__":
    main()
