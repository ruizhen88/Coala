

print("주민등록번호 분석기입니다.")

r_number = input("주민등록번호를 입력해주세요: ")
#9210062069215

birth_year = r_number[0:2]
birth_month = r_number[2:4]
birth_day = r_number[4:6]
sex = r_number[6]

if sex == '1' or sex == '3':
    sex = "남자"
elif sex == '2' or sex == '4':
    sex = "여자"
else:
    sex = "중성"

# 출생지역
local = r_number[7:9]
# 06
number_local = int(local)

if number_local < 9:
    name_local = "서울특별시"
elif number_local < 13:
    name_local = "부산광역시"
elif number_local < 16:
    name_local = "인천광역시"
elif number_local < 26:
    name_local = "경기도"
elif number_local < 35:
    name_local = "강원도"
elif number_local < 40:
    name_local = "충청북도"
elif number_local == 40:
    name_local = "대전광역시"
elif number_local == 44 or number_local == 96:
    name_local = "세종특별자치시"
elif number_local < 44 or number_local < 48:
    name_local = "충청남도"
elif number_local < 55:
    name_local = "전라북도"
elif number_local == 55 or number_local == 56:
    name_local = "광주광역시"
elif number_local < 67:
    name_local = "전라남도"
elif number_local < 71:
    name_local = "대구광역시"
elif number_local < 82:
    name_local = "경상북도"
elif number_local == 85:
    name_local = "울산광역시"
elif number_local < 86 or number_local < 91:
    name_local = "경상남도"
elif number_local < 96:
    name_local = "제주특별자치도"

print("\n생년월일: {0}년 {1}월 {2}일".format(birth_year, birth_month, birth_day))
print("성별: {0}".format(sex))
print("출생지역: {0}".format(name_local))
