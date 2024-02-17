from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk,Image #PIL -> Pillow
import mysql.connector
con=mysql.connector.connect(host="127.0.0.1",user="root",password="1718
10110306800307",database="db",port="3306")
cur=con.cursor()
def bookRegister():
 import mysql.connector
 
con=mysql.connector.connect(host="127.0.0.1",user="root",password="1718
10110306800307",database="db",port="3306")
 cur=con.cursor()
 bookid=bookInfo1.get()
 Title=bookInfo2.get()
 Author=bookInfo3.get()
 Summary=bookInfo4.get()
 insertBooks="insert into books values(%s,%s,%s)"
 summary="insert into summary values(%s,%s,%s)"
 sql=(bookid,Title,Author)
 info=(bookid,Title,Summary)
 try:
 cur.execute(insertBooks,sql)
 con.commit()
 cur.execute(summary,info)
 con.commit()
 messagebox.showinfo('Success',"Book added successfully")
 except:
 messagebox.showinfo("Error","Can't add data into Database")
def addBook(): 
 
 global bookInfo1 ,bookInfo2, bookInfo3,bookInfo4,Canvas1, con, cur, 
bookTable, root
 root =Toplevel()
 root.resizable(False,False)
 root.title("Library")
 root.minsize(width=400,height=400)
 root.geometry("700x500")
 
 
2.Addbook.py
 
 same=True
 n=1
 background_image =Image.open("add book.jpg")
 [imageSizeWidth, imageSizeHeight] = background_image.size
 newImageSizeWidth = int(imageSizeWidth*n)
 if same:
 newImageSizeHeight = int(imageSizeHeight*n)
 else:
 newImageSizeHeight = int(imageSizeHeight/n)
 background_image =
background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.A
NTIALIAS)
 img = ImageTk.PhotoImage(background_image)
 Canvas1 = Canvas(root)
 Canvas1.create_image(300,340,image = img)
 Canvas1.config(bg="white",width = newImageSizeWidth, height =
newImageSizeHeight)
 Canvas1.pack(expand=True,fill=BOTH)
 HF1 = Frame(root,bg="black",bd=5)
 HF1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
 HL = Label(HF1, text="Add Books", bg='black', fg='white', 
font=('Courier',15))
 HL.place(relx=0,rely=0, relwidth=1, relheight=1)
 LF = Frame(root,bg="black")
 LF.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
 lb1 = Label(LF,text="Book ID : ", bg='black', fg='white',font=("Courier"))
 lb1.place(relx=0.05,rely=0.2, relheight=0.08)
 bookInfo1 =Entry(LF)
 bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
 lb2 = Label(LF,text="Title : ", bg='black', fg='white',font=("Courier"))
 lb2.place(relx=0.05,rely=0.35, relheight=0.08)
 bookInfo2 =Entry(LF)
 bookInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
 lb3 = Label(LF,text="Author : ", bg='black', fg='white',font=("Courier"))
 lb3.place(relx=0.05,rely=0.50, relheight=0.08)
 bookInfo3 =Entry(LF)
 bookInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
 
 
lb4=Label(LF,text="Summary",bg="black",fg="white",font=("Courier"))
 lb4.place(relx=0.05,rely=0.65,relheight=0.08)
 bookInfo4=Entry(LF)
 bookInfo4.place(relx=0.3,rely=0.65,relwidth=0.62,relheight=0.08)
 SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', 
fg='black',command=bookRegister)
 SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
 quitBtn = Button(root,text="Quit",bg='#f7f1e3', 
fg='black',command=root.destroy)
 quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
 root.mainloop()
