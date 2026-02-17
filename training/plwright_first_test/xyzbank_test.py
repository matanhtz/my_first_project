

class TestLoginPage:


    def test_login(self, setup_playwright):
        page = setup_playwright
        page.goto("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
        login_manager = page.query_selector_all("[class='btn btn-primary btn-lg']")
        login_manager.click()



