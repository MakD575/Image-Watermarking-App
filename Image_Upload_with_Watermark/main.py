import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageDraw, ImageFont

file = file2 = None

def upload_image():
    global file
    file = filedialog.askopenfilename(initialdir='Users/picture', title="Select Your Image")
    upload_button.config(fg='green')
    f = file.split('/')[-1]
    uploaded_file_name.config(text=f"File Name: {f}")

def watermark():
    if file and file2:
        logo_image = Image.open(file2).convert("RGBA")
        background_image = Image.open(file).convert("RGBA")

        logo_width, logo_height = logo_image.size
        background_width, background_height = background_image.size

        if logo_width > background_width or logo_height > background_height:
            logo_image.thumbnail((background_width, background_height))

        logo_x = 0
        logo_y = 0

        background_image.paste(logo_image, (logo_x, logo_y), mask=logo_image)
        background_image.show()


def open_logo():
    global file2
    file2 = filedialog.askopenfilename(initialdir='Users/picture', title="Select Watermark")
    watermark_button.config(fg='green')
    f = file2.split('/')[-1]
    uploaded_logo_name.config(text=f"File Name: {f}")

window = tk.Tk()
window.title("Water Mark APP")
window.geometry('500x400')

label = tk.Label(window, text="Select Your Image", font=("Arial", 25))
label.pack()

upload_button = tk.Button(window, text="Select Image to Watermark", font=('Arial', 12, 'bold'),
                           command=upload_image)
upload_button.pack()
uploaded_file_name = tk.Label(text="File Name: ", fg='white', bg='black',
                              font=('Arial', 12, 'bold'), wraplength=500)
uploaded_file_name.pack()

watermark_button = tk.Button(window, text="Select Watermark Image", font=('Arial', 12, 'bold'),
                             command=open_logo)
watermark_button.pack()
uploaded_logo_name = tk.Label(text="File Name: ", fg='white', bg='black',
                              font=('Arial', 12, 'bold'), wraplength=500)
uploaded_logo_name.pack()

watermark_image = tk.Button(window, text="Show Watermarked Image", font=('Arial', 12, 'bold'),
                            command=watermark)
watermark_image.pack()


window.mainloop()



