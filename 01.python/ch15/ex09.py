import os
import shutil

shutil.copy("live.txt", "live2.txt")

def get_files(dir_path, ext):
    result = []
    files = os.listdir(dir_path)
    for file in files:
        if file.endswith(ext):
            result.append(file)

    return result


print()
def get_files(dir_path, ext):
    files = os.listdir(dir_path)
    return [ file for file in files if file.endswith(ext)]
#1. filter()함수
# return list(filter(lambda file: file.endswith(ext), files))

#2. 컴프리헨션



#3. 일반 순회
# result = []

# for file in files:
#     if file.endswith(ext):
#         result.append(file)
# return result

# files = get_files('.', '.txt')
# print(files)
