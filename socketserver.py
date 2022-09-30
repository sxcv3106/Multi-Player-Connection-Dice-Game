##Python codes to do server-side part of chat room.
import _thread
import socket
import threading
import time
from server_result import result

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# piece of code to allow IP address & Port
host="127.0.0.1"
port=5000
s.bind((host,port))
s.listen(10)
clients=[]
server_dice = result()
ad = '0'

#code to allow users to send messages
def connectNewClient(c):
    global server_dice,ad
    while True:
        global clients
        msg = c.recv(2048)
        ad = c.getpeername()
        boo = True
        if (msg.decode('utf-8')=='exit'):
            k = server_dice.poli.index(ad)
            msg = "Player leave."
            print(msg)
            sendToAll(msg,c)
            result.delply(server_dice, server_dice.nali[k])
            clients.remove(c)
            break;
        for i in server_dice.poli:
            if (ad == i):
                boo = False
        if boo: 
            result.inp(server_dice,ad)
        if (msg.decode('utf-8').find("c1: ") >= 0):     
            check, substring = result.ifres(msg.decode('utf-8'))
            result.inr(server_dice,ad,substring)
            msg = msg.decode('utf-8')
            p = server_dice.poli.index(ad)
            msg = 'Player ('+str(p+1)+') throw '+substring
            sendToAll(msg,c)
            if(check & (result.clnum(server_dice) > 1) & (result.clnum(server_dice) == result.rtnum(server_dice))):
                print(msg)
                winner = result.findmax(server_dice)
                result.setzero(server_dice)
                msg  = winner
                time.sleep(0.5)
                sendToAll(msg,c)
        else:
            msg ='Player ('+str(clients.index(c)+1)+'):  '+msg.decode('utf-8')
            sendToAll(msg,c)
        if (msg.find('r1: ') >= 0):
            print(msg[4:])
        else:
            print(msg)
        
        
def sendToAll(msg,con):
    for client in clients:
        client.send(msg.encode('utf-8')) 

if __name__ == '__main__':     
    while True:
        c,ad=s.accept()
        
        result.inp(server_dice,ad)
        clients.append(c)
        c.send(('Player ('+str(clients.index(c)+1)+')').encode('utf-8'))
        result.inn(server_dice,ad,'Player ('+str(clients.index(c)+1)+')')
        print('Player ('+str(clients.index(c)+1)+')'+' Connected ')
        
        _thread.start_new_thread(connectNewClient,(c,))
