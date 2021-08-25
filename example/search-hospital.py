# 병원, 보건소 검색하기 예제

from hcspy import HCSClient
from asyncio import run


async def search_hospital():
    client = HCSClient()
    school = await client.search_school(name="학교 이름", level="학교 레벨/유형", area="지역")
    user = await client.login(
        school=school[-1],  # 검색한 학교들 중 최상위에 있는 학교 가져오기
        name="사용자 이름",
        birthday="사용자 생년월일 6자리",
        password="4자리 비밀번호",
    )
    user1 = user[-1]  # 첫번째 유저 가져오기
    hospital_list = await user1.search_hospital(location="경기", name="보건소")
    for hospital in hospital_list:
        print(
            f"병원 | {hospital.name}, 주소: {hospital.state} {hospital.city} | 영업시간: {hospital.schedule} | 전화번호 {hospital.tell}\n\n"
        )


run(search_hospital())