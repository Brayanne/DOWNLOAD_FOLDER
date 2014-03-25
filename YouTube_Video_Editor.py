import subprocess
import Tkinter
import tkMessageBox


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
        self.ContinueButton = Tkinter.Button(self.third_window, text = "Rename", command = self.renameCommands)#takes to renameCommands def
        self.ContinueButton.pack()#Displays to GUI
        

    def renameCommands(self):
        
        OLD = self.originalName.get()#Gets the name into a variable
        NEW = self.newName.get()#Gets the name into a variable
        subprocess.call("cd Desktop", shell = True)#Command goes to users Desktop
        subprocess.call("cd DOWNLOAD_FOLDER", shell = True)#Command goes into the Downloads folder
        subprocess.call('REN "'+str(OLD)+".mp4"+'" '+str(NEW)+".mp4"+'"', shell = True)#Renames file in Command line
        self.forth_window = Tkinter.Tk()#Creates forth window
        self.filterAsk = Tkinter.Label(self.forth_window, text = "Do you want to add a filter?")#Choice of filter
        self.filterAsk.pack()#Displays label on GUI
        self.buttonYes = Tkinter.Button(self.forth_window, text = "Yes", command = self.filters)#Goes to filters if pressed
        self.buttonYes.pack()#Displays button on GUI
        self.buttonNo = Tkinter.Button(self.forth_window, text = "No", command = self.audio)#moves on to audio if pressed
        self.buttonNo.pack()#Displays button on GUI

    def filters(self):
        y = self.newName.get()#Gets new file name from user
        subprocess.call("cd Desktop", shell = True)#Takes command prompt to Desktop
        subprocess.call("cd DOWNLOAD_FOLDER", shell = True)#Takes command prompt to Downloads folder
        subprocess.call('ffplay -i "'+str(y)+ '.mp4"' + ' -vf' +' "crop=iw/2:ih:0:0,split[tmp],pad=2*iw[left]; [tmp]hflip[right]; [left][right] overlay=W/2"', shell = True)
        #Creates the filter for the video
        
    def audio(self):
        print("Not Yet")
                        

        


mygui = MyGUI()
