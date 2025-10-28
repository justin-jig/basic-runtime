import socketserver
import threading

HOST = ''
PORT = 9009
lock = threading.Lock()

class UserManager:
    def __init__(self):
        self.users = {}  # username -> (conn, addr)

    def addUser(self, username, conn, addr):
        if username in self.users:
            conn.send('이미 등록된 사용자입니다.\n'.encode())
            return None
        with lock:
            self.users[username] = (conn, addr)
        self.sendMessageToAll('[%s]님이 입장했습니다.' % username)
        print('+++ 대화 참여자 수 [%d]' % len(self.users))
        return username

    def removeUser(self, username):
        if username not in self.users:
            return
        with lock:
            del self.users[username]
        self.sendMessageToAll('[%s]님이 퇴장했습니다.' % username)
        print('--- 대화 참여자 수 [%d]' % len(self.users))

    def messageHandler(self, username, msg):
        if not msg:
            return
        if msg[0] != '/':
            self.sendMessageToAll('[%s] %s' % (username, msg))
            return
        if msg.strip() == '/quit':
            self.removeUser(username)
            return -1

    def sendMessageToAll(self, msg):
        for conn, _ in self.users.values():
            try:
                conn.send(msg.encode())
            except:
                pass

class MyTcpHandler(socketserver.BaseRequestHandler):
    userman = UserManager()

    def handle(self):
        print('[%s] 연결됨' % self.client_address[0])
        username = None
        try:
            username = self.registerUsername()
            msg = self.request.recv(1024)
            while msg:
                text = msg.decode()
                print(text)
                if self.userman.messageHandler(username, text) == -1:
                    self.request.close()
                    break
                msg = self.request.recv(1024)
        except Exception as e:
            print(e)
        finally:
            print('[%s] 접속종료' % self.client_address[0])
            if username:
                self.userman.removeUser(username)

    def registerUsername(self):
        while True:
            self.request.send('로그인ID:'.encode())
            username = self.request.recv(1024).decode().strip()
            if self.userman.addUser(username, self.request, self.client_address):
                return username

class ChatingServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
    allow_reuse_address = True

def runServer():
    print('+++ 채팅 서버를 시작합니다.')
    print('+++ 채팅 서버를 끝내려면 Ctrl-C를 누르세요.')
    server = None
    try:
        server = ChatingServer((HOST, PORT), MyTcpHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('--- 채팅 서버를 종료합니다.')
    finally:
        if server:
            server.shutdown()
        if server:
            server.server_close()

if __name__ == '__main__':
    runServer()
