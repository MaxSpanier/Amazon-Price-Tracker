import requests
from tkinter import font
import tkinter

top = tkinter.Tk()
top.geometry("600x400")
top.resizable(0, 0)
top.configure(background = "white")

helv18 = font.Font(family='Helvetica', size=18, weight=font.BOLD)
helv36 = font.Font(family='Helvetica', size=36, weight=font.BOLD)

def clear_console():
    from main import clear
    clear()

def start_scraping():
    clear_console()
    from worker import start_routine
    start_routine()
    print("scrape")

def close_window():
    top.destroy()

def log_vis():
    print("vis")

def log_change():
    print("change")


canvas = tkinter.Canvas(top, width = 600, height = 100, bd = 0, highlightthickness = 0,  background = "white")
canvas.create_text(300, 50, text = "Amazon price tracker", font = helv36)
canvas.pack()
top.update()

scrapeBtn = tkinter.Button(top, text="Start scraping", command=start_scraping, font=helv18)
scrapeBtn.place(x = 208, y = 120)
scrapeBtn.update()
#print("Scrape: ", scrapeBtn.winfo_height(), " - ", scrapeBtn.winfo_width())

visBtn = tkinter.Button(top, text="Visualize the Data", command=log_vis, font=helv18)
visBtn.place(x = 186.5, y = 180)
visBtn.update()
#print("Vis: ", visBtn.winfo_height(), " - ", visBtn.winfo_width())

changeBtn = tkinter.Button(top, text="Change the Product", command=log_change, font=helv18)
changeBtn.place(x = 174, y = 240)
changeBtn.update()
#print("Change: ", changeBtn.winfo_height(), " - ", changeBtn.winfo_width())

exitBtn = tkinter.Button(top, text="Exit", command=close_window, font=helv18)
exitBtn.place(x = 266.5, y = 300)
exitBtn.update()
#print("Exit: ", exitBtn.winfo_height(), " - ", exitBtn.winfo_width())



top.mainloop()
