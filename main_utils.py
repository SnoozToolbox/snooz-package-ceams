import json
import os
import shutil

def isValidChoice(choice):
    if choice < 1 or choice > 7:
        return False
    return True

if __name__ == '__main__':
    print("Please pick a tool: ")
    print("1- Create a package")
    print("2- Create a module")
    print("3- Create a tool")
    print("4- Create a tool step")
    print("5- Create an app")
    print("6- Create a release package")
    print("7- Quit")
    
    
    choice = 0
    while not isValidChoice(choice):
        try:
            choice = int(input("(1-7):"))
        except:
            choice = 0

    if choice == 1:
        import utils.create_package
    elif choice == 2:
        import utils.create_module
    elif choice == 3:
        import utils.create_tool
    elif choice == 4:
        import utils.create_tool_step
    elif choice == 5:
        import utils.create_app
    elif choice == 6:
        import utils.create_release_packages
    elif choice == 7:
        quit()