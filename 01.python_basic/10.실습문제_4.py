# 실습문제 4)
# 조건 10시간 이상 : 휴대폰 장금 해제 됩니다.
# 조건 5시간 이상 : 휴대폰 30분간 사용가능 합니다.
# 나머지 : 휴대폰 사용이 불가능 합니다.

mc_time = int(input("공부시간을 입력하세요(시간) >>>"))
if mc_time >= 10:
    print("휴대폰 장금 해제 됩니다.")
elif mc_time >=5 and mc_time < 10:
    print("휴대폰 30분간 사용가능합니다.")
else:
    print("휴대폰 사용이 불가능 합니다.")