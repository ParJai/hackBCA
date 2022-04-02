import socket
class Client():
    def __init__(self, game):
        self.HEADER = 16
        self.PORT = 9000
        self.IP = "3.222.120.133"
        self.ADDR = (self.IP, self.PORT)
        self.FORMAT = 'utf-8'
        self.msg = ""
        self.messageQueue = []
        self.recievingQueue = []
        self.userList = []

        self.mygame = game

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(self.ADDR)

        self.game = self.mygame.encode(self.FORMAT)
        self.game_header = f"{len(self.game):<{self.HEADER}}".encode(self.FORMAT)
        self.client_socket.send(self.game_header+self.game)

    def send_message(self, msg):
        while True:
            if self.messageQueue != []:
                msg = self.messageQueue[0]
                del(self.messageQueue[0])
            else:
                msg = 0
            if msg != 0:
                message = msg.encode(self.FORMAT)
                msg_length = len(message)
                send_length = str(msg_length).encode(self.FORMAT)
                send_length += b' ' * (self.HEADER - len(send_length))
                self.client_socket.send(send_length)
                self.client_socket.send(message)

    def recieve_message(self):
        while True:
            try:
                username_header = self.client_socket.recv(self.HEADER).decode(self.FORMAT)
                print('recieved')
                if username_header.split()[0] != 'userlist':
                    print('1')
                    username_length = int(username_header.strip())
                    print('2')
                    username = self.client_socket.recv(username_length).decode(self.FORMAT)
                    print('3')
                    message_header = self.client_socket.recv(self.HEADER).decode(self.FORMAT)
                    print('4')
                    message_length = int(message_header.strip())
                    print('5')
                    message = self.client_socket.recv(message_length).decode(self.FORMAT)
                    self.recievingQueue.append([username, message])
                else:
                    print('10')
                    userListLen = int(username_header.split()[1].strip())
                    userList = self.client_socket.recv(userListLen).decode(self.FORMAT)
                    userList = userList.split(":")
                    self.userList = userList[0:]
            except:
                pass
