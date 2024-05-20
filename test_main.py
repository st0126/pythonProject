import pytest
from playwright.sync_api import Page, expect

site_Url = "https://gvw-qa.illuminarean.com/"

def go_site(page):
    page.goto(site_Url)


def check_ui_first(page):
    # 타이틀
    title = page.get_by_role("heading", name="엔터테인먼트 전문 정산 관리 서비스")
    print(f"타이틀 확인 : {title.is_visible()}")



def bub(page):
    # 설명
    content = page.get_by_text("GoodVibe Works는 현재 무료로 사용 가능합니다.아래 정보 입력 후 신청 완료 해주시면 회원가입을 위한 메일이 전달될 예정입니다.")
    print(f"설명 확인 : {content.is_visible()}")

    # 회사명
    company= page.get_by_text("회사명")
    print(f"회사명 확인 : {company.is_visible()}")
    company_placeholder= page.get_by_placeholder("30자 이내로 입력해주세요.")
    print(f"회사명 플레이스 홀더 확인 : {company_placeholder.is_visible()}")

    # 대표자명
    ceo= page.get_by_text("대표자명")
    print(f"대표자명 확인 : {ceo.is_visible()}")
    ceo_placeholder= page.locator("#ceoName")
    print(f"대표자명 플레이스 홀더 확인 : {ceo_placeholder.is_visible()}")

    # 사업자 유형(드롭다운)
    bussinessType = page.get_by_text("사업자 유형")
    print(f"사업자 유형 확인 : {bussinessType.is_visible()}")
    type = page.locator('//*[@id="businessType"]/input').input_value()
    if type == 'CORPORATION':
        print('법인 확인 : True')
    else :
        print('법인 확인 : false')

    # 직원수(드롭다운)
    member = page.get_by_text("직원수")
    print(f"직원수 확인 : {member.is_visible()}")
    scale = page.locator('//*[@id="scale"]/input').input_value()
    if scale == 'ONE_TO_FIVE':
        print('1-5 명 확인 : True')
    else :
        print('1-5 명 확인 : false')

    # 담당자명
    manager = page.get_by_text("담당자명")
    print(f"담당자명 확인 : {manager.is_visible()}")
    manager_placeholder = page.locator("#name")
    print(f"담당자명 플레이스 홀더 확인 : {manager_placeholder.is_visible()}")

    # 이메일
    emailAddress = page.get_by_text("이메일")
    print(f"이메일 확인 : {emailAddress.is_visible()}")
    emailAddress_placeholder = page.get_by_placeholder("회사 이메일을 입력해주세요.")
    print(f"이메일 플레이스 홀더 확인 : {emailAddress_placeholder.is_visible()}")

    # 휴대폰 번호
    phoneNumber = page.get_by_text("휴대폰 번호")
    print(f"휴대폰 번호 확인 : {phoneNumber.is_visible()}")
    phoneNumber_placeholder = page.get_by_placeholder("숫자로 입력해주세요.")
    print(f"휴대폰 번호 플레이스 홀더 확인 : {phoneNumber_placeholder.is_visible()}")

    # 담당업무(드롭다운)
    task = page.get_by_text("담당 업무", exact=True)
    print(f"담당업무 확인 : {task.is_visible()}")
    task_placeholder = page.locator("dl").filter(has_text="담당 업무 담당 업무를 1개 이상 선택해주세요.").locator("button")
    print(f"담당 업무 플레이스 홀더 확인 : {task_placeholder.is_visible()}")

    # 서비스 이용약관 동의
    service_agree = page.get_by_text("서비스 이용약관 동의")
    print(f"서비스 이용약관 동의 체크 박스 확인 : {service_agree.is_checked() == False}")


    # 개인정보 취급방침 동의
    personal_information_agree = page.get_by_text("개인정보 취급방침 동의")
    print(f"개인정보 취급방침 동의 체크 박스 확인 : {personal_information_agree.is_checked() == False}")


    # 무료 이용 신청 버튼 비활성화
    submit_btn= page.locator('//html/body/div[5]/div/div/div/div/div/div/div/div[3]/button')
    print(f"신청 버튼 비활성화 확인 : {submit_btn.is_enabled() == False}")

    # 신청 취소
    delete_btn = page.locator("div").filter(has_text="신청 취소").locator("button")
    print(f"신청 취소 버튼 확인 : {delete_btn.is_enabled()}")

pass

def test(page):
    go_site(page)
    check_ui_first(page)
    #bub(page)
