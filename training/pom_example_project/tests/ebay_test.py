from training.pom_example_project.pages.search_page import SearchPage


class TestEbayTest:

    def test_search_for_camera(self,setup_playwright_project):
        page = setup_playwright_project
        page.goto("https://www.ebay.com")
        search_page = SearchPage(page)
        search_page.search_for_item("shoes men reebok white with ")
        text = search_page.get_result_after_search()
        assert int(text) > 100, "products did not found "