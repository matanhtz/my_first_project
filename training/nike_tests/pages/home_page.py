import logging

from pynput.keyboard import Key, Controller

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

    def check_help_menu(self,menu_item:int):
        self.page.locator("[data-testid='desktop-user-menu-item-message-1']").hover()
        help_sub_menu = self.page.get_by_role("list", name="Order Status")
        help_sub_menu_items = help_sub_menu.get_by_role("listitem").all()
        try:
            menu_item_url = help_sub_menu_items[menu_item].get_by_role("menuitem").get_attribute("href")
            help_sub_menu_items[menu_item].click()
            return menu_item_url
        except IndexError:
            logging.warning(f"this menu contains {len(help_sub_menu_items)} items")

    def click_jordan_button(self):
        jordan_button = self.page.locator("[aria-label='Jordan']")
        jordan_button.click()

    def get_header_items(self):
        header_menu = self.page.query_selector_all("[class='menu-hover-trigger-link']")
        menu_section_title = header_menu[2].inner_text()
        header_menu[2].click()
        return menu_section_title











