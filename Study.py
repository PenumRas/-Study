def parse_input(user_input):
    command, *args = user_input.split()
    command = command.strip().lower()
    return command, *args


def command_add(args, telephone_book):
    try:
        name, telephone = args
        telephone_book[name] = telephone
        return telephone_book
    except (ValueError, AttributeError):
        print("Try to write command {'add'} and then {'name'} and {'Phone number'} ")
        return None


def command_change_phone(args, telephone_book):
    try:
        name, telephone = args
        if name in telephone_book:
            telephone_book[name] = telephone
            return telephone_book
        else:
            print(f"Sorry, but {name} not found in book")
    except AttributeError:
        print("Try to write command {'change'} and then {'name'} and {'New Phone number'} ")


def command_del(args, telephone_book):
    name = args[0]
    if name in telephone_book:
        del telephone_book[name]
    return telephone_book


def command_phone_by_username(args, telephone_book):
    name = args[0]
    if name in telephone_book:
        return name, telephone_book[name]


def command_help():
    return """
Available commands:
- hi, hello: Greet the assistant
- add <name> <phone>: Add a new contact
- change <name> <new_phone>: Change number of contact
- help: Show this help message
- exit: Exit the assistant
"""


def main():
    telephone_book = {}
    print("Hello, I am personal assistant ")
    while True:
        user_input = input("command and values: ")
        command, *args = parse_input(user_input)

        if command in ["exit", "quit", "leave"]:
            break

        elif command in ["hi", "hello", "greet"]:
            print("Hi, what You want to do?")

        elif command == "help":
            print(command_help())

        elif command == "add":
            print(command_add(args, telephone_book))

        elif command == "change":
            print(command_change_phone(args, telephone_book))

        elif command == "del":
            print(command_del(args, telephone_book))

        elif command == "phone":
            print(command_phone_by_username(args, telephone_book))


        elif command == "all":
            print(f"List of Nanes and Numbers{telephone_book}")

        else:
            print("If Y dont know what I can - print 'Help'")


if __name__ == "__main__":
    main()
