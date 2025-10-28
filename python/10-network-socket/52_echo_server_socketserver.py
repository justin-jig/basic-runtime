import socketserver

HOST = ''
PORT = 9009

class MyTcpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print('[%s] 연결됨' % self.client_address[0])
        try:
            while True:
                data = self.request.recv(1024)
                if not data:
                    break
                if data.decode() == '/quit':
                    print('[%s] 사용자에 의해 중단' % self.client_address[0])
                    return
                print('[%s]' % data.decode())
                self.request.sendall(data)
        except Exception as e:
            print(e)

def runServer():
    print('+++ 에코 서버를 시작합니다.')
    print('+++ 에코 서버를 끝내려면 Ctrl-C를 누르세요.')
    try:
        server = socketserver.TCPServer((HOST, PORT), MyTcpHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('--- 에코 서버를 종료합니다.')

if __name__ == '__main__':
    runServer()
