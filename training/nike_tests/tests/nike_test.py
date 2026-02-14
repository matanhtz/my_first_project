from playwright.sync_api import expect
from training.nike_tests.globals import URL
from training.nike_tests.pages.home_page import HomePage
from training.nike_tests.pages.results_page import ResultsPage


class TestNike:

    def test_search_field(self,setup_playwright_nike_project):
        page = setup_playwright_nike_project
        page.goto(URL)
        home_page = HomePage(page)
        results_page = ResultsPage(page)
        item = "basketball shoes"
        home_page.search_for_item(item)
        results_title = results_page.get_results_title()
        assert item in results_title, "item not in title"

    def test_header_menu(self,setup_playwright_nike_project):
        page = setup_playwright_nike_project
        page.goto(URL)
        home_page = HomePage(page)
        section_title = home_page.get_header_items()
        url_section = section_title.lower()
        assert url_section in page.url, "section_title not in current_url"

    def test_jordan_button(self,setup_playwright_nike_project):
        page = setup_playwright_nike_project
        page.goto(URL)
        home_page = HomePage(page)
        home_page.click_jordan_button()
        expect(page).to_have_url("https://www.nike.com/il/jordan")

    def test_sort_results_button(self,setup_playwright_nike_project):
        page = setup_playwright_nike_project
        page.goto(URL)
        home_page = HomePage(page)
        results_page = ResultsPage(page)
        item = "Shirt"
        home_page.search_for_item(item)
        results_page.sort_results_by_price()
        expect(page).to_have_url("https://www.nike.com/il/w?q=Shirt&vst=Shirt&sortBy=priceAsc")

    def test_price_list(self,setup_playwright_nike_project):
        page = setup_playwright_nike_project
        page.goto("https://www.nike.com/il/w?q=Shirt&vst=Shirt&sortBy=priceAsc")
        results_page = ResultsPage(page)
        price_list = results_page.check_items_price_list()
        order_of_prices_correct = True
        for i in range(0, len(price_list)-1):
            if price_list[i] > price_list[i+1]:
                order_of_prices_correct = False
                break

        assert order_of_prices_correct == True, "unexpected result"