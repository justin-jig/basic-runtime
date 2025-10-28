# 입력받은 파일명에 확장자(.jpg) 자동 추가
# 문자열 결합과 f-string 활용 예제

filename = input('저장할 파일 이름을 입력하세요: ')
filename = filename + '.jpg'
display_msg = f'당신이 저장한 파일은 <{filename}> 입니다.'
print(display_msg)
