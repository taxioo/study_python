# 파일 목록
from typing import Text


# 1) addressbook.copy.Text
# 2) addressbook.Text
# 3) live.Text
# 4) live2.Text
# 5) memo.Text

# 파일 선택 :3
# live.txt. 내용을 출력

# 파일 선택 : -1
# 종료

# 무한루프로 운영

import os

# 디렉토리에서 지정한 파일 확장자를 가지는 파일 목록 얻기
def get_files(dir_path, ext):
    files = os.listdir(dir_path)
    return [ file for file in files if file.endswith(ext)]
#전달된 목록 출력
def print_file_list(files):
    print('파일목록')
    for ix, file in enumerate(files, 1):
        print(f'{ix} {file}')
#파일의 내용을 출력
def print_file(file_name):
    try:
        with open(file_name, 'rt', encoding='utf-8') as f:
            text = f.read()
            print(text)
    except Exception as e:
        print('[에러]', e)

while True:
    files = get_files('.', '.txt')
    print_file_list(files)
    sel_num = int(input('파일 선택: '))
    if sel_num == -1:
        break
    else:
        print_file(files[sel_num-1])

#디렉토리의 파일 목록 구하기 - 특정 확장자를 가지는 확장명의 파일만 -> 함수
#목록 출력하기 -> 함수
#파일 선택
#선택 파일 출력 -> 함수
#종료하기
#무한루프로 운영하기