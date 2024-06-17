telephone_book = {}
def parse_input(command):
    key_word = []   #назва команди з рядку введення(1 слово)
    value_mod = []  #все що треба зробити\зберегти командою(2 і наст слова)
    if " " in command:
        key_word, value_mod = command.split(" ", 1)
    else:
        return  command
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
    try:
        key_word, value_mod = parse_input(command)
        if key_word.lower() == ('add'):
            name, telephone = value_mod.split(" ", 1)
            telephone_book = {
                "name": name,
                "telephone": telephone
            }
            return  telephone_book
        return True
    except ValueError:
        print("Try to write command {'add'} and then {'name'} and {'Phone number'} ")
def main():
    print("Hello, I am personal assistant ")
    while True:
        command = input("command and values: ")
        if command_exit(command):
            break
        elif command_greeting(command):
            print("Hi, what You want to do?")
        elif command_add(command):
            telephone_book=command_add(command)
            print(telephone_book)
        else:
            print("If Y dont know what I can - print 'Help'")



main()