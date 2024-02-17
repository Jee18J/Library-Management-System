from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image #PIL -> Pillow
def text():
 root =Toplevel()
 root.resizable(False,False)
 root.title("Library")
 root.geometry("600x500")
 same=True
 n=1
 background_image =Image.open("t.jpg")
 [imageSizeWidth, imageSizeHeight] = background_image.size
 newImageSizeWidth = int(imageSizeWidth*n)
 if same:
 newImageSizeHeight = int(imageSizeHeight*n)
 else:
 newImageSizeHeight = int(imageSizeHeight/n)
 background_image =
background_image.resize((newImageSizeWidth,newImageSizeHeight),Ima
ge.ANTIALIAS)
 img = ImageTk.PhotoImage(background_image)
 Canvas1 = Canvas(root)
 Canvas1.create_image(300,340,image = img)
 Canvas1.config(bg="white",width = newImageSizeWidth, height =
newImageSizeHeight)
 Canvas1.pack(expand=True,fill=BOTH)
 root.mainloop()
