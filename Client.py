import socket
import os
from tkinter import *
from tkinter import filedialog 
import customtkinter
Bytesize=2000000
message1=input("Do you want do send or recive: (S/R)?") 
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 34536))
#print("Do you want do download or upload? (D/U)?")
print(f"\n{message1}") 
client.send(message1.encode())
def openf():
    global fpath
    fpath=filedialog.askopenfile()
    fpath=fpath.name
    print(fpath)
    app.destroy()
app=customtkinter.CTk()
button= Button(text="Open",command=openf)
button.pack()   
app.mainloop()
name=os.path.basename(fpath)
file=open(fpath,'rb')
data=file.read()
if(message1=="S"):
    client.send(name.encode())
    client.sendall(data)
    file.close()
    client.close()
if(message1=="R"): 
    client.send(name.encode())
    client.close()
    client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.bind((("localhost", 34538)))
    client.listen()
    client_socket, client_address= client.accept()
    os.chdir('C:\\Users\\איתי קליין\\Documents\\securefilesfolderRecive')
    print(f"YOUR CONNECTED{client_address} YABEN SHARMUTA")
    data=client_socket.recv(Bytesize)
    file1=open(name,'wb')
    file1.write(data)
    client.close()   
    client_socket.close()