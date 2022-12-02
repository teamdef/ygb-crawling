import os
from PIL import Image

# w정리할 확장자
extension_list = ['.jpg', '.png', '.jpeg', '.gif']

# 정리할 폴더
target = '02.python_automation/랜덤이미지'

# 만들 폴더
destination = os.path.join(target,'크기변경')

# 폴더가 없다면 만들기
if not os.path.exists(destination):
    os.mkdir(destination)

# 현재 폴더 내 모든 파일 출력
file_list = os.listdir(target)

# 반복문 통해 각 파일의 확장자를 확인해준다.
for file in file_list:
    name, ext = os.path.splitext(file)
    if ext in extension_list:
        # 이미지 열기
        img_path = os.path.join(target, file)
        img = Image.open(img_path)

        # 이미지 크기 수정
        width = int(img.width * 0.5)
        height = int(img.height * 0.5)
        resize = img.resize((width, height))

        # 이미지 저장
        save_path = os.path.join(destination, file)
        resize.save(save_path)