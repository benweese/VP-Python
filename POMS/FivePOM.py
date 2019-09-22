#!/usr/bin/env python

"""
LoginPOM.py: .
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


__author__ = "Ben Weese"
__copyright__ = "Copyright 2019, Python Automation"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Ben Weese"
__email__ = "ben@benweese.dev"
__status__ = "refactor"


class FivePOM(object):
    """
    This is the Page Object Model used in test_forms_Page.py for the filling out forms section
    of Ultimate QA's Automation Exercises.
    """
    got_it = (By.ID, 'triggerCloseCurtain')
    next_card = (By.CLASS_NAME, 'next-card-btn')
    daily_ribbon = (By.CLASS_NAME, 'daily-card-ribbon')

    def __init__(self, browser):
        self.browser = browser

    def wait(self):
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(self.next_card))

    def wait_btn(self):
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(self.got_it))

    def is_next(self):
        try:
            self.browser.find_element(*self.next_card)
        except NoSuchElementException:
            return False
        return True

    def click_next(self):
        next_card = self.browser.find_element(*self.next_card)
        next_card.click()

    def correct_card(self):
        try:
            self.browser.find_element(*self.daily_ribbon)
        except NoSuchElementException:
            return False
        return True

    def click_ok(self):
        ok = self.browser.find_element(*self.got_it)
        ok.click()
