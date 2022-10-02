import socket
import time


server = 'localhost'
port = 9090
main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
main_socket.bind((server, port))
main_socket.setblocking(0)
main_socket.listen(5)
print("[" + time.ctime() + "] server started")

class Player:
    def __init__(self, addr, conn, errors):
        self.addr = addr
        self.conn = conn
        self.errors = errors

players = []
while True:

    try:
        new_socket, addr = main_socket.accept()
        print("[" + time.ctime() + "] Joined ", addr)
        new_socket.setblocking(0)
        new_player = Player(addr, new_socket, 0)
        players.append(new_player)
    except:
        pass

    # for player in players:
    #     try:
    #         data = player.recv(1024)
    #         data = data.decode()
    #         print('Получил ', data)
    #     except:
    #         pass

    # for player in players:
    #     try:
    #         player.conn.send('connect '.encode())
    #
    #     except:
    #         player.errors += 1
        # print(player.errors)

    for player in players:
        if player.errors > 100:
            players.remove(player)
            player.conn.close()
            print("[" + time.ctime() + "] Disconnected ", addr)

    time.sleep(0.0001)