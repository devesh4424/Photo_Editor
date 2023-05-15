from PIL import Image, ImageFilter
from PIL.ImageFilter import (
    BLUR, CONTOUR, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
    EMBOSS, FIND_EDGES, SHARPEN
)
from tkinter import *
from PIL import ImageTk, Image


def sharpenPic(curImg, counter):
    current = Image.open(curImg)
    newImg = current.filter(SHARPEN)
    newImg.save('image' + str(counter) + '.png')


def blurPic(curImg, counter):
    current = Image.open(curImg)
    newImg = current.filter(BLUR)
    newImg.save('image' + str(counter) + '.png')


def rotateCounter(curImg, counter):
    newImg = Image.open(curImg)
    newImg.rotate(90).save('image' + str(counter) + '.png')


def rotateClock(curImg, counter):
    newImg = Image.open(curImg)
    newImg.rotate(270).save('image' + str(counter) + '.png')


def cropPic(curImg, counter):
    current = Image.open(curImg)
    width, height = current.size
    left = width / 4
    top = height / 4
    right = 3 * width / 4
    bottom = 3 * height / 4
    newImg = current.crop((left, top, right, bottom))
    newImg.save('image' + str(counter) + '.png')


def sketchPic(curImg, counter):
    current = Image.open(curImg)
    newImg = current.filter(CONTOUR)
    newImg.save('image' + str(counter) + '.png')


def oilPic(curImg, counter):
    current = Image.open(curImg)
    newImg = current.filter(EDGE_ENHANCE)
    newImg.save('image' + str(counter) + '.png')


def pencilPic(curImg, counter):
    current = Image.open(curImg)
    newImg = current.filter(EDGE_ENHANCE_MORE)
    newImg.save('image' + str(counter) + '.png')


def foilPic(curImg, counter):
    current = Image.open(curImg)
    newImg = current.filter(EMBOSS)
    newImg.save('image' + str(counter) + '.png')


def negativePic(curImg, counter):
    current = Image.open(curImg)
    newImg = current.filter(FIND_EDGES)
    newImg.save('image' + str(counter) + '.png')


def changeImage(counter):
    img = ImageTk.PhotoImage(Image.open('image' + str(counter) + '.png'))
    panel.configure(image=img)
    panel.image = img


def sharpenImgFunc():
    global counter
    curImg = 'image' + str(counter) + '.png'
    counter = counter + 1
    sharpenPic(curImg, counter)
    changeImage(counter)


def blurImgFunc():
    global counter
    curImg = 'image' + str(counter) + '.png'
    counter = counter + 1
    blurPic(curImg, counter)
    changeImage(counter)


def rotateCounterFunc():
    global counter
    curImg = 'image' + str(counter) + '.png'
    counter = counter + 1
    rotateCounter(curImg, counter)
    changeImage(counter)


def rotateClockFunc():
    global counter
    curImg = 'image' + str(counter) + '.png'
    counter = counter + 1
    rotateClock(curImg, counter)
    changeImage(counter)


def cropImgFunc():
    global counter
    curImg = 'image' + str(counter) + '.png'
    counter = counter + 1
    cropPic(curImg, counter)
    changeImage(counter)


def undoFunc():
    global counter
    if counter > 0:
        counter = counter - 1
    changeImage(counter)


def sketchImgFunc():
    global counter
    curImg = 'image' + str(counter) + '.png'
    counter = counter + 1
    sketchPic(curImg, counter)
    changeImage(counter)


def oilImgFunc():
    global counter
    curImg = 'image' + str(counter) + '.png'
    counter = counter + 1
    oilPic(curImg, counter)
    changeImage(counter)


def paintImgFunc():
    global counter
    curImg = 'image' + str(counter) + '.png'
    counter = counter + 1
    pencilPic(curImg, counter)
    changeImage(counter)


def foilImgFunc():
    global counter
    curImg = 'image' + str(counter) + '.png'
    counter = counter + 1
    foilPic(curImg, counter)
    changeImage(counter)


def negativeImgFunc():
    global counter
    curImg = 'image' + str(counter) + '.png'
    counter = counter + 1
    negativePic(curImg, counter)
    changeImage(counter)


main = Tk()
counter = 0
main.title("Photo Editor")
main.geometry("1000x505")
var = IntVar()
editingBox = Frame(main)

undoButton = Button(main, text="Undo", command=undoFunc, font=20)
undoButton.pack(side=BOTTOM, pady=10)
formatLabel = Label(editingBox, text="Format", font=16)
formatLabel.pack(side=TOP, pady=10)
SharpenButton = Button(editingBox, text="Sharpen Image",
                       command=sharpenImgFunc, width=20)
SharpenButton.pack(side=TOP)
BlurButton = Button(editingBox, text="Blur Image",
                    command=blurImgFunc, width=20)
BlurButton.pack(side=TOP)
CropButton = Button(editingBox, text="Crop", command=cropImgFunc, width=20)
CropButton.pack(side=TOP)
rotateCounterButton = Button(
    editingBox, text="Rotate Counter Clockwise", command=rotateCounterFunc, width=20)
rotateCounterButton.pack(side=TOP)
rotateClockButton = Button(
    editingBox, text="Rotate Clockwise", command=rotateClockFunc, width=20)
rotateClockButton.pack(side=TOP)
img = ImageTk.PhotoImage(Image.open('image' + str(counter) + '.png'))
panel = Label(main, image=img)
panel.pack(side=LEFT, padx=20)

negativeButton = Button(editingBox, text="Photo negative",
                        command=negativeImgFunc, width=20)
negativeButton.pack(side=BOTTOM)
foilButton = Button(editingBox, text="Foil art", command=foilImgFunc, width=20)
foilButton.pack(side=BOTTOM)
pencilButton = Button(editingBox, text="Sharp paint",
                      command=paintImgFunc, width=20)
pencilButton.pack(side=BOTTOM)
oilButton = Button(editingBox, text="Oil paint", command=oilImgFunc, width=20)
oilButton.pack(side=BOTTOM)
sketchButton = Button(editingBox, text="Sketch light",
                      command=sketchImgFunc, width=20)
sketchButton.pack(side=BOTTOM)
filterLabel = Label(editingBox, text="Filters", font=16)
filterLabel.pack(side=BOTTOM, pady=10)

editingBox.pack()
main.mainloop()
