import socket

while True:
    try:
        hostname = input("input hostname :")
        if hostname == "q":
            break
        print(socket.gethostbyname(hostname))
    except:
       print("could not transfer")
