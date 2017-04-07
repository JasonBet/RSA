from Tkinter import *
import tkMessageBox



master = Tk()


#n = 20497
#e = 19
#d = 1063



LUT_encryption=dict()

LUT_decryption=dict()    

def clear():
    t1.delete(1.0, END)
    t2.delete(1.0, END)
 
    
#to write stuff on t1   
def openfileQ():
    tj=open("decrypted.txt", 'r')
    t1.insert(END,tj.read())
    tj.close()

    
#to save stuff    
def openfileR():
    f = open("decrypted.txt", 'w')
    inputs = t1.get(1.0, END)
    f.write(inputs)
    f.close()

    
def encrypt_message():
    e= 5
    n= 11911
    msg= t1.get(1.0, END)
    encrypted_msg=""
    for i in msg:
        if i in LUT_encryption:
            encrypted_msg+=LUT_encryption[i]
        else:
            numerize=ord(i)
            encrypt=pow(numerize,e,n)
            LUT_encryption[i] = unichr(encrypt)
            encrypted_msg += unichr(encrypt)
    clear()
    t1.insert(END, encrypted_msg)
    tkMessageBox.showinfo("Encrypt", "OHHH you just got encrypted boi")

    
    
def decrypt_message():
    d= 1063
    n= 20497
    decrypted_msg=""
    msg= t2.get(1.0, END)
    for i in msg:
        if i in LUT_decryption:
            decrypted_msg+=LUT_decryption[i]
        else:
            numerize=ord(i)
            decrypt=pow(numerize,d,n)
            LUT_decryption[i] = unichr(decrypt)
            decrypted_msg+=unichr(decrypt)
    clear()
    t2.insert(END, decrypted_msg)
    tkMessageBox.showinfo("Decrypt", "OHHH you just got decrypted boi")





e1 = Entry(master, justify=RIGHT)
e2 = Entry(master, justify=RIGHT)
b1 = Button(master, text="ENCRYPT", command=encrypt_message)
b2 = Button(master, text="DECRYPT", command=decrypt_message)
t1 = Text(master, width=20, height=10)
t2 = Text(master, width=20, height=10)
l1 = Label(master, text="Public Key:")





Label(master, text="ENCRYPTION").grid(column = 1, row=0, sticky=W)
Label(master, text="                         ").grid(row=0, column=5)
Label(master, text="DECRYPTION").grid(row=0, column=10, sticky=W)
Label(master, text="N").grid(row=1, column = 1, sticky=W)
Label(master, text="E").grid(row=2, column = 1, sticky=W)
l1.grid(row=2, column=5)
e1.grid(row=1, column=1, sticky=W)


menubar = Menu(master)
filemenu = Menu(menubar, tearoff=0) 
filemenu2 = Menu(menubar, tearoff=0)    
filemenu.add_command(label="Save", command=openfileR)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_separator()
filemenu.add_command(label="Open", command=openfileQ)
menubar.add_cascade(label="App", menu=filemenu2)
filemenu2.add_command(label="Clear", command=clear)



editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Clear", command=clear)


e2.grid(row=2, column=1, sticky=W)
b1.grid(row=3, column = 1, sticky = W)
b2.grid(row=1, column=10)
t1.grid(row=4, column = 1)
t2.grid(row=4, column = 10)




master.config(menu=menubar)






mainloop()