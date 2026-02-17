# go to https://demo.guru99.com/test/newtours/reservation.php
# make full process of ordering flight
from time import sleep

from training.new_file import name


class TestOrderFlight:

    def test_order_flight(self,setup_playwright):
        page = setup_playwright
        page.goto("https://demo.guru99.com/test/newtours/reservation.php")
        departing_from_dropdown = page.locator("[name='fromPort']")
        departing_from_dropdown.select_option("Paris")
        trip_type_radio_button = page.locator("[value='oneway']")
        trip_type_radio_button.set_checked(True)
        departing_month_dropdown = page.locator("[name='fromMonth']")
        departing_month_dropdown.select_option(index=10)
        find_flights_button = page.locator("[name='findFlights']")
        find_flights_button.click()
        sleep(3)
        assert page.url=="https://demo.guru99.com/test/newtours/reservation2.php", "search results not loading"


