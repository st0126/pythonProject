import pytest
from playwright.sync_api import Page, expect

site_Url = "https://gvw-qa.illuminarean.com/"
login_Url = "https://gvw-qa.illuminarean.com/login"
findPw_Url = "https://gvw-qa.illuminarean.com/find/password"

email = "seungtae.bang@illuminarean.com"
w_email = "seungtae.bang+258528@illuminarean.com"
n_email = "qqqqqqqqqqqqq.com"


def go_site(page):
    page.goto(site_Url)


def move_page(page):
    # 로그인 버튼 확인
    login_btn = page.get_by_role("button", name="로그인")
    print(f"로그인 버튼 확인 : {login_btn.is_enabled()}")

    # 로그인 버튼 클릭
    login_btn.click()

    # 비밀번호 찾기 버튼 확인
    findPw_btn = page.get_by_role("link", name="비밀번호 찾기")
    print(f"비밀번호 찾기 버튼 확인 : {findPw_btn.is_enabled()}")

    # 비밀번호 찾기 버튼 클릭
    findPw_btn.click()

    # 비밀 번호 찾기 페이지 이동 됐는지 확인
    print("비밀번호 찾기 url : ", page.url == findPw_Url)



def check_ui(page):
    # 타이틀
    title = page.get_by_role("heading", name='비밀번호 찾기')
    print(f"타이틀 확인 : {title.is_visible()}")

    # 설명
    content1 = page.get_by_text("가입시 작성한 이메일 주소를 입력하시면,비밀번호 재설정 링크를 메일로 받아보실 수 있습니다.")
    print(f"설명 확인 : {content1.is_visible()}")

    # 인풋박스
    email_input = page.locator('//*[@id="email"]')
    print(f"입력칸 확인 : {email_input.is_enabled()}")

    # 발송버튼 비활성화 확인
    email_btn = page.get_by_role("button", name="이메일 발송")
    print(f"버튼 비활성화 확인 : {email_btn.is_enabled() == False}")

    # 로그인 화면으로 이동 버튼
    back_login = page.get_by_role("link", name="로그인 화면으로 이동")
    print(f"로그인 화면으로 이동 버튼 확인:  {back_login.is_enabled()}")


def send_email(page):
    page.goto("https://gvw-qa.illuminarean.com/find/password")

    # 비유효 이메일 입력
    input_email = page.locator('//*[@id="email"]')
    input_email.fill(n_email)
    print("비유효 이메일 : ", page.get_by_text('이메일 주소를 정확하게 입력해주세요.').count() == 1)

    # 이메일 삭제 버튼
    erase_btn = page.locator("button[name=\"email\"]")
    input_email.hover()
    print(f"삭제 버튼 : {erase_btn.is_visible()}")
    erase_btn.click()
    print(f"삭제 버튼 클릭 후 : {input_email.input_value()}")


    # 유효 이메일 입력 - 버튼 활성화
    input_email.fill(email)
    print("유효 이메일 : ", page.get_by_text('이메일 주소를 정확하게 입력해주세요.').count() == 0)
    email_btn = page.get_by_role("button", name="이메일 발송")
    print(f"이메일 발송 버튼 활성화 확인 : {email_btn.is_enabled()}")
    email_btn.click()

    # 회원
    senten = page.get_by_text('비밀번호 재설정 링크를 발송했습니다.')
    page.wait_for_timeout(1000)
    print(f'회원 내용 : {senten.is_visible()}')
    print(f'입력된 이메일 : {page.get_by_text(email).is_visible()}')

    # 확인 버튼
    confirm_btn = page.get_by_text("확인", exact=True)
    print(f"확인 버튼 존재 : {confirm_btn.is_enabled()}")
    confirm_btn.click()

    # 비회원
    input_email.fill(w_email)
    email_btn.click()
    senten2 = page.get_by_text('메일 주소를 다시 한 번 확인후 입력해주세요.')
    page.wait_for_timeout(1000)
    print(f'비회원 내용 : {senten2.is_visible()}')
    print(f'입력된 이메일 : {page.get_by_text(w_email).is_visible()}')
    confirm_btn.click()

    # 로그인 화면으로 이동 버튼 클릭해서 로그인 화면으로 이동되는지 확인
    back_login = page.get_by_role("link", name="로그인 화면으로 이동")
    back_login.click()
    print("로그인 화면 url : ", page.url == login_Url)



def test(page):
    go_site(page)
    move_page(page)
    check_ui(page)
    send_email(page)
