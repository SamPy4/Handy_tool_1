from tkinter import *
import win32gui, thesaurus_translator
from pynput.keyboard import Key, Listener


class widget:
    def __init__(self):
        self.w = 300
        self.h = 75
        return

    def getWord(self, word):
        if word == "/exit" or word == "\exit":
            exit()
            
        return thesaurus_translator.fetch(word)


    def startWindow(self):
        self.root = Tk()
        self.descText = Label(self.root, text="")
        try:
            x,y = win32gui.GetCursorPos()
        except:
            x, y = self.root.winfo_screenwidth(), self.root.winfo_screenheight()

        self.root.geometry("{}x{}+{}+{}".format(self.w, self.h, int( (x) ), int( (y) ) ))
        def show(info):
            self.descText.destroy()
            if not info:
                self.h = 75
                self.root.geometry("{}x{}".format(self.w, self.h))
                self.descText = Label(self.root, text="Couldn't find anything about {}".format(wordToLook.get()))
                self.descText.pack()
                return self.descText
            text = "{};\n    {}.\n\nSome Synonyms for the word {}:\n\n".format(info[0], info[1], wordToLook.get())

            self.h = 75
            for w in info[2]:
                text += "{}\n".format(w)
                self.h += 18
            self.root.geometry("{}x{}".format(self.w, self.h))

            self.descText = Label(self.root, text=text)
            self.descText.pack()
            return self.descText

    # def poistu(self):
    #     self.root.destroy()
    #
    #     self.root.bind("<Escape>", self.poistu)

        wordToLook = StringVar(self.root)
        wordE = Entry(self.root, textvariable=wordToLook, takefocus=True)
        wordE.bind("<Enter>")
        wordE.pack()

        def painettu(event):
            """ Ottaa painetun napin ja tekee sillä jotain """
            nappi = event.keysym
            # print(nappi)
            if nappi == "Escape":
                self.root.destroy()
            if nappi == "Return":
                info = ["Word type","Word description","List of synonyms for that word"]
                if self.getWord(wordToLook.get()):
                    info[0], info[1], info[2] = self.getWord(wordToLook.get())
                    self.descText = show(info)
                else:
                    self.descText = show(False)

        self.root.bind("<Key>", painettu)

        mainloop()


if __name__ == "__main__":
    w = widget()
    def on_press(key):
        if key == Key.ctrl_r:
            w.startWindow()

    with Listener(on_press=on_press) as listener:
        listener.join()
