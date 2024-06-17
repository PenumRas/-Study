telephone_book = {}



def parse_input(command):
    if " " in command:
        key_word, *args = command.split(" ", 1)
    else:
        return command, None
    return key_word, *args


def command_exit(command):
    command_exit_words = ["exit", "quit", "leave"]
    if any(command.lower() == el for el in command_exit_words):
        return True


def command_greeting(command):
    command_greeting_words = ["hi", "hello", "greet"]
    if any(command.lower() == el for el in command_greeting_words):
        return True


def command_add(command):
    key_word, value_mod = parse_input(command)
    if key_word.lower() == 'add' in key_word:
        try:
            name, telephone = value_mod.split(" ", 1)
            telephone_book[name] = telephone
            return telephone_book
        except (ValueError, AttributeError):
            print("Try to write command {'add'} and then {'name'} and {'Phone number'} ")
            return None
    return False


def command_change_phone(command):
    key_word, value_mod = parse_input(command)
    if key_word.lower() == 'change':
        try:
            name, telephone = value_mod.split(" ", 1)
            if name in telephone_book:
                telephone_book[name] = telephone
                return telephone_book
            else:
                print(f"Sorry, but {name} not found in book")
        except AttributeError:
            print("Try to write command {'change'} and then {'name'} and {'New Phone number'} ")

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
    print("Hello, I am personal assistant ")
    while True:
        command = input("command and values: ")
        if command_exit(command):
            break

        elif command_greeting(command):
            print("Hi, what You want to do?")

        elif command == "help":
            print(command_help())

        elif command_change_phone(command):
            result = command_change_phone(command)
            if result:
                print(f"Updated Phone_book is {telephone_book}")
            if result is None:
                continue

        elif command_add(command):
            result = command_add(command)
            if result:
                print(f"Updated Phone_book is {telephone_book}")
            if result is None:
                continue
        else:
            print("If Y dont know what I can - print 'Help'")


main()
