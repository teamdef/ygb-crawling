# 리스트
# 여러개의 데이터를 저장하는 자료형

# 변수 - [데이터, 데이터, 데이터]
company_list = ['삼성전자', 'SK하이닉스', '네이버']

# 데이터 접근하기
print(company_list[0])
print(company_list[-1]) # -1 index = 마지막 원소

# 데이터 할당하기
company_list[0] = "애플"
company_list[1] = "구글"
company_list[2] = "테슬라"

print(company_list)

# 데이터 삭제하기
del company_list[0]

print(company_list)

# 데이터 추가하기
company_list.append("아마존")

print(company_list)

# 리스트 길이
print(len(company_list))