import tkinter as tk
import main

megamind = main.main


window = tk.Tk()
window.title("Hello World")

label = tk.Label(text="Game")
search = tk.Entry()

def enter_search(event):
    if str(search.get()).strip() != "":
        inquiry = str(search.get().strip())
        search.delete(0,tk.END)
        megamind.getdata(inquiry)
    else:
        search.delete(0,tk.END)
        print("Invalid entry!")

    

label.pack()
search.pack()
window.bind("<Return>", enter_search)
# Start the event loop.
window.mainloop()