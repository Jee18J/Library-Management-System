from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image #PIL -> Pillow
import mysql.connector
mydatabase="db"
con=mysql.connector.connect( 
host="127.0.0.1",user="root",password="171810110306800307",database=
mydatabase,port="3306")
cur = con.cursor()
# Enter Table Names here
def View():
 root=Toplevel()
 root.title("Library")
 root.minsize(width=400,height=400)
 root.geometry("700x500")
 root.resizable(False,False)
 
 same=True
 n=1
 background_image =Image.open("view.jpg")
 [imageSizeWidth, imageSizeHeight] = background_image.size
 newImageSizeWidth = int(imageSizeWidth*n)
if same:
 newImageSizeHeight = int(imageSizeHeight*n)
else:
 newImageSizeHeight = int(imageSizeHeight/n)
background_image =
background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.
ANTIALIAS)
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
Canvas1.create_image(300,340,image = img)
Canvas1.config(bg="white",width = newImageSizeWidth, height =
newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)
 headingFrame1 = Frame(root,bg="black",bd=5)
 headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
 headingLabel = Label(headingFrame1, text="View Books", bg='black', 
fg='white', font = ('Courier',15))
 headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
 labelFrame = Frame(root,bg='black')
 labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
 y = 0.25
 Label(labelFrame, 
text="%-10s%-40s%-30s"%('bookid','Title','Author'),bg='black',fg='white',f
ont=("Courier",10)).place(relx=0.07,rely=0.1)
 Label(labelFrame, text =
"----------------------------------------------------------------------------",bg='bla
ck',fg='white').place (relx=0.05,rely=0.2)
 getBooks = "select * from books"
 
try:
 cur.execute(getBooks)
 ans=cur.fetchall()
 con.commit()
 for i in ans:
 Label(labelFrame,text="%-10s%-30s%-30s"%(i[0],i[1],i[2]) 
,bg='black', fg='white',font=("Courier",10)).place(relx=0.07,rely=y)
 y += 0.1
 except:
 messagebox.showinfo("Failed to fetch files from database")
 
 quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', 
command=root.destroy)
 quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
 
 root.mainloop()
