from pages.main_page import MainPage, Page

class FreetrialPage(MainPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.id = 0
        self.name = "FT"

    #회사명
    inp_companyName = '//input[@id="companyName"]'

    def fill_companyName(self,companyName):
        self.get_loc(self.inp_companyName).fill(companyName)

    #대표자명
    inp_ceoName = '//input[@id="ceoName"]'

    #사업자 유형


    #직원수

    #담당자명

    #이메일

    #휴대폰 번호

    #담당 업무

    #서비스 이용약관

    #개인정보취급 방침 동의

    #신청


