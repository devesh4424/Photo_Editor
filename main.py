from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo
from turtle import bgcolor
from PIL import Image, ImageTk, ImageFilter, ImageEnhance
import os
import cv2
from PIL.ImageFilter import (
    CONTOUR, DETAIL, EDGE_ENHANCE_MORE, EMBOSS, SHARPEN, FIND_EDGES)

# Features


def rotate1():  # rotate anticlockwise
    global img8, img9
    img = Image.open('img'+str(counter-1)+'.png')
    img.thumbnail((600, 420))
    img8 = img.rotate(90)
    img9 = ImageTk.PhotoImage(img8)
    canvas2.create_image(300, 210, image=img9)
    canvas2.image = img9


def rotate2():  # rotate clockwise
    global img10, img11
    img = Image.open('img'+str(counter-1)+'.png')
    img.thumbnail((600, 420))
    img10 = img.rotate(-90)
    img11 = ImageTk.PhotoImage(img10)
    canvas2.create_image(300, 210, image=img11)
    canvas2.image = img11


def flip1():  # flip left to Right
    global img12, img13
    img = Image.open('img'+str(counter-1)+'.png')
    img.thumbnail((600, 420))
    img12 = img.transpose(Image.FLIP_LEFT_RIGHT)
    img13 = ImageTk.PhotoImage(img12)
    canvas2.create_image(300, 210, image=img13)
    canvas2.image = img13


def flip2():  # flip Top to bottom
    global img14, img15
    img = Image.open('img'+str(counter-1)+'.png')
    img.thumbnail((600, 420))
    img14 = img.transpose(Image.FLIP_TOP_BOTTOM)
    img15 = ImageTk.PhotoImage(img14)
    canvas2.create_image(300, 210, image=img15)
    canvas2.image = img15


def filter1():
    window_3()


def filter():
    global img16, img17
    img17 = ImageTk.PhotoImage(img16)
    canvas2.create_image(300, 210, image=img17)
    canvas2.image = img17


def contour():
    global img16
    img = Image.open('img'+str(counter-1)+'.png')
    img.thumbnail((600, 420))
    img16 = img.filter(CONTOUR)
    filter()


def detail():
    global img16
    img = Image.open('img'+str(counter-1)+'.png')
    img.thumbnail((600, 420))
    img16 = img.filter(DETAIL)
    filter()


def edge_enhance_more():
    global img16
    img = Image.open('img'+str(counter-1)+'.png')
    img.thumbnail((600, 420))
    img16 = img.filter(EDGE_ENHANCE_MORE)
    filter()


def emboss():
    global img16
    img = Image.open('img'+str(counter-1)+'.png')
    img.thumbnail((600, 420))
    img16 = img.filter(EMBOSS)
    filter()


def sharpen():
    global img16
    img = Image.open('img'+str(counter-1)+'.png')
    img.thumbnail((600, 420))
    img16 = img.filter(SHARPEN)
    filter()


def find_edges():
    global img16
    img = Image.open('img'+str(counter-1)+'.png')
    img.thumbnail((600, 420))
    img16 = img.filter(FIND_EDGES)
    filter()


def blur(any):
    global img1, img2, canvas2
    for m in range(0, v1.get()+1):
        img = Image.open('img'+str(counter-1)+'.png')
        img.thumbnail((650, 600))
        img1 = img.filter(ImageFilter.BoxBlur(m))
        img2 = ImageTk.PhotoImage(img1)
        canvas2.create_image(0, 0, anchor=NW, image=img2)
        canvas2.image = img2


def brightness(any):
    global img2, img3, img4, counter, canvas2
    for m in range(0, v2.get()+1):
        img = Image.open('img'+str(counter-1)+'.png')
        img.thumbnail((650, 600))
        img2 = ImageEnhance.Brightness(img)
        img3 = img2.enhance(m)
        img4 = ImageTk.PhotoImage(img3)
        canvas2.create_image(0, 0, anchor=NW, image=img4)
        canvas2.image = img4


def contrast(any):
    global img5, img6, img7, canvas2
    for m in range(0, v3.get()+1):
        img = Image.open('img'+str(counter-1)+'.png')
        img.thumbnail((650, 600))
        img5 = ImageEnhance.Contrast(img)
        img6 = img5.enhance(m)
        img7 = ImageTk.PhotoImage(img6)
        canvas2.create_image(0, 0, anchor=NW, image=img7)
        canvas2.image = img7

# Window1


def window_1():
    global window1
    window1 = Tk()
    window1.geometry("1200x900")
    window1.attributes('-fullscreen', True)
    window1.title('Photo Editor GUI')
    window1.configure(bg='#141414')
    background = PhotoImage(file="img.png")
    label1 = Label(window1, image=background)
    label1.place(x=0, y=0)
    window1.configure(bg='#141414')
    btn1 = Button(window1, width=2, height=1, text="←", bg='black', fg='white',
                  font=('ariel 40 bold'), relief=FLAT, command=window1.destroy)
    btn1.place(x=400, y=350)
    btn2 = Button(window1, width=5, height=1, text="📷", bg='black', fg='white',
                  font=('ariel 40 bold'), relief=FLAT, command=cam)
    btn2.place(x=800, y=350)
    btn3 = Button(window1, width=10, height=1, text="Edit Image", bg='black', fg='white',
                  font=('ariel 20 bold'), relief=FLAT, command=open_image)
    btn3.place(x=550, y=380)

    canvas3 = Canvas(window1, width="900", height="100",
                     relief=SUNKEN, bd=0, bg='#FF0000')
    canvas3.place(x=250, y=80)
    canvas3.create_text(450, 50, text='Welcome to Photo Editor',
                        fill='white', font='oxanium 48 bold')
    window1.mainloop()

# Window2++


def window_2():
    global window2, canvas1, canvas2
    window2 = Tk()
    window2.geometry("1256x944")
    window2.attributes('-fullscreen', True)
    window2.configure(bg='#141414')
    window2.title("Editing Window")
    title = Label(window2, text="Photo Editor", font=40,
                  relief=GROOVE, bg="#141414", fg='#25dae9')
    title.place(x=600, y=50)
    canvas1 = Canvas(window2, width="550", height="420",
                     relief=SUNKEN, bd=1, bg='#141414')
    canvas1.place(x=10, y=160)
    canvas2 = Canvas(window2, width="550", height="420",
                     relief=SUNKEN, bd=1, bg='#141414')
    canvas2.place(x=800, y=160)
    frame = Frame(window2, borderwidth=9,
                  bg="#ffcc66", relief=SUNKEN)
    frame.pack(side=RIGHT)
    text = Text(window2, height=2, bd=0, bg='#141414',
                font='oxanium 20 bold', fg='white')
    text.place(x=200, y=610)
    text.insert('1.0', 'Original Image')
    text2 = Text(window2, height=2, bd=0, bg='#141414',
                 font='oxanium 20 bold', fg='white')
    text2.place(x=1000, y=610)
    text2.insert('1.0', 'Edited Image')
    button(window2, 15, 8, "Blur", '#25dae9', "#141414", 25, 9, 1, scale1)
    button(window2, 15, 98, "Contrast", '#25dae9', "#141414", 25, 9, 1, scale3)
    button(window2, 650, 290, "Undo", '#ffa157', "#141414", 25, 9, 1, undo)
    button(window2, 15, 53, "Brightness",
           '#ffa157', "#141414", 25, 9, 1, scale2)
    button(window2, 1270, 90, "✔️", '#00FF00',
           "#141414", ('ariel 20 bold'), 4, 1, temp_save)
    button(window2, 600, 350, "Exit", '#25dae9',
           "#141414", 28, 9, 1, window2.destroy)
    button(window2, 570, 10, "Filter", '#ffcc66',
           "#141414", 25, 9, 1, filter1)
    button(window2, 320, 8, "↶", '#25dae9', "#141414", 25, 9, 1, rotate1)
    button(window2, 420, 8, "↷", '#25dae9', "#141414", 25, 9, 1, rotate2)
    button(window2, 690, 350, "Save", '#ffcc66', "#141414", 28, 9, 1, save)
    button(window2, 320, 45, "Flip Right",
           '#ffccc6', "#141414", 25, 9, 1, flip1)
    button(window2, 420, 45, "Flip Top", '#ffccc6', "#141414", 25, 9, 1, flip2)
    button(window2, 1180, 90, "❌", '#FF0000',
           "#141414", ('ariel 20 bold'), 4, 1, cross)
    button(window2, 650, 380, "⌂", '#FF0000',
           "#141414", ('ariel 40 bold'), 2, 1, home)
# Window3


def window_3():
    global window3
    window3 = Tk()
    window3.geometry("200x200+570+10")
    window3.maxsize(200, 200)
    window3.title('Filters')
    window3.configure(bg='#141414')
    button1(0, 0, 'Contour', contour)
    button1(0, 40, 'Detail', detail)
    button1(0, 80, 'Edge_Enhance_More', edge_enhance_more)
    button1(0, 120, 'Emboss', emboss)
    button1(0, 160, 'Sharpen', sharpen)
    button1(0, 200, 'Find_Edges', find_edges)
# Home Function


def home():
    global counter
    while(counter > 0):
        counter -= 1
        os.remove('img'+str(counter)+'.png')
    window2.destroy()
    window_1()
# Undo Function


def undo():
    global counter
    if counter > 1:
        counter -= 1
        open_undo(counter)
        os.remove("img"+str(counter)+'.png')
# Cross Function


def cross():
    if counter > 0:
        open_undo(counter)
# Button function


def button1(x, y, name, cmd):
    button1 = Button(window3, width=17, text=name, bg='black', fg='white',
                     font='oxanium 15', activebackground='#25dae9', relief=GROOVE, command=cmd)
    button1.place(x=x, y=y, anchor=NW)


def start():
    window1.destroy()
    window_2()


def button(window, x, y, text, bcolor, fcolor, z, w, h, cmd):
    global window2

    def on_enter(e):
        mybutton['background'] = bcolor
        mybutton['foreground'] = fcolor

    def on_leave(e):
        mybutton['background'] = fcolor
        mybutton['foreground'] = bcolor
    mybutton = Button(window, width=w, height=h, text=text, font=z,
                      fg=bcolor,
                      bg=fcolor,
                      border=0,
                      activeforeground=fcolor,
                      activebackground=bcolor,
                      command=cmd)
    mybutton.bind("<Enter>", on_enter)
    mybutton.bind("<Leave>", on_leave)
    mybutton.place(x=x, y=y)


# Open Image Functions


def open_undo(counter):
    global canvas2
    image = Image.open("img"+str(counter-1)+'.png')
    image.thumbnail((650, 600))
    img1 = ImageTk.PhotoImage(image)
    canvas2.create_image(0, 0, anchor=NW, image=img1)
    canvas2.image = img1


def open_image_cam():
    global canvas1
    img = Image.open("img"+str(counter-1)+'.png')
    img.thumbnail((650, 600))
    img1 = ImageTk.PhotoImage(img)
    canvas1.create_image(0, 0, anchor=NW, image=img1)
    canvas1.image = img1


def open(counter):
    global canvas2
    canvas2.delete('all')
    image = Image.open("img"+str(counter)+'.png')
    image.thumbnail((650, 600))
    img1 = ImageTk.PhotoImage(image)
    canvas2.create_image(0, 0, anchor=NW, image=img1)
    canvas2.image = img1


def open_image():
    global img, counter, canvas1
    img_path = filedialog.askopenfilename(initialdir=os.getcwd())
    img = Image.open(img_path)
    img.save('img'+str(counter)+'.png')
    counter += 1
    window1.destroy()
    window_2()
    image = Image.open("img"+str(counter-1)+'.png')
    image.thumbnail((650, 600))
    img1 = ImageTk.PhotoImage(image)
    canvas1.create_image(0, 0, anchor=NW, image=img1)
    canvas1.image = img1

# Camera Function


def cam():
    global counter
    cam = cv2.VideoCapture(0)
    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("Camera (Press enter to capture image)", frame)
        k = cv2.waitKey(1)
        if k % 256 == 27:
            cam.release()
            cv2.destroyAllWindows()
            break
        elif k % 256 == 13:
            window1.destroy()
            window_2()
            img_name = 'img'+str(counter)+'.png'.format(img_counter)
            counter += 1
            cv2.imwrite(img_name, frame)
            img_counter += 1
            break
    open_image_cam()
    cam.release()
    cv2.destroyAllWindows()


# To save the applied feature on image
def temp_save():
    global img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11
    global img12, img13, img14, img15, img16, img17, counter
    if canvas2.image == img2:
        img1.save('img'+str(counter)+'.png')  # blur
        open(counter)
        counter += 1
    elif canvas2.image == img4:
        img3.save('img'+str(counter)+'.png')  # brightness
        open(counter)
        counter += 1
    elif canvas2.image == img7:
        img6.save('img'+str(counter)+'.png')  # contrast
        open(counter)
        counter += 1
    elif canvas2.image == img9:
        img8.save('img'+str(counter)+'.png')  # rotate 1
        open(counter)
        counter += 1
    elif canvas2.image == img11:
        img10.save('img'+str(counter)+'.png')  # rotate2
        open(counter)
        counter += 1
    elif canvas2.image == img13:
        img12.save('img'+str(counter)+'.png')  # flip 1
        open(counter)
        counter += 1
    elif canvas2.image == img15:
        img14.save('img'+str(counter)+'.png')  # flip2
        open(counter)
        counter += 1
    elif canvas2.image == img17:
        img16.save('img'+str(counter)+'.png')  # filter
        open(counter)
        counter += 1
# To save the final edited image


def save():
    global counter
    img_path = filedialog.asksaveasfilename(initialdir=os.getcwd(), filetypes=[(
        "PNG file", ".png"), ("JPG file", ".jpg")], defaultextension=".png")
    file = img_path
    image = Image.open("img"+str(counter-1)+'.png')
    image.save(file)
    while(counter > 0):
        counter -= 1
        os.remove('img'+str(counter)+'.png')
    window2.destroy()
    window_1()
# Scale functions


def scale1():
    global v1
    v1 = IntVar()
    scale1 = ttk.Scale(window2, from_=0, to=10, variable=v1,
                       orient=HORIZONTAL, command=blur)
    scale1.place(x=120, y=15)


def scale2():
    global v2
    v2 = IntVar()
    scale2 = ttk.Scale(window2, from_=0, to=10, variable=v2,
                       orient=HORIZONTAL, command=brightness)
    scale2.place(x=120, y=50)


def scale3():
    global v3
    v3 = IntVar()
    scale3 = ttk.Scale(window2, from_=0, to=10, variable=v3,
                       orient=HORIZONTAL, command=contrast)
    scale3.place(x=120, y=87)


# Start of main code
counter = 0
img2 = None
img4 = None
img7 = None
img9 = None
img11 = None
img13 = None
img15 = None
window_1()
