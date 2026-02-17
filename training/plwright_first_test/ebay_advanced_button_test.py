
class TestAdavancedButon():

    def test_ebay_advanced_button_test(self,setup_playwright):
        page = setup_playwright
        page.goto("https://www.ebay.com/")
        advanced_button = page.get_by_role("link","Advanced")
        advanced_button.click()
        assert page.url == "https://www.ebay.com/sch/ebayadvsearch","Advanced page not loading"
        print("Test end")