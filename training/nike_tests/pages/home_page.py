import logging
from time import sleep
from pynput.keyboard import Key, Controller
from training.nike_tests.globals import URL


class HomePage:
    def __init__(self, page):
        self.page = page

    def search_for_item(self,item:str):
        search_field = self.page.locator("[data-testid='visual-search-container']")
        search_field.click()
        search_field.type(item)
        item_text = item.split()
        keyboard = Controller()
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        self.page.wait_for_url("**/il/w?q=**")
        return item_text

    def check_help_menu(self):
        self.page.locator("[data-testid='desktop-user-menu-item-message-1']").hover()
        help_menu = self.page.get_by_role("list", name="Order Status")
        help_menu_items = help_menu.get_by_role("listitem").all()
        help_menu_valid = True
        for i in range(0,3):
            href = help_menu_items[i].get_by_role("menuitem").get_attribute("href")
            help_menu_items[i].click()
            sleep(3)
            response = self.page.request.get(href, timeout=5000)
            status = response.status
            if status == 200:
                self.page.goto(URL)
                sleep(3)
                self.page.locator("[data-testid='desktop-user-menu-item-message-1']").hover()

            else:
                logging.warning(f"the url of item {i} in this menu is broken")
                help_menu_valid = False
                break

        return help_menu_valid

    def click_jordan_button(self):
        jordan_button = self.page.locator("[aria-label='Jordan']")
        jordan_button.click()

    def check_women_header_menu(self):
        header_menu = self.page.query_selector_all("[class='menu-hover-trigger-link']")
        women_menu_section = header_menu[2].inner_text()
        women_menu_section_lowercase = women_menu_section.lower()
        header_menu[2].click()
        return women_menu_section_lowercase











