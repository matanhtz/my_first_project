from training.plwright_first_test.my_first_test import search_menu


class SearchPage:
    def __init__(self, page):
        self.page = page

    def search_for_item(self,item:str):
        search_menu_field = self.page.locator("[id='gh-ac']")
        search_menu_field.click()
        search_menu_field.fill(item)
        self.page.get_by_role("button",name="Search").click()

    def get_result_after_search(self):
        print("trying to get result")
        text_element = self.page.locator("[class='s-answer-region s-answer-region-center-top']")
        text = text_element.inner_text()
        # if "+" in text:
        #     index= text.index("+")
        #     text = text[:index]

        text = text.replace("+", "")
        text = text.replace(",", "")

        # if "+" not in text:
        index = text.index("results")
        text = text[:index]

        print(f"result text is {text}")
        return text

    def click_on_advanced_link(self):
        pass