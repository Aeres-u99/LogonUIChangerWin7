
import Modification_module,os
def clearscr_():
    _ = os.system("cls")
menustring = """

=============================================================
|                          Welcome                          |
=============================================================
|                       1].[R]andomly set                   |
|                       2].[S]lideshow                      |
|                       3].[D]isplay Help                   |
|                       4].E[x]it                           |
=============================================================

"""
while(True):
    Modification_module.wait(1)
    clearscr_()
    print(menustring)
    choice=input("Enter your choice: ")
    if choice == 'R' or choice == 'r' or choice == '1' or choice == 'random' or choice == 'Random':
        Modification_module.RandomPic()
    elif choice == 'S' or choice == 's' or choice == '2' or choice == 'slideshow' or choice == 'Slideshow':
        Modification_module.SlideShow()
    elif choice == 'D' or choice == 'd' or choice == '3' or choice == 'display help' or choice == 'Display Help':
        Modification_module.HelpMenu()
    elif choice == 'X' or choice == 'x' or choice == '4' or choice == 'exit' or choice == 'Exit':
        exit(1);
    else:
        print("Incorrect input")
        break;



