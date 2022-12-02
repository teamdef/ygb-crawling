# while 문
# 조건이 false 가 될때까지 반복

i = 1 #초기식
while i <= 10: #조건식
    print(f'{i}번째 자동화 작업 중')
    i = i + 1 #증감식

while True:
    x = input('종료하려면 exit를 입력하세요 >>>')
    if x == 'exit':
        break