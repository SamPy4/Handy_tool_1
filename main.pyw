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

        return thesaurus_translator.fetch(word) # to be replaced with .getData()

    def show(self, info):
        self.w = 300
        self.h = 75

        self.descText.destroy()
        if info == False:
            self.h = 75
            self.root.geometry("{}x{}".format(self.w, self.h))
            self.descText = Label(self.root, text="Couldn't find anything about {}".format(self.wordToLook.get()))
            self.descText.pack()
            return self.descText
        if info == None:
            self.h = 75
            self.root.geometry("{}x{}".format(self.w, self.h))
            self.descText = Label(self.root, text="No internet connection...")
            self.descText.pack()
            return self.descText

        if info:
            text = "{};\n    {}.\n\nSome synonyms for the word {}:\n\n".format(info[0], info[1], self.wordToLook.get().title())

            for w in info[2]:
                text += "{}\n".format(w)
                self.h += 18

            self.descText = Label(self.root, text=text)
            self.descText.pack()

            self.root.geometry("{}x{}".format(self.w, self.h))

            return self.descText

    def painettu(self, event):
        """ Ottaa painetun napin ja tekee sillä jotain """
        nappi = event.keysym
        # print(nappi)
        if nappi == "Escape":
            self.root.destroy()
        if nappi == "Return":
            info = ["Word type","Word description","List of synonyms for that word"]



            wordInfo = self.getWord(self.wordToLook.get())
            if wordInfo:
                info[0], info[1], info[2] = wordInfo
                self.descText = self.show(info)
            if wordInfo == None:
                self.descText = self.show(None)
            if wordInfo == False:
                self.descText = self.show(False)

    def startWindow(self):
        self.w = 300
        self.h = 75

        self.root = Tk()
        self.descText = Label(self.root, text="")
        self.root.lift()
        self.root.attributes("-topmost", True)
        self.root.wm_attributes('-toolwindow', False)
        self.root.overrideredirect(True)

        emptyMenu = Menu(self.root)
        self.root.config(menu=emptyMenu)

        self.root.lift()
        self.root.focus_force()
        self.root.grab_set()
        self.root.grab_release()

        try:
            self.x, self.y = win32gui.GetCursorPos()
        except:
            self.x, self.y = self.root.winfo_screenwidth(), self.root.winfo_screenheight()

        self.root.geometry("{}x{}+{}+{}".format(self.w, self.h, int( int(self.x) - self.w/2 ), int( int(self.y) - self.h/8 )))

    # def poistu(self):
    #     self.root.destroy()
    #
    #     self.root.bind("<Escape>", self.poistu)

        self.wordToLook = StringVar(self.root)
        wordE = Entry(self.root, textvariable=self.wordToLook, takefocus=True)
        wordE.bind("<Enter>")
        wordE.pack()
        wordE.lift()
        wordE.focus_force()
        wordE.grab_set()
        wordE.grab_release()

        self.root.bind("<Key>", self.painettu)

        mainloop()


if __name__ == "__main__":
    w = widget()
    def on_press(key):
        if key == Key.ctrl_r:
            w.startWindow()

    with Listener(on_press=on_press) as listener:
        listener.join()
