telephone_book = {}
help_command = "exit", "hi", "add"
def parse_input(command):
    key_word = []   #назва команди з рядку введення(1 слово)
    value_mod = []  #все що треба зробити\зберегти командою(2 і наст слова)
    if " " in command:
        key_word, value_mod = command.split(" ", 1)
    else:
        return  command, None
    return key_word, value_mod

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
    if key_word.lower() == ('add') in key_word:
        try:
            name, telephone = value_mod.split(" ", 1)
            telephone_book[name] = telephone
            return  telephone_book
        except (ValueError, AttributeError):
            print("Try to write command {'add'} and then {'name'} and {'Phone number'} ")
            return None
    return False

def command_help(command):
    if command == ("help"):
        print(f"for exit print some word{help_command} ")
def main():
    print("Hello, I am personal assistant ")
    while True:
        command = input("command and values: ")
        if command_exit(command):
            break
        elif command_greeting(command):
            print("Hi, what You want to do?")
        elif command_add(command):
            result = command_add(command)
            if result:
                print(f"Updated Phone_book is {telephone_book}")
            if result is None:
                continue
        elif command == "help":
            print(command_help(command))
        else:
            print("If Y dont know what I can - print 'Help'")



main()