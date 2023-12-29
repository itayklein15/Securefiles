import socket
import os

Bytesize=2000000
server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(socket.gethostbyname(socket.gethostname()))
server.bind((("localhost", 34536)))
server.listen()
print("Server is runing...\n")
os.chdir('C:\\Users\\איתי קליין\\Documents\\securefilesfolderSend')
print("Do you want do download or upload? (S/R)?")


while True:
        server_socket, server_address= server.accept()
        message=server_socket.recv(Bytesize).decode()
        print(message)
        if(message=="S"):
            print(f"ata mehoobar le {server_address} yaben zona")
            file=server_socket.recv(Bytesize).decode() 
            data=server_socket.recv(Bytesize)
            file1=open(file,'wb')
            file1.write(data)
            break 
        if(message=="R"):
                
                file=server_socket.recv(Bytesize).decode() 
                server.close()
                server_socket.close()
                server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server.connect(("localhost", 34538))    
                try:
                    server.send("file was found".encode())
                    file1=open(file,'rb')
                    data=file1.read()
                    server.sendall(data)
                    server.close()
                    break
                except Exception as error:
                    print(error)
                    print(f"\n{"file wasnt found"}") 
                    break
