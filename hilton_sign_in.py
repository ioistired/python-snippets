#!/usr/bin/env python3
# encoding: utf-8

import sys
import urllib.parse

import selenium.webdriver

def exit():
	driver.quit()
	sys.exit(0)

driver = selenium.webdriver.Firefox()
# for some reason, detectportal.firefox.com and connectivitycheck.gstatic.com are not blocked
# therefore, they cannot be used to detect connectivity
# we instead visit a site that is known not to ever have TLS, not because the owner
# wants us to detect our connectivity, but because the owner is a giant faggot
# I tried to use yahoo.com here, but it takes too long to load
driver.get('http://www.n-gate.com')
if 'n-gate.com' in urllib.parse.urlparse(driver.current_url).netloc:
	exit()

driver.find_element_by_css_selector('label[for="promo_button"]').click()
driver.find_element_by_css_selector('input[alt="Next"]').click()
driver.find_element_by_css_selector('#PromotionCode').send_keys('lobby18')
driver.find_element_by_css_selector('input[alt="Connect"]').click()
exit()
