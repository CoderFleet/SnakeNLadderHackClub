import tkinter as tk
from menu import PlayerMenu

def main():
    root = tk.Tk()
    root.title("Snakes and Ladders")

    menu = PlayerMenu(root)
    menu.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
