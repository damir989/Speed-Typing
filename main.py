import tkinter as tk
import time
import threading
import random


class Application:

    def __init__(self):
        self.root = tk.Tk()
        self.frame = tk.Frame(self.root)
        self.root.title("typing speed application")
        self.geometry = self.root.geometry("800x650")
        self.texts = open("text.txt").read().split("\n")
        self.label = tk.Label(self.frame, text=random.choice(self.texts),font=("Sans-serif", 15))
        self.label.grid(row=0, column=0, columnspan=2, padx=5, pady=10)

        self.entry = tk.Entry(self.frame, width=40, font=("Sans-serif", 20))
        self.entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
        self.entry.bind("<KeyPress>",self.start)

        self.speedLabel = tk.Label(self.frame, text="Speed: \n 0.00 CPM", font=("Sans", 24))
        self.speedLabel.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

        self.resetButton = tk.Button(self.frame, text="Reset", command=self.resetButton)
        self.resetButton.grid(row=3, column=0, columnspan=2, padx=5, pady=10)
        self.frame.pack(expand=True)
        self.counter = 0
        self.isRunning = False
        self.root.mainloop()

    def start(self, event):
        if not self.isRunning:
            if not event.keycode in [16, 17, 18]:
                self.isRunning = True
                threading.Thread(target=self.timer).start()
        if not self.label.cget('text').startswith( self.entry.get()):
            self.entry.config(fg="red")
        else:
            self.entry.config(fg="black")
        if self.entry.get() == self.label.cget("text")[:-1]:
            self.isRunning = False
            self.entry.config(fg="green")

    def timer(self):
        while self.isRunning:
            time.sleep(0.1)
            self.counter += 0.1
            cps = len(self.entry.get()) / self.counter
            cpm = cps * 60
            self.speedLabel.config(text=f"Speed: \n {cpm:.2f} CPM")

    def resetButton(self):
        self.isRunning=False
        self.counter=0
        self.speedLabel.config(text="Speed: \n 0.00 CPM")
        self.label.config(text=random.choice(self.texts))
        self.entry.delete(0,tk.END)
Application()
