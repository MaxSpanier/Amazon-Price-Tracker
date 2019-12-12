from worker import start_routine, change_product, URL
from visualizer import visualize
import requests
from tkinter import font
import tkinter

top = tkinter.Tk()
top.geometry("600x400")
top.resizable(0, 0)
helv36 = font.Font(family='Helvetica', size=18, weight=font.BOLD)

def log():
    print("test")
def close_window():
    top.destroy()

scrapeBtn = tkinter.Button(top, text="Start scraping", command=log, font=helv36)
scrapeBtn.place(x = 214.5, y = 80)
scrapeBtn.update()
print("Scrape: ", scrapeBtn.winfo_height(), " - ", scrapeBtn.winfo_width())

visBtn = tkinter.Button(top, text="Visualize the Data", command=log, font=helv36)
visBtn.place(x = 192.5, y = 140)
visBtn.update()
print("Vis: ", visBtn.winfo_height(), " - ", visBtn.winfo_width())

changeBtn = tkinter.Button(top, text="Change the Product", command=log, font=helv36)
changeBtn.place(x = 180, y = 200)
changeBtn.update()
print("Change: ", changeBtn.winfo_height(), " - ", changeBtn.winfo_width())

exitBtn = tkinter.Button(top, text="Exit", command=close_window, font=helv36)
exitBtn.place(x = 267.5, y = 260)
exitBtn.update()
print("Exit: ", exitBtn.winfo_height(), " - ", exitBtn.winfo_width())



top.mainloop()
