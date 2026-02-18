

class ResultsPage:
    def __init__(self,page):
        self.page = page

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

    def check_search_filters(self):
        filters_selected = []
        gender_filter = self.page.get_by_text("Gender")
        gender_filter.click()
        men_filter = self.page.locator("[aria-label='Filter for Men']")
        men_filter.click()
        men_label = men_filter.inner_text()
        filters_selected.append(men_label)
        self.page.get_by_text("Sale & Offers").click()
        sale_filter = self.page.locator("[aria-label='Filter for Sale']")
        sale_filter.click()
        sale_label = sale_filter.inner_text()
        filters_selected.append(sale_label)
        filters_selected_lowercase = []
        for item in filters_selected:
            filters_selected_lowercase.append(item.lower())
        return filters_selected_lowercase






