import socket
import threading

HEADER = 16
PORT = 9000
IP = socket.gethostbyname(socket.gethostname())
ADDR = (IP, PORT)
FORMAT = 'utf-8'

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(ADDR)

sockets_list = [server_socket]
clients = {}
userList = []

with open('nothing.txt') as data: nstring = data.read().strip()

games = {'ttt': 2, 'c4': 2, 'agm': 2, 'bts' : 2, 'bj': 4, 'nim': 2}
tttGames, tempTTTgame = [['tempgame']], []
c4, tempc4game = [['tempgame']], []
agm, tempAGMgame = [['tempgame']], []
bts, tempBTSgame = [['tempgame']], []
bj, tempBJgame = [['tempgame']], []
nim, tempNIMgame = [['tempgame']], []

def checkValidGame(game, conn):
    if game == "ttt":
        if len(tempTTTgame) < games[game]-1:
            tttGames.append([])
            tempTTTgame.append(conn)
            return len(tttGames)
        else:
            tempTTTgame.append(conn)
            tttGames[-1] = tempTTTgame
            tempTTTgame=[]
            return len(tttGames)-1
    elif game == 'c4':
        if len(tempc4game) < games[game]-1:
            tempc4game.append(conn)
            c4.append([])
            return len(c4)
        else:
            tempc4game.append(conn)
            c4[-1] = tempc4game
            tempc4game=[]
            return len(c4)-1
    elif game == 'agm':
        if len(tempAGMgame) < games[game]-1:
            agm.append([])
            tempAGMgame.append(conn)
            return len(agm)
        else:
            tempAGMgame.append(agm)
            agm[-1] == tempAGMgame
            tempAGMgame=[]
            return len(agm)-1
    elif game == 'bts':
        if len(tempBTSgame) < games[game]-1:
            bts.append([])
            tempBTSgame.append(conn)
            return len(bts)
        else:
            tempBTSgame.append(bts)
            bts[-1] == tempBTSgame
            tempBTSgame=[]
            return len(bts)-1
    elif game == 'bj':
        if len(tempBJgame) < games[game]-1:
            bj.append([])
            tempBJgame.append(conn)
            return len(bj)
        else:
            tempBJgame.append(bj)
            bj[-1] == tempBJgame
            tempBJgame=[]
            return len(bj)-1
    elif game == 'nim':
        if len(tempNIMgame) < games[game]-1:
            nim.append([])
            tempNIMgame.append(conn)
            return len(nim)-1
        else:
            tempNIMgame.append(nim)
            nim[-1] == tempNIMgame
            tempNIMgame=[]
            return len(nim)-1

def handle_client(conn, addr):

    global userList

    print(f"[NEW CONNECTION] {addr} connected.")

    try:
        msg_len = conn.recv(HEADER)
        message_length = msg_len.decode(FORMAT)
        message_length = int(message_length)
        game = {'header': message_length, 'data': conn.recv(message_length).decode(FORMAT)}
        print(game['data'])
    except:
        print('unable to get username')
    
    gameList = checkValidGame(game[data], conn)
    
    sockets_list.append(conn)
    ignoreDisconnected = []
    connected = True
    while connected:
        if len(gameList) != 0:
            try:
                msg_len = conn.recv(HEADER).decode(FORMAT)
                if msg_len: 
                    msg_len = int(msg_len)
                    msg = conn.recv(msg_len).decode(FORMAT)
                    print(msg)
                    if msg != nstring: 
                        print(msg, "message")
                        for client_socket in clients:
                            if client_socket != conn:
                                try:
                                    clients[client_socket].append(f"{user['header']:<{HEADER}}:{user['data']}:{msg_len:<{HEADER}}:{msg}")
                                    split_msg = clients[client_socket][0].split(":")
                                    client_socket.send(split_msg[0].encode(FORMAT))
                                    client_socket.send(split_msg[1].encode(FORMAT))
                                    client_socket.send(split_msg[2].encode(FORMAT))
                                    client_socket.send(''.join(split_msg[3:]).encode(FORMAT))
                                    del clients[client_socket][0]
                                except:
                                    ignoreDisconnected.append(client_socket)
                        for discon in ignoreDisconnected:
                            del clients[discon]
                        ignoreDisconnected = []
                    else:
                        if len(clients[conn]) != 0:
                            split_msg = clients[client_socket][0].split(":")
                            client_socket.send(split_msg[0].encode(FORMAT))
                            client_socket.send(split_msg[1].encode(FORMAT))
                            client_socket.send(split_msg[2].encode(FORMAT))
                            client_socket.send(''.join(split_msg[3:]).encode(FORMAT))
                        else:
                            conn.send(nstring.encode(FORMAT))
                else:
                    connected = False
            except:
                connected = False
    
    userList.remove(user['data'])
    del clients[conn]
    conn.close()
    joinedUserList = ':'.join(userList)
    for client in clients.keys():
        client.send(f"{'userlist      '+str(len(joinedUserList)):<{HEADER}}".encode(FORMAT))
        client.send(joinedUserList.encode(FORMAT))
def start():
    server_socket.listen(999)
    print(f"[LISTENING] Server is listening on {IP}")
    while True:
        conn, addr = server_socket.accept()
        clients[conn] = []
        print('Accepted new connection from {}:{}'.format(*addr))
        thread = threading.Thread(target = handle_client, args = (conn, addr))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.active_count() -1}')

print("[STARTING] server is starting...")
start()