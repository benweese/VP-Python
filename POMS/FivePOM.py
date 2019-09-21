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
    # (By.CSS_SELECTOR, "#ID button.class")
    card = (By.CSS_SELECTOR, "programs[card='card']")
    got_it = (By.ID, 'triggerCloseCurtain')
    next_card = (By.CLASS_NAME, 'next-card-btn')

    def __init__(self, browser):
        self.browser = browser

    def wait(self):
        WebDriverWait(self.browser, 10).until(EC.visibility_of(self.card))

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
            self.browser.find_element(*self.got_it)
        except NoSuchElementException:
            return False
        return True

    def click_ok(self):
        ok = self.browser.find_element(*self.got_it)
        ok.click()
