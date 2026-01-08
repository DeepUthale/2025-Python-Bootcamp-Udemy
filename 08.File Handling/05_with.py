# file = open("deep.txt", "r")
# content = file.read()
# print(content)
# file.close()

with open("deep.txt", "r") as file: # Context Manager
    content = file.read()
    print(content)
    # No need to write file.close(), file is closed by default, when using with syntax
