file_name = "_03. 타입.pdf"
file_name2 = "_04. 연산지.pptx"
file_name3 = "_05. 반복문.doc"

ix = file_name.rfind('.')
if ix != -1: # 문자가 있는 경우
    ext_name = file_name[ix+1:]
    print(ext_name)
else:  # '.' 문자가 없는 경우
    print('확장자 없음')

ix = file_name2.rfind('.')
if ix != -1: # 문자가 있는 경우
    ext_name = file_name[ix+1:]
    print(ext_name)
else:  # '.' 문자가 없는 경우
    print('확장자 없음')

ix = file_name3.rfind('.')
if ix != -1: # 문자가 있는 경우
    ext_name = file_name[ix+1:]
    print(ext_name)
else:  # '.' 문자가 없는 경우
    print('확장자 없음')

def print_file_ext(fname):
    ix = fname.rfind('.')
    if ix != -1: # 문자가 있는 경우
        ext_name = file_name[ix+1:]
        print(ext_name)
    else: # '.' 문자가 없는 경우
        print('확장자 없음')

print_file_ext(file_name)
print_file_ext(file_name2)
print_file_ext(file_name3)