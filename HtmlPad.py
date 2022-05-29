from tkinter import *
import tkinter.messagebox as meassge1
import webbrowser
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
root = Tk()
root.title(f"Untitled - HtmlPad")
def quit():
    a = meassge1.askquestion("Exit","Are you sure you want to exit")
    if a == "yes":
     root.destroy()
def gethelp():
    meassge1.showinfo("Info", "This App Made By Saksham Jain")
def run():
    global HTMLFILE
    if HTMLFILE == None:

        if HTMLFILE == None:
            HTMLFILE = asksaveasfilename(initialfile="WritePadUntitled.html", defaultextension=".html",
                                         filetypes=[("All Files", "*.*"), ("Html documents", "*.html")])
            if HTMLFILE == "":
                HTMLFILE = None
            else:
                fileinside = open(HTMLFILE, 'w')
                fileinside.write(textarea.get(1.0, END))
                fileinside.close()
                root.title(os.path.basename(HTMLFILE) + "-HtmlPad")
        else:
            fileinside = open(HTMLFILE, 'w')
            fileinside.write(textarea.get(1.0, END))
            fileinside.close()
            root.title(os.path.basename(HTMLFILE) + "-HtmlPad")
    else:
     f = open(HTMLFILE, 'w')
     f.write(textarea.get(1.0,END))
     f.close()
    webbrowser.open_new_tab(HTMLFILE)
def help():
    meassge1.askquestion("Help","Do You Want Recieve Help")
def cut():
    textarea.event_generate("<<Cut>>")
def copy():
    textarea.event_generate("<<Copy>>")
def paste():
    textarea.event_generate("<<Paste>>")
def newfile():
       global HTMLFILE
       root.title("Untitled - HtmlPad")
       HTMLFILE = None
       textarea.delete(1.0,END)
def openfile():
      global HTMLFILE
      HTMLFILE = askopenfilename(defaultextension=".html",filetypes=[("All Files","*.*"),("Html documents","*.html")])
      if HTMLFILE==" ":
          HTMLFILE=None
      else:
           root.title(os.path.basename(HTMLFILE)+"-HtmlPad")
           textarea.delete(1.0, END)
           fileinside=open(HTMLFILE,"r")
           textarea.insert(1.0,fileinside.read())
           fileinside.close()
def savefile():
        global HTMLFILE
        HTMLFILE=asksaveasfilename(initialfile="WritePadUntitled.html",defaultextension=".html",filetypes=[("All Files","*.*"),("Text Documents","*.html")])
        if HTMLFILE == "":
           HTMLFILE=None
        else:
           fileinside = open(HTMLFILE, 'w')
           fileinside.write(textarea.get(1.0, END))
           fileinside.close()
           root.title(os.path.basename(HTMLFILE) + "-WritePad")
def sae():
    global HTMLFILE
    if HTMLFILE==None:
       HTMLFILE = asksaveasfilename(initialfile="WritePadUntitled.html", defaultextension=".html",filetypes=[("All Files", "*.*"),("Html documents", "*.html")])
       if HTMLFILE == "":
        HTMLFILE = None
       else:
          fileinside = open(HTMLFILE, 'w')
          fileinside.write(textarea.get(1.0, END))
          fileinside.close()
          root.title(os.path.basename(HTMLFILE) + "-HtmlPad")
    else:
     fileinside = open(HTMLFILE, 'w')
     fileinside.write(textarea.get(1.0, END))
     fileinside.close()
     root.title(os.path.basename(HTMLFILE) + "-HtmlPad")
def enter():
     textarea.insert(END,'''<!DOCTYPE html>
<html>
<head><title></title></head>
<body>

</body>
</html>''')


def js():
    textarea.insert(INSERT,'''<!DOCTYPE html>
<html>
<head><title></title></head>
<body>
<script>
</script>
</body>
</html>''')
def h():
    textarea.insert(INSERT,"<h1></h1>")
def p():
    textarea.insert(INSERT, "<p></p>")
scroll = Scrollbar(root)
scroll.pack(side=RIGHT,fill=Y)
HTMLFILE = None
textarea = Text(root, font=("Lucida Console",17),yscrollcommand=scroll.set)
textarea.pack(fill=BOTH,expand=TRUE)
scroll.config(command=textarea.yview)
MainMenu=Menu(root,background='red', fg='white')
Filemenu=Menu(MainMenu,tearoff=0)
Filemenu.add_command(label="New",command=newfile)
Filemenu.add_command(label="Open",command=openfile)
Filemenu.add_command(label="Save",command=sae)
Filemenu.add_command(label="Save As",command=savefile)
Filemenu.add_separator()
Filemenu.add_command(label="Exit",command=quit)
basic=Menu(MainMenu,tearoff=0)
basic.add_command(label="Enter basic structure",command=enter)
basic.add_command(label="Insert Basic JS with HTML",command=js)
basic.add_command(label="H1",command=h)
basic.add_command(label="P",command=p)
MainMenu.add_cascade(menu=Filemenu,label="File")
MainMenu.add_cascade(menu=basic,label="Enter")
Edit=Menu(MainMenu,tearoff=0)
Edit.add_command(label="Cut",command=cut)
Edit.add_command(label="Copy",command=copy)
Edit.add_command(label="Paste",command=paste)
MainMenu.add_cascade(menu=Edit,label="Commands")
r=Menu(MainMenu,tearoff=0)
r.add_command(label="Run",command=run)
MainMenu.add_cascade(menu=r,label="Run")
Help=Menu(MainMenu,tearoff=0)
Help.add_command(label="About",command=gethelp)
Help.add_command(label="Help",command=help)
MainMenu.add_cascade(menu=Help,label="Help")
root.config(menu=MainMenu)
root.mainloop()