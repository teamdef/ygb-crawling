# up & down 게임을 만들어보자.
# 프로그램이 시작되면 컴퓨터가 1부터 100까지 중 램덤으로 하나의 번호를 고른다.
# 사용자는 해당 번호를 맞출 때까지 계속 입력한다.
# 번호를 맞추면 총시도 횟수를 출력해 준다.

import random

print("컴퓨터가 숫자를 골랐습니다.")
answer = random.randint(1,100)
try_count = 1

while True:
    x = int(input("(1~100) 숫자를 맞춰 보세요 >>>"))

    # 정답 
    if x == answer:
        print("정답입니다!")
        print("총시도 횟수", try_count)
        break
    elif x > answer:
        print("down 입니다.")
    else:
        print("up 입니다.")

    try_count = try_count + 1 #try_count += 1
    