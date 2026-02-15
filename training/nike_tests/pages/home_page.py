
from pynput.keyboard import Key, Controller

class HomePage:
    def __init__(self, page):
        self.page = page

    def search_for_item(self,item:str):
        search_field = self.page.locator("[data-testid='visual-search-container']")
        search_field.click()
        search_field.type(item)
        keyboard = Controller()
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

    def get_header_items(self):
        header_menu = self.page.query_selector_all("[class='menu-hover-trigger-link']")
        menu_section_title = header_menu[2].inner_text()
        header_menu[2].click()
        return menu_section_title

    def click_jordan_button(self):
        jordan_button = self.page.locator("[aria-label='Jordan']")
        jordan_button.click()











