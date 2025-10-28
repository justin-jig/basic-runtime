import os
import socket

HOST = 'localhost'
PORT = 9009

def ensure_dir(path):
    if not os.path.isdir(path):
        os.makedirs(path, exist_ok=True)

def getFileFromServer(filename):
    data_transferred = 0
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(filename.encode())

        data = sock.recv(1024)
        if not data:
            print('파일[%s]: 서버에 존재하지 않거나 전송중 오류발생' % filename)
            return

        ensure_dir('download')
        with open(os.path.join('download', filename), 'wb') as f:
            try:
                while data:
                    f.write(data)
                    data_transferred += len(data)
                    data = sock.recv(1024)
            except Exception as e:
                print(e)

    print('파일 [%s] 전송종료. 전송량 [%d]' % (filename, data_transferred))

if __name__ == '__main__':
    filename = input('다운로드 받을 파일이름을 입력하세요: ').strip()
    getFileFromServer(filename)
