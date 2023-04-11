import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Two Screen App")
        self.geometry("400x300")

        # Create the first screen
        self.screen1 = tk.Frame(self)
        tk.Label(self.screen1, text="Welcome to Screen 1").pack()
        tk.Button(self.screen1, text="Go to Screen 2", command=self.show_screen2).pack()
        self.screen1.pack()

        # Create the second screen
        self.screen2 = tk.Frame(self)
        tk.Label(self.screen2, text="Welcome to Screen 2").pack()
        tk.Button(self.screen2, text="Go to Screen 1", command=self.show_screen1).pack()

    def show_screen1(self):
        self.screen2.pack_forget()
        self.screen1.pack()

    def show_screen2(self):
        self.screen1.pack_forget()
        self.screen2.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()
