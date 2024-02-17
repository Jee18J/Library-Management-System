from PIL import ImageTk,Image #PIL -> Pillow
import mysql.connector
from tkinter import messagebox
from Addbook import addBook
from Deletebook import delete
from Viewbooks import View
from summary import summary
from Text import text
mydatabase="db"
con =mysql.connector.connect
(host="localhost",user="root",password="",database=mydatabase)
cur = con.cursor()
root = Tk()
root.resizable(False,False)
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("700x500")
same=True
n=1
background_image =Image.open("summary.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size
newImageSizeWidth = int(imageSizeWidth*n)
if same:
 newImageSizeHeight = int(imageSizeHeight*n)
else:
 newImageSizeHeight = int(imageSizeHeight/n)
background_image =
background_image.resize((newImageSizeWidth,newImageSizeHeight),Image
.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
Canvas1.create_image(300,340,image = img)
Canvas1.config(bg="white",width = newImageSizeWidth, height =
newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)
hf=Frame(root,bg="black",bd=5)
hf.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
hl=Label(hf, text="LIBRARY", bg='black', fg='mint cream',font=("Courier",20))
hl.place(relx=0,rely=0, relwidth=1, relheight=1)
label=Label(root,text="By:Jeevitha Venkatesh,Lavisha.M.Haran and Neha
Zabi",fg="black",bg="white",font=("Courier"))
label.place(relx=0.0,rely=1.0,anchor="sw")
btn1 = Button(root,text="Add books",bg='black',
fg='white',command=addBook,font=("Courier"))
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
 
btn2 = Button(root,text="Delete Book",bg='black',
fg='white',command=delete,font=("Courier"))
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
 
btn3 = Button(root,text="View Books",bg='black',
fg='white',command=View,font=("Courier"))
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
 
btn4 = Button(root,text="Short summary",bg='black',
fg='white',command=summary,font=("Courier"))
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
btn5=Button(root,text="About the
project",bg="black",fg="white",command=text,font=("Courier"))
btn5.place(relx=0.28,rely=0.8,relwidth=0.45,relheight=0.1)
root.mainloop()
