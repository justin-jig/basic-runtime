# 44_access_log_analysis.py
# Apache/Nginx 유사 access_log 분석
# log 포맷 가정: 공백 구분, [0]=IP, [8]=status, [9]=bytes

from os.path import exists

LOGFILE = 'access_log'

def load_lines(path=LOGFILE):
    if not exists(path):
        print(f'경고: {path} 파일이 없습니다.')
        return []
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        return f.readlines()

def count_pageviews(lines):
    """상태코드 200인 요청 수"""
    pv = 0
    for line in lines:
        parts = line.split()
        if len(parts) > 8 and parts[8] == '200':
            pv += 1
    return pv

def count_unique_ip(lines):
    """고유 방문 IP 수"""
    ips = set()
    for line in lines:
        parts = line.split()
        if parts:
            ips.add(parts[0])
    return len(ips)

def total_service_kb(lines):
    """전송 바이트 총합(KB)"""
    KB = 1024
    total = 0
    for line in lines:
        parts = line.split()
        if len(parts) > 9 and parts[9].isdigit():
            total += int(parts[9])
    return total // KB

def bytes_by_ip(lines):
    """IP별 전송 바이트 합계(내림차순)"""
    svc = {}
    for line in lines:
        parts = line.split()
        if len(parts) > 9:
            ip = parts[0]
            byte = parts[9]
            byte = int(byte) if byte.isdigit() else 0
            svc[ip] = svc.get(ip, 0) + byte
    return sorted(svc.items(), key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    logs = load_lines()

    pv = count_pageviews(logs)
    print('총 페이지뷰: [%d]' % pv)

    uv = count_unique_ip(logs)
    print('고유 방문자수: [%d]' % uv)

    kb = total_service_kb(logs)
    print('총 서비스 용량: %dKB' % kb)

    ranking = bytes_by_ip(logs)
    print('사용자IP – 서비스용량')
    for ip, b in ranking:
        print('[%s] – [%d]' % (ip, b))
