import socket
import _socket
import thread

def threaded_client(f_client,addr):   #just have addr as argu if we need it later:)
    f_client.send(str.encode('Welcome to the Server\n'))
    while True:
        try:
            data1, data2 = [int(i) for i in f_client.recv(2048).decode('utf-8').split('\n')]
        except:
            break
        if len(str(data1)) == 0: break
        f_client.send(str(data1 + data2))
    global connection_count
    connection_count -= 1
    print("connection number (after minuse one): "+str(connection_count))
    return

#___________________________________________________________________________

ServerSocket = socket.socket()
host = '127.0.0.1'
port = 12345
connection_count=0

try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(10) #its enough we can add it


while True:
    Client, address = ServerSocket.accept()
    if connection_count < 4 :
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        thread.start_new_thread(threaded_client, (Client, address,))
        connection_count += 1
        print('connection Number (after add one): ' + str(connection_count))
    else:
        Client.send("Server Is Busy")

ServerSocket.close()






'''
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.bind(("127.0.0.1",12345))
except socket.error as e:
  print(str(e))

s.listen(4)
while True:
    threading.Thread(target=handle, args=(s.accept(),)).start()
    '''
# client, addr =s.accept()
# print("Client : "+ str(addr))
# data=client.recv(1024)
# print(data)

# client.send("hello i am server")
# client.close()
