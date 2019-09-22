#!/usr/bin/env python

"""
test_virgin_pulse.py: Uses Selenium and Pytest to showcase testing automation.
"""

import time

from POMS.LoginPOM import LoginPOM
from POMS.FivePOM import FivePOM
from POMS.TrackPOM import TrackPOM

__author__ = "Ben Weese"
__copyright__ = "Copyright 2019, Python Automation"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Ben Weese"
__email__ = "ben@benweese.dev"
__status__ = "refactor"


def test_1(browser):
	"""
	This fills out the First form on the page and makes sure the date was entered.
	Then it will verify if the message was successfully sent.
	:param browser:
	"""
	login = LoginPOM(browser)
	login.load()
	login.login()
	card = FivePOM(browser)
	card.wait()
	while card.is_next():
		if card.correct_card():
			card.click_ok()
			card.click_next()
		else:
			card.click_next()
	track = TrackPOM(browser)
	track.load()
	track.wait()
	track.click_stairs()
	track.track_sleep('7')
	browser.quit()


