#Gui Programming Part
import tkinter as tk
from tkinter import PhotoImage, scrolledtext
from tkinter.constants import CENTER, END, LEFT
import socket
import _thread
import sys
import time
from client_dice import dice,clistr

# Code to create a new client socket  and connect to the server


client = 0
start = True
receivestart = True
tf = True
def sendMessage ():
    global receivestart
    msg = chat.get()
    client.send(msg.encode('utf-8'))
    if (msg == 'exit'):
        receivestart = False
        exit()
    textbox.configure(state='normal')
    if(chat.get() != ''):
        chat.delete(0, END)
    textbox.configure(state='disabled')

def recievingMessage (c):
    global receivestart,tf
    while receivestart :
        msg=c.recv(2048).decode('utf-8')       
            
        if not msg :
            sys.exit(0)
        global start
         
        if (msg.find('throw') >= 0):
            statusbox.configure(state='normal')
            statusbox.insert("end", msg+"\n")
            statusbox.configure(state='disabled') 
        elif (msg.find('r1: ') >= 0):
            statusbox.configure(state='normal')
            msg = msg[msg.find('r1: ')+4:]
            statusbox.insert("end", msg+"\n")
            tf = True
            statusbox.configure(state='disabled')
        else:
            textbox.configure(state='normal')
            if(msg != ''):
                textbox.insert("end", msg+"\n")
            textbox.configure(state='disabled')        
        
        if (start) :
            start = False
            #tkinter codes starts
            # window.title(msg)
            continue

#Socket Creation
def socketCreation ():    
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#Local Host    
# import all functions /
#  everthing from chat.py file
    host = '127.0.0.1'
    port = 5000
    c.connect((host,port))
    global client
    client = c
    #chatent['command'] = sendMessage
    _thread.start_new_thread(recievingMessage, (c,) )

def closew():
    global receivestart
    msg = "exit"
    client.send(msg.encode('utf-8'))
    receivestart = False
    exit()

#method to roll dice
def rolldice():
    global tf
    statusbox.configure(state='normal')
    if (tf):
        statusbox.configure(state='normal')
        di = dice()
        message = "十八啦!!!"
        client.send(message.encode('utf-8'))
        dice.throw(di)
        dice_result = str(di.a)+" "+str(di.b)+" "+str(di.c)+" "+str(di.d)+" \n"
        temp, message = clistr.dicetostring(di)
        if (temp):
            time.sleep(1)
            statusbox.insert("end",dice_result)
            client.send(message.encode('utf-8'))
            temp = False
        else:
            statusbox.insert("end",dice_result)
            statusbox.insert("end","請重骰！\n")
            temp = True
        tf = temp    
    else:
        statusbox.insert("end","你骰過了！\n")
        tf = False
    statusbox.configure(state='disabled')    

#method to send message by press enter on keyboard
def entmsg(event):  
    sendMessage()

#Create a new window
window = tk.Tk()
window.title("Shibadaua")
window.geometry('480x560')
window.resizable(False, False)
window.protocol("WM_DELETE_WINDOW", closew)
img = PhotoImage(file='dice.png')
img2 = PhotoImage(file='dice2.png')
window.tk.call('wm', 'iconphoto', window._w, img)
window.bind('<Return>', entmsg)
window.configure(bg='#616775')

#Define the text box to show the status
statusbox = scrolledtext.ScrolledText(window, state='disabled', width = 50 , height = 6, font=('微軟正黑體', 12))
statusbox.place(x=240,y=95,anchor=CENTER)

#Define the text box to show the chat message
textbox = scrolledtext.ScrolledText(window, state='disabled', width = 50 , height = 6, font=('微軟正黑體', 12))
textbox.place(x=240,y=260,anchor=CENTER)

#Define the button to roll the dice
roll = tk.Button(image=img2,compound=LEFT,text=" Roll the dice!!!",bg='white',command=rolldice,font=('微軟正黑體', 12))
roll.place(x=240,y=370,anchor=CENTER)

#Define the entry box to type the chat words
chat = tk.Entry(window, width=40, font=('微軟正黑體', 12))
chat.place(x=200, y=455, anchor=CENTER)

#Define the button to exit
exitbu = tk.Button(text="Exit", width = 5, command=closew, font=('微軟正黑體', 10))
exitbu.place(x=425, y=370, anchor=CENTER)

#Define the button to send the chat message, can be instead by press enter on keyboard
chatent = tk.Button(text="Enter", width = 5, command=sendMessage,font=('微軟正黑體', 10))
chatent.place(x=425, y=455, anchor=CENTER)

#Define the label that indicate the status box
status = tk.Label(window, text="Status",fg='white',bg='#616775',font=('微軟正黑體', 12))
status.place(x=30,y=20,anchor=CENTER)

#Define the label that indicate the chat box
text = tk.Label(window, text="Chatbox",fg='white',bg='#616775',font=('微軟正黑體', 12))
text.place(x=39,y=185,anchor=CENTER)

#Define the label that indicate the message typing box
typemsg = tk.Label(window, text="Type your message here. (Type exit to leave.)",fg='white',bg='#616775',font=('微軟正黑體', 12))
typemsg.place(x=190,y=425,anchor=CENTER)

#Define the label that indicate the warning message
warning = tk.Label(window, text="★小賭怡情，切勿過度沉迷★",fg='white',bg='#616775',font=('微軟正黑體', 16))
warning.place(x=240,y=510,anchor=CENTER)

#Define the label that indicate the copyright message
cpr = tk.Label(window, text="Copyright © 2022, 404 Entertainment",fg='white',bg='#616775',font=('微軟正黑體', 8))
cpr.place(x=375,y=550,anchor=CENTER)


_thread.start_new_thread(socketCreation, () )

window.mainloop()
