# 40_network_http_basics.py
# HTTP 문서 가져오기 (urllib.request.urlopen)
# + HTML 저장, 이미지 다운로드, 대용량 파일 스트리밍 다운로드

from urllib.request import urlopen

# ------------------------------------------------------------
# 1) HTML 페이지를 가져와 파일로 저장
# ------------------------------------------------------------
url = 'https://www.python.org/'
with urlopen(url) as f:
    doc = f.read().decode()
    with open('pythonhome.html', 'w', encoding='utf-8') as h:
        h.writelines(doc)
print('[저장 완료] pythonhome.html')

# ------------------------------------------------------------
# 2) 이미지 다운로드 (바이너리)
# ------------------------------------------------------------
imgurl = 'http://www.epaiai.com/img_sample.jpg'
imgname = imgurl.split('/')[-1]
try:
    with urlopen(imgurl) as f:
        with open(imgname, 'wb') as h:
            img = f.read()
            h.write(img)
    print(f'[이미지 다운로드 완료] {imgname}')
except Exception as e:
    print('[이미지 다운로드 실패]', e)

# ------------------------------------------------------------
# 3) 대용량 파일을 버퍼로 스트리밍 다운로드
#    ⚠️ 실제로 매우 큰 파일일 수 있으므로 네트워크/저장공간 주의
# ------------------------------------------------------------
BUFSIZE = 256 * 1024
fileurl = 'https://www.python.org/ftp/python/3.5.2/python-3.5.2.exe'
filename = fileurl.split('/')[-1]
try:
    with urlopen(fileurl) as f:
        with open(filename, 'wb') as h:
            buf = f.read(BUFSIZE)
            while buf:
                h.write(buf)
                buf = f.read(BUFSIZE)
    print(f'[대용량 다운로드 완료] {filename}')
except Exception as e:
    print('[대용량 다운로드 실패]', e)
