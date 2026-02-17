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
        item = "Basketball shoes"
        home_page.search_for_item(item)
        item_text = item.split()
        page.wait_for_url("**/il/w?q=**")
        current_url = page.url
        results_page_reached = all(item in current_url for item in item_text)
        assert results_page_reached, "item not in url"

    def test_header_menu(self,setup_playwright_nike_project):
        page = setup_playwright_nike_project
        page.goto(URL)
        home_page = HomePage(page)
        section_title = home_page.get_header_items()
        url_section = section_title.lower()
        assert url_section in page.url, "section title not in current url"

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
        home_page.search_for_item("Shirt")
        results_page.sort_results_by_price()
        expect(page).to_have_url("https://www.nike.com/il/w?q=Shirt&vst=Shirt&sortBy=priceAsc")

    def test_price_list(self,setup_playwright_nike_project):
        page = setup_playwright_nike_project
        page.goto(URL)
        home_page = HomePage(page)
        results_page = ResultsPage(page)
        home_page.search_for_item("baseball cap")
        results_page.sort_results_by_price()
        sleep(3)
        page.wait_for_url("**priceAsc")
        price_list = results_page.check_items_price_list()
        order_of_prices_correct = True
        for i in range(0, len(price_list)-1):
            if price_list[i] > price_list[i+1]:
                order_of_prices_correct = False
                break

        assert order_of_prices_correct == True, "order of prices incorrect"

    def test_search_filters(self,setup_playwright_nike_project):
        page = setup_playwright_nike_project
        page.goto(URL)
        home_page = HomePage(page)
        home_page.search_for_item("tennis shoes")
        results_page = ResultsPage(page)
        filters_selected = results_page.check_search_filters()
        current_url = page.url
        item_is_in_url = all(item in current_url for item in filters_selected)
        assert item_is_in_url == True, "item not in url"
