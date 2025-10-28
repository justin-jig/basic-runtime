# 43_baby_names_analysis.py
# SSA baby names 데이터 분석
# - names/yobYYYY.txt 파일 필요 (예: names/yob2015.txt)
# - 포맷: name,sex,births

from os.path import exists

def countBirths():
    """1880~2015 연도별 전체 출생아 수 집계"""
    ret = []
    for y in range(1880, 2016):
        filename = f'names/yob{y}.txt'
        if not exists(filename):
            # 없으면 0으로 채우고 계속
            ret.append((y, 0))
            continue
        count = 0
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.rstrip('\n')
                birth = line.split(',')[2]
                count += int(birth)
        ret.append((y, count))
    return ret

def countBirthsBySex():
    """1880~2015 연도별 성별(F/M) 출생아 수 집계"""
    ret = []
    for y in range(1880, 2016):
        filename = f'names/yob{y}.txt'
        if not exists(filename):
            ret.append((y, 0, 0))
            continue
        count_f = 0
        count_m = 0
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.rstrip('\n')
                name, sex, birth = line.split(',')
                if sex == 'F':
                    count_f += int(birth)
                else:
                    count_m += int(birth)
        ret.append((y, count_f, count_m))
    return ret

def write_birth_csv():
    result = countBirths()
    with open('birth_by_year.csv', 'w', encoding='utf-8') as f:
        for year, birth in result:
            row = f'{year},{birth}\n'
            print(row, end='')
            f.write(row)

    result = countBirthsBySex()
    with open('birth_by_sex.csv', 'w', encoding='utf-8') as f:
        for y, bf, bm in result:
            row = f'{y},{bf},{bm}\n'
            print(row, end='')
            f.write(row)

def getTop10BabyName(year):
    """특정 연도 Top10(F/M) 출력"""
    filename = f'names/yob{year}.txt'
    if not exists(filename):
        print(f'[{filename}] 파일이 존재하지 않습니다.')
        return None

    nameF, nameM = {}, {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')
            name, sex, birth = line.split(',')
            target = nameF if sex == 'F' else nameM
            target[name] = target.get(name, 0) + int(birth)

    retF = sorted(nameF.items(), key=lambda x: x[1], reverse=True)[:10]
    retM = sorted(nameM.items(), key=lambda x: x[1], reverse=True)[:10]

    for i, item in enumerate(retF, start=1):
        print(f'TOP_{i} 여자아기이름: {item}')
    for i, item in enumerate(retM, start=1):
        print(f'TOP_{i} 남자아기이름: {item}')

if __name__ == '__main__':
    # CSV 출력
    write_birth_csv()

    # Top10 조회
    y = input('인기순 상위10개 이름을 알고 싶은 출생년도를 입력하세요(예:2001): ').strip()
    getTop10BabyName(y)
