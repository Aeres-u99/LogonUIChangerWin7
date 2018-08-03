#The script checks the size of file and moves it into
#Bg folder, and deletes the previous one. This way the logonUI changes everytime
import time,shutil,os,random

file_location="C:\\Windows\\System32\\oobe\\info\\Backgrounds\\"

def cpy(src,dest):
    shutil.copy(src,dest)

def rename(old,new):
    shutil.move(old,new)

def wait(delay):
    time.sleep(delay)

print("This program Automatically changes LogonUI wallpaper in Windows 7")
print("It randmoly selects the images from the Images folder!")

def RandomPic():
    cwdd = os.getcwd()
    print("Directory Before changing : ")
    print(cwdd)
    os.chdir(".\\Images")
    cwdd = os.getcwd()
    print("Directory After changing: ")
    print(cwdd)
    print("Selecting a random file ... ")
    filename = random.choice(os.listdir(".")) #This selects the random image from folder.
    print(filename+"                    ... [OK] ")
    print("renaming... "+filename+"              [OK]")
    rename(filename,"Backgrounddefault.jpg")
    print("checking for Already existing file... [OK]")
    if os.path.exists(file_location) and os.path.isfile(file_location+"\\Backgrounddefault.jpg"):
        print("File found! at location ... \n Removing the file ...                     [OK]")
        os.remove("C:\\Windows\\System32\\oobe\\info\\Backgrounds\\Backgrounddefault.jpg")              #removes the older image.
    print("Copying the file ... "+filename+"           [OK] ")
    cpy("Backgrounddefault.jpg",file_location)
    print("Renaming the file "+filename+" to its original name       ...     [OK]")
    rename("Backgrounddefault.jpg",filename)
    print("File name reverted back to original ...                           [OK]")
    print("Going back to normal directory ...")
    os.chdir("..")
    print("[OK]")
    print("Background file successfully changed! press Alt+Ctrl+Del to check!")
    wait(3)


def SlideShow():
    delaystring = """
                Slideshow basically changes the background image of your windows 7 continuously after a short period of time
                so, apparently every time you open the task manager window alt+ctrl+del you see a different randomly selected pic.
                By default time is set to 1 minute and its wise to not go below that. Upper limit can be changed as per wish.
                """
    print(delaystring)
    flag=True
    while(flag):
        try:
            delay = int(input("Enter time in seconds:  "))
        except ValueError:
            print("Cmon, time must be integer stupid.")
        if delay<60:
            flag=True
            print("Dont do this,it will get heavy on your system!!Time must be greater than 60s!!")
        else:
            flag=False
            print("Time accepted, minimise the terminal window to keep it running \n or press ctrl+C to exit")

    while True:
        RandomPic()
        _=os.system('cls')
        time.sleep(delay)

def HelpMenu():
    helpstr= """
                                            This code is written by ShiroiAkuma.
                                                aeres99[at]hotmail.com :D
                                ===================================================================
                                We all know that the logon ui of windows 7
                                is more or less very common and it becomes
                                dull and boring eventually, here this program
                                can be used to change that image dynamically.
                                It uses the registry value of OEMDEfault background
                                to change logon ui wallpaper.
                                It can be run in two modes.
                                1] Random mode: wherein the files are selected at once randomly
                                2] SLideShow mode: wherein the files are selected after a specified
                                interval of time.
                                feel free to use the code as per your requirement, Read the readme for
                                instructions on how to install, and also do remember to put in your favourite
                                images in Images folder.

            """
    print(helpstr)
    print("Thank you!")


