import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1",12345))
data=s.recv(1024)
print (data)
if str(data)!="Server Is Busy":
    data1=raw_input("enter data1 : ")
    data2=raw_input("enter data2 : ")
    s.sendall(str.encode("\n".join([str(data1), str(data2)])))
    data=s.recv(1024)
    print (data)
    data1=raw_input("enter some thing to close :")
    s.close()