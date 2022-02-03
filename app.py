import tkinter as tk
from tkinter import *
from tkinter import ttk
# Import Function
from cypher_model import *
from enigma import *
from playfair import *

root = tk.Tk()

#Define Fungsi Untuk Open New Window
def openNewWindowVigChip():
    newWindow = Toplevel(root)
    newWindow.title("Vigenere Chiper")
    newWindow.geometry("720x360")
    newWindow.configure(bg="#E1EAF7")

    def ShowVigChip():
        INPUT = inputtxt.get("1.0", "end-1c")
        print(INPUT)
        KUNCI = inputkunci.get("1.0", "end-1c")
        print(KUNCI)
        Output.insert(END, str(vigEncode(INPUT, KUNCI)))
        
    def ShowPlainteks():
        INPUT = inputtxt.get("1.0", "end-1c")
        print(INPUT)
        KUNCI = inputkunci.get("1.0", "end-1c")
        print(KUNCI)
        Output.insert(END, str(vigDecode(INPUT, KUNCI)))

    #Close Button
    def Close():
        newWindow.destroy()

    l = Label(newWindow, text = "Masukkan 26 Huruf")
    inputtxt = Text(newWindow, height = 5, width = 25, bg = "light yellow")
    inputtxt.insert(END, "Ketik di sini")
    inputkunci = Text(newWindow, height = 5, width = 25, bg = "light yellow")
    inputkunci.insert(END, "Ketikkan kunci di sini")
    Output = Text(newWindow, height = 5, width = 25, bg = "light cyan")
    
    l.pack()
    inputtxt.pack()
    inputkunci.pack()
    Output.pack()

    ttk.Button(newWindow,text='Tampilkan Hasil Enkripsi', command=ShowVigChip).pack(expand=True)
    ttk.Button(newWindow,text='Tampilkan Hasil Dekripsi', command=ShowPlainteks).pack(expand=True)
    ttk.Button(newWindow, text="Exit", command=Close).pack(expand=True)

def openNewWindowExt():
    newWindow3 = Toplevel(root)
    newWindow3.title("Extended Vigenere Chiper")
    newWindow3.geometry("720x360")
    newWindow3.configure(bg="#E1EAF7")

    def ShowExtVigChip():
            INPUT = inputtxt.get("1.0", "end-1c")
            print(INPUT)
            KUNCI = inputkunci.get("1.0", "end-1c")
            print(KUNCI)
            Output.insert(END, str(vigASCIIEncode(INPUT, KUNCI)))

    def ShowPlainteks():
        INPUT = inputtxt.get("1.0", "end-1c")
        print(INPUT)
        KUNCI = inputkunci.get("1.0", "end-1c")
        print(KUNCI)
        Output.insert(END, str(vigASCIIDecode(INPUT, KUNCI)))        
    
    #Close Button
    def Close():
        newWindow3.destroy()
    
    l = Label(newWindow3, text = "Masukkan karakter yang ingin dienkripsi/dekripsi")
    inputtxt = Text(newWindow3, height = 5, width = 25, bg = "light yellow")
    inputtxt.insert(END, "Ketik di sini")
    inputkunci = Text(newWindow3, height = 5, width = 25, bg = "light yellow")
    inputkunci.insert(END, "Ketikkan kunci di sini")
    Output = Text(newWindow3, height = 5, width = 25, bg = "light cyan")
        
    l.pack()
    inputtxt.pack()
    inputkunci.pack()
    Output.pack()

    ttk.Button(newWindow3,text='Tampilkan Hasil Enkripsi', command=ShowExtVigChip).pack(expand=True)
    ttk.Button(newWindow3,text='Tampilkan Hasil Dekripsi', command=ShowPlainteks).pack(expand=True)
    ttk.Button(newWindow3, text="Exit", command=Close).pack(expand=True)

def openNewWindowPlayfair():
    newWindow2 = Toplevel(root)
    newWindow2.title("Playfair Chiper")
    newWindow2.geometry("720x360")
    newWindow2.configure(bg="#E1EAF7")

    def ShowPlayfairChip():
            INPUT = inputtxt.get("1.0", "end-1c")
            print(INPUT)
            KUNCI = inputkunci.get("1.0", "end-1c")
            print(KUNCI)
            Output.insert(END, str(encrypt(INPUT, generateKeyMatrix(KUNCI))))

    def ShowPlainteks():
        INPUT = inputtxt.get("1.0", "end-1c")
        print(INPUT)
        KUNCI = inputkunci.get("1.0", "end-1c")
        print(KUNCI)
        Output.insert(END, str(decrypt(INPUT, generateKeyMatrix(KUNCI))))

    #Close Button
    def Close():
        newWindow2.destroy()

    l = Label(newWindow2, text = "Masukkan karakter yang ingin dienkripsi/dekripsi")
    inputtxt = Text(newWindow2, height = 5, width = 25, bg = "light yellow")
    inputtxt.insert(END, "Ketik di sini")
    inputkunci = Text(newWindow2, height = 5, width = 25, bg = "light yellow")
    inputkunci.insert(END, "Ketikkan kunci di sini")
    Output = Text(newWindow2, height = 5, width = 25, bg = "light cyan")
        
    l.pack()
    inputtxt.pack()
    inputkunci.pack()
    Output.pack()

    ttk.Button(newWindow2,text='Tampilkan Hasil Enkripsi', command=ShowPlayfairChip).pack(expand=True)
    ttk.Button(newWindow2,text='Tampilkan Hasil Dekripsi', command=ShowPlainteks).pack(expand=True)
    ttk.Button(newWindow2, text="Exit", command=Close).pack(expand=True)

def openNewWindowEnigma():
    newWindow = Toplevel(root)
    newWindow.title("Enigma Chiper")
    newWindow.geometry("720x360")
    newWindow.configure(bg="#E1EAF7")

canvas = tk.Canvas(root, height=360, width=720, bg="#C0D1EB")
canvas.pack()

titleText = Text(root, height=10, width=52)
labelTitle = Label(root, text="Tugas 1 II4031 Kriptografi dan Koding")
labelTitle.config(font = ("Arial", 24))
labelTitle.pack()

frame = tk.Frame(root, bg="#E1EAF7")
frame.place(relwidth=0.9, relheight=0.8, relx=0.05, rely=0.05)

#Add Button
vigChip = tk.Button(frame, text = "Vigenere Chiper", padx=10, pady=5, fg="black", bg="white", command=openNewWindowVigChip)
vigChip.pack(pady=10)
extVigChip = tk.Button(frame, text = "Extended Vigenere Chiper", padx=10, pady=5, fg="black", bg="white", command=openNewWindowExt)
extVigChip.pack(pady=10)
playfairChip = tk.Button(frame, text = "Playfair Chiper", padx=10, pady=5, fg="black", bg="white", command=openNewWindowPlayfair)
playfairChip.pack(pady=10)
enigmaChip = tk.Button(frame, text = "Enigma Chiper", padx=10, pady=5, fg="black", bg="white", command=openNewWindowEnigma)
enigmaChip.pack(pady=10)

root.mainloop()