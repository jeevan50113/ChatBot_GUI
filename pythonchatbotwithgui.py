from tkinter import *

window = Tk()
window.title("UNQ CHAT BOT")
window.geometry('400x500')


def send():
    send ="you:"+messagewindow.get()

    chatarea.insert(END,"\n"+send)

    if(messagewindow.get()== "hi"):
        chatarea.insert(END,"\n"+"BOT: hello")
    elif(messagewindow.get()== "what is your name"):
        chatarea.insert(END,"\n"+"BOT: my name is LYRA")
    elif(messagewindow.get()== "how are you"):
        chatarea.insert(END,"\n"+"BOT: I am fime. what about you")
    elif(messagewindow.get()== "i am fine"):
        chatarea.insert(END,"\n"+"BOT: good to hear that")
    else:
        chatarea.insert(END,"\n"+"BOT: I didn't get that")


#create chat area in the window

chatarea = Text(window,bg='white',width=50,height=8)
chatarea.place(x=6,y=6, height=385,width=370)


#message area in the window

messagewindow = Entry(window,bg='white',width= 30)
messagewindow.place(x=128,y=400,height=88,width=260)

#Button 
send = Button(window,text="send",bg='blue',activebackground='light blue' ,width=20, height=5,font=('Arial',12),command= send)
send.place(x=6,y=400,height=81,width=120)


window.mainloop()