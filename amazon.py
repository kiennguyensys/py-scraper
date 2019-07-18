# -*- coding: utf-8 -*-
import amazonscraper
import tkinter as tk
from tkinter import ttk

def retrieveContent(keyword):

    results = amazonscraper.search(keyword)

    for result in results:
        print("{}".format(result.title))
        print("  - ASIN : {}".format(result.asin))
        print("  - {} out of 5 stars, {} customer reviews".format(result.rating, result.review_nb))
        print("  - {}".format(result.url))
        print("  - Image : {}".format(result.img))
        print()

    print("Number of results : %d" % (len(results)))

win = tk.Tk()
# Application Name
win.title("Amazon Crawler GUI")
# Label
lbl = ttk.Label(win, text = "Enter Search Link:").grid(column = 0, row = 0)
# Click event
def Submit():
    retrieveContent(key.get())
# Textbox widget
key = tk.StringVar()

keyEntered = ttk.Entry(win, width = 12, textvariable = key).grid(column = 0, row = 1)
# Button widget
button = ttk.Button(win, text = "submit", command = Submit).grid(column = 1, row = 1)
win.mainloop()