#started 28th wed jan 2026 :)
#just a better version of automate love :)
# all dis fuckery for what gain? 
import os
import tkinter as tk
from tkinter import filedialog,messagebox
from pathlib import Path

state = {"path":"","fullPath":""}

mainString = '''local fps\n\nfunction love.load()\n\nend\n\nfunction love.update(dt)\n\tfps = love.timer.getFPS()\nend
				\n\nfunction love.draw()\n\tlove.graphics.print(fps)\nend'''

confString = '''function love.conf(t)\n--t.window.width = 0\n--t.window.height = 0\nend'''

def confirmProjectPath():
	message = "Your project will be created at"+" "+str(state["fullPath"])
	return messagebox.askyesno("LoL",message)
	#return messagebox.askyesno("Confirm", message)

def successConfirmation():
	messagebox.showinfo('weeeeeeeeeeeeee','Project Created Successfully')

def setProjectDirectory():
	dirName = filedialog.askdirectory(title="Select where to create the project's folder")
	state["path"]= dirName	 	

def writeAFile(filepath,string):
	with open(filepath,'w') as file:
		file.write(string)

def makeADirectory(dirPath):
	os.mkdir(dirPath)


def createProject():
	state["fullPath"] = os.path.join(state["path"],projectName.get())
	mainPath = os.path.join(state["fullPath"],'main.lua')
	confPath = os.path.join(state["fullPath"],'conf.lua')
	#optional folders
	assetsPath = os.path.join(state["fullPath"],'assets')
	libsPath = os.path.join(state["fullPath"],'libs')
	scenesPath = os.path.join(state["fullPath"],'scenes')
	objectsPath = os.path.join(state["fullPath"],'objects')

	if confirmProjectPath():
		makeADirectory(state["fullPath"])
		writeAFile(mainPath,mainString)
	
		if createConf.get() == 1:
			writeAFile(confPath,confString)
		if createOptionalFolders.get() == 1:
			makeADirectory(assetsPath)
			makeADirectory(libsPath)
			makeADirectory(scenesPath)
			makeADirectory(objectsPath)
	#print(mainPath+'\n'+confPath)
	successConfirmation()

root = tk.Tk()
root.geometry('500x250')
root.title('create main.lua')

#tkinter variables
createConf = tk.IntVar()
createOptionalFolders = tk.IntVar()

tk.Label(root,text="Enter a name for your new Project :)").pack()

projectName = tk.Entry()
projectName.pack(pady=5)

tk.Label(root,text="Where to create the Project").pack()
browseButton = tk.Button(text='Browse',command=setProjectDirectory)
browseButton.pack()

configSelect = tk.Checkbutton(root, text="Create Config file?", variable=createConf,onvalue=1,offvalue=0)
configSelect.pack(anchor="w", padx=0)
assetsSelect = tk.Checkbutton(root, text="Create Optional Folders(assets,libs,etc)?", variable=createOptionalFolders,onvalue=1,offvalue=0)
assetsSelect.pack(anchor="w", padx=0)

createProjectButton = tk.Button(text='Create It :)',command=createProject)
createProjectButton.pack()

root.mainloop()