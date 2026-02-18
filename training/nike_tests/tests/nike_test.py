from time import sleep
from playwright.sync_api import expect
from training.nike_tests.globals import URL
from training.nike_tests.pages.home_page import HomePage
from training.nike_tests.pages.results_page import ResultsPage


class TestNike:

    def test_search_field(self,setup_playwright_nike_project):
        page = setup_playwright_nike_project
        page.goto(URL)
        home_page = HomePage(page)
        item_text = home_page.search_for_item("Basketball shoes")
        correct_results_page_reached = all(item in page.url for item in item_text)
        assert correct_results_page_reached, "item not in url"

    def test_help_menu(self,setup_playwright_nike_project):
        page = setup_playwright_nike_project
        page.goto(URL)
        home_page = HomePage(page)
        help_menu_valid = home_page.check_help_menu()
        assert help_menu_valid, "help menu with error"

    def test_results_sort_by_price(self,setup_playwright_nike_project):
        page = setup_playwright_nike_project
        page.goto(URL)
        home_page = HomePage(page)
        results_page = ResultsPage(page)
        home_page.search_for_item("baseball cap")
        results_page.sort_results_by_price()
        order_of_prices_correct = results_page.check_items_price_list()
        assert order_of_prices_correct, "order of prices incorrect"

    def test_search_filters(self,setup_playwright_nike_project):
        page = setup_playwright_nike_project
        page.goto(URL)
        home_page = HomePage(page)
        home_page.search_for_item("tennis shoes")
        results_page = ResultsPage(page)
        filters_selected = results_page.check_search_filters()
        item_is_in_url = all(item in page.url for item in filters_selected)
        assert item_is_in_url, "item not in url"

    def test_women_header_menu(self,setup_playwright_nike_project):
        page = setup_playwright_nike_project
        page.goto(URL)
        home_page = HomePage(page)
        section_title = home_page.get_women_header_items()
        assert section_title in page.url, "section title not in current url"

    def test_jordan_button(self,setup_playwright_nike_project):
        page = setup_playwright_nike_project
        page.goto(URL)
        home_page = HomePage(page)
        home_page.click_jordan_button()
        expect(page).to_have_url("https://www.nike.com/il/jordan")
