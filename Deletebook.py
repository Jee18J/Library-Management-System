from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image #PIL -> Pillow
import mysql.connector
mydatabase="db"
con =mysql.connector.connect 
(host="127.0.0.1",user="root",password="171810110306800307",database=mydatabase,
port="3306")
cur = con.cursor()
# Enter Table Names here
issueTable = "books_issued"
bookTable = "books" #Book Table
def deleteBook():
 bid=bookInfo1.get()
 print(bid)
 deletebook="delete from books where bookid=%s"
 deletesummary="delete from summary where bookid=%s"
 sql=bid
 try:
 cur.execute(deletebook,(sql,))
 con.commit()
 cur.execute(deletesummary,(sql,))
 con.commit()
 messagebox.showinfo('Success',"Book Deleted Successfully")
 
except:
 messagebox.showinfo("Looks like it's an Invalid Bookid")
 root.destroy()
def delete(): 
 
 global
bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root
 
 root =Toplevel()
 root.title("Library")
 root.minsize(width=400,height=400)
 root.geometry("700x500")
 same=True
 n=1
 background_image =Image.open("delete2.jpg")
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
 
 headingFrame1 = Frame(root,bg="black",bd=5)
 headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
 
 headingLabel = Label(headingFrame1, text="Delete Book", bg='black', 
fg='white', font=('Courier',15))
 headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
 
 labelFrame = Frame(root,bg='black')
 labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5) 
 
 
# Book ID to Delete
 lb2 = Label(labelFrame,text="Book ID : ", bg='black', 
fg='white',font=("Courier"))
 lb2.place(relx=0.05,rely=0.5)
 
 bookInfo1 = Entry(labelFrame)
 bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
 
 #Submit Button
 SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', 
fg='black',command=deleteBook)
 SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
 
 quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', 
command=root.destroy)
 quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
 
 root.mainloop()
