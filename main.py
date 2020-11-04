from tkinter import *
import Game

def createGame():
    root.destroy()
    game = Game.Game(6, diff=6 + vardiff.get(), coef=40)
    game.root.mainloop()


root = Tk()

vardiff = IntVar()
vardiff.set(4)

easy = Radiobutton(root, text="Easy", variable=vardiff, value=4)
medium = Radiobutton(root, text="Medium", variable=vardiff, value=6)
hard = Radiobutton(root, text="Hard", variable=vardiff, value=8)

button = Button(text="Set", command=createGame)

easy.pack(side=TOP)
medium.pack(side=TOP)
hard.pack(side=TOP)

button.pack(side=TOP)

root.mainloop()


