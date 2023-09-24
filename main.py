from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image
import cryptocode

window = Tk()
window.title("Secret Note")
window.minsize(300, 600)
window.resizable(False, False)
window.config(padx=20, pady=20)

favicon = PhotoImage(file="document.png")
window.iconphoto(False, favicon)

FONT = ("Trebuchet MS", 12, "normal")


def mb_missing_value():
    pass


def write_to_file():
    pass


def encrypt_save():
    anahtar = entryMasterKey.get()
    metin = textNote.get("1.0", END)
    baslik = entryNote.get()

    if len(anahtar) == 0 and len(metin) == 0:
        messagebox.showwarning("Warning", "Fill in all text boxes")

    else:
        sifreli_metin = cryptocode.encrypt(metin, anahtar)

        baslikli_metin = baslik + ":" + "\n" + sifreli_metin + "\n"

        myFile = open("MySecretNotes.txt")
        with open("MySecretNotes.txt", mode="a") as myFile:
            myFile.write(baslikli_metin)


def decrypt():
    anahtar = entryMasterKey.get()
    metin = textNote.get("1.0", END)
    cozulecek_metin = cryptocode.decrypt(metin, anahtar)

    textNote.delete("1.0", END)
    textNote.insert(END, cozulecek_metin)


frame = Frame(window, width=200, height=200)
frame.grid(row=0, column=0)
img = ImageTk.PhotoImage(Image.open("document.png"))
label = Label(frame, image=img)
label.grid(row=1, column=0)

labelNoteTitle = Label(text="Your Secret Note Title", font=FONT, pady=10)
labelNoteTitle.grid(row=2, column=0)

entryNote = Entry(font=FONT)
entryNote.config(width=35)
entryNote.grid(row=3, column=0)

labelNoteText = Label(text="Your Secret Note", font=FONT, pady=10)
labelNoteText.grid(row=4, column=0)

textNote = Text(font=FONT, width=35, height=5)
textNote.grid(row=5, column=0)

labelMasterKey = Label(text="Master Key", font=FONT, pady=10)
labelMasterKey.grid(row=6, column=0)

entryMasterKey = Entry(font=FONT)
entryMasterKey.config(width=35)
entryMasterKey.grid(row=7, column=0)

labelSpace = Label(text="")
labelSpace.grid(row=8, column=0)

buttonSave = Button(text="Encrypt and Save", width=15, pady=5, command=encrypt_save)
buttonSave.grid(row=9, column=0)

labelSpace2 = Label(text="")
labelSpace2.grid(row=10, column=0)

buttonSave = Button(text="Decrypt", width=15, pady=5, command=decrypt)
buttonSave.grid(row=11, column=0)

window.mainloop()
