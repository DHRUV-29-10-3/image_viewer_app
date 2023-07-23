from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Image Viewer App")

image1 = Image.open("images_folder/birthday_photo_1.png")
image_1 = ImageTk.PhotoImage(image1.resize((500, 450)))

image2 = Image.open("images_folder/photo_2.png")
image_2 = ImageTk.PhotoImage(image2.resize((500, 450)))

image3 = Image.open("images_folder/photo_3.png")
image_3 = ImageTk.PhotoImage(image3.resize((500, 450)))

image4 = Image.open("images_folder/photo_4.png")
image_4 = ImageTk.PhotoImage(image4.resize((500, 450)))

image5 = Image.open("images_folder/photo_5.png")
image_5 = ImageTk.PhotoImage(image5.resize((500, 450)))


img_list = [image_1,image_2,image_3,image_4,image_5]

img_label = Label(root,image=image_1)
img_label.grid(row = 0, column = 0, columnspan = 3)

def button_forward(image_number):
    global button_forward
    global img_label
    global button_back

    img_label.grid_forget()

    img_label = Label(root, image=img_list[image_number-1])
    buttonforward = Button(root, text=">>", font="15", command=lambda: button_forward(image_number + 1))
    buttonback = Button(root, text="<<", font="15", command=lambda: button_back(image_number - 1))

    if image_number == 5:
        buttonforward = Button(root, text=">>", font="15", state=DISABLED)
        buttonforward.grid(row=1, column=2)

    img_label.grid(row=0, column=0, columnspan=3)
    buttonforward.grid(row=1, column=2)
    buttonback.grid(row=1, column=0, pady=10)


def button_back(image_number):
    global button_forward
    global img_label
    global button_back

    img_label.grid_forget()

    img_label = Label(root, image=img_list[image_number - 1])
    buttonforward = Button(root, text=">>", font="15", command=lambda: button_forward(image_number + 1))
    buttonback = Button(root, text="<<", font="15", command=lambda: button_back(image_number - 1))

    if image_number == 1:
        buttonback = Button(root, text="<<", font="15", state=DISABLED)
        buttonback.grid(row=1, column=2)

    img_label.grid(row=0, column=0, columnspan=3)
    buttonforward.grid(row=1, column=2)
    buttonback.grid(row=1, column=0, pady=10)

buttonback = Button(root, text="<<", font="15",command=button_back, state=DISABLED)
buttonexit = Button(root, text="EXIT", command=root.quit, font="15")
buttonforward = Button(root, text=">>", font="15", command = lambda: button_forward(2))

buttonback.grid(row=1, column=0,pady=10)
buttonexit.grid(row=1, column=1)
buttonforward.grid(row=1, column=2)

root.mainloop()


