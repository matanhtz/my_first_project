
class ResultsPage:
    def __init__(self,page):
        self.page = page

    def get_results_title(self):
        results_found_element = self.page.locator("[class='wall-header__title css-r2u0ax']")
        results_title = results_found_element.inner_text()
        return results_title

    def sort_results_by_price(self):
        self.page.get_by_text("Sort By").click()
        sort_by_items = self.page.query_selector_all("[class='dropdown__option css-10h9yp8']")
        sort_by_price = sort_by_items[3]
        sort_by_price.click()

    def check_items_price_list(self):
        prices = []
        for i in range(1,7):
            result = self.page.locator(f"[data-product-position='{i}']").text_content()
            price = result.split("₪")[-1]
            price_nis = float(price)
            prices.append(price_nis)

        return prices








