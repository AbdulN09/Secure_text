import tkinter
from tkinter import *
import base64


def encryption():
    text_to_encrypt=text_field_top.get(1.0,END)
    if text_to_encrypt!="//s":
        bytes_text_to_encrypt=text_to_encrypt.encode("ascii")
        encoded_msg=base64.b64encode(bytes_text_to_encrypt)
        text_field_bottom.insert(0.0,str(encoded_msg))
    else:
        text_field_bottom.insert(END, ".......wait!!!!!Enter valid text to decrypt")



def decryption():
    text_to_decrypt=text_field_top.get(1.0,END)
    if text_to_decrypt[0]=="b":
        text_field_bottom.delete(1.0,END)
        decoded_msg=base64.b64decode(text_to_decrypt[1::])
        decoded_msg = decoded_msg.decode("ascii")
        text_field_bottom.insert(END,decoded_msg)
    else:
        text_field_bottom.insert(END, ".......wait!!!!!Enter valid text to decrypt")

def reset():
    text_field_bottom.delete(1.0, END)
    text_field_top.delete(1.0, END)


screen=Tk()
screen.title("Encryptor_Decryptor")
screen.geometry("475x400")
screen.maxsize(width=475,height=400)

screen.config(bg="#E0FFFF")


label1=Label(text="Enter Your Text Here",font=("Courier New",12,"bold"),bg="#E0FFFF",foreground="black")
label1.pack(pady=5)


text_field_top=Text(screen,width=62,bg="#FEF8DD",height=6,font=("Courier New",10,"bold"),borderwidth="2")
text_field_top.pack(pady=3,padx=6)
text_field_top.focus()

encrypt_button=Button(screen,text="ENCRYPT",width=7,height=2,font=("Courier New",8,"bold"),bg="#FFCCCB",command=encryption)
encrypt_button.place(x=17,y=182.5)


reset_button=Button(screen,text="RESET",width=7,height=2,font=("Courier New",8,"bold"),bg="white",command=reset)
reset_button.place(x=210,y=182.5)

decrypt_button=Button(screen,text="DECRYPT",width=7,height=2,font=("Courier New",8,"bold"),bg="#3EB489",command=decryption)
decrypt_button.place(x=400,y=182.5)

text_field_bottom=Text(screen,width=57,bg="#FEF8DD",height=6,font=("Courier New",10,"bold"),borderwidth="2")
text_field_bottom.place(x=6,y=260)


label2=Label(text="Encrypted Text/Decrypted Text",font=("Courier New",12,"bold"),bg="#E0FFFF",foreground="black")
label2.place(x=95,y=370)

screen.mainloop()
