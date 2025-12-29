from tkinter import *


root = Tk()

# size and color of window
root.geometry("1200x6000")
root.configure(bg='gray98')

# title of window
root.title("Message Encryption and Decryption")

Tops = Frame(root, width=1600, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, relief=SUNKEN)
f1.pack(side=LEFT)




lblInfo = Label(Tops, font=('helvetica', 50, 'bold'),
                text="SECRET MESSAGING \n Caeser Cipher",
                fg="Black", bd=10, bg="gray90",anchor='w')

lblInfo.grid(row=0, column=0)


# Initializing variables
Msg = StringVar()
key = IntVar()
mode = StringVar()
Result = StringVar()


# labels for the message
lblMsg = Label(f1, font=('arial', 16, 'bold'),
               text="MESSAGE", bd=16, anchor="w")

lblMsg.grid(row=1, column=0)
# Entry box for the message
txtMsg = Entry(f1, font=('arial', 16, 'bold'),
               textvariable=Msg, bd=10, insertwidth=4,
               bg="powder blue", justify='right')


txtMsg.grid(row=1, column=1)
# labels for the key
lblkey = Label(f1, font=('arial', 16, 'bold'),
               text="KEY (Only Integer)", bd=16,bg="white smoke",  anchor="w")

lblkey.grid(row=2, column=0)


# Entry box for the key
txtkey = Entry(f1, font=('arial', 16, 'bold'),
               textvariable=key, bd=10, insertwidth=4,
               bg="powder blue", justify='right')

txtkey.grid(row=2, column=1)

# labels for the mode
lblmode = Label(f1, font=('arial', 16, 'bold'),
                text="MODE(e/E for encrypt, d/D for decrypt)",
                bd=16 ,bg="white smoke", anchor="w")

lblmode.grid(row=3, column=0)
# Entry box for the mode
txtmode = Entry(f1, font=('arial', 16, 'bold'),
                textvariable=mode, bd=10, insertwidth=4,
                bg="powder blue", justify='right')

txtmode.grid(row=3, column=1)

# labels for the result
lblResult = Label(f1, font=('arial', 16, 'bold'),
                  text="Result-", bd=16,fg="IndianRed1", anchor="w")

lblResult.grid(row=2, column=2)

# Entry box for the result
txtResult = Entry(f1, font=('arial', 16, 'bold'),
                  textvariable=Result, bd=10, insertwidth=4,
                  bg="misty rose", justify='right')

txtResult.grid(row=2, column=3)

# caese cipher

# Function to encode


def encode(key, msg):
    print(key,msg)
    cipher=""
    for char in msg:
        if char==' ':
            cipher=cipher+char
        elif char.isupper():
            cipher=cipher+chr((ord(char)+key-65)%26+65)
        else:
            cipher=cipher+chr((ord(char)+key-97)%26+97)
    print("cipher:", cipher)
    return cipher
    


# Function to decode

def decode(key, msg):
   
    cipher=""
    for char in msg:
        if char==' ':
            cipher=cipher+char
        elif char.isupper():
            cipher=cipher+chr((ord(char)-key-65)%26+65)
        else:
            cipher=cipher+chr((ord(char)-key-97)%26+97)
    
    return cipher
    


def Results():
    # print("Message= ", (Msg.get()))

    msg = Msg.get()
    k = key.get()
    m = mode.get()
    if str(k).isdigit:
        if (m == 'e' or m == 'E'):
            Result.set(encode(k, msg))
        elif (m == 'd' or m == 'D'):
            Result.set(decode(k, msg))   

    
def Reset():

    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")


btnTotal = Button(f1, padx=16, pady=5, bd=16, fg="black",
                  font=('arial', 16, 'bold'), height=1,width=8,
                  text="Show/Hide", bg="misty rose",
                  command=Results).grid(row=7, column=1)

btnReset = Button(f1, padx=16, pady=8, bd=16,
                  fg="black", font=('arial', 16, 'bold'),
                  width=10, text="Reset", bg="powder blue",
                  command=Reset).grid(row=7, column=2)


root.mainloop()
