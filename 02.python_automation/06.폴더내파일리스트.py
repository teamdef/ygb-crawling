import os
from posixpath import splitext

# 현재 폴더 내 모든 파일 출력
file_list = os.listdir('C:/Users/User/Downloads/')
print(file_list)

# 반목문 통해 각 파일의 확장자 확인한다.
for file in file_list:
    name, ext = os.path.splitext(file)
    print(name, ext)

    # = 
    # tuple_a = os.path.splitext(file)
    # name = tuple_a[0]
    # ext = tuple_a[1]