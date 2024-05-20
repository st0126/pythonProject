
from playwright.sync_api import Page, expect

id = 'seungtae.bang@illuminarean.com'
n_id = 'sssssssssssssssssss'
pw = '!qkdtmd753'
n_pw = '12345678'

def test_example(page: Page):
    page.goto("https://gvw-qa.illuminarean.com")
    page.get_by_role("button",name="로그인").click()
    page.locator('//*[@id="email"]').fill(n_id)
    page.locator('//*[@id="password"]').fill(n_pw)
    # print(page.get_by_text('이메일 주소를 정확하게 입력해주세요.').count() == 1)
    print(page.get_by_text('이메일 주소를 정확하게 입력해주세요.').is_visible())

    page.locator('//*[@id="email"]').fill(id)
    page.locator('//*[@id="password"]').fill(pw)
    # print(page.get_by_text('이메일 주소를 정확하게 입력해주세요.').count() == 0)
    print(page.get_by_text('이메일 주소를 정확하게 입력해주세요.').is_visible())
    page.wait_for_timeout(2000)


