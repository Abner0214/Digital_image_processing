import tkinter as tk
import PIL
from PIL import Image,ImageTk
from tkinter import filedialog


# open image
def open_img():
    
    # Dynamic_Island.config(text = "Processing ...", bg = "green3", font = ("Arial", 14), width = 30, height = 1)
    # window.update_idletasks()
    print("open an image")
    # global fileName
    # global NOW_img
    # global ORIGNAL_open_img
    # global ORIGNAL_img
    # global lbl_PRESENT_img  # current image in the window
    fileName = filedialog.askopenfilename()
    ORIGNAL_open_img = Image.open(fileName)
    NOW_img = ORIGNAL_open_img
    ORIGNAL_img = ImageTk.PhotoImage(ORIGNAL_open_img)
    image = PIL.Image.open(fileName)
    wid, hei = image.size
    lbl_PRESENT_img = tk.Label(window, image = ORIGNAL_img, width = wid, height = hei)
    lbl_PRESENT_img.image = ORIGNAL_img
    lbl_PRESENT_img.grid(row = 2, column = 0)
    
    nameStr = fileName.split("/")

    Dynamic_Island.config(text = "You open this image: " + nameStr[-1] , bg = "AntiqueWhite1", font = ("Arial", 16), width = 80, height = 2)
    window.update_idletasks()

    return image

# open .raw file
def open_raw():

    # Dynamic_Island.config(text = "Processing ...", bg = "green3", font = ("Arial", 14), width = 30, height = 1)
    # window.update_idletasks()
    print("open a .raw file")
    global fileName
    global NOW_img
    global ORIGNAL_open_img
    global ORIGNAL_img
    global lbl_PRESENT_img  # current image in the window
    fileName = filedialog.askopenfilename(initialdir = "/", title = "Select a .raw file",)
    x = open(fileName,'rb')
    ORIGNAL_open_img = Image.frombytes("L", (512, 512), x.read(), 'raw')
    NOW_img = ORIGNAL_open_img
    ORIGNAL_img = ImageTk.PhotoImage(ORIGNAL_open_img)
    #image = PIL.Image.open(fileName)
    #wid, hei = image.size
    lbl_PRESENT_img = tk.Label(window, image = ORIGNAL_img, width = 512, height = 512)
    lbl_PRESENT_img.image = ORIGNAL_img
    lbl_PRESENT_img.grid(row = 2, column = 0)

    nameStr = fileName.split("/")
    
    Dynamic_Island.config(text = "You open this .raw file: " + nameStr[-1] , bg = "AntiqueWhite1", font = ("Arial", 16), width = 80, height = 2)
    window.update_idletasks()
    if not fileName:
        Dynamic_Island.config(text = "Fail to open this .raw file" , bg = "AntiqueWhite1", font = ("Arial", 16), width = 80, height = 2)
        window.update_idletasks()
        return

# save image 
def save_img(imgName = "imgName"):

    # Dynamic_Island.config(text = "Processing ...", bg = "green3", font = ("Arial", 14), width = 30, height = 1)
    # window.update_idletasks()
    newName = imgName
    if newName[-3:] == ".tif":
        NOW_img.save(newName, "tiff")
        Dynamic_Island.config(text = "The image has been saved in the TIF format! Please check your folder!", bg = "aquamarine", font = ("Arial", 16), width = 80, height = 2)
    else:
        NOW_img.save(newName, "JPEG")
        Dynamic_Island.config(text = "The image has been saved in the JPG format! Please check your folder!", bg = "aquamarine", font = ("Arial", 16), width = 80, height = 2)

    window.update_idletasks()


                    ######  Define  ######
                          
        ### open / save / dispaly
# Label
lbl_open = tk.Label(window, text = "First step  ========  OPEN   ====   ==   = > ",font = ("Arial", 12))
lbl_save_dispaly = tk.Label(window, text = "Please enter a file name to Save / Display the image (contain filename extenstion)",font = ("Arial", 10))
# Entry
entry_fileName = tk.Entry(window, width = 25)
# Button
btn_open = tk.Button(window, text = "Open a image", command = open_img)
btn_save = tk.Button(window, text = "Save image", command = save_img)
btn_display = tk.Button(window, text = "Display image", command = display_img)
        ### open .raw file
btn_raw = tk.Button(window, text = "Open .raw file", command = open_raw)
        ### Haruki reset!
btn_reset = tk.Button(window, text = "Reset current image", command = reset_img)
        ### Display the histogram of images
lbl_eql = tk.Label(window, text = "Histogram Equlization")
btn_htg = tk.Button(window, text = "Histogram of current images", command = display_htg)
btn_htg_eql = tk.Button(window, text = "Equlization", command = auto_level)


##################################  window  ##################################

window = tk.Tk()
window.title("Image File Operations")
Dynamic_Island = tk.Label(window, text = "Simple graphic user interface of PIL.", bg = "yellow", font = ("Arial", 16), width = 70, height = 2)


                    ######  composition  ######

# Heading
Dynamic_Island.grid(row = 0, column = 0, columnspan = 15, rowspan = 1)
# Open / Save / Dispaly
lbl_open.grid(row = 1, column = 0)
btn_open.grid(row = 1, column = 1)
lbl_save_dispaly.grid(row = 3, column = 0)
entry_fileName.grid(row = 4, column = 0)
btn_save.grid(row = 4, column = 1)
btn_display.grid(row = 4, column = 2)
# open .raw file
btn_raw.grid(row = 1, column = 2)
# Haruki reset!
btn_reset.grid(row = 2, column = 1)