import json

def parsing_input():
    expression = input("Enter expression (e.g., 5 + 3): ")
    try:
        a, op, b = expression.split()
        return float(a), op, float(b)
    except ValueError:
        print("Invalid input")
        return None, None, None


def calculation(a, op, b):
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b if b != 0 else None,
        "%": lambda a, b: a % b if b != 0 else None
    }

    if op in operations:
        return operations[op](a, b)
    return None


def save_history(history):
    with open("history.json", "w") as f:
        json.dump(history, f)


def load_history():
    try:
        with open("history.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def main():
    history = load_history()

    a, op, b = parsing_input()

    if a is None:
        return

    result = calculation(a, op, b)

    if result is None:
        print("Invalid operation")
        return

    history.append(f"{a} {op} {b} = {result}")
    print("Result:", result)
    save_history(history)

    while True:
        expr = input("Enter (* 2) or command (history/clear/exit): ").lower()

        if expr == "history":
            for h in history:
                print(h)
            continue

        elif expr == "clear":
            history.clear()
            save_history(history)
            print("History cleared")
            continue

        elif expr == "exit":
            print("Thank you!")
            break

        try:
            op, b = expr.split()
            b = float(b)
        except ValueError:
            print("Invalid input")
            continue

        result = calculation(result, op, b)

        if result is None:
            print("Invalid operation")
            continue

        history.append(f"{op} {b} = {result}")
        print("Result:", result)
        save_history(history)


if __name__ == "__main__":
    main()
