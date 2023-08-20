import tkinter as tk 
import qrcode
import random as ran 
import string 
import os 

#get working path
path = os.getcwd()

# set the windo
windo = tk.Tk()
windo.geometry("800x650")
windo.title("QRcode genrater")

#set the  first func
def QRG(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black",back_color="white")
    img.save(filename)
    enter.delete(0,tk.END)
    libel1.config(text=f"The qrcode has genrated succsfully as {filename} in  path {path}")

#the func who make the QRG func works
def realQRG():
    data = enter.get()
    filename = words() 
    QRG(data,filename)

#------ function make a random word -------
def words():
    lett = string.ascii_letters
    words1 = ''.join(ran.choice(lett)for i in range(5))
    words = words1 + ".png"
    return words

#set the libels and bttons
libel = tk.Label(windo , text="WELCOM to QR genrater",font=('Arial Bold', 20))
libel.pack()
libel = tk.Label(windo , text="write any thing and I will convert it to qrcode",font=('Arial Bold', 15))
libel.pack()
enter = tk.Entry(windo, width=40)
enter.pack()
btton = tk.Button(windo, text="Genrate",command=realQRG)
btton.pack()
libel1 = tk.Label(windo, text="",font=('Arial Bold', 15))
libel1.pack()
libel2 = tk.Label(windo, text="This tool made by some-man1",font=('Arial Bold', 15))
libel2.pack()
libel3 = tk.Label(windo, text="Github: https://github.com/some-man1", font=('Arial Bold', 10), fg="red")
libel3.pack(side=tk.BOTTOM, anchor=tk.SW) 
libel4 = tk.Label(windo, text="Telegram: @RD515Y", font=('Arial Bold', 10), fg="blue")
libel4.pack(side=tk.BOTTOM, anchor=tk.SW) 

#set the args
data = enter.get()
filename = words() 

tk.mainloop()
