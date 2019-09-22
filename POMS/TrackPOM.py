#!/usr/bin/env python

"""
LoginPOM.py: .
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


__author__ = "Ben Weese"
__copyright__ = "Copyright 2019, Python Automation"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Ben Weese"
__email__ = "ben@benweese.dev"
__status__ = "refactor"


class TrackPOM(object):
    """
    This is the Page Object Model used in test_forms_Page.py for the filling out forms section
    of Ultimate QA's Automation Exercises.
    """
    URL = 'https://app.member.virginpulse.com/#/healthyhabits?tracker=3'

    stairs = (By.ID, 'tracker-13-track-yes')
    sleep_text = (By.ID, 'sleepHours')
    submit_sleep = (By.ID, 'track-sleep')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def wait(self):
        WebDriverWait(self.browser, 10).until(EC.visibility_of(self.stairs))

    def click_stairs(self):
        ok = self.browser.find_element(*self.stairs)
        ok.click()

    def track_sleep(self, hours):
        track_sleep = self.browser.find_element(*self.sleep_text)
        submit = self.browser.find_element(*self.submit_sleep)
        track_sleep.send_keys(hours)
        submit.click()

