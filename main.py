import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageFont, ImageDraw


def add_watermark():
    picture_location = picture_location_entry.get()
    watermark = text_entry.get()

    if picture_location == "":
        messagebox.showinfo(title="Error", message="Insert file location")
    if watermark == "":
        messagebox.showinfo(title="Error", message="Pls insert ur watermark text")
    else:
        try:
            with Image.open(picture_location) as im:
                width, height = im.size
                draw = ImageDraw.Draw(im)
                font = ImageFont.truetype('arial.ttf', 40)
                text_width, text_height = draw.textsize(watermark, font)
                margin = 20
                x = width - text_width - margin
                y = height - text_height - margin
                color = kolor()
                draw.text((x, y), watermark, color, font=font)
                im.show()
                place = f"{picture_location[:-4]}-WATERMARK{picture_location[-4:]}"
                im.save(place)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No File Found!")
        else:
            pass


def kolor():
    if kol.get() == 1:
        return (0, 0, 0)
    else:
        return (255, 255, 255)

window = Tk()
window.title("Watermarker")
window.config(padx=50, pady=50)
window.geometry("600x550")

canvas = Canvas(height=240, width=280)
logo_img = PhotoImage(file="1212.png")
canvas.create_image(120, 150, image=logo_img)
canvas.grid(row=0, column=1)

picture_location_label = Label(text="Picture location:").grid(row=1, column=0)
what_text_label = Label(text="Text of ur watermark:").grid(row=2, column=0)

picture_location_entry = Entry(width=54)
picture_location_entry.grid(row=1, column=1)
picture_location_entry.focus()

text_entry = Entry(width=54)
text_entry.grid(row=2, column=1)
text_entry.focus()

kol = tkinter.IntVar()
c = tkinter.Checkbutton(window, text="Black watermark", variable = kol, onvalue=1, offvalue=0)
c.grid(row=3, column=0)

add_button = Button(text="Add watermark to picture", width=46, command=add_watermark).grid(row=3, column=1, columnspan=2)
quit_button = Button(text="Quit", command=window.destroy).grid(column=1, row=5)

window.mainloop()
