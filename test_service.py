import pytest
from playwright.sync_api import Page, expect

site_Url = "https://gvw-qa.illuminarean.com/"
input_company_test = "test_company"
input_ceo_test = "test_ceo"
input_manager_test = "test_manager"

email = "aaaaa@naver.com"
n_email = "aaaaaaaaa"
phone = "01011112222"
n_phone = "1111"

service_agree_url = "https://gvw.notion.site/GoodVibe-Works-2023-06-13-10aa4177bb4846219c12e2c348e9a2cd"
info_agree_url = "https://gvw.notion.site/GoodVibe-Works-2023-06-13-5e2c8cf01bb145d2a8f0d88e859f1f7f"

def go_site(page):
    page.goto(site_Url)


def enter_page(page):
    # 무료체험신청 버튼 클릭
    enter_page = page.get_by_role("banner").get_by_role("button", name="무료 체험 신청")
    enter_page.click()


def check_ui(page):
    # 타이틀
    title = page.get_by_text("서비스 이용신청")
    print(f"타이틀 확인 : {title.is_visible()}")

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


def submit(page):
    #회사명
    company_erase_btn = page.locator("button[name=\"companyName\"]")
    input_company = page.get_by_placeholder("30자 이내로 입력해주세요.")
    input_company.fill(input_company_test)
    print(f"회사명 삭제 버튼 : {company_erase_btn.is_visible()}")
    company_erase_btn.click()
    print(f"회사명 삭제 버튼 클릭 후 : {input_company.input_value()}")

    #대표자명
    ceo_erase_btn = page.locator("button[name=\"ceoName\"]")
    input_ceo = page.locator("#ceoName")
    input_ceo.fill(input_ceo_test)
    print(f"대표자명 삭제 버튼 : {ceo_erase_btn.is_visible()}")
    ceo_erase_btn.click()
    print(f"대표자명 삭제 버튼 클릭 후 : {input_ceo.input_value()}")

    #사업자 유형

    #직원수
    # print(page.locator('//*[@id="scale"]/input').input_value())
    #
    # page.locator('//*[@id="scale"]/div').click()
    # page.locator('//*[@id="scale"]/div[2]').locator('#react-select-scale-option-0').click()
    # print(page.locator('//*[@id="scale"]/input').input_value())
    #
    # page.locator('//*[@id="scale"]/div').click()
    # page.locator('//*[@id="scale"]/div[2]').locator('#react-select-scale-option-0').click()
    # print(page.locator('//*[@id="scale"]/input').input_value())

    #담당자명
    manager_erase_btn = page.locator("button[name=\"name\"]")
    input_manager = page.locator("#name")
    input_manager.fill(input_manager_test)
    print(f"담당자명 삭제 버튼 : {manager_erase_btn.is_visible()}")
    manager_erase_btn.click()
    print(f"담당자명 삭제 버튼 클릭 후 : {input_manager.input_value()}")

    #이메일
    email_erase_btn = page.locator("button[name=\"email\"]")
    input_email = page.get_by_placeholder("회사 이메일을 입력해주세요.")
    input_email.fill(n_email)
    print("비유효 이메일 : ", page.get_by_text('이메일 주소를 정확하게 입력해주세요.').count() == 1)
    email_erase_btn.click()
    input_email.fill(email)
    print(f"이메일 삭제 버튼 : {email_erase_btn.is_visible()}")
    email_erase_btn.click()
    print(f"이메일 삭제 버튼 클릭 후 : {input_email.input_value()}")

    #휴대폰 번호
    phone_erase_btn = page.locator("button[name=\"mobile\"]")
    input_phone = page.get_by_placeholder("숫자로 입력해주세요.")
    input_phone.fill(n_phone)
    print("비유효 번호 : ", page.get_by_text('휴대폰 번호를 정확하게 입력해주세요.').count() == 1)
    phone_erase_btn.click()
    input_phone.fill(phone)
    print(f"휴대폰 번호 삭제 버튼 : {phone_erase_btn.is_visible()}")
    phone_erase_btn.click()
    print(f"휴대폰 번호 삭제 버튼 클릭 후 : {input_phone.input_value()}")

    #담당업무

    #서비스 이용약관 동의
    service_agree_box = page.locator("label").filter(has_text="서비스 이용약관 동의").locator("div").first
    expect(service_agree_box, message="서비스 이용약관 동의 선택되었습니다.").not_to_be_checked()
    print(f"서비스 이용 약관 동의 체크박스 off : {service_agree_box.is_checked() == False}")
    service_agree_box.click()
    print(f"서비스 이용 약관 동의 체크박스 체크박스 클릭 후 on : {service_agree_box.is_checked()}")

    with page.expect_popup() as np:  #열기 위한 행동
        page.locator("label").filter(has_text="서비스 이용약관 동의").locator("a").click()
    new_page_notion = np.value

    print("서비스 이용약관 동의 url : ", new_page_notion.url == service_agree_url)
    expect(new_page_notion, message="잘못된 url입니다.").to_have_url(service_agree_url)

    #개인 정보 동의
    info_agree_box = page.locator("label").filter(has_text="개인정보 취급방침 동의").locator("div").first
    expect(info_agree_box, message="개인 정보 동의 선택되었습니다.").not_to_be_checked()
    print(f"개인 정보 동의 체크박스 off : {info_agree_box.is_checked()== False}")
    info_agree_box.click()
    print(f"개인 정보 동의 체크박스 클릭 후 on : {info_agree_box.is_checked()}")

    with page.expect_popup() as np2:
        page.locator("label").filter(has_text="개인정보 취급방침 동의").locator("a").click()
    new_page_notion2 = np2.value

    print("개인정보 취급방침 동의 url : ", new_page_notion2.url == info_agree_url)
    expect(new_page_notion2, message="잘못된 url입니다.").to_have_url(info_agree_url)


def test(page):
    go_site(page)
    enter_page(page)
    #check_ui(page)
    submit(page)
