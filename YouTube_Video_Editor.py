##########################################################################################
## This program downloads YouTube video's determined by the URL entered by the user
## and gives the user the choice to mirror the video (more filters will be added in
## the continuation project as well as converting the mp4 files to others such as
## avi or jpg) or an audio filter such as echo, lowers, highers the
## volume.  It can also convert the audio from Mp4 file to Mp3.
##
## Creators: Devon Rusconi - created GUI, downloaded ffmpeg, ffplay, and youtube-dl
## and coded into python using command line, used ffplay to play video and add filter
##
## Brayanne Reyes- created audio Gui, used ffmpeg to add audio filters, used ffmpeg to
## convert mp4 to mp3 using command line coded for python.
##
## Date: March 26, 2014
###########################################################################################

import subprocess
import Tkinter
import tkMessageBox


###########################################DEVON RUSCONI####################################

class MyGUI:
    def __init__(self):
        self.main_window=Tkinter.Tk() #Creates Window        
        self.label1 = Tkinter.Label(self.main_window, text = "YouTube Video Editor!") #Name of Program
        self.label1.pack() #Displays Name
        self.label2 = Tkinter.Label(self.main_window, text = "Copy and paste video URL here: ") #Instructions for user
        self.label2.pack()#Display instructions
        self.textEntry = Tkinter.Entry(self.main_window, width = 70) #Text Box and Size
        self.textEntry.pack() #Displays Textbox   
        self.b1=Tkinter.Button(self.main_window, text="Download", command=self.tryURL) #Download Button
        self.b1.pack() #Displays Button  
        Tkinter.mainloop() #Creates GUI
        
    def  tryURL(self):        
        y = self.textEntry.get() #Grabs the user's URL to download
        s = 'youtube-dl.exe "'+y+'"' #Takes the .exe file and the user's URL as string for command line
        x = subprocess.call(s, shell = True) #Takes that string and enters it in the command line
        tkMessageBox.showinfo("Complete!", "Your Download is completed. Check your 'Downloads' folder for your video.")
        #Download is in the DOWNLOAD_FOLDER on Desktop
        self.second_window=Tkinter.Tk() #Displays a second window
        self.label3 = Tkinter.Label(self.second_window, text = "Let's start editing!!") #takes user to editing software
        self.label3.pack()#Displays label in GUI
        self.b2= Tkinter.Button(self.second_window, text = "Let's GO!", command=self.rename)#Will take user to rename video
        self.b2.pack()
               

    def rename(self):
        self.third_window=Tkinter.Tk()#Displays a third window
        self.FILENAME = Tkinter.Label(self.third_window, text = "Copy and paste original file name here: ") #Instructions for user
        self.FILENAME.pack()#Display instructions
        self.originalName = Tkinter.Entry(self.third_window, width = 70) #Text Box and Size
        self.originalName.pack() #Displays textEntry to GUI       
        self.NEW_FILENAME = Tkinter.Label(self.third_window, text = "Enter your new file name here: ") #Instructions for user
        self.NEW_FILENAME.pack()#Display instructions
        self.newName = Tkinter.Entry(self.third_window, width = 70) #Text Box and Size
        self.newName.pack()#Displays textEntry to GUI        
        self.ContinueButton = Tkinter.Button(self.third_window, text = "Rename", command = self.renameCommands)#Renames file
        self.ContinueButton.pack()#Displays to GUI
        

    def renameCommands(self):
        OLD = self.originalName.get()#Gets the name into a variable
        NEW = self.newName.get()#Gets the name into a variable
        subprocess.call("cd Desktop", shell = True)#Command goes to users Desktop
        subprocess.call("cd DOWNLOAD_FOLDER", shell = True)#Command goes into the Downloads folder
        subprocess.call('REN "'+str(OLD)+".mp4"+'" '+str(NEW)+".mp4"+'"', shell = True)#Renames file in Command line
        self.forth_window = Tkinter.Tk()
        self.filterAsk = Tkinter.Label(self.forth_window, text = "Do you want to add a filter?")#Choice of filter
        self.filterAsk.pack()#Displays label on GUI
        self.buttonYes = Tkinter.Button(self.forth_window, text = "Yes", command = self.mirrorFilters)#Goes to filters if pressed
        self.buttonYes.pack()#Displays button on GUI
        self.buttonNo = Tkinter.Button(self.forth_window, text = "No", command = self.audio)#moves on to audio if pressed
        self.buttonNo.pack()#Displays button on GUI

    def mirrorFilters(self):
        y = self.newName.get()#Gets file name from user
        subprocess.call("cd Desktop", shell = True)#Takes command line to desktop
        subprocess.call("cd DOWNLOAD_FOLDER", shell = True)#Takes command line to folder
        subprocess.call('ffplay -i "'+str(y)+ '.mp4"' + ' -vf' +' "crop=iw/2:ih:0:0,split[tmp],pad=2*iw[left]; [tmp]hflip[right]; [left][right] overlay=W/2"', shell = True)
        #Adds mirror filter

#########################BRAYANNE REYES#############################################
        

    def audio(self):
        self.audio_window=Tkinter.Tk()#creates a window for audio
        self.echoButton = Tkinter.Button(self.audio_window, text="Echo",fg="red",
                                        command=self.echo)
        self.echoButton.pack()#creates a button for echo, when selected it goes to the echo function
        
        self.convertButton = Tkinter.Button(self.audio_window, text="MP4 to MP3", fg="blue",
                                         command=self.convert)
        self.convertButton.pack()#creates a button for convert, when selected it goes to the convert function

        self.highButton = Tkinter.Button(self.audio_window, text="high", fg="green",
                                         command=self.high)
        self.highButton.pack()#creates a button for high volume, when selected it goes to the high volume function

        self.lowButton = Tkinter.Button(self.audio_window, text="low", fg="yellow",
                                         command=self.low)
        self.lowButton.pack()#creates a button for low volume, when selected it goes to the low volume function
        
        
        
    def echo(self):
        x = self.newName.get()
        subprocess.call("cd Desktop", shell = True)#does a process on the command prompt to direct to desktop
        subprocess.call("cd DOWNLOAD_FOLDER", shell = True)#does a process in the command prompt that redirects to the folder where program is saved
        subprocess.call('ffplay -i ' + str(x) + '.mp4 -af aecho=0.8:0.9:1000:0.5',shell = True)
        #proces for command prompt which gets the audio
        #from video and echoes it by a second with a decay to sound lower

    def convert(self):
        x = self.newName.get()#gets new name from the other function 
        subprocess.call("cd Desktop", shell = True)#does a process on the command prompt to direct to desktop
        subprocess.call("cd DOWNLOAD_FOLDER", shell = True)
        #does a process in the command prompt that redirects to the folder where program is saved
        subprocess.call('ffmpeg -i ' + str(x) + '.mp4 ' + str(x) + '.mp3', shell = True)
        #converts an mp4 file into an mp3 file
        subprocess.call('ffplay -i ' + str(x) + '.mp3', shell = True)
        #plays the song with a graphic window
        
    def high(self):
        x = self.newName.get()#gets new name from the other function 
        subprocess.call("cd Desktop", shell = True)
        #does a process on the command prompt to direct to desktop
        subprocess.call("cd DOWNLOAD_FOLDER", shell = True)
        #doess a process in the command prompt that redirects to the folder where program is saved
        subprocess.call('ffplay -i ' + str(x) + '.mp4 -af aeval=val(ch)*4:c=same',shell = True)
        #audio is 4 times stronger and plays video

    def low(self):
        x = self.newName.get()#gets new name from the other function
        subprocess.call("cd Desktop", shell = True)
        #does a process on the command prompt to direct to desktop
        subprocess.call("cd DOWNLOAD_FOLDER", shell = True)
        #does a process in the command prompt that redirects to the folder where program is saved
        subprocess.call('ffplay -i ' + str(x) + '.mp4 -af aeval=val(ch)/4:c=same',shell = True)
        #audio is 4 times lower ad plays video


mygui = MyGUI()
