#Logon UI changer Win7 
I mostly do not like the plain blue background of windows 7.
There is a way to change it. It requires enabling a bit in regedit and then putting up the required image in %windir%//System32/oobe/info/backgrounds/[Backgrounddefault.jpg]  #without the [] 
if the file size is less than 250Kb it is accepted as the Logon UI background. 
Here in this program, I have used python to copy the file, the required image file to the location by selecting a random file from the Images folder.
In this way we can automatically change the LoginUIImage
TBH its fun to use and try. 

Instructions for installations:

Step1] Get ready to work with windows 7, one of the hardest decisions. **sighs


Step2] clone the Repository using `git clone https://github.com/Aeres-u99/LogonUIChangerWin7.git`


Step3] copy the Images which you like and are below 245kb to the Imgaes folder of the cloned repository.


Step4] Double click on Windows_Enable_LogonUI_change.reg to enable the bit.
``[[**warning: messing with registry can be riskier, for your own safety purposes kindly check the reg file that it doesnot contains anything unnecessary!]]``


Step5] Run the Program.py file by typing 
`%> python3 Program.py `


Select 1 to randomly set any of the image as background UI


Select 2 to Slideshow with the time interval of 60s atleast.
	The code can be modified to go and allow values lower than 60s but the problem with it is that it is riskier and can Lead to troubles


Select 3 to display help!


Slect 4 to exit the program.

Feel free to share the code and modify it as per your will, give me some credit for it tho ;)
