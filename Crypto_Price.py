import json  
import tkinter as tk
import requests
from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime

from requests.api import request

# font

f1 = ("Source Code Pro", 24, "bold")
f2 = ("Source Code Pro", 22, "bold")
f3 = ("Source Code Pro", 18, "normal")

# setting the parameters for the window

root = tk.Tk()
root.geometry("500x300")
root.title("Crypto Price Tracker")
root.configure(background='White')

# creating the label for the bitcoin logo

img = Image.open("/Users/jerielmartinez/Desktop/istockphoto-1139020309-612x612.jpeg")
resized = img.resize((75, 75), Image.ANTIALIAS)
new_img = ImageTk.PhotoImage(resized)
title_label = Label(root, image=new_img)
title_label.pack(pady=20)

# data for GUI

def trackBitcoin():
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
    response = requests.get(url).json()
    price = response["USD"]
    time = datetime.now().strftime("%H:%M:%S")

    labelPrice.config(text=str(price) + " $")
    labelTime.config(text= "Updated at: " + time)

    root.after(1000, trackBitcoin)

# Price of Bitcoin label

labelPrice = tk.Label(root, font = f2 )
labelPrice.pack(pady = 20)

labelTime = tk.Label(root, font = f3 )
labelTime.pack(pady=20)

trackBitcoin()
root.mainloop()